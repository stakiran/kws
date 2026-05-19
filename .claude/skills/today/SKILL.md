---
name: today
description: 今日の日付 yyyy-mm-dd で wiki/yyyy-mm-dd.scb を作成し、wiki/index.scb の daily pages セクション先頭にリンクを prepend してから VSCode で開く。既に存在する場合は作成・prepend をスキップして開くだけ。/today で起動する。
---

# today — 今日のデイリーページを開く

`wiki/yyyy-mm-dd.scb` を用意して VSCode で開くスキル。

実処理はすべて `today.py` に任せる。Claude は引数なしでスクリプトを 1 回呼び、結果（標準出力 1 行）をそのままユーザーへ短く報告するだけにする。

## 手順

1. リポジトリルートから次を実行する:

   ```
   python .claude/skills/today/today.py
   ```

2. 標準出力の 1 行（`CREATED: ...` または `EXISTS: ...`）を確認し、会話には「作成して開いた」か「既存を開いた」かだけ短く伝える。
3. スクリプトが非ゼロで終了した場合のみ、stderr の内容を報告する。

## やらないこと

- Claude 自身による日付計算・ファイル作成・index.scb 編集・`code` 起動。すべて `today.py` に任せる。
- スクリプトが想定外の挙動をしたとき以外、Python コードを編集する判断を勝手にしない（ユーザーに相談する）。
