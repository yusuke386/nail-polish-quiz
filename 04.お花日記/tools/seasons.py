# 2月〜12月の季節テーマのCSSを作って index.html に差し込む
import math, sys

def uri(svg):
    return "data:image/svg+xml;utf8," + svg.replace("#", "%23").replace("\n", "")

def svg(vb, body):
    return f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='{vb}'>{body}</svg>"

def tile(w, h, body, op=1):
    return f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'><g opacity='{op}'>{body}</g></svg>"

def g(x, y, s, rot, body):
    return f"<g transform='translate({x} {y}) rotate({rot}) scale({s})'>{body}</g>"

# ---------- 部品（原点中心・おおよそ半径10） ----------
HEART = "M0 7 C-9 0 -9 -8 -3.5 -8 C-1.5 -8 0 -6.5 0 -5 C0 -6.5 1.5 -8 3.5 -8 C9 -8 9 0 0 7Z"
def heart(c): return f"<path d='{HEART}' fill='{c}'/>"

def plum(c, center="#ffe08a"):
    out = "".join(f"<circle cx='{4.6*math.cos(math.radians(-90+i*72)):.2f}' cy='{4.6*math.sin(math.radians(-90+i*72)):.2f}' r='4.3' fill='{c}'/>" for i in range(5))
    return out + f"<circle r='2.2' fill='{center}'/>"

SAKURA_P = "M0 0 C-4.6 -3 -4.6 -8.6 -1.5 -10 L0 -8.3 L1.5 -10 C4.6 -8.6 4.6 -3 0 0Z"
def sakura(c, center="#f7c1cf"):
    return "".join(f"<path d='{SAKURA_P}' fill='{c}' transform='rotate({i*72})'/>" for i in range(5)) + f"<circle r='1.8' fill='{center}'/>"
def petal(c): return f"<path d='{SAKURA_P}' fill='{c}' transform='translate(0 5)'/>"

LEAF = "M0 -9 C6 -5 6 5 0 9 C-6 5 -6 -5 0 -9Z"
def leaf(c, vein="#ffffff"):
    return f"<path d='{LEAF}' fill='{c}'/><path d='M0 -7 V8' stroke='{vein}' stroke-width='1' opacity='.6'/>"

def floret(c, center="#ffffff"):
    return "".join(f"<ellipse cx='0' cy='-3.6' rx='3' ry='3.8' fill='{c}' transform='rotate({i*90})'/>" for i in range(4)) + f"<circle r='1.3' fill='{center}'/>"

DROP = "M0 -6 C3 -1 4 2 4 3.5 A4 4 0 0 1 -4 3.5 C-4 2 -3 -1 0 -6Z"
def drop(c): return f"<path d='{DROP}' fill='{c}'/>"

def sunflower(petal="#ffc93c", center="#8a5a2b"):
    return "".join(f"<ellipse cx='0' cy='-6' rx='2.3' ry='4.2' fill='{petal}' transform='rotate({i*30})'/>" for i in range(12)) + f"<circle r='4.4' fill='{center}'/>"

def wave(c, w=1.8):
    return f"<path d='M-12 0 q3 -4 6 0 t6 0 t6 0 t6 0' stroke='{c}' stroke-width='{w}' fill='none' stroke-linecap='round'/>"

def star(c, n=5, r1=9, r2=4):
    pts = []
    for i in range(n*2):
        r = r1 if i % 2 == 0 else r2
        a = math.radians(-90 + i*180/n)
        pts.append(f"{r*math.cos(a):.2f},{r*math.sin(a):.2f}")
    return f"<polygon points='{' '.join(pts)}' fill='{c}' stroke='{c}' stroke-linejoin='round' stroke-width='1.2'/>"

def crescent(c, bg):
    return f"<circle r='8' fill='{c}'/><circle cx='4' cy='-3' r='7' fill='{bg}'/>"

BAT = ("M0 -1 C-1.5 -3.5 -3.5 -3.5 -4.5 -1.5 C-6.5 -4 -10 -4 -12 -1 C-9 -1 -8.5 1.5 -7.5 3.5 "
       "C-5.5 1.5 -3 1.5 -2 3.5 C-1 2.5 1 2.5 2 3.5 C3 1.5 5.5 1.5 7.5 3.5 C8.5 1.5 9 -1 12 -1 "
       "C10 -4 6.5 -4 4.5 -1.5 C3.5 -3.5 1.5 -3.5 0 -1Z")
def bat(c): return f"<path d='{BAT}' fill='{c}'/>"

def pumpkin(c="#f59a3a", dark="#e07d1e", stem="#6aa84f"):
    return (f"<ellipse cx='-4' cy='1' rx='5' ry='6.5' fill='{dark}'/><ellipse cx='4' cy='1' rx='5' ry='6.5' fill='{dark}'/>"
            f"<ellipse cx='0' cy='1' rx='5.5' ry='7' fill='{c}'/><path d='M0 -5.5 q1 -3 3 -3.5' stroke='{stem}' stroke-width='2' fill='none' stroke-linecap='round'/>")

def maple(c):
    pts = []
    radii = [10, 4.2, 7.5, 3.8, 9, 4.2, 9, 3.8, 7.5, 4.2]
    for i, r in enumerate(radii):
        a = math.radians(-90 + i*36)
        pts.append(f"{r*math.cos(a):.2f},{r*math.sin(a):.2f}")
    return f"<polygon points='{' '.join(pts)}' fill='{c}' stroke='{c}' stroke-linejoin='round' stroke-width='1.4'/><path d='M0 2 L1.5 9' stroke='{c}' stroke-width='1.4' stroke-linecap='round'/>"

GINKGO = "M0 6 L-8.5 -3 A9.5 9.5 0 0 1 -1 -7 L0 -3.5 L1 -7 A9.5 9.5 0 0 1 8.5 -3 Z"
def ginkgo(c): return f"<path d='{GINKGO}' fill='{c}'/><path d='M0 6 L0 10' stroke='{c}' stroke-width='1.4' stroke-linecap='round'/>"

def snowflake(c, w=1.4):
    out = ""
    for a in (0, 60, 120):
        out += (f"<g transform='rotate({a})'><path d='M0 -9 V9' stroke='{c}' stroke-width='{w}' stroke-linecap='round'/>"
                f"<path d='M-2.5 -7 L0 -4.5 L2.5 -7 M-2.5 7 L0 4.5 L2.5 7' stroke='{c}' stroke-width='{w}' fill='none' stroke-linecap='round'/></g>")
    return out

def dot(c, r=1.5): return f"<circle r='{r}' fill='{c}'/>"

def place(items):
    return "".join(g(x, y, s, rot, body) for (x, y, s, rot, body) in items)

# ---------- 月ごとの設定 ----------
M = {}

# 2月 バレンタイン
M[2] = dict(
    name="バレンタイン（ハート・チョコ・ラブレター）",
    cal_bg="#fff5f6", border="#f6cfd8",
    cal_tile=tile(56, 56, place([(14,14,.55,-10,heart("#f9d2dc")),(42,40,.45,12,heart("#f3dccd"))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 40 40",
        "<path d='M20 36 C4 25 3 12 11 9 C15 7.5 18.5 9.5 20 12 C21.5 9.5 25 7.5 29 9 C37 12 36 25 20 36Z' fill='#8b5a3c'/>"
        "<path d='M20 32 C8 24 7.5 14 13 12 C16 11 18.8 12.6 20 14.6 C21.2 12.6 24 11 27 12 C32.5 14 32 24 20 32Z' fill='#a8704c'/>"
        "<path d='M20 12 V36 M6 19 H34' stroke='#f28bab' stroke-width='3'/>"
        "<path d='M20 12 C14 4 9 8 13 11 Z M20 12 C26 4 31 8 27 11 Z' fill='#f28bab'/><circle cx='20' cy='12' r='2.4' fill='#e0617f'/>"),
    right=svg("0 0 40 40",
        "<rect x='4' y='11' width='32' height='22' rx='3' fill='#fff' stroke='#f3c4cf' stroke-width='1.5'/>"
        "<path d='M5 12 L20 24 L35 12' fill='none' stroke='#f3c4cf' stroke-width='1.5'/>"
        + g(20, 23, .62, 0, heart("#e0526f"))),
    label=svg("0 0 24 20", g(12, 11, 1.05, 0, heart("#e0526f"))),
    today="#fde2e8", today_n="#e0526f", sel="#c93d5c", n="#c93d5c",
    wk=("#fde8ed", "#fad3dd", "#c93d5c"),
    page_bg="#fff1f4", topbar="rgba(255,241,244,.97)",
    page_tile=tile(200, 200, place([
        (30,30,.7,-12,heart("#f6b6c6")),(150,52,.55,14,heart("#e9c3a8")),(90,110,.8,6,heart("#f8c6d3")),
        (22,150,.5,-20,heart("#e9c3a8")),(170,160,.65,-8,heart("#f6b6c6")),(110,185,.4,10,heart("#f8c6d3")),
        (64,70,1,0,dot("#e9c3a8",1.6)),(180,110,1,0,dot("#f6b6c6",1.8)),(120,20,1,0,dot("#f6b6c6",1.4))]), .8),
)

# 3月 梅
M[3] = dict(
    name="梅（紅梅・白梅・うぐいす）",
    cal_bg="#fff7f6", border="#f3d3d3",
    cal_tile=tile(56, 56, place([(14,14,.5,0,plum("#f8d0d4","#fbe6b0")),(42,40,.42,20,plum("#f3e6e8","#fbe6b0"))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 40 40",
        "<path d='M3 37 C10 30 14 24 19 17 C23 11 29 8 37 5' stroke='#7a5236' stroke-width='3' fill='none' stroke-linecap='round'/>"
        "<path d='M16 21 C20 24 25 25 30 24' stroke='#7a5236' stroke-width='2' fill='none' stroke-linecap='round'/>"
        + g(12, 27, .75, 0, plum("#e5566a", "#ffd966")) + g(25, 11, .7, 15, plum("#fff", "#ffd966"))
        + g(31, 23, .55, 30, plum("#e5566a", "#ffd966")) + "<circle cx='35' cy='6' r='2' fill='#e5566a'/>"),
    right=svg("0 0 40 40",
        "<path d='M4 24 C4 16 12 12 20 14 C26 11 33 13 34 19 C35 26 28 31 19 31 C11 31 4 29 4 24Z' fill='#a3b54a'/>"
        "<path d='M14 21 C18 18 24 18 27 22 C23 26 17 26 14 21Z' fill='#8c9d38'/>"
        "<circle cx='29' cy='17' r='1.6' fill='#3b3b2b'/><path d='M34 18 L38.5 19 L34 20.5Z' fill='#6b5a2e'/>"
        "<path d='M4 24 L-1 22 L1 27Z' fill='#8c9d38'/><circle cx='31' cy='21' r='1.8' fill='#f3c1c6' opacity='.8'/>"),
    label=svg("0 0 24 20", g(12, 10, .95, 0, plum("#e5566a", "#ffd966"))),
    today="#fde4e6", today_n="#d6485c", sel="#c23c4f", n="#c23c4f",
    wk=("#fde9ea", "#fad6d9", "#c23c4f"),
    page_bg="#fff5f3", topbar="rgba(255,245,243,.97)",
    page_tile=tile(200, 200, place([
        (32,34,.8,0,plum("#f4a8b3","#fbe0a0")),(150,56,.6,20,plum("#f7e1e4","#fbe0a0")),(92,118,.7,40,plum("#f4a8b3","#fbe0a0")),
        (24,160,.55,10,plum("#f7e1e4","#fbe0a0")),(168,164,.75,-15,plum("#f4a8b3","#fbe0a0")),
        (66,80,1,0,dot("#f4a8b3",1.6)),(186,112,1,0,dot("#f7c9cf",1.8)),(120,180,1,0,dot("#f4a8b3",1.4))]), .75),
)

# 4月 桜
M[4] = dict(
    name="桜（桜の枝・三色団子・花びら）",
    cal_bg="#fff6f9", border="#f8d3df",
    cal_tile=tile(56, 56, place([(14,14,.5,0,sakura("#fbd5e0","#fbe3ea")),(42,40,.5,40,petal("#fbd5e0"))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 40 40",
        "<path d='M2 36 C9 30 14 23 20 17 C25 12 31 9 38 8' stroke='#8a5a44' stroke-width='3' fill='none' stroke-linecap='round'/>"
        "<path d='M17 20 C19 25 23 28 28 29' stroke='#8a5a44' stroke-width='2' fill='none' stroke-linecap='round'/>"
        + g(12, 27, .85, 0, sakura("#f7a8c0", "#e0668b")) + g(26, 12, .8, 20, sakura("#fbc7d6", "#e0668b"))
        + g(30, 28, .6, 40, sakura("#f7a8c0", "#e0668b"))),
    right=svg("0 0 40 40",
        "<path d='M8 36 L33 5' stroke='#c9a06a' stroke-width='2.4' stroke-linecap='round'/>"
        "<circle cx='26' cy='13' r='7' fill='#f7a8c0'/><circle cx='20' cy='21' r='7' fill='#ffffff' stroke='#f0e4e6'/>"
        "<circle cx='14' cy='29' r='7' fill='#a8d38c'/>"),
    label=svg("0 0 24 20", g(12, 10.5, .95, 0, sakura("#f28bab", "#ffe08a"))),
    today="#ffe4ec", today_n="#e97a9a", sel="#d25c80", n="#d25c80",
    wk=("#ffebf1", "#fdd6e2", "#d25c80"),
    page_bg="#fff4f8", topbar="rgba(255,244,248,.97)",
    page_tile=tile(200, 200, place([
        (30,30,.8,0,sakura("#f9bfd0","#f49ab5")),(150,50,.8,30,petal("#f9bfd0")),(92,110,.75,15,sakura("#fbd2de","#f49ab5")),
        (26,150,.8,-40,petal("#fbd2de")),(170,150,.7,10,sakura("#f9bfd0","#f49ab5")),(110,185,.8,60,petal("#f9bfd0")),
        (60,74,.7,100,petal("#fbd2de")),(186,104,.6,-20,petal("#f9bfd0"))]), .75),
)

# 5月 新緑
M[5] = dict(
    name="新緑（若葉・鯉のぼり）",
    cal_bg="#f5fbf1", border="#cfe7c3",
    cal_tile=tile(56, 56, place([(14,14,.5,-30,leaf("#d5edc7")),(42,40,.45,35,leaf("#e3f3d6"))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 34 46",
        "<path d='M4 3 V45' stroke='#9a7650' stroke-width='2.4' stroke-linecap='round'/><circle cx='4' cy='3' r='2.2' fill='#f4c95d'/>"
        "<path d='M5 7 H27 L22 12 L27 17 H5Z' fill='#4a82c9'/><circle cx='9.5' cy='11' r='2' fill='#fff'/><circle cx='9.5' cy='11' r='1' fill='#233'/>"
        "<path d='M13 9 q2 2 0 4 M17 9 q2 2 0 4' stroke='#b9d4f2' stroke-width='1.1' fill='none'/>"
        "<path d='M5 20 H24 L19.5 24.5 L24 29 H5Z' fill='#e8606d'/><circle cx='9.5' cy='23.5' r='1.8' fill='#fff'/><circle cx='9.5' cy='23.5' r='.9' fill='#233'/>"
        "<path d='M13 21.5 q2 2 0 4 M17 21.5 q2 2 0 4' stroke='#f6b9bf' stroke-width='1.1' fill='none'/>"),
    right=svg("0 0 40 40",
        "<path d='M20 38 V20' stroke='#6aa84f' stroke-width='2.6' stroke-linecap='round'/>"
        + g(12, 17, 1.05, -50, leaf("#8bc76e")) + g(28, 14, 1.15, 45, leaf("#6fb356"))),
    label=svg("0 0 24 20", g(12, 10, .95, 40, leaf("#6fb356"))),
    today="#e4f4db", today_n="#5aa55a", sel="#4a8a44", n="#4a8a44",
    wk=("#e8f5e0", "#d4ecc6", "#4a8a44"),
    page_bg="#f3faee", topbar="rgba(243,250,238,.97)",
    page_tile=tile(200, 200, place([
        (30,30,.9,-30,leaf("#c7e6b3")),(150,50,.7,40,leaf("#b6dea0")),(92,112,.85,10,leaf("#d3ecc3")),
        (26,152,.7,60,leaf("#b6dea0")),(170,158,.85,-20,leaf("#c7e6b3")),(112,184,.6,80,leaf("#d3ecc3")),
        (64,74,1,0,dot("#c7e6b3",1.6)),(186,104,1,0,dot("#b6dea0",1.8))]), .75),
)

# 6月 紫陽花
M[6] = dict(
    name="紫陽花（紫陽花・てるてる坊主・雨つぶ）",
    cal_bg="#f6f4fd", border="#d9d3f3",
    cal_tile=tile(56, 56, place([(14,14,.55,0,floret("#dcd5f6")),(42,40,.55,0,drop("#d6e6f7"))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 40 40",
        g(9, 31, .9, -40, leaf("#6fb356")) + g(30, 32, .8, 40, leaf("#6fb356"))
        + "".join(g(x, y, .62, r, floret(c, "#fff")) for x, y, r, c in [
            (14,14,0,"#8e9be6"),(24,11,20,"#a88fe0"),(31,19,10,"#8e9be6"),(19,22,30,"#b4a4ec"),
            (9,21,15,"#a88fe0"),(27,26,5,"#b4a4ec"),(20,30,25,"#8e9be6")])),
    right=svg("0 0 40 40",
        "<path d='M20 3 V8' stroke='#b7b1c7' stroke-width='1.2'/>"
        "<path d='M11 20 L7 36 L20 31 L33 36 L29 20Z' fill='#fff' stroke='#e2dcef' stroke-width='1.2'/>"
        "<circle cx='20' cy='16' r='9' fill='#fff' stroke='#e2dcef' stroke-width='1.2'/>"
        "<path d='M11 22 Q20 26 29 22' stroke='#8e9be6' stroke-width='2' fill='none'/>"
        "<circle cx='17' cy='15' r='1.2' fill='#4a3a41'/><circle cx='23' cy='15' r='1.2' fill='#4a3a41'/>"
        "<path d='M17 19 Q20 21 23 19' stroke='#4a3a41' stroke-width='1.1' fill='none' stroke-linecap='round'/>"
        "<circle cx='14.5' cy='18' r='1.4' fill='#f7b6c6' opacity='.8'/><circle cx='25.5' cy='18' r='1.4' fill='#f7b6c6' opacity='.8'/>"),
    label=svg("0 0 24 20",
        "<path d='M2 10 A10 9 0 0 1 22 10 Q19.5 8 17 10 Q14.5 8 12 10 Q9.5 8 7 10 Q4.5 8 2 10Z' fill='#8e9be6'/>"
        "<path d='M12 10 V16.5 A2 2 0 0 1 8 16.5' stroke='#7a6aa8' stroke-width='1.6' fill='none' stroke-linecap='round'/>"),
    today="#ebe7fb", today_n="#8a7cd6", sel="#6b5cc0", n="#6b5cc0",
    wk=("#eeebfc", "#dfd9f7", "#6b5cc0"),
    page_bg="#f4f2fc", topbar="rgba(244,242,252,.97)",
    page_tile=tile(200, 200, place([
        (30,30,.8,0,floret("#cdc5f2")),(150,50,.8,0,drop("#c8dcf3")),(92,110,.8,15,floret("#c9d2f3")),
        (26,150,.7,0,drop("#cdc5f2")),(170,152,.8,20,floret("#d8cff4")),(112,184,.7,0,drop("#c8dcf3")),
        (64,72,.6,0,drop("#c8dcf3")),(186,102,.6,0,floret("#cdc5f2"))]), .75),
)

# 7月 ひまわり
M[7] = dict(
    name="ひまわり（ひまわり・麦わら帽子）",
    cal_bg="#fffbeb", border="#f6e2a4",
    cal_tile=tile(56, 56, place([(14,14,.5,0,sunflower("#fbe7a6","#f0d9a8")),(42,40,.9,0,dot("#fbe7a6",2.2))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 34 46",
        "<path d='M17 26 V45' stroke='#6aa84f' stroke-width='3' stroke-linecap='round'/>"
        + g(11, 37, .75, -50, leaf("#7fbf63")) + g(23, 34, .7, 50, leaf("#6fb356"))
        + g(17, 16, 1.25, 0, sunflower("#ffc93c", "#8a5a2b")) + "<circle cx='17' cy='16' r='3' fill='#6e4420'/>"),
    right=svg("0 0 40 40",
        "<ellipse cx='20' cy='26' rx='18' ry='7' fill='#e8c27a'/>"
        "<path d='M9 25 C9 12 31 12 31 25 Z' fill='#f0cf8a'/>"
        "<path d='M9.5 22 C14 24.5 26 24.5 30.5 22 L31 25 C26 27.5 14 27.5 9 25Z' fill='#e0525f'/>"
        "<path d='M13 19 q7 -4 14 0' stroke='#dcb56c' stroke-width='1' fill='none'/>"),
    label=svg("0 0 24 20", g(12, 10, .85, 0, sunflower("#ffc93c", "#8a5a2b"))),
    today="#fff1c7", today_n="#f0a020", sel="#d08a10", n="#c98a0e",
    wk=("#fff4d3", "#ffe8a8", "#b87a08"),
    page_bg="#fffae6", topbar="rgba(255,250,230,.97)",
    page_tile=tile(200, 200, place([
        (30,30,.75,0,sunflower("#fbe08a","#e8c79a")),(150,54,.55,15,sunflower("#fbe08a","#e8c79a")),(92,112,.65,5,sunflower("#fbe08a","#e8c79a")),
        (26,156,.5,0,sunflower("#fbe08a","#e8c79a")),(170,160,.7,20,sunflower("#fbe08a","#e8c79a")),
        (64,76,1,0,dot("#fbe08a",1.8)),(186,108,1,0,dot("#fbe08a",2)),(118,184,1,0,dot("#f6d27a",1.6))]), .7),
)

# 8月 海
M[8] = dict(
    name="海（波・貝がら・浮き輪）",
    cal_bg="#effafd", border="#c3e6f2",
    cal_tile=tile(48, 24, place([(24,12,1,0,wave("#d3eef7",1.6))])),
    cal_tile_size="48px 24px",
    left=svg("0 0 40 40",
        "<path d='M20 36 L5 17 C5 9 12 5 20 5 C28 5 35 9 35 17 Z' fill='#f7b3bf'/>"
        "<path d='M20 36 L10 10 M20 36 L15 6.5 M20 36 V5 M20 36 L25 6.5 M20 36 L30 10' stroke='#fbd6dd' stroke-width='1.6'/>"
        "<path d='M16 33 H24 L22 38 H18Z' fill='#ee9aa9'/>"),
    right=svg("0 0 40 40",
        "<circle cx='20' cy='20' r='16' fill='#ffffff'/>"
        "<path d='M20 4 A16 16 0 0 1 36 20 L28 20 A8 8 0 0 0 20 12Z' fill='#f0606f'/>"
        "<path d='M20 36 A16 16 0 0 1 4 20 L12 20 A8 8 0 0 0 20 28Z' fill='#f0606f'/>"
        "<circle cx='20' cy='20' r='8' fill='#eaf7fb'/><circle cx='20' cy='20' r='16' fill='none' stroke='#e3eef2' stroke-width='1'/>"),
    label=svg("0 0 24 20", g(12, 7, .9, 0, wave("#3fa9d6", 2.4)) + g(12, 13, .9, 0, wave("#8fd0ea", 2.4))),
    today="#dcf2fa", today_n="#3fa9d6", sel="#2d8fb9", n="#2d8fb9",
    wk=("#e2f4fb", "#cdebf6", "#2d8fb9"),
    page_bg="#eef9fd", topbar="rgba(238,249,253,.97)",
    page_tile=tile(200, 200, place([
        (40,30,1.1,0,wave("#bfe4f2",1.8)),(150,60,.9,0,wave("#cdeaf5",1.8)),(80,120,1,0,wave("#bfe4f2",1.8)),(170,160,.9,0,wave("#cdeaf5",1.8)),
        (26,160,.6,15,star("#f9c7a7",5,8,3.6)),(122,20,1,0,"<circle r='3' fill='none' stroke='#bfe4f2' stroke-width='1.2'/>"),
        (186,112,1,0,"<circle r='2.2' fill='none' stroke='#bfe4f2' stroke-width='1.2'/>"),(58,84,1,0,"<circle r='1.8' fill='none' stroke='#bfe4f2' stroke-width='1.2'/>")]), .8),
)

# 9月 お月見
M[9] = dict(
    name="お月見（満月・すすき・月見団子）",
    cal_bg="#fbf8ee", border="#ecdcb4",
    cal_tile=tile(56, 56, place([(14,14,.5,0,crescent("#f3e2b2","#fbf8ee")),(42,40,.4,0,star("#efe0bd",5,8,3.6))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 34 46",
        "<path d='M10 45 C11 32 9 20 5 10 M17 45 C17 30 18 18 22 6 M24 45 C24 34 27 26 31 18' stroke='#b89560' stroke-width='1.6' fill='none' stroke-linecap='round'/>"
        "<path d='M5 10 C2 14 3 19 6 22 C7 18 7 14 5 10Z M22 6 C19 9 19 15 21 18 C23 15 24 10 22 6Z M31 18 C27 20 26 25 28 28 C30 25 32 22 31 18Z' fill='#e2c68f'/>"
        "<path d='M9 36 C4 33 2 28 3 24 M18 38 C23 34 27 32 30 32' stroke='#9fb56a' stroke-width='1.4' fill='none' stroke-linecap='round'/>"),
    right=svg("0 0 40 40",
        "<rect x='6' y='30' width='28' height='4' rx='1' fill='#d9b27a'/><path d='M9 34 H31 L29 39 H11Z' fill='#c79a5e'/>"
        + "".join(f"<circle cx='{x}' cy='{y}' r='4.4' fill='#fffdf6' stroke='#eadfc8' stroke-width='1'/>" for x, y in
                  [(11,26),(20,26),(29,26),(15.5,19),(24.5,19),(20,12)])),
    label=svg("0 0 24 20", "<circle cx='12' cy='10' r='8' fill='#f6d676'/><circle cx='9.5' cy='8' r='1.6' fill='#ecc35a'/><circle cx='14' cy='12.5' r='1.2' fill='#ecc35a'/>"),
    today="#f7eed6", today_n="#d0a045", sel="#d2ae62", n="#9a7430",
    wk=("#f8f0dc", "#efe1bd", "#9a7430"),
    page_bg="#f4f2fa", topbar="rgba(244,242,250,.97)",
    page_tile=tile(200, 200, place([
        (34,34,.8,0,crescent("#efd99a","#f4f2fa")),(150,52,.5,0,star("#e5d6a8",5,8,3.6)),(92,112,.45,15,star("#dcd4ee",5,8,3.6)),
        (26,154,.4,0,star("#e5d6a8",5,8,3.6)),(168,158,.6,0,crescent("#e9d6a6","#f4f2fa")),
        (64,78,1,0,dot("#e5d6a8",1.5)),(186,106,1,0,dot("#dcd4ee",1.8)),(118,186,1,0,dot("#e5d6a8",1.4))]), .8),
)

# 10月 ハロウィン
M[10] = dict(
    name="ハロウィン（かぼちゃ・おばけ・コウモリ）",
    cal_bg="#fff6ed", border="#f5d6b6",
    cal_tile=tile(56, 56, place([(14,14,.5,0,pumpkin("#fbdcbb","#f7cfa6","#cfe3c3")),(42,40,.5,0,bat("#e6d9f0"))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 40 40",
        "<ellipse cx='12' cy='24' rx='9' ry='11' fill='#e07d1e'/><ellipse cx='28' cy='24' rx='9' ry='11' fill='#e07d1e'/>"
        "<ellipse cx='20' cy='24' rx='10' ry='12' fill='#f59a3a'/>"
        "<path d='M20 12 q1 -5 5 -6' stroke='#5f8f45' stroke-width='3' fill='none' stroke-linecap='round'/>"
        "<path d='M12 20 L16 24 L10 24Z M28 20 L24 24 L30 24Z' fill='#5a3a1a'/>"
        "<path d='M11 28 Q20 35 29 28 L26 29 L24 27 L22 29.5 L20 27 L18 29.5 L16 27 L14 29Z' fill='#5a3a1a'/>"),
    right=svg("0 0 40 40",
        "<path d='M8 36 V17 A12 12 0 0 1 32 17 V36 L28 32.5 L24 36 L20 32.5 L16 36 L12 32.5Z' fill='#ffffff' stroke='#e6def0' stroke-width='1.2'/>"
        "<ellipse cx='16' cy='18' rx='2' ry='2.8' fill='#4a3a41'/><ellipse cx='24' cy='18' rx='2' ry='2.8' fill='#4a3a41'/>"
        "<ellipse cx='20' cy='24.5' rx='2.4' ry='1.8' fill='#4a3a41'/>"
        "<circle cx='12.5' cy='22' r='1.6' fill='#f7b6c6' opacity='.8'/><circle cx='27.5' cy='22' r='1.6' fill='#f7b6c6' opacity='.8'/>"),
    label=svg("0 0 24 20", g(12, 11, .9, 0, pumpkin())),
    today="#ffe7d1", today_n="#f08a24", sel="#8b5cc0", n="#c96a12",
    wk=("#fdeede", "#f3e3f7", "#8b5cc0"),
    page_bg="#fbf4ff", topbar="rgba(251,244,255,.97)",
    page_tile=tile(200, 200, place([
        (34,32,.8,-8,bat("#d9c6ec")),(150,52,.7,0,pumpkin("#f8c99a","#f5bb84","#bfd8b0")),(92,112,.7,10,bat("#e2d3f0")),
        (26,154,.6,0,pumpkin("#f8c99a","#f5bb84","#bfd8b0")),(168,160,.8,-12,bat("#d9c6ec")),
        (64,78,.4,0,star("#f8d7a8",5,8,3.6)),(186,106,1,0,dot("#d9c6ec",1.8)),(118,186,.4,0,star("#f8d7a8",5,8,3.6))]), .8),
)

# 11月 紅葉
M[11] = dict(
    name="紅葉（もみじ・いちょう・どんぐり）",
    cal_bg="#fff6f0", border="#f4d2c0",
    cal_tile=tile(56, 56, place([(14,14,.55,-15,maple("#f8d3c2")),(42,40,.5,20,ginkgo("#f6e3b0"))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 40 40",
        g(15, 16, 1.25, -15, maple("#e2553a")) + g(28, 28, .95, 25, maple("#f08a3c")) + g(10, 32, .7, 10, maple("#f5b53d"))),
    right=svg("0 0 40 40",
        "<path d='M8 18 C8 8 32 8 32 18 Z' fill='#8a5a34'/>"
        "<path d='M9 17 H31' stroke='#6e4424' stroke-width='1.2'/><path d='M13 13 H27 M11 15 H29' stroke='#a8764a' stroke-width='1'/>"
        "<path d='M10 18 H30 C30 30 24 36 20 37 C16 36 10 30 10 18Z' fill='#c98b4e'/>"
        "<path d='M14 21 C14 27 16 31 19 33' stroke='#e0ad78' stroke-width='1.6' fill='none' stroke-linecap='round'/>"
        "<path d='M20 8.5 V4' stroke='#6e4424' stroke-width='2' stroke-linecap='round'/>"),
    label=svg("0 0 24 20", g(12, 9.5, .85, 0, maple("#e2553a"))),
    today="#fde3d8", today_n="#df6a3f", sel="#b94a28", n="#b94a28",
    wk=("#fdeae1", "#fad6c5", "#b94a28"),
    page_bg="#fff4ec", topbar="rgba(255,244,236,.97)",
    page_tile=tile(200, 200, place([
        (32,32,.85,-15,maple("#f5b4a0")),(150,52,.75,20,ginkgo("#f5dc98")),(92,112,.8,30,maple("#f8c49b")),
        (26,154,.7,-20,ginkgo("#f5dc98")),(170,158,.85,10,maple("#f5b4a0")),(114,184,.6,45,maple("#f8c49b")),
        (64,76,1,0,dot("#f5b4a0",1.6)),(186,106,1,0,dot("#f5dc98",1.8))]), .75),
)

# 12月 クリスマス
M[12] = dict(
    name="クリスマス（ツリー・プレゼント・雪の結晶）",
    cal_bg="#f8fcf9", border="#cfe5d4",
    cal_tile=tile(56, 56, place([(14,14,.6,0,snowflake("#d7e9dc",1.4)),(42,40,.45,0,snowflake("#f3d3d6",1.4))])),
    cal_tile_size="56px 56px",
    left=svg("0 0 34 46",
        "<rect x='14.5' y='38' width='5' height='7' fill='#9a7650'/>"
        "<path d='M17 5 L27 19 H22 L30 30 H24 L32 40 H2 L10 30 H4 L12 19 H7Z' fill='#4f9a5e'/>"
        + g(17, 5, .55, 0, star("#f4c95d", 5, 9, 4))
        + "".join(f"<circle cx='{x}' cy='{y}' r='1.9' fill='{c}'/>" for x, y, c in
                  [(14,17,'#e0525f'),(21,24,'#f4c95d'),(11,29,'#f4c95d'),(20,33,'#e0525f'),(26,36,'#8ec3f0'),(8,37,'#e0525f')])),
    right=svg("0 0 40 40",
        "<rect x='6' y='17' width='28' height='20' rx='2' fill='#e0525f'/><rect x='4' y='12' width='32' height='7' rx='2' fill='#ec6c77'/>"
        "<rect x='17.5' y='12' width='5' height='25' fill='#4f9a5e'/>"
        "<path d='M20 12 C13 4 8 9 13 12 Z M20 12 C27 4 32 9 27 12 Z' fill='#4f9a5e'/><circle cx='20' cy='12' r='2.2' fill='#3f7d4b'/>"),
    label=svg("0 0 24 20",
        g(8, 10, .6, -35, "<path d='M0 -9 C3 -7 5 -4 4 -1 C6 1 6 4 4 6 C3 8 1 9 0 9 C-1 9 -3 8 -4 6 C-6 4 -6 1 -4 -1 C-5 -4 -3 -7 0 -9Z' fill='#4f9a5e'/>")
        + g(16, 10, .6, 35, "<path d='M0 -9 C3 -7 5 -4 4 -1 C6 1 6 4 4 6 C3 8 1 9 0 9 C-1 9 -3 8 -4 6 C-6 4 -6 1 -4 -1 C-5 -4 -3 -7 0 -9Z' fill='#5fae6a'/>")
        + "<circle cx='10.5' cy='13' r='2.2' fill='#e0525f'/><circle cx='13.5' cy='13' r='2.2' fill='#e0525f'/><circle cx='12' cy='10.8' r='2.2' fill='#ec6c77'/>"),
    today="#fde4e4", today_n="#d9434f", sel="#3c8a4f", n="#c23c48",
    wk=("#e8f4ea", "#d4ebd9", "#3c8a4f"),
    page_bg="#f3f8f4", topbar="rgba(243,248,244,.97)",
    page_tile=tile(200, 200, place([
        (32,32,.85,0,snowflake("#c9e0cf",1.4)),(150,52,.7,20,snowflake("#f1c6ca",1.4)),(92,112,.9,10,snowflake("#c9e0cf",1.4)),
        (26,154,.5,0,star("#f4dc9a",5,8,3.6)),(170,158,.8,-10,snowflake("#c9e0cf",1.4)),(116,186,.45,0,star("#f1c6ca",5,8,3.6)),
        (64,78,1,0,dot("#f1c6ca",1.6)),(186,106,1,0,dot("#c9e0cf",1.8))]), .8),
)

TALL = {5, 7, 9, 12}   # 縦長の左上イラスト（34×46）

def css_for(m, c):
    left_size = "width:30px;height:40px;top:-20px;left:-4px;" if m in TALL else "width:34px;height:34px;top:-16px;left:-6px;"
    return f"""
  /* {m}月：{c['name']} */
  body[data-season="{m}"]{{background-color:{c['page_bg']};background-image:url("{uri(c['page_tile'])}")}}
  body[data-season="{m}"] .topbar{{background:{c['topbar']}}}
  .nav .label[data-season="{m}"]::before{{display:inline-block;background-image:url("{uri(c['label'])}")}}
  .cal[data-season="{m}"]{{
    border-color:{c['border']};
    background-color:{c['cal_bg']};
    background-image:url("{uri(c['cal_tile'])}");
    background-size:{c['cal_tile_size']};
  }}
  .cal[data-season="{m}"]::before{{-webkit-mask:none;mask:none;transform:none;background:url("{uri(c['left'])}") center/contain no-repeat;{left_size}}}
  .cal[data-season="{m}"]::after{{-webkit-mask:none;mask:none;transform:none;background:url("{uri(c['right'])}") center/contain no-repeat;width:30px;height:30px;top:-16px;right:-9px}}
  .cal[data-season="{m}"] .day{{background:rgba(255,255,255,.82)}}
  .cal[data-season="{m}"] .day.today{{background:{c['today']}}}
  .cal[data-season="{m}"] .day.today .n{{background:{c['today_n']}}}
  .cal[data-season="{m}"] .day.sel{{box-shadow:0 0 0 2px {c['sel']} inset}}
  .cal[data-season="{m}"] .day.has-photo .n{{color:{c['n']}}}
  .cal[data-season="{m}"] .wk{{background:linear-gradient({c['wk'][0]},{c['wk'][1]});color:{c['wk'][2]}}}"""

BEGIN = "  /* ---- 2月〜12月（seasons.py で生成） ---- */"
END = "  /* ---- 2月〜12月ここまで ---- */"
block = BEGIN + "".join(css_for(m, M[m]) for m in range(2, 13)) + "\n" + END + "\n"

path = sys.argv[1]
s = open(path, encoding="utf-8").read()
if BEGIN in s:
    a = s.index(BEGIN); b = s.index(END) + len(END) + 1
    s = s[:a] + block + s[b:]
else:
    anchor = '  .cal[data-season="1"] .wk{background:linear-gradient(#fdebe8,#fbd9d4);color:#c9474f}\n'
    assert s.count(anchor) == 1
    s = s.replace(anchor, anchor + block)
open(path, "w", encoding="utf-8").write(s)
print("ok", len(block))
