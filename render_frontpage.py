#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news front page (1024x1024 PNG).

Fresh render for news-image-20261123. Pillow only, no network, no
randomness: the same script always writes identical bytes.

Stories (all first reported / developed on Mon 23 Nov 2026, verified by
web search before drawing):
  LEAD  COP31 collapses in Antalya, Turkey: no deal, longest COP ever,
        EU/UK reject the "Antalya Pact" because it never names fossil
        fuels; first COP failure since Copenhagen 2009.
        Sources: BBC, CNN, Reuters, Le Monde, The Times.
  2     Russian strikes on Ukraine's Kyiv region: at least 14 missing,
        a 7-year-old boy pulled from the rubble. BBC / Reuters.
  3     US midterms: Democrats win at least 258 House seats, their
        largest majority since 1992. BBC.
  4     Explosion on a Russian ship at a Libya port, suspected drone
        attack, officials say. BBC / Reuters.
  5     South Korea's education minister resigns over the exam-cheating
        scandal (AI-assisted cheating). BBC.
  6     Fire at an Indonesian confectionery factory: 3 killed, 36
        missing. BBC.
  ALSO  Italian jeweller Paolo Bulgari dies aged 89; Miley Cyrus marries
        Maxx Morando; Pochettino's Man Utd lose to Liverpool; US Army to
        detonate tonnes of unstable explosives in Iowa despite a court
        order. BBC.
"""

import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

INK = (18, 18, 18)
PAPER = (250, 247, 238)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
GREY = (90, 90, 90)
LIGHTGREY = (200, 196, 186)
BLUE = (24, 62, 110)
TEAL = (14, 92, 84)
ORANGE = (196, 94, 10)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, leading, fill=INK):
    """Draw wrapped paragraph; return y after last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, x, y, text, color=RED):
    f = font(SANS_B, 15)
    draw.text((x, y), text.upper(), font=f, fill=color)
    return y + 21


def headline(draw, x, y, text, size, width, leading=None, fill=INK):
    f = font(SERIF_B, size)
    leading = leading or size + 6
    for line in wrap(draw, text, f, width):
        draw.text((x, y), line, font=f, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def box(draw, x0, y0, x1, y1, outline=INK, width=2, fill=None):
    draw.rectangle([x0, y0, x1, y1], outline=outline, width=width, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.text((W // 2, 14), "THE WORLD", font=font(SERIF_B, 66), fill=INK,
       anchor="ma")
d.text((W // 2, 92), "MONDAY 23 NOVEMBER 2026", font=font(SANS_B, 20),
       fill=RED, anchor="ma")
rule(d, 36, 126, 988, width=3)
d.text((W // 2, 134), "THE DAY'S NEWS  •  ONE PAGE  •  SIX STORIES THAT MATTER",
       font=font(SANS, 13), fill=GREY, anchor="ma")

# ---------------------------------------------------------------- lead panel
LX0, LX1, LY0, LY1 = 36, 648, 158, 486
box(d, LX0, LY0, LX1, LY1)
y = LY0 + 12
y = kicker(d, LX0 + 14, y, "Lead story — Climate  •  Antalya, Turkey")
y = headline(d, LX0 + 14, y + 2, "COP31 COLLAPSES:", 40, LX1 - LX0 - 28,
             leading=46)
y = headline(d, LX0 + 14, y, "NO DEAL ON CLIMATE", 40, LX1 - LX0 - 28,
             leading=46, fill=DARKRED)

# Graphic: cracked globe over a crossed-out "FOSSIL FUELS" pact line.
gx, gy, gr = LX0 + 74, y + 66, 52
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(178, 216, 228),
          outline=BLUE, width=3)
# land masses (simple blobs)
d.ellipse([gx - 48, gy - 34, gx - 6, gy + 2], fill=(96, 160, 90))
d.ellipse([gx + 4, gy + 6, gx + 46, gy + 40], fill=(96, 160, 90))
d.ellipse([gx - 10, gy - 52, gx + 30, gy - 20], fill=(120, 178, 96))
# crack across the globe
d.line([(gx - 50, gy - 46), (gx - 18, gy - 8), (gx - 34, gy + 22),
        (gx + 6, gy + 44), (gx + 40, gy + 52)], fill=DARKRED, width=4)
d.line([(gx - 18, gy - 8), (gx + 12, gy - 26)], fill=DARKRED, width=3)
# red X over the globe
d.line([(gx - gr - 8, gy - gr - 8), (gx + gr + 8, gy + gr + 8)],
       fill=RED, width=5)
d.line([(gx + gr + 8, gy - gr - 8), (gx - gr - 8, gy + gr + 8)],
       fill=RED, width=5)
# pact label beside the globe
px = LX0 + 170
d.text((px, gy - 52), "THE “ANTALYA PACT”", font=font(SANS_B, 19), fill=INK)
d.text((px, gy - 26), "Final draft, Sunday:", font=font(SANS, 16), fill=GREY)
d.text((px, gy - 2), "“FOSSIL FUELS”", font=font(SANS_B, 22), fill=INK)
d.line([(px, gy + 26), (px + 200, gy + 26)], fill=RED, width=4)
d.text((px, gy + 36), "— never mentioned", font=font(SANS_B, 17), fill=RED)

y = gy + gr + 12
y = para(d, LX0 + 14, y,
         "After two weeks of talks and two days of overtime — the longest "
         "COP ever — the EU, Britain and others rejected the final text. "
         "President Murat Kurum conceded no consensus: the first no-deal "
         "COP since Copenhagen 2009.",
         font(SANS, 15), LX1 - LX0 - 28, 20)
assert y <= LY1 - 6, f"lead panel overflow: y={y}"

# ------------------------------------------------- right column: Ukraine
RX0, RX1 = 664, 988
box(d, RX0, 158, RX1, 296)
y = 158 + 10
y = kicker(d, RX0 + 12, y, "Ukraine  •  Kyiv region")
y = headline(d, RX0 + 12, y + 2, "Strikes leave 14 missing", 22,
             RX1 - RX0 - 24, leading=28)
y = para(d, RX0 + 12, y + 4,
         "A Russian drone hit a Kyiv home; a 7-year-old boy was pulled "
         "from the rubble.",
         font(SANS, 14), RX1 - RX0 - 24, 18)
assert y <= 296 - 6, f"ukraine panel overflow: y={y}"

# ------------------------------------------------- right column: US midterms
box(d, RX0, 312, RX1, 486)
y = 312 + 10
y = kicker(d, RX0 + 12, y, "United States  •  Midterms", color=BLUE)
y = headline(d, RX0 + 12, y + 2, "Democrats' biggest House win since 1992", 22,
             RX1 - RX0 - 24, leading=28)
y = para(d, RX0 + 12, y + 4,
         "At least 258 seats to the Republicans' 173 after a North "
         "Carolina flip — the largest Democratic majority in 34 years.",
         font(SANS, 14), RX1 - RX0 - 24, 18)
assert y <= 486 - 6, f"midterms panel overflow: y={y}"

# ---------------------------------------------------------------- row 2
# Libya ship (left) / South Korea (right)
box(d, 36, 502, 500, 656)
y = 502 + 10
y = kicker(d, 50, y, "Libya  •  Mediterranean")
y = headline(d, 50, y + 2, "Blast on Russian ship at Libya port", 22,
             500 - 36 - 28, leading=28)
y = para(d, 50, y + 4,
         "Officials blame a suspected drone attack on the vessel, stopped "
         "for fuel en route back to Russia. A second ship was towed away "
         "in the Gulf of Finland.",
         font(SANS, 15), 500 - 36 - 28, 19)
assert y <= 656 - 6, f"libya panel overflow: y={y}"

box(d, 516, 502, 988, 656)
y = 502 + 10
y = kicker(d, 530, y, "South Korea  •  Seoul", color=TEAL)
y = headline(d, 530, y + 2, "Education minister quits over exam-cheating scandal", 22,
             988 - 516 - 28, leading=28)
y = para(d, 530, y + 4,
         "Choi Kyo-jin resigned after last-minute measures against AI "
         "cheating in the college entrance exam caused chaos.",
         font(SANS, 14), 988 - 516 - 28, 18)
assert y <= 656 - 6, f"korea panel overflow: y={y}"

# ---------------------------------------------------------------- row 3
# Indonesia fire (left) / COP31 by numbers (right)
box(d, 36, 672, 500, 822)
y = 672 + 10
y = kicker(d, 50, y, "Indonesia  •  Factory fire", color=ORANGE)
y = headline(d, 50, y + 2, "Three killed, 36 missing in factory blaze", 22,
             500 - 36 - 28, leading=28)
y = para(d, 50, y + 4,
         "The fire tore through a confectionery factory; dozens are still "
         "unaccounted for as rescuers search the wreckage.",
         font(SANS, 14), 500 - 36 - 28, 18)
assert y <= 822 - 6, f"indonesia panel overflow: y={y}"

box(d, 516, 672, 988, 822, fill=(238, 234, 222))
y = 672 + 10
y = kicker(d, 530, y, "COP31 by numbers", color=DARKRED)
nums = [("194", "countries at the talks"),
        ("2 days", "into overtime — longest COP ever"),
        ("2009", "last COP to end with no deal")]
for big, small in nums:
    d.text((530, y), big, font=font(SERIF_B, 26), fill=DARKRED)
    d.text((640, y + 5), small, font=font(SANS, 15), fill=INK)
    y += 36
assert y <= 822 - 6, f"numbers panel overflow: y={y}"

# ---------------------------------------------------------------- also today
box(d, 36, 838, 988, 942)
d.text((52, 848), "ALSO TODAY", font=font(SANS_B, 16), fill=RED)
items = [
    ("OBITUARY", "Italian jeweller Paolo Bulgari dies aged 89."),
    ("CULTURE", "Miley Cyrus marries Maxx Morando in California."),
    ("SPORT", "Pochettino's Man Utd lose to Liverpool on his debut."),
    ("USA", "Army to detonate explosives in Iowa despite court order."),
]
col_w = (988 - 36 - 32) // 4
for i, (tag, txt) in enumerate(items):
    x = 52 + i * col_w
    d.text((x, 874), tag, font=font(SANS_B, 13), fill=GREY)
    yy = para(d, x, 892, txt, font(SANS, 13), col_w - 16, 17)
    assert yy <= 942 - 4, f"strip overflow col {i}: y={yy}"

# ---------------------------------------------------------------- footer
rule(d, 36, 958, 988, width=2)
d.text((W // 2, 968),
       "Drawn from BBC, CNN, Reuters, Le Monde and The Times — all stories reported 23 November 2026",
       font=font(SANS, 13), fill=GREY, anchor="ma")
d.text((W // 2, 988), "THE WORLD  •  MONDAY 23 NOVEMBER 2026  •  PAGE 1 OF 1",
       font=font(SANS_B, 13), fill=INK, anchor="ma")

final_y = 988 + 18
assert final_y <= H, f"page overflow: final_y={final_y}"
print(f"final y = {final_y}")
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}")
