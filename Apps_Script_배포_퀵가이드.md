# Apps Script 배포 퀵가이드

## 1. Google Sheets 준비

1. 새 Google Sheets 생성
2. 시트 이름을 `leads`로 변경
3. [구글시트_컬럼샘플.csv](C:/Codex/20260627_vibe/구글시트_컬럼샘플.csv)의 첫 줄 헤더를 1행에 복사
4. 주소창에서 Spreadsheet ID 복사

예:

```text
https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
```

## 2. Apps Script 코드 반영

1. [script.new](https://script.new) 열기
2. 기본 `Code.gs` 내용을 모두 지우고 [Code.gs](C:/Codex/20260627_vibe/Code.gs) 내용 붙여넣기
3. `SPREADSHEET_ID`를 실제 값으로 변경
4. 필요하면 `SHEET_NAME`, `ALLOWED_DEVELOPER` 확인
5. 프로젝트 설정에서 `appsscript.json` 내용이 필요하면 [appsscript.json](C:/Codex/20260627_vibe/appsscript.json) 기준으로 반영

## 3. Web App 배포

1. 우측 상단 `Deploy`
2. `New deployment`
3. 유형 `Web app`
4. `Execute as`: `Me`
5. `Who has access`: `Anyone`
6. `Deploy`
7. 권한 승인
8. 배포 URL 복사

## 4. 랜딩페이지 설정 반영

1. [landing.config.js](C:/Codex/20260627_vibe/landing.config.js) 열기
2. 아래 항목 수정

```js
window.LANDING_CONFIG = {
  appScriptUrl: "실제_배포_URL",
  phoneNumber: "010-6689-2348",
  developer: "박시은",
};
```

## 5. 최소 확인

- 브라우저에서 `index.html` 열기
- 상단 히어로 폼에서 이름/연락처 입력 후 제출
- Google Sheets에 한 줄 저장되는지 확인
- `developer`가 `박시은`인지 확인

## 6. 실패 시 가장 먼저 볼 것

- `SPREADSHEET_ID` 오타
- 시트 이름 `leads` 불일치
- Apps Script 권한 승인 누락
- `landing.config.js`에 배포 URL 미반영
- 너무 빠르게 제출해서 차단된 경우
