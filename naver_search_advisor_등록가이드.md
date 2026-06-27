# 네이버 서치어드바이저 등록 가이드

## 이미 준비된 파일

- [robots.txt](C:/Codex/20260627_vibe/robots.txt)
- [sitemap.xml](C:/Codex/20260627_vibe/sitemap.xml)
- [index.html](C:/Codex/20260627_vibe/index.html)

## 등록할 사이트 URL

```text
https://sieunssam.github.io/
```

## 네이버 서치어드바이저에서 해야 할 것

1. 네이버 서치어드바이저 접속
2. 사이트 등록
3. 사이트 주소 입력
4. 소유확인 진행

## 소유확인 방법

네이버는 보통 아래 둘 중 하나를 요구합니다.

1. `meta` 태그 삽입
2. HTML 파일 업로드

### 1. meta 태그 방식

네이버가 아래 형태의 태그를 줍니다.

```html
<meta name="naver-site-verification" content="발급받은값" />
```

이 값을 [index.html](C:/Codex/20260627_vibe/index.html)의 `<head>` 안에 넣으면 됩니다.

### 2. HTML 파일 방식

네이버가 예를 들어 아래와 같은 파일명을 요구할 수 있습니다.

```text
naverabcd1234efgh.html
```

그 경우 그 파일명을 그대로 루트에 만들고, 네이버가 준 내용을 파일 안에 넣어야 합니다.

## 사이트맵 제출 정보

네이버 서치어드바이저의 사이트맵 제출 메뉴에서 아래 주소를 입력하면 됩니다.

```text
https://sieunssam.github.io/sitemap.xml
```

## robots.txt 확인 주소

```text
https://sieunssam.github.io/robots.txt
```

## 점검 순서

1. GitHub Pages 반영 확인
2. `robots.txt` 접속 확인
3. `sitemap.xml` 접속 확인
4. 네이버 소유확인 완료
5. 사이트맵 제출

## 추가 메모

- 네이버 인증용 `meta` 값이나 HTML 파일명은 아직 고정값이 없으므로, 발급받은 뒤 최종 반영해야 합니다.
- 인증값을 받으면 그때 제가 바로 파일 또는 메타 태그에 넣어드릴 수 있습니다.
