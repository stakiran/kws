---
layout: default
title: 吉良野式支出管理
---

# 吉良野式支出管理

## コンセプト
- 支出は可能な限りその場で記録する
- その場で記録した分は、あとでまとめる
- 最終的に Excel にまとめる

## 登場人物
- ガラケー
- Gmail
- Python
- Excel

# 全体像
- Phase1「メモ」 …… その場で記録する
- Phase2「テキストデータ化」 …… 加工しやすいよう PC 上に集める
- Phase3「Excel 記入」 …… 集計しやすいよう Excel に記入する

## Phase1. メモフェーズ
ガラケーの送信メールに以下フォーマットで記載。

```
[タイトル]
190510

[本文]
1839 3977＊ガス代
1837 800＊とんかつ
1803 120＊電車
1437 265＊トッボ
1308 120＊コーヒー
1233 623＊揚げ出し豆腐セット
0848 100＊水
0809 124＊電車
```

つまり一日ごとに「いつ、何に、何円使ったか」をメモしていく。

## Phase2. テキストデータ化
ガラケーでメモしたデータは、一日の終わり(今日はもう支出しないというタイミングなど)に、Gmail に送信する。これを PC からアクセスしてコピペし、以下フォーマットで記録。

```
[ファイル名]
diary.dry

[中身]
*190510(Fri)
1839 3977＊ガス代
1837 800＊とんかつ
1803 120＊電車
1437 265＊トッボ
1308 120＊コーヒー
1233 623＊揚げ出し豆腐セット
0848 100＊水
0809 124＊電車

*190509(Thu)
...
```

ファイル名や記録方法は適当で良い(ここでは .dry ファイルをつくり、一日一見出しで記載している)。

## Phase3. Excel 記入
このフェーズでは「テキストデータを Excel 用フォーマットに変換」した後、それを Excel にコピペする。

### Excel フォーマット
以降では Excel は以下のようなフォーマットを想定する。

シート: 201905

| 日付 | 名前 | カテゴリ | 金額 | flag | 備考 |
| ---- | ---- | -------- | ---- | ---- | ---- |
| 2019/5/10 | ガス代 | 公共料金 | 3977 |  |  |
| 2019/5/10 | とんかつ | 夕食 | 900 |  |  |
| 2019/5/10 | 電車 | 交通費 | 154 | c |  |
| 2019/5/10 | トッボ | 間食 | 265 | c |  |
| 2019/5/10 | コーヒー | 飲料 | 90 | c |  |
| 2019/5/10 | 揚げ出し豆腐 | 昼食 | 623 | c |  |
| 2019/5/10 | 水 | 飲料 | 100 | c |  |
| 2019/5/10 | 電車 | 交通費 | 154 | c |  |

シート：Category

```
朝食
昼食
夕食
飲料
間食
ゲーム
本：マンガラノベ
本：技術書
本：その他
交通費
日用品
清潔・身嗜み
病院・治療
PC関連
運動関連
家電・乗物
服
クレジットカード
収納
洗濯
公共料金
家賃
```

### 変換(フォーマット)
テキストデータを「Excel 上のフォーマット」に変換する。

Before:

```
1839 3977＊ガス代
1837 800＊とんかつ
1803 120＊電車
1437 265＊トッボ
1308 120＊コーヒー
1233 623＊揚げ出し豆腐セット
0848 100＊水
0809 124＊電車
```

After:

```
2019/05/13	ガス代	公共料金	3977
2019/05/13	とんかつ		800
2019/05/13	電車	交通費	120
2019/05/13	トッボ		265
2019/05/13	コーヒー	飲料	120
2019/05/13	揚げ出し豆腐セット		623
2019/05/13	水	飲料	100
2019/05/13	電車	交通費	124
```

### 変換(スクリプト)
変換スクリプトは Python 3 で以下のとおり。ただし一部自製ライブラリは割愛する。

```python
# -*- coding: utf-8 -*-

import datetime
import os
import sys
from time import sleep

import pywintypes

from libclipboard import Clipboard

LINEBREAK = '\n'

def abort(msg):
    print(msg)
    exit(1)

def todaystr():
    return datetime.datetime.today().strftime('%Y/%m/%d')

def precise_clipget():
    c = 0
    cb = ''
    while True:
        try:
            cb = Clipboard.get()
            return cb
        except pywintypes.error:
            pass
        c += 1
        if c>100:
            raise RuntimeError('Clipboard.get() is failing...')
        sleep(0.05)

def clipboard2lines():
    cb = precise_clipget()
    if cb=='':
        abort('Clipboard is empty.')
    lines = cb.split(LINEBREAK)
    return lines

def lines2clipboard(lines):
    ret = LINEBREAK.join(lines)
    Clipboard.set(ret)

def booksline2booklines(line, todaystr, category, total_price):
    # 3969＊7冊、ナナマルサンバツ123、すうの空気攻略1、食戟のソーマ28、氷菓11、信長の忍び13
    SEP = '冊、'

    line = line.strip(' \t\n\r')

    if line.find(SEP) == -1:
        return None

    lines = []

    booksline = line.split(SEP)[1]
    booknames = booksline.split('、')
    bookcount = len(booknames)

    def get_number_pos(s):
        for idx,c in enumerate(s):
            if c in '123456789':
                return idx
        return -1

    def split_kansus(kansu_part):
        # 3969＊7冊、ナナマルサンバツ1 2 3、すうの空気攻略1
        #                            ^ ^ ^
        # 1,2,3, ← こうする
        if kansu_part.find(' ')==-1:
            return kansu_part

        new_kansu_str = ','.join(kansu_part.split(' '))

        return new_kansu_str

    def determin_incremented_bookcount(booknames):
        ret = 0
        for bookname in booknames:
            number_pos = get_number_pos(bookname)
            kansu_part = bookname[number_pos:]
            # Q: -1 の根拠は?
            # 1,2  -> ["1","2"]
            # 1    -> ["1"]      これでもカウント1になっちゃうのでこの分は省く
            count = len(kansu_part.split(' ')) - 1
            ret += count
        return ret

    # 分母となる巻数系は先に計算する.
    # (先に全部走査しきらないと正しい値にならない)
    bookcount += determin_incremented_bookcount(booknames)

    for bookname in booknames:
        flag_dummy = ''
        
        number_pos = get_number_pos(bookname)
        bookname_only = bookname[:number_pos]
        kansu_part = bookname[number_pos:]
        kansu_str = split_kansus(kansu_part)

        itemname = bookname_only
        note = '{},'.format(kansu_str)
        price = '={}/{}'.format(total_price, bookcount)

        new_line = '{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(todaystr, itemname, category, price, flag_dummy, note)
        lines.append(new_line)

    return lines

convertions="""
朝食               | パン
昼食               | 
夕食               |
飲料               | いろはす,ライフガード,コーヒー,水,エメマン,モニショ,カフェオレ,カフェラテ,綾鷹,ジュース
間食               | カロリーメイト,チョコ,ちょこ,ポテチ,ポテトチップス,じゃがりこ,間食,菓子
ゲーム             | maimai,チュウニ,舞,パンプ,ダンス,パセリ
本：マンガラノベ   | 冊
本：技術書         |
本：その他         |
交通費             | タクシー,JR,バス,駐輪,jr,電車,新幹線
日用品             | リップクリーム,ムヒ,歯ブラシ,歯磨き,洗顔,洗う,シャンプー,電池,石鹸,日用,調味,ティッシュ
清潔・身嗜み       | 散髪
病院・治療         | 病院
PC関連             |
運動関連           |
家電・乗物         |
服                 |
クレジットカード   | github,slack,biglobe
公共料金           | 電気,ガス,水道
"""

convertion_dict = {}
convertion_lines = convertions.split(LINEBREAK)
for line in convertion_lines:
    if len(line)==0:
        continue

    catename, triggerwords = [elm.strip() for elm in line.split('|')]
    if len(triggerwords)==0:
        continue

    for triggerword in triggerwords.split(','):
        convertion_dict[triggerword] = catename

ret_lines = []
lines = clipboard2lines()
for line in lines:
    uline = line
    if uline.find('＊')==-1:
        continue

    body = uline[5:]
    price, itemname = body.split('＊')
    itemname = itemname[:-1] # なぜか改行文字が入っているので...
    itemname = itemname.split('。', 1)[0]
    price = int(price)
    today = todaystr()

    category = '' # @todo CSV前提にするなら空値より"★"とかの方が「要編集」だとわかりやすい?
    for key in convertion_dict:
        if itemname.find(key)!=-1:
            category = convertion_dict[key]
            break

    booklines_candidate = booksline2booklines(line, todaystr(), category, price)
    if booklines_candidate != None:
        booklines = booklines_candidate
        ret_lines.extend(booklines)
        continue

    ret = '{0}\t{1}\t{2}\t{3}'.format(today, itemname, category, price)
    ret_lines.append(ret)

lines2clipboard(ret_lines)
```

長々としているが、要点をまとめると以下のとおり。

- Before のテキストデータをコピーしてからこのスクリを実行すると、After の書式に変換してからコピーし直す
- After ではタブ区切り `\t` を用いる
  - Excel 上で直接コピペできるため
- 本の記入については各タイトルで分かれるようにしている(下記参照)
- カテゴリについては、品名から特定できるものは特定する(convertions 変数)

要するに手作業で Before から After に直すのが面倒だから自動化している。方法は何でも良いし、自動化が難しいなら無理にしなくてもよい。

### 書籍データの変換(フォーマット)
この変換は必須ではないが、個人的によくマンガ・ライトノベルについては、何のタイトルの何の巻を買ったかを網羅しておきたかったため、少し力を入れて整えた。

Before:

```
3969＊7冊、ナナマルサンバツ123、すうの空気攻略1、食戟のソーマ28、氷菓11、信長の忍び13
```

After:

```
2019/05/13	ナナマルサンバツ	本：マンガラノベ	=3969/5		123,
2019/05/13	すうの空気攻略	本：マンガラノベ	=3969/5		1,
2019/05/13	食戟のソーマ	本：マンガラノベ	=3969/5		28,
2019/05/13	氷菓	本：マンガラノベ	=3969/5		11,
2019/05/13	信長の忍び	本：マンガラノベ	=3969/5		13,
```

# TIPS

## その場でメモできない支出はどう記録するか
たとえばクレジットカードによる引き落としは月一で紙明細が届くか、Web で確認するようになっており、Phase1 のメモフェーズで記録するタイミングがない。このような支出はどうするか。

以下のようにする。

- 支出内容が判明したら、すぐに Phase2 または Phase3 で直接記入する
- 記入を忘れないよう、ルーチンタスク化しておくのが賢い

ルーチンタスク化については、たとえば私は以下のようにしている。

```
3 2019/05/15 Wed             zk 1 Biglobe メアド確認 rep:30
3 2019/05/15 Wed             zk 1 Biglobe ログインして請求確認(毎月13日に前月分出る)＆当月分kakeibo記入 rep:30
```

これは Biglobe に絡む支出記入を、毎月 13 日の後に行うルーチンタスクである。 [Tritask](https://tritask.github.io/tritask-web/) というタスク管理ツールを使っている。しかし手段は何でも良い。最も簡単なのは、デジタルカレンダーでリマインドを設定しておくことだろう。

## 集計作業はどのように行うか
月ごとに作ったシート(内のデータ)を一つのシートにまとめるのが良い。その際、月ごとや年ごとの集計が行えるよう、別途列を設けるのが望ましい。以下に例を示す。

| 日付 | 名前 | カテゴリ | 金額 | Flag | 備考 | 月 | 年 | 
| 2013/3/10 | オーザックうす塩 | 間食 | 128 |  |  | 3 | 2013 | 
| 2013/3/10 | 弁当 唐揚げととん汁 | 昼食 | 580 |  | おごり | 3 | 2013 | 

このようなシートをつくった後は、ピボットテーブル機能などで集計を行う。

- 集計の例: [2018 年の支出を振り返る - ストレスフリーなソロ充ライフ](https://stressfree-fulfilling-solo.hatenablog.com/entry/2018/12/31/074400)

## カテゴリはどのように設計するか
試行錯誤するしかないが、自分の生活と照らし合わせると良い。

たとえば私の場合、食事がほぼ外食(自炊しない)であることと、各食事にかかった費用はちゃんと記録しておきたいことから「朝食」「昼食」「夕食」「飲料」「間食」というカテゴリをつくっている。もし私とは違い、自炊する派であれば、単に「食費」だけで済むだろう。あるいは「食費」「外食費」あたりだろうか。

また本については、私は「本：マンガラノベ」「本：技術書」「本：その他」としている。これも人によっては「本」一つで良かったり、逆に「本：小説」「本：マンガ」「本：ラノベ」「本：実用書」「本：図鑑」のような細分化もありえる。ちなみに、表示順でまとめやすくするために「本：」のような接頭辞は極力設けるのが望ましい。

# 参考
- [支出管理（出費の記録）をスムーズに行うために欠かせないポイント 5 点 - ストレスフリーなソロ充ライフ](https://stressfree-fulfilling-solo.hatenablog.com/entry/2018/11/21/070600) 
