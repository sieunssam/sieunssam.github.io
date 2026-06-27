const SPREADSHEET_ID = "REPLACE_WITH_SPREADSHEET_ID";
const SHEET_NAME = "leads";
const ALLOWED_DEVELOPER = "박시은";
const MIN_SUBMIT_DELAY_MS = 1500;

function doPost(e) {
  try {
    const payload = parseRequestBody_(e);
    validatePayload_(payload);

    const sheet = getSheet_();
    const row = buildRow_(payload);
    sheet.appendRow(row);

    return jsonResponse_({
      ok: true,
      message: "saved",
      row: sheet.getLastRow(),
    });
  } catch (error) {
    return jsonResponse_({
      ok: false,
      message: error.message || "unexpected error",
    });
  }
}

function doGet() {
  return jsonResponse_({
    ok: true,
    message: "running",
  });
}

function parseRequestBody_(e) {
  if (!e) {
    throw new Error("empty request body");
  }

  let data = {};

  if (e.postData && e.postData.contents) {
    try {
      data = JSON.parse(e.postData.contents);
    } catch (error) {
      data = e.parameter || {};
    }
  } else {
    data = e.parameter || {};
  }

  return {
    name: stringValue_(data.name),
    phone: normalizePhone_(data.phone),
    developer: stringValue_(data.developer),
    consult_type: stringValue_(data.consult_type),
    interest_type: stringValue_(data.interest_type),
    visit_request: stringValue_(data.visit_request || "N"),
    visit_datetime: stringValue_(data.visit_datetime),
    page_url: stringValue_(data.page_url),
    device: stringValue_(data.device),
    utm_source: stringValue_(data.utm_source),
    utm_medium: stringValue_(data.utm_medium),
    utm_campaign: stringValue_(data.utm_campaign),
    memo: stringValue_(data.memo),
    website: stringValue_(data.website),
    form_started_at: stringValue_(data.form_started_at),
  };
}

function validatePayload_(payload) {
  if (!payload.name) {
    throw new Error("name is required");
  }

  if (!payload.phone || payload.phone.length < 9) {
    throw new Error("phone is required");
  }

  if (!payload.developer) {
    throw new Error("developer is required");
  }

  if (payload.developer !== ALLOWED_DEVELOPER) {
    throw new Error("developer is invalid");
  }

  if (payload.website) {
    throw new Error("spam detected");
  }

  if (!payload.form_started_at || isNaN(Number(payload.form_started_at))) {
    throw new Error("form_started_at is required");
  }

  if (Date.now() - Number(payload.form_started_at) < MIN_SUBMIT_DELAY_MS) {
    throw new Error("submitted too quickly");
  }

  if (payload.visit_request && !["Y", "N"].includes(payload.visit_request)) {
    throw new Error("visit_request must be Y or N");
  }
}

function getSheet_() {
  const spreadsheet = SpreadsheetApp.openById(SPREADSHEET_ID);
  const sheet = spreadsheet.getSheetByName(SHEET_NAME);
  if (!sheet) {
    throw new Error(`sheet not found: ${SHEET_NAME}`);
  }
  return sheet;
}

function buildRow_(payload) {
  return [
    new Date(),
    payload.name,
    payload.phone,
    payload.developer,
    payload.consult_type,
    payload.interest_type,
    payload.visit_request,
    payload.visit_datetime,
    payload.page_url,
    payload.device,
    payload.utm_source,
    payload.utm_medium,
    payload.utm_campaign,
    payload.memo,
  ];
}

function normalizePhone_(value) {
  return stringValue_(value).replace(/\D/g, "");
}

function stringValue_(value) {
  return String(value || "").trim();
}

function jsonResponse_(payload) {
  return ContentService
    .createTextOutput(JSON.stringify(payload))
    .setMimeType(ContentService.MimeType.JSON);
}
