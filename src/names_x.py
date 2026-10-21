# -*- coding: utf-8 -*-
"""アーティスト名・曲名を大量に作る(時代の色つき)。ランタイムの差し替え用バンクを生成する。"""
import random, json, sys
sys.path.insert(0, '/home/claude')

# ---------- 語彙 ----------
N = ("郵便受け ガードレール 公衆電話 ひまわり ミルクティー 写真館 月曜日 飛行機雲 鉄塔 夕立 文房具 裏通り 時刻表 乾電池 洗濯機 水族館 図書館 灯台 屋上 踊り場 公園 歩道橋 缶コーヒー 扇風機 "
     "ストーブ 目覚まし 定期券 回転寿司 ラムネ カセット 傘立て 防波堤 商店街 銭湯 団地 タクシー 海岸線 天気予報 マフラー ブランコ プラネタリウム 改札 踏切 自販機 コンビニ 終電 始発 台風 花火 "
     "夏休み 通学路 校庭 体育館 保健室 放課後 卒業アルバム 制服 自転車 バス停 国道 路地 ベランダ 窓際 食卓 湯気 冷蔵庫 蛍光灯 輪ゴム 消しゴム 鉛筆 万華鏡 風鈴 金魚 蚊取り線香 麦茶 "
     "かき氷 ひこうき 流れ星 入道雲 虹 霧 雪 木漏れ日 陽炎 夕焼け 夜明け 真夜中 満月 三日月 潮風 砂浜 波止場 桟橋 渡し船 観覧車 メリーゴーランド 遊園地 映画館 喫茶店 ジュークボックス "
     "レコード 針 ラジオ テレビ ビデオ カメラ フィルム 現像 ポラロイド 手紙 切手 葉書 電報 ポケベル ガラケー 留守電 公衆トイレ 路線図 乗り換え 終着駅 ホーム 車窓 トンネル 峠 坂道 "
     "階段 非常口 エレベーター 屋根裏 押し入れ 縁側 庭 垣根 畑 田んぼ 川原 土手 橋 渡り廊下 校舎 黒板 チョーク 給食 運動会 文化祭 修学旅行 夏祭り 屋台 提灯 盆踊り 神社 お守り おみくじ").split()
A = ("不確かな 最後の 三日目の 優しい 無数の 夜更かしの ぼやけた さえない ふやけた ちぎれた 薄情な ぐるぐるの ひねくれた 低温の 午前三時の 臆病な 裸足の 退屈な 古い 眠そうな 孤独な 片道の "
     "夕暮れの 真夏の 甘い 苦い 不機嫌な 使い捨ての 曇りの 四畳半の 未来の 壊れた 銀色の 朝焼けの 無料の 透明な 半透明の 間に合わない 行き止まりの ぬるい 眠れない 懐かしい 見知らぬ "
     "ささやかな 不器用な 無口な 眠たげな ひとりきりの はじまりの おわりの 途中の 名もない 忘れられた 借り物の 逆さまの 傾いた すれ違いの 手のひらの 夜行の 各駅停車の 十七歳の").split()
EMO = ("寂しさ やさしさ 後悔 期待 焦り ためらい 照れ隠し 嫉妬 憧れ 諦め 迷い 予感 余韻 面影 未練 強がり ひとりごと 空騒ぎ 勘違い 寝ぼけ まぼろし 気まぐれ 見栄 つよがり 甘え 名残 "
       "あくび ため息 すれ違い 思い出し笑い 寝坊 鼻歌 空回り 負けず嫌い 臆病 弱音 本音 嘘 言い訳 約束 秘密 願い 祈り").split()
TIM = ("月曜日 日曜日 午前三時 夏の終わり 梅雨明け 冬至 大晦日 夜明け前 放課後 終電後 日没 十五夜 春一番 土曜の夜 昼下がり 真夜中 週末 朝焼け 雨上がり 三月 八月 十一月 年の暮れ 元日 "
       "夕立のあと 帰り道 寝る前 食後 午後四時 午前零時 明け方 十七時 夜の九時 満員電車 連休明け 誕生日 卒業式 始業式 終業式 引っ越しの日").split()
PLC = ("高円寺 下北沢 新宿 渋谷 中野 吉祥寺 梅田 心斎橋 栄 博多 札幌 仙台 三宮 横浜 江ノ島 阿佐ヶ谷 西荻 北千住 京都 神戸 長崎 那覇 函館 金沢 名古屋 広島 小倉 松山 高松 岡山 熊本 鹿児島 "
       "青森 盛岡 秋田 山形 福島 水戸 宇都宮 前橋 熊谷 千葉 川崎 鎌倉 小田原 静岡 浜松 岐阜 津 大津 奈良 和歌山 鳥取 松江 山口 徳島 高知 福岡 佐賀 大分 宮崎 国立 町田 立川 八王子 西尾").split()
VB = ("忘れる 笑う 泣く 走る 眠る 燃える 溶ける 帰る 待つ 歌う 踊る 話す 探す 迷う 見送る 振り返る 立ち止まる 数える 拾う 投げる 送る 渡す 受け取る 許す 信じる 願う 祈る 逃げる 追いかける 消える").split()
VBO = ("忘れる 探す 見送る 数える 拾う 投げる 送る 渡す 受け取る 許す 信じる 願う 祈る 追いかける 預かる 借りる 思い出す").split()
VBI = ("燃える 溶ける 帰る 眠る 笑う 泣く 走る 踊る 迷う 消える 止まる 揺れる 光る").split()
VBP = ("忘れない 泣かない 帰れない 眠れない 止まらない 終わらない 言えない 会えない 戻れない 負けない 迷わない 逃げない 諦めない 変わらない 消えない 離さない 動けない 言わない 知らない 気づかない").split()
VBT = ("忘れたい 会いたい 帰りたい 眠りたい 歌いたい 逃げたい 笑いたい 変わりたい 走りたい 戻りたい 話したい 触れたい 終わりたくない 消えたい 気づきたい").split()
PERS = ("きみ ぼく わたし あの子 あいつ 誰か みんな ふたり ぼくら きみたち あなた 彼女 彼 おれ あたし うち").split()
KAT = ("シグナル ハイライト ミッドナイト サンデー ラストダンス ノスタルジア スローモーション プラットフォーム アンブレラ ブルーバード パラレル メランコリー ハニー ゴースト ネオン セレナーデ "
       "ララバイ ロンリー ミラージュ コンパス フラッシュバック ドリーマー メモリー ハーモニー カーニバル パレード ルーキー ウィークエンド エスケープ リフレイン ナイトクルーズ モノクローム "
       "サイレン ジャンクション ラビリンス レイニー ボーダー ステレオ フリーウェイ オルゴール シンクロ リバーブ アナログ シャンデリア ブルース ポラリス スプートニク ピクニック スウィング").split()
EN = ("LOST FOUND MIDNIGHT SUNDAY NEON PAPER GLASS VELVET RUSTY SILENT BROKEN HOLLOW TINY SLOW FADED WILD COLD SOFT PALE BITTER SWEET ELECTRIC LATE EARLY HIDDEN SLEEPY LAZY GENTLE LONELY CHEAP BLUE PLASTIC "
      "UNDERGROUND MONDAY HONEY STATIC ECHO ORBIT SIGNAL HARBOR LANTERN COMPASS PARADE CAROUSEL TELESCOPE POSTCARD CASSETTE MARBLE TUNNEL LADDER VOYAGE PICNIC SPARROW BISCUIT PILLOW KETTLE MIRROR WINDOW GARAGE "
      "FESTIVAL DAYDREAM RAINFALL THUNDER SATELLITE ELEVATOR BAKERY AIRPORT PENCIL ENVELOPE MARMALADE LIGHTHOUSE CRAYON RIVER MOON STAR SUMMER WINTER AUTUMN SPRING GHOST SHADOW FLAME OCEAN DESERT FOREST ISLAND").split()
ENS = ("SIGNALS ELEVATORS ANIMALS COMMUTERS RADIOS DOGS TRAINS BALLOONS GHOSTS MACHINES STATIONS BICYCLES LETTERS ORCHESTRA WEATHER SUBMARINES STRANGERS KIDS BOYS GIRLS ROBOTS DREAMERS SPARROWS CLOUDS "
       "FIREFLIES LANTERNS CAMERAS TICKETS COMETS PLANETS DOORS WINDOWS STAIRS UMBRELLAS").split()
ENV = ("RUN WAIT STAY LEAVE FALL FLY SLEEP DANCE SING CRY LAUGH BURN FADE BREATHE DRIVE FOLLOW WANDER REMEMBER FORGET HIDE SHINE").split()
ENT = ("Tonight Tomorrow Forever Again Alone Together Somewhere Anyway Maybe Someday Midnight Sunrise Summer Rain Home Goodbye Hello Yesterday Weekend Daylight").split()
NUM = ("午前四時 三分間 第三象限 百円ライター 七番線 十五夜 二軍 零時 九月 第二回 五反田 四十九日 一年生 三丁目 十七歳 二十歳 八畳 千円札 百万回 四季 一分 二番目 三日月 四面楚歌 五月雨 六畳 七夕 八百屋 九官鳥 十字路").split()
KANJ2 = ("夜行 迷子 残響 白昼 逆光 蜃気楼 空洞 余白 点滅 透過 遠雷 薄暮 浮遊 反射 微熱 終点 深呼吸 行方 軌道 回遊 夜明 残像 追憶 幻灯 水脈 風待 月影 虹彩 無声 潮騒 夕凪 木霊 陽炎 星屑 白夜 暁 朧 凪 宵 刹那").split()
HIRA = ("ぼんやり ふわふわ ゆらゆら きらきら ぽつぽつ くるくる ぐるぐる とろとろ ひらひら のろのろ ちくちく しんしん ざわざわ ほかほか ぷかぷか すやすや てくてく ことこと ふらふら").split()
SUR = ("佐藤 鈴木 高橋 田中 伊藤 渡辺 山本 中村 小林 加藤 吉田 山田 松本 井上 木村 清水 斉藤 森 藤原 西村 近藤 石川 前田 小川 岡田 長谷川 村上 遠藤 青木 坂本 福田 太田 三浦 藤井 後藤 岡本 原田 中島 竹内 金子 和田 野口 菊地 内田 柴田 酒井 宮本 横山 大野 安田").split()
GIV = ("ミナト レイ ハル ソラ ユウ ナギ カエデ リク ミオ アカリ サクヤ トワ ヒカル ノゾミ シオン アオイ ツバサ イブキ ルカ カナタ ヨウ リョウ ミサキ ナツキ アユム ヒビキ セナ ユイ コウ スイ ミライ "
       "蓮 凛 葵 陽 湊 結 澪 朔 颯 瞬 悠 渚 茜 栞 岬 樹 奏 楓 玲 詩 響 光 環 灯 慧 想 凪 翠").split()
ROMA = ("mina haru sora yuu nagi kaede riku mio akari toa hikaru nozomi shion aoi rui kou tsubasa ibuki luka kanata you ryo misaki natsuki ayumu hibiki sena yui sui mirai ren rin sho kai").split()
NICK = ("ちゃん くん さん ぴ ぽん たん めろ ぷー ころ もち まる ぴょん").split()
SUF_BAND = ("オーケストラ クラブ 少年 ガールズ ブラザーズ ボーイズ 会議 連合 研究所 楽団 倶楽部 レコード ユニオン 計画 協会 探検隊 合唱団 同好会 一座 工場 ラボ 隊 組 党 団 衆 係 委員会 帝国 王国 少女 ジャンクション").split()
PRE_BAND = ("THE ザ・ ").split()
SUF_E = ("ORCHESTRA CLUB BOYS GIRLS BROTHERS SOCIETY UNION PROJECT ARMY GANG CREW CIRCUS RECORDS BAND SOUND SYSTEM PARADE CHOIR").split()
ERA_BAND = {
    'old': ("とその仲間たち フォークキャンプ ブギ ヒーローズ ロックンロールバンド ブルースバンド 青春座 ハウス サーカス 少年隊 シスターズ ファミリー 一座 ツイスト").split(),
    'mid': ("ヴィジュアル系 サウンドトラック 少年 レコーズ 渋谷系 ポップス クラブ エクスプレス ハイスクール ガールズ").split(),
    'new': ("ガチ勢 の件 配信 ch. ラジオ 公式 サークル 係 同盟 ごっこ 研究会 FC").split(),
}
MC_PRE = ("MC DJ 般若 ZEEBRA KREVA").split()  # 実在の名前はバンク生成時に除外する(下で除外語を使用)
MC_PRE = ["MC", "DJ", "Lil", "Young", "Big", "Mad", "Sick", "Cool", "Rude", "Dope"]
MC_NAME = ("Kaede Riku Sora Nagi Haru Ren Ryo Sho Kai Yuu Toa Mio Aoi Shin Jun Takt Zero Bit Pop Gum Rust Salt Pepper Yen Zen Wax Moss Fog Ash Ink").split()
GANG = ("GANG CREW 組 一家 連合 MOB CLAN SQUAD 軍団 兄弟 FAMILY 会 団地組 町内会").split()
DJ_SUF = ("beats mix sound system radio selector cuts tapes wax lab").split()

# ---------- 曲名 ----------
def title(r, era='mid'):
    P = [
        lambda: f"{r.choice(TIM)}の{r.choice(N)}", lambda: f"{r.choice(N)}のままで", lambda: f"{r.choice(EMO)}の手前", lambda: f"{r.choice(KAT)}と{r.choice(N)}",
        lambda: f"{r.choice(PLC)}で会おう", lambda: f"{r.choice(N)}を{r.choice(['投げる','拾う','数える','貸して','返して','探して','忘れた'])}", lambda: f"{r.choice(KAT)}・{r.choice(KAT)}",
        lambda: f"{r.choice(EMO)}、{r.choice(TIM)}", lambda: f"{r.choice(N)}を失くした{r.choice(TIM)}",
        lambda: f"{r.choice(A)}{r.choice(N)}", lambda: f"{r.choice(A)}{r.choice(EMO)}", lambda: f"{r.choice(PERS)}の{r.choice(N)}", lambda: f"{r.choice(PERS)}と{r.choice(PERS)}と{r.choice(N)}",
        lambda: f"{r.choice(VBP)}{r.choice(PERS)}", lambda: f"{r.choice(VBT)}{r.choice(TIM)}", lambda: f"{r.choice(TIM)}、{r.choice(PERS)}は{r.choice(VBP)}", lambda: f"{r.choice(N)}が{r.choice(VBI)}まで",
        lambda: f"{r.choice(VBO)}{r.choice(['前に','まえに','ついでに','だけの'])}{r.choice(N)}", lambda: f"{r.choice(NUM)}の{r.choice(N)}", lambda: f"{r.choice(NUM)}、{r.choice(EMO)}", lambda: f"{r.choice(KANJ2)}",
        lambda: f"{r.choice(KANJ2)}{r.choice(KANJ2)}", lambda: f"{r.choice(KANJ2)}の{r.choice(N)}", lambda: f"{r.choice(HIRA)}{r.choice(N)}", lambda: f"{r.choice(HIRA)}、{r.choice(TIM)}",
        lambda: f"{r.choice(PLC)}{r.choice(['発','行き','ブルース','ナイト','カラー','心中','エレジー','慕情','物語','日和'])}", lambda: f"{r.choice(PLC)}の{r.choice(N)}", lambda: f"{r.choice(N)}と{r.choice(N)}",
        lambda: f"{r.choice(A)}{r.choice(N)}と{r.choice(A)}{r.choice(N)}", lambda: f"{r.choice(N)}みたいな{r.choice(PERS)}", lambda: f"{r.choice(PERS)}が{r.choice(VBI)}{r.choice(TIM)}",
        lambda: f"{r.choice(EMO)}はいつも{r.choice(N)}", lambda: f"もしも{r.choice(N)}が{r.choice(VBI)}なら", lambda: f"{r.choice(N)}を{r.choice(VBO)}{r.choice(['夜','朝','夏','日'])}",
        lambda: f"{r.choice(EN)} {r.choice(ENS)}", lambda: f"{r.choice(EN)} {r.choice(ENT)}", lambda: f"{r.choice(ENV).capitalize()} {r.choice(ENT)}", lambda: f"{r.choice(ENT)}, {r.choice(ENT)}",
        lambda: f"{r.choice(EN).capitalize()} {r.choice(ENS).capitalize()}", lambda: f"Dear {r.choice(ENS).capitalize()}", lambda: f"{r.choice(ENV).capitalize()} Me {r.choice(ENT)}",
    ]
    NEWP = [
        lambda: f"{r.choice(N)}、{r.choice(['通知オフ','既読スルー','未読のまま','圏外','充電切れ','電波悪い','低評価'])}", lambda: f"{r.choice(VBT)}だけの{r.choice(TIM)}", lambda: f"{r.choice(HIRA)}してたら{r.choice(TIM)}",
        lambda: f"{r.choice(PERS)}のせいで{r.choice(EMO)}", lambda: f"{r.choice(EMO)}デリバリー", lambda: f"{r.choice(N)}コンプレックス", lambda: f"{r.choice(N)}ロス", lambda: f"{r.choice(KAT)}症候群",
    ]
    OLDP = [
        lambda: f"{r.choice(PLC)}{r.choice(['挽歌','ブルース','フォーク','の夜','を出る朝'])}", lambda: f"{r.choice(N)}よ、{r.choice(VB)}な", lambda: f"{r.choice(TIM)}の{r.choice(['手紙','葉書','電話','横顔','約束'])}",
        lambda: f"風に{r.choice(VB)}{r.choice(PERS)}", lambda: f"{r.choice(PERS)}の{r.choice(['ことば','青春','夏','ふるさと','ともしび'])}",
    ]
    pool = P + (NEWP if era == 'new' else OLDP if era == 'old' else [])
    return r.choice(pool)()

# ---------- アーティスト名 ----------
def artist(r, style, era='mid'):
    en = lambda: f"{r.choice(EN)} {r.choice(ENS)}"
    def human(): return f"{r.choice(SUR)}{r.choice(GIV)}" if r.random() < .5 else f"{r.choice(GIV)}"
    if style in ('band', 'inst'):
        P = [
            lambda: f"THE {en()}", lambda: f"{r.choice(TIM)}の{r.choice(N)}", lambda: f"{r.choice(A)}{r.choice(N)}", lambda: f"{r.choice(N)}と{r.choice(N)}", lambda: f"{r.choice(KANJ2)}{r.choice(SUF_BAND)}",
            lambda: f"{r.choice(N)}{r.choice(SUF_BAND)}", lambda: f"{r.choice(PLC)}{r.choice(SUF_BAND)}", lambda: f"{r.choice(KAT)}{r.choice(SUF_BAND)}", lambda: f"{r.choice(EN)} {r.choice(SUF_E)}",
            lambda: f"{r.choice(NUM)}の{r.choice(KANJ2)}", lambda: f"{r.choice(PERS)}と{r.choice(N)}", lambda: f"{r.choice(HIRA)}{r.choice(SUF_BAND)}", lambda: f"{r.choice(VB)}{r.choice(SUF_BAND)}",
            lambda: f"{r.choice(A)}{r.choice(SUF_BAND)}", lambda: f"{en()}", lambda: f"{r.choice(ENS)}", lambda: f"{r.choice(KAT)} {r.choice(ENT)}", lambda: f"{r.choice(EN).capitalize()}{r.choice(range(2, 99))}",
            lambda: f"{r.choice(VBP)}{r.choice(['係','同盟','クラブ','会議','の会'])}", lambda: f"{r.choice(N)}{r.choice(['係','党','同盟','解放戦線','の会','探偵団','少年団'])}", lambda: f"{r.choice(['ザ・','THE '])}{r.choice(KAT)}{r.choice(['ズ','ス','ーズ'])}",
        ]
        if style == 'inst': P += [lambda: f"{r.choice(KANJ2)}について", lambda: f"{r.choice(EN)} {r.choice(['QUARTET','TRIO','ENSEMBLE','ORCHESTRA'])}", lambda: f"{r.choice(N)}カルテット", lambda: f"{r.choice(PLC)}ジャズ組"]
        e = {'old': lambda: f"{human()}{r.choice(ERA_BAND['old'])}", 'mid': lambda: f"{r.choice(KAT)}{r.choice(ERA_BAND['mid'])}", 'new': lambda: f"{r.choice(N)}{r.choice(ERA_BAND['new'])}"}[era]
        return r.choice(P + [e, e])()
    if style == 'duo':
        P = [lambda: f"{r.choice(GIV)}と{r.choice(GIV)}", lambda: f"{r.choice(N)}と{r.choice(N)}", lambda: f"{r.choice(EN)} & {r.choice(EN)}", lambda: f"{r.choice(KAT)}×{r.choice(KAT)}", lambda: f"{r.choice(GIV)}&{r.choice(GIV)}",
             lambda: f"{r.choice(SUR)}兄弟", lambda: f"{r.choice(SUR)}姉妹", lambda: f"{r.choice(N)}ブラザーズ", lambda: f"{r.choice(A)}ふたり", lambda: f"{r.choice(TIM)}デュオ", lambda: f"{r.choice(PLC)}ツイン", lambda: f"{r.choice(KANJ2)}と{r.choice(KANJ2)}"]
        return r.choice(P)()
    if style == 'rap':
        P = [lambda: f"{r.choice(MC_PRE)} {r.choice(MC_NAME)}", lambda: f"{r.choice(PLC)}{r.choice(GANG)}", lambda: f"{r.choice(N)}{r.choice(GANG)}", lambda: f"{r.choice(MC_NAME)} from {r.choice(PLC)}", lambda: f"{r.choice(SUR)}{r.choice(['MC','改め','BOY','の息子','兄貴'])}",
             lambda: f"{r.choice(MC_NAME).upper()}{r.choice(range(2, 99))}", lambda: f"{r.choice(KANJ2)}MC", lambda: f"{r.choice(A)}{r.choice(['MC','ラッパー','詩人'])}", lambda: f"{r.choice(NUM)}MC", lambda: f"{r.choice(MC_NAME)} a.k.a. {r.choice(N)}",
             lambda: f"{r.choice(PLC)}の{r.choice(['アニキ','若頭','番長','詩人','語り部'])}", lambda: f"{r.choice(EN)} {r.choice(['MC','CYPHER','BARS','FLOW'])}"]
        return r.choice(P)()
    if style == 'dj':
        P = [lambda: f"DJ {r.choice(N)}", lambda: f"DJ {r.choice(MC_NAME)}", lambda: f"{r.choice(N)}DJ", lambda: f"{r.choice(MC_NAME).lower()} {r.choice(DJ_SUF)}", lambda: f"DJ {r.choice(NUM)}", lambda: f"{r.choice(PLC)}DJ",
             lambda: f"{r.choice(KANJ2)} DJ", lambda: f"DJ {r.choice(EN).capitalize()}", lambda: f"{r.choice(MC_NAME)}{r.choice(range(2, 99))}", lambda: f"{r.choice(KAT)} {r.choice(DJ_SUF)}"]
        return r.choice(P)()
    if style == 'beat':
        P = [lambda: f"{r.choice(MC_NAME).lower()}{r.choice(range(2, 99))}", lambda: f"{r.choice(EN).lower()}_{r.choice(ENS).lower()}", lambda: f"{r.choice(N)}ビート", lambda: f"{r.choice(KAT)} Tapes", lambda: f"{r.choice(ROMA)}.wav",
             lambda: f"{r.choice(ROMA)}{r.choice(['_','-',''])}{r.choice(['beats','tape','lab','works','room'])}", lambda: f"{r.choice(N)}の部屋", lambda: f"{r.choice(KANJ2)}ラボ", lambda: f"{r.choice(NUM)}号室", lambda: f"{r.choice(EN).capitalize()} Room"]
        return r.choice(P)()
    if style in ('ai_pure', 'ai_collab'):
        P = [lambda: f"{r.choice(GIV)}{r.choice(['ちゃん','ん','たん','ぴ'])}", lambda: f"{r.choice(ROMA)}-{r.choice(range(1, 99)):02d}", lambda: f"{r.choice(['AI','ai_','Neo','Cyber'])}{r.choice(GIV)}", lambda: f"{r.choice(GIV)}_{r.choice(['AI','v2','unit','mk2','type'])}",
             lambda: f"{r.choice(KAT)}{r.choice(GIV)}", lambda: f"{r.choice(EN).title()} {r.choice(GIV)}", lambda: f"{r.choice(GIV)}={r.choice(range(2, 99))}", lambda: f"{r.choice(KANJ2)}{r.choice(['型','式','号'])}", lambda: f"{r.choice(ROMA)}{r.choice(['AI','bot','ia','x'])}"]
        if style == 'ai_collab': P += [lambda: f"{human()} with AI", lambda: f"{human()}+{r.choice(ROMA)}", lambda: f"{r.choice(GIV)} × {r.choice(ROMA).upper()}"]
        return r.choice(P)()
    # solo
    P = [lambda: human(), lambda: f"{r.choice(GIV)}・{r.choice(SUR)}", lambda: f"{r.choice(GIV)}の{r.choice(N)}", lambda: f"{r.choice(ROMA)}{r.choice(range(2, 99))}", lambda: f"{r.choice(ROMA)}_{r.choice(['','x','o','z'])}",
         lambda: f"{r.choice(GIV)}とブランコ", lambda: f"{r.choice(SUR)}{r.choice(GIV)}と{r.choice(['弾き語り','ギター','夜','猫','犬','ラジオ'])}", lambda: f"{r.choice(A)}{r.choice(GIV)}", lambda: f"{r.choice(KANJ2)}{r.choice(GIV)}",
         lambda: f"{r.choice(TIM)}の{r.choice(GIV)}", lambda: f"{r.choice(EN).capitalize()} {r.choice(GIV)}", lambda: f"{r.choice(GIV)}{r.choice(NICK)}", lambda: f"{r.choice(GIV)}{r.choice(['うた','の歌','のうた','ソロ','ひとり旅'])}",
         lambda: f"{r.choice(PLC)}の{r.choice(GIV)}", lambda: f"{r.choice(HIRA)}{r.choice(GIV)}", lambda: f"{r.choice(NUM)}{r.choice(GIV)}", lambda: f"{r.choice(SUR)}{r.choice(['某','氏','先生','屋','堂'])}"]
    if era == 'old': P += [lambda: f"{r.choice(SUR)}{r.choice(GIV)}{r.choice(['とその仲間','ひとり','ソロ'])}", lambda: f"{r.choice(PLC)}の{r.choice(['フォーク歌手','流し','弾き語り','青年'])}"]
    return r.choice(P)()

BAD = ('"', '\\')
ERAS3 = {'old': (-1, 0), 'mid': (1, 2), 'new': (3, 4, 5)}
STYLES = ['band', 'inst', 'duo', 'solo', 'rap', 'beat', 'dj', 'ai_pure', 'ai_collab']

def build(n_art=1800, n_ti=14000, seed=2026):
    import ongaku_storyline_gen as g
    r = random.Random(seed); bank = {'a': {}, 't': {}}
    for st in STYLES:
        for eb in ERAS3:
            s = []; seen = set()
            tries = 0
            while len(s) < n_art and tries < n_art * 12:
                tries += 1
                x = artist(r, st, eb)
                if r.random() < .15:
                    try: x = g.mk_artist(r, st, None)
                    except Exception: pass
                x = x.strip()
                if not (2 <= len(x) <= 26) or any(b in x for b in BAD) or x in seen: continue
                seen.add(x); s.append(x)
            # パロディ名(出自の分かるもの)を一定数混ぜる
            if st not in ('ai_pure', 'ai_collab'):
                pl = [p[0] for p in g.PUN_VARS if st in p[2] and p[3] <= max(ERAS3[eb])] + [p[0] for p in g.PUNS if st in p[2] and p[3] <= max(ERAS3[eb])]
                r.shuffle(pl)
                for x in pl[:700]:
                    if x not in seen and not any(b in x for b in BAD): seen.add(x); s.append(x)
            r.shuffle(s); bank['a'].setdefault(st, {})[eb] = s
    for eb in ERAS3:
        s = []; seen = set(); tries = 0
        while len(s) < n_ti and tries < n_ti * 12:
            tries += 1
            x = title(r, eb) if r.random() < .8 else g.mk_title(r)
            x = x.strip()
            if not (2 <= len(x) <= 24) or any(b in x for b in BAD) or x in seen: continue
            seen.add(x); s.append(x)
        bank['t'][eb] = s
    return bank

if __name__ == '__main__':
    b = build()
    json.dump(b, open('/home/claude/namebank.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    import os
    print(os.path.getsize('/home/claude/namebank.json') / 1e6, 'MB', {st: {e: len(v) for e, v in d.items()} for st, d in list(b['a'].items())[:2]}, {e: len(v) for e, v in b['t'].items()})
    r = random.Random(5)
    for st in STYLES: print(st, [artist(r, st, 'mid') for _ in range(6)])
    print([title(r, 'new') for _ in range(10)])
