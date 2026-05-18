
# tms 筆者用メモ

| 和名称   | 進捗 |
| -------- | ---------- |
| 分解支援 | x 少なすぎるのでもっと|
| 集中支援 | x まあまあだがもうちょい |
| 資料支援 | o 本質的にネタ少なめだがもうちょいあってもいい |
| 操作支援 | x もっと観点あるはず |
| 心理支援 | x もっと増やしたい |
| 想起支援 | o |
| 予定支援 | o |

# 記述したタスクリストにどこまで従うか → 準拠率？密度で分ける？
密度/準拠率
高   低       目的が弱い、意志が弱い、弱くても済む状態下にいる
高   高       目的や意志が高い、単に仕事量多いのをタスク管理技術で捌いてるマン
低   低       素人
低   高       タスク管理初心者

面白そうな概念だが tm にも tms にも書けないので没。自己満っぽいし。

# タスク管理とは～～である
2019/05/30 

メモである。

- 忘れないためにやることを書いておく

整理である。

- いつ何をどの順でやればいいかを頭で判断できない
- 書いて、並べれば、判断しやすい

言語である。

- 共通認識。共通言語。
  - ゴールに行くために何がどの順で立ちはだかっているのか
  - 誰が何に取り組んでいるのか
  - このあたりを共通的に語れるようにする

設計である。

- ゴールにどのように進むかを考えるもの
- 考える = 必要なタスクを洗う、実行順序を決める、実行日を配分する……

# タスク生成管理として tms から隔離した分
2019/05/23

タスクを集める収集系はどうする？トリガーリスト / 収集は英語的には collect 一択だが集中と被る。この分解に含めちゃう？だが分解って意味だとピンと来ない。breakdown ならギリギリありかもしれん。 / 人生という大タスクを分解すると考えれば収集も分解の範疇になる……。 / そうしよう。

# タスク管理ツール一覧
2019/05/08 07:23:44 きりないし大半は自分で使ってないゆえに表面的なゴミ解説にしかならないのでやらない

ただし以下に該当するものは扱わない。

- TTaM(特に「プロジェクト管理」と呼ばれることがあるもの)
  - TTaM については Wikipedia が詳しい → [Comparison of project management software - Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_project_management_software)
- 一般的に「タスク管理ツール」とは言わないが、タスク管理機能を持つ(あるいはタスク管理として使いこなせる)もの
  - 例: Microsoft Outlook
    - 一般的には「メーラー」あるいは「PIM」である
    - → [List of personal information managers - Wikipedia](https://en.wikipedia.org/wiki/List_of_personal_information_managers)
  - 例: Google カレンダー
    - 一般的には「カレンダー」である
  - 例: Dynalist 
    - 一般的には「アウトライナー」である
- ToM(Todoリストを扱うアプリは星の数ほど存在するから)

★2019/04/09 まずはブレスト。整理はその後で。

★自己啓発書でしれっと取り上げられてるタスク管理手法とかはどうする？

```
Microsoft Todo
Google Todo
Outlook
TaskChute
Taskuma
TaskChute Cloud
Tritask
todo.txt
todo.md
Todoist
Toodledo
Remember the milk
みかんリスト
```

既存情報源:

- [Category:Task management software - Wikipedia](https://en.wikipedia.org/wiki/Category:Task_management_software)
  - 編集者による主観で 2019/05/08 現在で 30 ほど

# task management 論文ネタ
★一応論文 [(Riss U.V., Rickayzen A., Maus H., van der Aalst W.M.P.) Challenges for Business Process and Task Management](http://www.jucs.org/jukm_0_2/riss/jukm_0_2_77_100_riss.html) personal task management ってキーワードあるな。7 Conclusions 読んだ限りだと「こういう条件整ったら生産性捗るよ」的な知見っぽくて、tm あまり関係なさそうだが

★タスク管理は自由であるべき？権威を定めて導くべき？理論化とかするべき？いやたぶん知らないだけで既に論文とかたくさんある気がするけども……。 ["task management" - Google Scholar](https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q=%22task+management%22&btnG=) ジョブネタが多め。どんぴしゃなのもちらほら→[What a to-do](https://dl.acm.org/citation.cfm?id=985785) これはtaskvistaというツールが出てる、歴史も少し。task list management tlm → pim personal information managementとか。……方向性違うなぁ。手段の話じゃなくてタスクという概念の話。概念をどう捉えて体系化するかの話。その辺扱った前例はないのだろか。

# 権限系分類
没理由: 元々 open closed list を属性として扱おうとしたが、これはリスト単位でつくものであってタスク単位でつくものではない、つまり扱えないので没。

## 分類-権限系
権限系の属性は、タスクに対する操作を制限するために付与されるもの。

権限系の属性は、タスクそのものに付与されないことがある。上位の概念（タスクを包含しているコンテナやタスクを管理するツール側の設定）側で付与され、結果的に各タスクにも当該権限属性が働くという動きをする。つまり、あるタスクにある権限が働いているからといって、それがタスクそのものについた権限属性によるものとは限らない。そのタスクを扱う上位概念によるものかもしれない。

### ロック
ロック(Lock) とは
