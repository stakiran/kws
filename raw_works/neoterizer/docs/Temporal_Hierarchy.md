# Temporal Hierarchy
# 日週月年といった日以上の単位をどう構造化するかという話、あるいは構造そのものを指す

# 例
🌎️[Temporal hierarchy for monthly time series. | Download Scientific Diagram](https://www.researchgate.net/figure/Temporal-hierarchy-for-monthly-time-series_fig1_358425154)
<img src="https://gyazo.com/1f3b5a6922d196e6597ff4a9b06bc055.png" />

🌎️[A cross-temporal hierarchical framework and deep learning for supply chain forecasting - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0360835220305040)
<img src="https://gyazo.com/fefe6ba912660c7952d97cf18ac04ce4.png" />

- DWMY
    - Year、Month、Week、Dayのみからなる最もシンプルなモデルです<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
- sta式
    - どの階層も5要素以下で抑えられていますl<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
    - Day
    - Weekday
        - 5-day
    - Holiday
        - 2-day
    - Week
        - 1-weekday + 1-holiday
    - Month
        - 4-5week
    - Quater
        - 3-month
    - Year
        - 4-quatter

# 開発秘話
- 元々はsta式と名付けたモデルをつくっていました
    - これを一般化してTemporal Hierarchyと名付けました
- ちなみにsta式の背景ですが、生成AIを用いた要約で使うためです
    - GTDのレビューがそうですが、週次レビューでは日次のノート7個をインプットにし、月次レビューでは週次レビューのノート4-5個をインプットにし、と一つ前の階層のアウトプットを使うと現実的におさまります（そうしないと月次レビューで30の日次ノートを見るなんてことになるor日次ノートすらなくて思い出せない）
    - さて、生成AIにもコンテキストウィンドウがあるため、あまりたくさん情報は渡せません。DWMYだとMonthの7個やYの12個で溢れてしまいそうです。もう少し抑えたいです、というわけで平日、休日、クォーターを導入して、5個以内、できれば4個以内に抑えた構造にしたのです。それがsta式です
    - つまり7ノート分はコンテキストウィンドウに入りきらなくとも、4-5ノートなら入るのではないかということです。少なくとも入る可能性は上がります

