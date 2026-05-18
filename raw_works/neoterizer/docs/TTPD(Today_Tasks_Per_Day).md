# TTPD(Today Tasks Per Day)
# 毎日「その日のタスク」を生成すること。
# [軽量タスク管理](軽量タスク管理.md)の一種。

# 例
- 筆者による実装として[Todaros]がある:
🌎️[stao/todaros](https://scrapbox.io/stao/todaros)
<img src="https://gyazo.com/c50eb5faa4202a6c9b8af0761a71c252.png" />


# 概要
- 概念的には以下がある:
    - [タスクソース]。タスクを発生させる元
        - TTPDでは「今日やるタスク」を常に取り出せる必要があります。上記のTodarosでは「どれくらいの頻度で行うタスクか」を事前に定義しておく、という形で実現しています<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
    - タスクリスト。今日やるタスクを記載するもの
        - TTPDでは毎日ここに「今日やるタスク」が自動で記入されます<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
- つまり毎日タスクソースを自動で読み込み、その日やるタスクを自動でタスクリストに転記する仕組み
    - ポイントは「自動」であること
    - 原始的には「毎日朝一で今日やるタスクを考えて洗い出そう」とするタスク管理手法が可能ですし、名前をつけるまでもなく多くの人が実践していることですが、違います。TTPDでは自動でやります<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>

# メリット
- [🙏ルーチンタスク](🙏ルーチンタスク.md)を効率的に処理できること
    - 今のところ、ルーチンタスク管理として有用であることがわかっています。事前定義 + それに基づいて日ごとに自動生成、という形で自動化することによって、毎日手作業で生成する手間をなくすのです<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
