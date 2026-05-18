---
layout: default
title: tGTD
---

2019/05/28 いったん中断。筆者自身が十分に GTD を運用できてないため。できてから来よう。最低でも一年後くらい？

tGTD(text GTD)とはプレインテキストとテキストエディタのみで GTD を実現すること。

GTD 全般や各リストの運用方法(たとえばレビュー頻度など)については [GTD](gtd.md) の項を参照。

# ●misc
todo.md がムズい。どこまでタスク管理システムを入れるか。要するにルーチンタスクの機構を手動(特にトリガーリスト)で実現する方法が必要になる。2018年帰省時に試してみたけど難しすぎて一般向けじゃない……

リマインダーの実現もむずい。

チェックリストどうしよ。trigger でくくるのは強引だよなぁ。gtd.md ではトリガーリストの一部にしてる。今思ったのは「資料の範疇かなぁ」

# 全般情報

## ファイル形式
何でも良い。

本文書では基本的に Markdown ファイルを用いる。

## バージョン管理
変更履歴を記録しておきたい場合は行う。

GitHub で管理を行えば、ブラウザからの閲覧や検索がしやすい。

## フォルダ構成
任意のフォルダに各ファイルをフラットに配置する。

## ファイル一覧

| List              | Filename           |
| ----------------- | ------------------ |
| 5000m Philosophy  | height.md          |
| 4000m Ideal       | height.md          |
| 3000m Milestone   | height.md          |
| 2000m Restriction | height.md          |
| 1000m Project     | project.md         |
| 0000m Nextaction  | todo.md            |
| Inbox             | inbox.md           |
| Document          | document.md        |
| Someday           | someday.md         |
| Waiting           | todo.md            |
| Calendar          | calendar.md        |
| Context           | context.txt        |
| Trigger           | trigger_if_XXXX.md |

# height.md
2000-5000m の内容を一行一項目で書き並べる。

フォーマット:

```
# Height

## 5000m Philosophy
...

## 4000m Ideal
...

## 3000m Milestone
...

## 2000m Restriction
...

```

## inbox.md
気になることを一行一項目で書き並べる。

- 突発収集に対応するため秒速で呼び出せること、また書けることが望ましい

フォーマット:

```
...
気になること3
気になること2
気になること1
```

## someday.md
いつかやることを一行一項目で書き並べる。

- 後で絞り込めるようコンテキストを付けておく
- 未分類は未分類用のコンテキストを付ける(何も付けないと未分類のみ抽出することが難しい)
- 抽出は grep で行う

全体フォーマット:

```
...
いつかやること3
いつかやること2
いつかやること1
```

各行フォーマット:

```
(ContextTags) (いつかやること)
```

## context.txt
コンテキストを一行一項目で書き並べる。

- コンテキストタグはテキストエディタの補完機能で入力できるように工夫する
  - タグのフォーマット
  - タグの冒頭に接頭辞を付ける

フォーマット:

```
(ContextTag-1) (ContextDescription-1)
(ContextTag-2) (ContextDescription-2)
(ContextTag-3) (ContextDescription-3)
...
```

例:

```
ccmisc        未分類
ccbuy         買う
ccblog        ブログネタ
ccbook        書籍ネタ
ccdev         開発ネタ
ccnovel       小説ネタ
ccbusiness    ビジネスアイデア
ccfuture      将来への備え
```

## calendar.md 
今後の予定を一行一項目で書き並べる。

- 直近の予定を素早く知るため秒速で呼び出せることが望ましい
- 週報への転記を想定し、週報準拠のフォーマットで書くのも良い

フォーマット:

```
(EventDate-1) (EventDescription-1)
(EventDate-2) (EventDescription-2)
(EventDate-3) (EventDescription-3)
...
```

例:

```
- 05/21 tue          通院午前休
- 05/23 thu 9-12     研修 in 秋葉原
- 06/03 mon 14-1430  上位上司面談
```

## trigger_if_XXXX.md
トリガーを一行一項目で書き並べる。

- このファイルの意味は「XXXX の時のトリガーリスト」「XXXX のためのトリガーリスト」
- 必要に応じて複数個作っても良い
  - というより 10 を超えることも珍しくない

例:

- → [改善するべき不満や問題を洗い出すためのトリガーリスト](gtd_triggerlist_sample.md)
