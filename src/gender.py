# -*- coding: utf-8 -*-
"""ボーカルの性別(m/f)。音楽生成AIへのプロンプトと歌詞の一人称に反映する。"""
import random, hashlib

F_GIV2 = ("カエデ", "ミオ", "アカリ", "ノゾミ", "アオイ", "ココロ", "セナ", "ルカ", "ミズキ")
M_GIV2 = ("ミナト", "リク", "ヨウ", "リョウ", "ハヤト", "カナタ", "シュン")
SRC_G = {"米津玄師": "m", "あいみょん": "f", "藤井風": "m", "宇多田ヒカル": "f", "椎名林檎": "f", "星野源": "m", "Vaundy": "m", "Ado": "f", "Eve": "m", "aiko": "f", "スガシカオ": "m", "奥田民生": "m", "斉藤和義": "m",
         "山下達郎": "m", "竹内まりや": "f", "松任谷由実": "f", "中島みゆき": "f", "井上陽水": "m", "ミツキ": "f", "Cocco": "f", "UA": "f", "bird": "f", "MISIA": "f", "JUJU": "f", "きゃりーぱみゅぱみゅ": "f",
         "細野晴臣": "m", "坂本龍一": "m", "hide": "m", "カネコアヤノ": "f", "崎山蒼志": "m", "Awich": "f", "ZORN": "m", "KOHH": "m", "般若": "m", "ZEEBRA": "m", "Ken Yokoyama": "m", "中村一義": "m",
         "Creepy Nuts": "m", "あいみょん ": "f"}
ROMA_F = ("mina", "mio", "akari", "nozomi", "aoi", "rui", "kaede")
ROMA_M = ("haru", "riku", "kou", "tsubasa", "hikaru")


def _h(*a): return int(hashlib.md5("|".join(map(str, a)).encode()).hexdigest()[:8], 16)


def solo_gender(seed, artist, pun_src):
    if pun_src and pun_src in SRC_G: return SRC_G[pun_src]
    if any(n in artist for n in F_GIV2) or any(n in artist.lower() for n in ROMA_F): return "f"
    if any(n in artist for n in M_GIV2) or any(n in artist.lower() for n in ROMA_M): return "m"
    return "m" if _h(seed, "sg") % 100 < 55 else "f"


def vocal(c, mem):
    """その時点のボーカル性別コード: m / f / mf / fm / am / af / inst"""
    st = c['style']; seed = c['seed']
    if st == 'inst': return 'inst'
    if st in ('ai_pure', 'ai_collab'): return 'af' if _h(seed, "ai") % 2 else 'am'
    if st == 'band':
        vo = next((m for m in mem if m['r'].startswith('Vo')), None)
        return vo['g'] if vo else solo_gender(seed, c['artist'], c.get('pun_src'))
    if st == 'duo':
        if len(mem) >= 2:
            a, b = mem[0]['g'], mem[1]['g']
            return a if a == b else a + b
        return mem[0]['g'] if mem else 'm'
    return solo_gender(seed, c['artist'], c.get('pun_src'))
