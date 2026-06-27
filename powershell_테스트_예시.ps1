$AppScriptUrl = "https://script.google.com/macros/s/REPLACE_WITH_DEPLOYMENT_ID/exec"

$Body = @{
  name = "파워셸테스트"
  phone = "010-1212-3434"
  developer = "박시은"
  consult_type = "상담하기"
  interest_type = "84A"
  visit_request = "N"
  visit_datetime = ""
  page_url = "https://example.com/braincity"
  device = "desktop"
  utm_source = "powershell"
  utm_medium = "qa"
  utm_campaign = "braincity_ps_test"
  memo = "powershell manual test"
  website = ""
  form_started_at = [string]([DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds() - 3000)
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri $AppScriptUrl `
  -Method Post `
  -ContentType "application/json" `
  -Body $Body
