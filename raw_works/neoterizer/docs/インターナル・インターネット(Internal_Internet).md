# インターナル・インターネット(Internal Internet)
# 普段インターネットで受けている体験と同程度の体験を、社内で実現すること。したもの。

# 例
- Xと同程度のマイクロブログを実現する
    - 社員全員がアカウントを持っており、誰でも誰のポストを見れたりフォローできたりする
- Youtubeと同程度の動画共有を実現する
    - 社内の外には出ず、Public = 社内全体
    - Youtubeと同等の使い心地、探索体験、ブクマやリストなどの便宜、交流などが行える
- Stack OverFlowと同程度のQ&Aを実現する
    - 同社製品がすでにある:
🌎️[The trusted knowledge engine that powers people and AI. – Stack Overflow for Teams](https://stackoverflow.co/teams/)
🌎️[チーム専用のプライベートなQ＆Aサイトが作れる「Stack Overflow for Teams」提供開始。月額10ドルから － Publickey](https://www.publickey1.jp/blog/18/qastack_overflow_for_teams10.html)
            - 少し古いです。たとえば現在は大組織向けも For Teams に統合されているように見えます<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
- GitHubと同程度のVCS及びSocial Coding Platformを実現する
    - すでにEnterpriseプランやオンプレ版がある:
🌎️[企業向けGitHub。スマートなコラボレーションを促進 | GitHub](https://github.co.jp/enterprise.html)

# 背景
- インターネットの力は非常に強力であり、社内で使えると非常に優位だと考えられる
- しかし、この概念はわかりやすそうでわかりづらく、また実践例も皆無に等しい
- そんな中、[📖PLURALITY 対立を創造に変える、協働テクノロジーと民主主義の未来]が⿻の観点で、インターネットの素晴らしさを改めて啓蒙してくれた
    - 今こそチャンスだと考え、啓蒙のための概念をつくりなおしました。社内でインターネットをつくればいい、ということでInternal Internetとしました。ただのイントラネットとは違います。インターネットの、現在皆さんが日頃から受けている恩恵と同レベルを社内でもつくるというものです。イントラネットごときとは全然違います。この点を強調するため、このような名前にしています<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>

# 概要
- 主な想定は千人以上の大企業
    - これ以下の中小規模の場合、普通にインターネット上の各種SaaSを使えば事足りる
- インターナル・インターネットのために必要なこと
    - 1. [トランスフォーマトリー(Transformatory)](トランスフォーマトリー(Transformatory).md)への適応
        - 全社員全員が自由に使えるだけの投資（全社教育や継続的なインフラやサポートのメンテナンスも含む）をするということ
    - 2. キラー製品が社内版を公開すること、また同等レベルの製品が登場すること
        - 上記の例ではStack OverflowとGitHubのみです。マイクロブログや動画共有については、現状インターナル・インターネットレベルの製品はないと思います。動画については、Micorsoft Stream などがありますが、YouTubeにはとても及びません<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
        - 戦略としては「製品のバイナリ」自体を配布するか、企業ユースに耐えうる機能を揃えるかがあります。たとえば後者の例はGitHubで、Organizationという単位を導入したりしています。たとえばYouTubeも同じ戦略を取れるでしょう。企業という[🙏組織単位](🙏組織単位.md)をつくらせ、社員1人1人にアカウントをつくらせ、かつその組織単位のみが閲覧できるという公開設定をサポートすればいいのです。もっとも、BtoC戦略のYouTube（を要するGoogle）はそんなことはしないでしょうが<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
    - 3. インターナル・インターネット利用の解禁
        - 業務時間中でも自由に使えるようにすること
        - いかなる制約もあってはいけません。むやみに制約を課すのは、子供にフィルタリングソフトウェアを適用するようなものです。もちろんルール、ガイドラインや罰則や、動的な監視などガバナンス自体は必要です<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
    - 4. インターナル・インターネット利用に耐えうる個人デバイスの支給
        - 意外と盲点なのがここです<a href="sta.md"><img src="https://gyazo.com/a0a22d2fc5cf4fb2525db091fb66594b.png" alt="sta" width="16"/></a>
            - デバイスとはPCやスマホを想定しますが、普段プライベートでインターネットを快適に使えているのは、相応のデバイスを使っているからです。一方、会社ではそれらよりもスペックの劣った、使いづらいデバイスを使わされていることが多かったりします。これではインターナル・インターネットは行えません。
