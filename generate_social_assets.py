from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
SOCIAL = ASSETS / "social"
SOCIAL.mkdir(parents=True, exist_ok=True)

BG_PATH = ROOT / "hero_render" / "hero_render.jpg"
OG_PATH = SOCIAL / "og-cover.png"
APPLE_PATH = SOCIAL / "apple-touch-icon.png"
FAVICON_PNG_PATH = SOCIAL / "favicon-512.png"
FAVICON_SVG_PATH = SOCIAL / "favicon.svg"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/malgunbd.ttf" if bold else "C:/Windows/Fonts/malgun.ttf",
        "C:/Windows/Fonts/PRETENDARD-BOLD.TTF" if bold else "C:/Windows/Fonts/PRETENDARD-REGULAR.TTF",
        "C:/Windows/Fonts/NanumGothicBold.ttf" if bold else "C:/Windows/Fonts/NanumGothic.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_og() -> None:
    base = Image.open(BG_PATH).convert("RGB")
    canvas = Image.new("RGB", (1200, 630), "#16383d")

    base_ratio = base.width / base.height
    target_ratio = 1200 / 630
    if base_ratio > target_ratio:
        new_height = 630
        new_width = int(new_height * base_ratio)
    else:
        new_width = 1200
        new_height = int(new_width / base_ratio)
    resized = base.resize((new_width, new_height), Image.Resampling.LANCZOS)
    left = (new_width - 1200) // 2
    top = (new_height - 630) // 2
    cropped = resized.crop((left, top, left + 1200, top + 630))
    canvas.paste(cropped, (0, 0))

    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1200, 630), fill=(8, 24, 28, 110))
    od.rounded_rectangle((46, 42, 1154, 588), radius=34, fill=(250, 248, 242, 225))
    od.rounded_rectangle((72, 72, 280, 118), radius=22, fill=(198, 156, 104, 230))
    od.rounded_rectangle((72, 470, 294, 544), radius=28, fill=(15, 143, 151, 245))
    od.rounded_rectangle((312, 470, 566, 544), radius=28, fill=(255, 255, 255, 232))
    od.rounded_rectangle((822, 440, 1108, 546), radius=26, fill=(255, 179, 66, 240))
    overlay = overlay.filter(ImageFilter.GaussianBlur(0.2))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(canvas)
    white = "#FFFFFF"
    ink = "#20373d"
    muted = "#536c71"
    teal = "#0f8f97"

    draw.text((98, 80), "의료 프리미엄 단지", font=font(24, True), fill=white)
    draw.text((98, 154), "브레인시티 메디스파크", font=font(58, True), fill=ink)
    draw.text((98, 226), "로제비앙 모아엘가", font=font(58, True), fill=ink)

    body = (
        "아주대병원, 초중학교, 상업시설, 공원을 도보로 누리는\n"
        "브레인시티 메디컬 프리미엄 주거 선택지"
    )
    draw.multiline_text((100, 320), body, font=font(26, False), fill=muted, spacing=10)

    draw.text((110, 491), "상담 연결받기", font=font(26, True), fill=white)
    draw.text((346, 491), "관심고객 등록", font=font(26, True), fill=ink)

    draw.text((850, 462), "대표번호", font=font(20, True), fill=ink)
    draw.text((852, 496), "010-6689-2348", font=font(32, True), fill=ink)

    meta = "총 1,215세대  ·  초중학교 도보 1분  ·  아주대병원 도보 3분"
    draw.text((98, 570), meta, font=font(20, True), fill=teal)

    canvas.convert("RGB").save(OG_PATH, quality=95)


def draw_icon() -> None:
    size = 512
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((24, 24, 488, 488), radius=112, fill="#0f8f97")
    draw.rounded_rectangle((78, 78, 434, 434), radius=92, outline="#f6e2bf", width=12)
    draw.text((112, 118), "M", font=font(220, True), fill="#fffaf1")
    draw.rounded_rectangle((128, 332, 388, 392), radius=24, fill="#ffb342")
    draw.text((172, 343), "PARK", font=font(34, True), fill="#11343a")
    img.save(FAVICON_PNG_PATH)
    img.resize((180, 180), Image.Resampling.LANCZOS).save(APPLE_PATH)

    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="112" fill="#0f8f97"/>
  <rect x="78" y="78" width="356" height="356" rx="92" fill="none" stroke="#f6e2bf" stroke-width="12"/>
  <text x="116" y="292" font-family="Malgun Gothic, Arial, sans-serif" font-size="220" font-weight="700" fill="#fffaf1">M</text>
  <rect x="128" y="332" width="260" height="60" rx="24" fill="#ffb342"/>
  <text x="171" y="372" font-family="Arial, sans-serif" font-size="34" font-weight="700" fill="#11343a">PARK</text>
</svg>
"""
    FAVICON_SVG_PATH.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    draw_og()
    draw_icon()
