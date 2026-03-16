"""Generate Google Play Store assets for Yubi AppGate -- v2 polished."""

from PIL import Image, ImageDraw, ImageFont
import math
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(SCRIPT_DIR, "images")
os.makedirs(OUT_DIR, exist_ok=True)

# Theme colors
BG_DARK = (6, 6, 12)
BG_CARD = (14, 14, 26)
CYAN = (0, 212, 255)
GREEN = (0, 255, 136)
PURPLE = (155, 89, 255)
WHITE = (230, 230, 238)
GREY = (120, 120, 150)
MUTED = (60, 60, 85)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def soft_glow(img, cx, cy, radius, color, intensity=40):
    """Paint a soft radial glow onto an RGBA image."""
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    step = max(2, radius // 80)
    for r in range(radius, 0, -step):
        t = r / radius
        a = int(intensity * (1 - t * t))
        if a < 1:
            continue
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))
    return Image.alpha_composite(img, ov)


def draw_shield(draw, cx, cy, size, fill, outline, width=4):
    """Draw a clean symmetric shield."""
    pts = []
    steps = 20
    for i in range(steps + 1):
        angle = math.pi + (math.pi * i / steps)
        x = cx + math.cos(angle) * size * 0.7
        y = cy - size * 0.85 - math.sin(angle) * size * 0.18
        pts.append((x, y))
    pts.append((cx + size * 0.7, cy - size * 0.15))
    pts.append((cx + size * 0.55, cy + size * 0.35))
    pts.append((cx + size * 0.3, cy + size * 0.7))
    pts.append((cx, cy + size))
    pts.append((cx - size * 0.3, cy + size * 0.7))
    pts.append((cx - size * 0.55, cy + size * 0.35))
    pts.append((cx - size * 0.7, cy - size * 0.15))

    draw.polygon(pts, fill=fill)
    draw.line(pts + [pts[0]], fill=outline, width=width, joint="curve")


def draw_padlock(draw, cx, cy, body_w, color_body, color_hole):
    """Draw a clean padlock centered at (cx, cy)."""
    body_h = body_w * 0.7
    r = body_w * 0.12

    bx0 = cx - body_w / 2
    by0 = cy - body_h * 0.25
    draw.rounded_rectangle(
        [bx0, by0, bx0 + body_w, by0 + body_h],
        radius=r, fill=color_body
    )

    shackle_w = body_w * 0.52
    shackle_h = body_h * 0.6
    sw = max(4, int(body_w * 0.1))
    sx0 = cx - shackle_w / 2
    sy0 = by0 - shackle_h + sw
    draw.arc(
        [sx0, sy0, sx0 + shackle_w, by0 + shackle_h * 0.15],
        start=180, end=0, fill=color_body, width=sw
    )

    khr = body_w * 0.08
    kcy = by0 + body_h * 0.4
    draw.ellipse(
        [cx - khr, kcy - khr, cx + khr, kcy + khr],
        fill=color_hole
    )
    slit_w = max(2, int(body_w * 0.04))
    draw.rectangle(
        [cx - slit_w / 2, kcy + khr * 0.6, cx + slit_w / 2, kcy + body_h * 0.32],
        fill=color_hole
    )


# ===================================================================
# APP ICON -- 512 x 512
# ===================================================================
def generate_app_icon():
    S = 512
    img = Image.new("RGBA", (S, S), (*BG_DARK, 255))

    # Ambient glows
    img = soft_glow(img, S * 0.3, S * 0.25, 360, CYAN, 30)
    img = soft_glow(img, S * 0.7, S * 0.75, 300, PURPLE, 22)

    draw = ImageDraw.Draw(img)

    # Rounded background card
    pad = 8
    draw.rounded_rectangle([pad, pad, S - pad, S - pad], radius=100,
                           fill=(*BG_CARD, 240))

    # Central shield
    scx, scy = S // 2, int(S * 0.39)
    shield_r = 130
    shield_fill = (12, 28, 42, 230)
    draw_shield(draw, scx, scy, shield_r, fill=shield_fill, outline=CYAN, width=5)

    # Padlock inside shield
    draw_padlock(draw, scx, scy + 10, shield_r * 0.68, CYAN, BG_DARK)

    # Thin gradient line under shield
    line_y = int(scy + shield_r + 24)
    for x in range(S // 2 - 100, S // 2 + 100):
        t = abs(x - S // 2) / 100
        a = int(180 * (1 - t))
        draw.point((x, line_y), fill=(*CYAN, a))

    # App name
    font_big = ImageFont.truetype(FONT_BOLD, 52)
    font_sm = ImageFont.truetype(FONT_REG, 21)

    name_y = line_y + 14
    bb1 = draw.textbbox((0, 0), "YUBI ", font=font_big)
    w1 = bb1[2] - bb1[0]
    bb2 = draw.textbbox((0, 0), "APPGATE", font=font_big)
    w2 = bb2[2] - bb2[0]
    total = w1 + w2
    x_start = (S - total) / 2
    draw.text((x_start, name_y), "YUBI ", fill=CYAN, font=font_big)
    draw.text((x_start + w1, name_y), "APPGATE", fill=WHITE, font=font_big)

    # Tagline
    tag = "Hardware App Lock"
    bbt = draw.textbbox((0, 0), tag, font=font_sm)
    ttw = bbt[2] - bbt[0]
    draw.text(((S - ttw) / 2, name_y + 60), tag, fill=GREY, font=font_sm)

    # Save
    final = img.convert("RGB")
    path = os.path.join(OUT_DIR, "app-icon-512.png")
    final.save(path, "PNG", optimize=True)
    sz = os.path.getsize(path)
    print(f"App icon: {path}  ({sz/1024:.0f} KB)")


# ===================================================================
# FEATURE GRAPHIC -- 1024 x 500
# ===================================================================
def generate_feature_graphic():
    W, H = 1024, 500
    img = Image.new("RGBA", (W, H), (*BG_DARK, 255))

    # Ambient glows
    img = soft_glow(img, W * 0.15, H * 0.4, 380, CYAN, 28)
    img = soft_glow(img, W * 0.85, H * 0.5, 320, PURPLE, 20)
    img = soft_glow(img, W * 0.5, H * 1.0, 350, GREEN, 12)

    draw = ImageDraw.Draw(img)

    # Subtle dot grid
    for x in range(20, W, 32):
        for y in range(20, H, 32):
            draw.rectangle([x, y, x + 1, y + 1], fill=(*MUTED, 35))

    # -- Left side: Shield icon --
    icon_cx = int(W * 0.18)
    icon_cy = int(H * 0.46)
    sr = 95

    # Glow behind icon
    img = soft_glow(img, icon_cx, icon_cy, 180, CYAN, 35)
    draw = ImageDraw.Draw(img)

    shield_fill = (10, 24, 38, 220)
    draw_shield(draw, icon_cx, icon_cy, sr, fill=shield_fill, outline=CYAN, width=4)
    draw_padlock(draw, icon_cx, icon_cy + 8, sr * 0.62, CYAN, BG_DARK)

    # -- Right side: Text --
    font_title = ImageFont.truetype(FONT_BOLD, 56)
    font_sub = ImageFont.truetype(FONT_REG, 24)
    font_badge = ImageFont.truetype(FONT_BOLD, 14)
    font_feat = ImageFont.truetype(FONT_REG, 18)

    tx = int(W * 0.38)

    # Badge pill
    badge = "HARDWARE-BACKED SECURITY"
    bbb = draw.textbbox((0, 0), badge, font=font_badge)
    bw, bh = bbb[2] - bbb[0], bbb[3] - bbb[1]
    pill_y = int(H * 0.1)
    px, py = 14, 7
    draw.rounded_rectangle(
        [tx, pill_y, tx + bw + px * 2, pill_y + bh + py * 2],
        radius=14, fill=(*CYAN, 25), outline=(*CYAN, 60), width=1
    )
    draw.text((tx + px, pill_y + py), badge, fill=CYAN, font=font_badge)

    # Title
    title_y = pill_y + bh + py * 2 + 22
    bb1 = draw.textbbox((0, 0), "Yubi ", font=font_title)
    w1 = bb1[2] - bb1[0]
    draw.text((tx, title_y), "Yubi ", fill=CYAN, font=font_title)
    draw.text((tx + w1, title_y), "AppGate", fill=WHITE, font=font_title)

    # Subtitle
    sub_y = title_y + 72
    draw.text((tx, sub_y),
              "Lock Android Apps with Your YubiKey",
              fill=GREY, font=font_sub)

    # Divider line
    div_y = sub_y + 42
    for x in range(tx, tx + 260):
        t = (x - tx) / 260
        a = int(100 * (1 - t))
        draw.point((x, div_y), fill=(*CYAN, a))

    # Feature list
    features = [
        "YubiKey HMAC-SHA1 Authentication",
        "NFC & USB-C Support",
        "System-wide App Protection",
        "No Cloud \u2014 Fully Offline",
    ]
    feat_y = div_y + 16
    for i, text in enumerate(features):
        y = feat_y + i * 30
        draw.text((tx, y), "\u2713", fill=GREEN, font=font_feat)
        draw.text((tx + 22, y), text, fill=GREY, font=font_feat)

    # Top accent line (gradient)
    for x in range(0, W):
        t = x / W
        r = int(CYAN[0] * (1 - t) + PURPLE[0] * t)
        g = int(CYAN[1] * (1 - t) + PURPLE[1] * t)
        b = int(CYAN[2] * (1 - t) + PURPLE[2] * t)
        draw.point((x, 0), fill=(r, g, b, 200))
        draw.point((x, 1), fill=(r, g, b, 100))

    # Bottom accent line (gradient)
    for x in range(0, W):
        t = x / W
        r = int(GREEN[0] * (1 - t) + CYAN[0] * t)
        g = int(GREEN[1] * (1 - t) + CYAN[1] * t)
        b = int(GREEN[2] * (1 - t) + CYAN[2] * t)
        draw.point((x, H - 1), fill=(r, g, b, 200))
        draw.point((x, H - 2), fill=(r, g, b, 100))

    # Save
    final = img.convert("RGB")
    path = os.path.join(OUT_DIR, "feature-graphic-1024x500.png")
    final.save(path, "PNG", optimize=True)
    sz = os.path.getsize(path)
    print(f"Feature graphic: {path}  ({sz/1024:.0f} KB)")


if __name__ == "__main__":
    generate_app_icon()
    generate_feature_graphic()
    print("\nDone.")
