---
layout: default
title: GitHub Pages Jekyll まわりの試行とか
---

# links
- [Configuration - Jekyll](https://jekyllrb.com/docs/configuration/)
  - [kramdown option](https://jekyllrb.com/docs/configuration/markdown/)

## デフォ
- [ghpages デフォ設定解説](https://help.github.com/en/articles/configuring-jekyll)

```
github: [metadata]
encoding: UTF-8
kramdown:
  input: GFM
  hard_wrap: false
future: true
jailed: false
theme: jekyll-theme-primer
gfm_quirks: paragraph_end
```

# todo
- ~~リンクの altext 中に `|` があると表と解釈されてリンクにならない~~
  - 無理っぽい
  - 唯一見つかったのが [Kramdown bug - pipe character in Markdown link creates a table · Issue #2818 · jekyll/jekyll · GitHub](https://github.com/jekyll/jekyll/issues/2818) だが「ハイフンに置き換えるしかない」で結論
- ~~トップに戻るリンクをどっかに設置する フッターとか？~~ フッターに
- url 張っただけでリンクさせる anglebracket使えじゃなくて
  - js で re で後で張るしかなさそうか……

# test area
:smile:
