# sftf(Single Function Text File)
**sftf(Single Function Text Files)** とは、単一の機能を持つテキストファイルを指す。プレーンテキストかつローカルで管理するため軽量であり、管理もしやすく、現代ではもちろん生成 AI との連携もしやすい。各ファイルはシンプルであり、フォーマットや運用に工夫の余地もあるため、カスタマイズ性とクリエイティビティにも優れている。

## sftf の例

### from [Thymer](https://thymer.com/)

```
todo.txt
notes.txt
wiki.txt
projects.txt
journal.txt
reminders.txt
thoughts.txt
goals.txt
tasks.txt
research.txt
clients.txt
trips.txt
thesis.txt
recipes.txt
draft.txt
books.txt
ideas.txt
```

### [GTDを噛み砕く](https://stakiran.github.io/gtd_kamikudaku/)

```
inbox.txt
someday.txt
documents.txt
recyclebin.txt
projects.txt
calendar.txt
waiting.txt
nextactions.txt
```

### 生成AIによる例
OpenAI API を使用。

GPT-4.1

```
1. contacts.txt（連絡先リスト）
2. passwords.txt（パスワードやIDリスト）※セキュリティ注意
3. expenses.txt（支出・家計簿）
4. meetings.txt（会議メモ／議事録）
5. shopping.txt（買い物リスト）
6. anniversaries.txt（記念日・誕生日リスト）
7. health.txt（健康メモ・通院記録）
8. study.txt（学習メモ／勉強計画）
9. links.txt（お気に入り・参考リンク集）
10. movies.txt（観たい映画・観た映画リスト）
11. music.txt（好きな曲やアーティスト）
12. inspiration.txt（インスピレーションや名言集）
13. habits.txt（習慣・ルーティン管理）
14. milestones.txt（達成したこと・進捗管理）
15. questions.txt（疑問点や調べたいこと）
16. schedules.txt（スケジュールや締切リスト）
17. bugreport.txt（気付いたバグや改善点）
18. gratitude.txt（感謝日記・good things）
19. fitness.txt（運動記録・目標）
20. travelbucket.txt（行きたい場所リスト）
```

GPT-4o

```
1. contacts.txt - 連絡先情報を管理するためのファイル
2. budget.txt - 予算や財務計画のためのファイル
3. workouts.txt - トレーニングやエクササイズの記録用
4. logs.txt - 日々の活動や進捗を記録するためのログファイル
5. shoppinglist.txt - 買い物リスト用のファイル
6. passwords.txt - パスワード管理（ただし、セキュリティに注意してください）
7. music.txt - お気に入りの曲やプレイリストの管理用
8. movies.txt - 見たい映画や観た映画の記録用
9. travelideas.txt - 訪れたい場所や旅行のアイデアを書き留めるため
10. meetings.txt - 会議やイベントの予定を管理するため
11. supplies.txt - 仕事や趣味で必要な物を記録するため
12. habits.txt - 習慣トラッカー用
13. gratitude.txt - 感謝日記用
14. chores.txt - 家事や雑用のリスト
15. milestones.txt - 達成した目標や重要な出来事を記録するため
```

GPT-5.1

```
inbox.txt（とりあえず何でも放り込む収集箱）
log.txt（作業ログ・行動ログ）
plan.txt（週次・月次の計画）
habits.txt（習慣トラッカー・ルール）
finance.txt（お金のメモ・出費・収入）
health.txt（体調・運動・睡眠の記録）
study.txt（勉強計画・進捗）
work.txt（仕事専用メモ）
home.txt（家事・家の管理系）
shopping.txt（買い物リスト）
packing.txt（持ち物リスト・パッキング）
meeting.txt（会議メモ・議事録）
contacts.txt（連絡先・人脈メモ）
bookmarks.txt（URLと簡単な説明）
quotes.txt（好きな言葉・引用）
snippets.txt（よく使う文章・コード片）
templates.txt（メール・書類・手順の定型文）
archive.txt（完了したメモの退避場所）
someday.txt（いつかやりたいことリスト）
problems.txt（今抱えている問題と対策案）
decisions.txt（重要な決断と理由の記録）
learnings.txt（学んだことのまとめ）
mistakes.txt（失敗メモと再発防止）
wishlist.txt（欲しいもの・やりたい体験）
routines.txt（朝・夜・仕事前後のルーティン）
travelplan.txt（旅行計画・日程案）
movies.txt（観たい／観た映画とメモ）
music.txt（曲・アルバム・プレイリスト案）
fitness.txt（トレーニングメニュー・記録）
cooking.txt（料理メモ・下ごしらえ・コツ）
```

GPT-5.2

```
inbox.txt（思いついたことの一時受け皿）
someday.txt（いつかやる／やりたい）
next.txt（次にやることだけ）
waiting.txt（返信待ち・納品待ち・依頼待ち）
calendar.txt（予定のメモ。日付＋用件）
log.txt（作業ログ／変更履歴）
review.txt（週次・月次の振り返り用）
decisions.txt（決定事項と理由）
meeting_notes.txt（会議メモ）
meeting_agenda.txt（会議アジェンダ）
people.txt（人脈・連絡先・メモ）
contacts.txt（連絡先だけを集約）
passwords.txt（※推奨はしない。作るなら暗号化前提）
finances.txt（支出・収入・予算）
invoices.txt（請求・見積の記録）
assets.txt（所持品・サブスク・ライセンス一覧）
subscriptions.txt（契約サービスと更新日）
health.txt（体調・通院・服薬メモ）
workouts.txt（筋トレ・運動ログ）
meals.txt（食事ログ）
habits.txt（習慣トラッキング）
checklists.txt（定型手順：旅行準備、引っ越し等）
templates.txt（よく使う文章テンプレ）
snippets.txt（定型文・コピペ用）
links.txt（後で読むURL置き場）
reading_list.txt（読みたい記事・本）
watchlist.txt（観たい映画・動画）
learning.txt（学習メモ、講座進捗）
glossary.txt（用語集・自分用辞書）
faq.txt（自分用FAQ／詰まりポイント集）
troubleshooting.txt（ハマりどころと解決策）
commands.txt（よく使うコマンド集）
configs.txt（設定メモ、環境構築の要点）
backup_plan.txt（バックアップ方針）
security.txt（セキュリティの注意点）
garden.txt（アイデアを育てるメモの寄せ集め）
writing_queue.txt（書きかけ・書く予定のネタ）
pitches.txt（提案文・企画案）
content_calendar.txt（投稿・公開予定）
portfolios.txt（実績・リンク集）
gratitude.txt（感謝メモ）
quotes.txt（引用・フレーズ集）
misc.txt（分類できないもの置き場）
```

o1

```
1. code_snippets.txt ちょっとしたコード例やメモを保存・再利用したいときに便利です。
2. cheatsheet.txt コマンドの使い方や定型文、よく使う式などを一覧にしておくと、必要な際に素早く参照できます。
3. references.txt 論文や記事、オンラインリソースのリンクや書誌情報をまとめておきましょう。
4. budget.txt / finances.txt 日々の支出入のメモや、月々の予算管理などを記録するのに便利です。
5. chores.txt ルーチンの家事や作業のチェックリストとして使えます。
6. reading_list.txt 読みたい本や記事、ウェブサイトなどをリストアップしておくファイルです。
7. vocabulary.txt 学習中の単語や気になる言葉を記録しておくと、自分だけの辞書として活用できます。
8. quotes.txt 心に残った言葉や名言などをメモするのにぴったりです。
9. blog_ideas.txt ブログ記事にしたいテーマやトピックを思いついたときに書き留めておきましょう。
10. habit_tracker.txt 運動や学習などの習慣目標を記録し、進捗を確認するのに役立ちます。
11. gratitude.txt 日々感謝していることや嬉しかったことを書き留めておくと、モチベーション維持に役立ちます。
12. dream_log.txt 起きたときに覚えている夢やアイデアをすぐに書いておけるファイルです。
13. meeting_notes.txt 会議や打ち合わせの内容、決まったこと、宿題項目などを整理するために使います。
14. lessons_learned.txt 失敗や成功から学んだことをまとめると、同じ失敗を繰り返さずに済みます。
15. anniversary_reminders.txt 記念日や誕生日など、忘れたくない大切な日のリストを管理するのに便利です。
```

o3mini

```
• contacts.txt – 連絡先や取引先の情報を管理  
• schedule.txt – 日程、アポイント、予定表を記録  
• expenses.txt または budget.txt – 家計簿や経費、予算の管理  
• bookmarks.txt – お気に入りのURLや参考サイトのリスト  
• meeting_minutes.txt – ミーティングの議事録や要点を記録  
• study_notes.txt – 学んだことや参考資料の要約  
• workouts.txt – トレーニングメニューや運動記録を管理  
• log.txt – 日々の活動ログやエラー記録  
• reading_list.txt – 読書予定・読了リスト、書籍管理  
• playlist.txt – お気に入り音楽などのリスト（ジャンル別に整理も可）  
• passwords.txt – パスワードのメモ（※セキュリティ上の注意が必要）  
• archives.txt – 過去の資料やデータの保管場所として  
• workflow.txt – 業務手順やプロセスのマニュアルとして  
• brainstorming.txt または ideas_archive.txt – 新しいアイデアの記録・蓄積  
• travel_itinerary.txt – 旅行の詳細な計画や行程表  
```

o4mini

```
・contacts.txt（連絡先一覧）  
・addresses.txt（住所録）  
・passwords.txt（パスワード管理 ※暗号化推奨）  
・budget.txt（予算管理）  
・expenses.txt（支出記録）  
・shopping_list.txt（買い物リスト）  
・wish_list.txt（欲しいものリスト）  
・habit_tracker.txt（習慣トラッカー）  
・mood_log.txt（気分／メンタルログ）  
・health_log.txt（健康記録）  
・fitness_log.txt（運動・トレーニング記録）  
・dream_journal.txt（夢日記）  
・gratitude.txt（感謝ノート）

・meeting_notes.txt（会議メモ）  
・agenda.txt（アジェンダ）  
・minutes.txt（議事録）  
・roadmap.txt（ロードマップ）  
・status_report.txt（進捗報告）  
・proposals.txt（企画書・提案書メモ）  
・invoices.txt（請求書履歴）  
・clients.txt（※既出ですが顧客管理として）

・itinerary.txt（旅程表）  
・packing_list.txt（持ち物リスト）  
・travel_expenses.txt（旅行費用管理）
・vocabulary.txt（単語帳）  
・language.txt（語学メモ）  
・experiments.txt（実験・検証ノート）  
・bibliography.txt（参照文献一覧）  
・citations.txt（引用メモ）

・code_snippets.txt（コードスニペット）  
・cheatsheet.txt（チートシート）  
・command_reference.txt（コマンドリファレンス）  
・config_notes.txt（設定メモ）  
・bug_list.txt（バグ／Issue リスト）

・story_ideas.txt（物語アイデア集）  
・characters.txt（登場人物設定）  
・plot_outline.txt（筋書きアウトライン）  
・script.txt（台本／セリフ）  
・world_building.txt（世界観メモ）

・movies.txt（観た映画リスト）  
・books_to_read.txt（読みたい本リスト）  
・music_list.txt（音楽リスト）  
・podcasts.txt（ポッドキャストメモ）  
・quotes.txt（名言・引用集）

・checklists.txt（汎用チェックリスト）  
・maintenance_log.txt（メンテナンス記録）  
・events.txt（行事・イベント管理）  
・goals_progress.txt（目標達成度ログ）  
```

## sftf のフレームワーク「キラノ分類」
**キラノ分類** とは sftf の全体像を網羅した分類体系であり、開発者の吉良野（きらの）にちなんでキラノ分類と呼ぶ。

- SFTF を比較的高精度に分類できる
    - 1 つのシステムは 4 つのカテゴリーを持ち、これをシステムモジュールと呼ぶ
    - キラノ分類では 5 つのシステムモジュールをつくる
        - 記録系、適用系、駆動系、行動系、処理系
- あなたオリジナルのシステムモジュールをつくっても構わないが、キラノ分類に従うなら1モジュール4カテゴリーの単位でつくるべきである
    - 4 という数字は理解のしやすさ、使いやすさ、分類の精度などをバランスよく取れる数である

以下全モジュールを示す。

記録系のMILC（ミルク）

| 英語名 | 意味 | 解説 |
| --- | --- | --- |
| Material | 情報 | 知識、事実、解釈など |
| Inventory | 目録 | 網羅やメンテナンスも重視。趣味も可能だが実用寄り |
| Log | 記録 | あとで振り返るために。時系列がある |
| Collection | 収集 | 必要に応じて見返すために。実用も可能だが趣味寄り |

適用系のGRRS（グルーズ）

| 英語名 | 意味 | 解説 |
| --- | --- | --- |
| Guide | 手順 | レシピほど厳密性はない。広域でありリファレンスも含む |
| Recipe | 手順 | 厳密に上から順に適用するニュアンス |
| Review | 点検 | 点検の観点を並べたもの。厳密性は問わない。チェックリストやトリガーリスト |
| Spell | 呪文 | パスワードやコマンドや設定値など「常に同じ文字列を使う」もの |

駆動系のCRAP（クラップ）

| 英語名 | 意味 | 解説 |
| --- | --- | --- |
| Constraint | 制約 | 責任、任務、所属、役割、肩書、プロジェクトなど「負っている」もの |
| Resouce | リソース | 自分が持っていて、使うことができて、消耗するもの。資産、資源、手札、武器 |
| Aim | エイム | 目指したいもの、手に入れたいもの、ほしいもの。あるいはそれらを細分化したもの |
| Plan | プラン | エイム、コンストレイント、リソースを踏まえた短期的・中長期的な動き方 |

行動系のAICE（エーアイス）

| 英語名 | 意味 | 解説 |
| --- | --- | --- |
| Action | 行動 | タスク、TODO、やりたいこと、あとで読むなど。対象は具体的 |
| Idea | 行動 | アクションほど具体的ではないもの |
| Concept | 概念 | 行動的ではなく、かつマテリアルでもないもの |
| Event | 予定 | - |

処理系のPAID（ペイド）

| 英語名 | 意味 | 解説 |
| --- | --- | --- |
| Inbox | 未処理 | 未処理と未分類 |
| Archive | 保管 | 最悪削除してもいいがいったん保存しておきたいもの |
| Pending | 未整理 | 完了していない、かつ分解できていないもの|
| Draft | 下書き | 誰かに話したり書いたりするもの・するかもしれないもの |
