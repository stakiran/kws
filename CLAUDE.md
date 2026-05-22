# kws
このリポジトリは、私のナレッジワーク作業場である。

この作業場では、新しい概念をつくることに力点を置く。日々の作業は wiki/ 上で行い、結実したものは別途作品化を行う。作品は別のリポジトリなどで公開するだろう。そうして完了した作品が raw_works/ に入る。つまり kws とは、「過去の作品」を配置し、wiki ベースで日々次の作品を育てる場と言える。

作品をつくって kws に取り込むまでは、以下を想定する:

- 1: この作業場で日々 wiki/ を育てる
- 2: wiki/ の中で、新しい概念が出てきたり、体系的な整理が見えてきたりする
- 3: ある程度見えてきたら、別のリポジトリをつくって、そこで改めて整理をし、リリースする
- 4: 3 を終えた作品を、kws の raw_works/ として配置する

作品の歴史と背景も整理しておく:

- 2020年: 概念をつくる営みに足を踏み入れており、ブログ風に色んなテーマで書いたり、古典とも言えるメソッド GTD の解釈を試みたりしている
    - monolithic: monolithic/index.md から辿れる。ブログのように、思いつくままに概念をつくっている
    - GTDを噛み砕く: gtd-kamikudaku/book.md から辿れる。GTD を自分の言葉で整理し直し、かつ具体的な方法にまで踏み込んで実装したもの
- 2024年: 実は Cosense（当時 Scrapbox）を使い始め、傾注しており 2 万ページ以上を書いていた。その集大成として、かねてから研究していたタスク管理の整備に踏み込む。また概念をつくる営みで食べていくために、Workware Engineering を 2 週間で整備した上で R&D の会社に応募したりしていた
    - タスク管理を噛み砕く: taskmanagement-kamikudaku/merged.md から辿れる。未だ整理されていない「タスク管理」を体系化したもの。全体像から周辺技法まで回収しつつ、終盤は文芸的タスク管理や探索的タスク管理といった提案にまで踏み込む
    - Workware Engineering: workware-engineering/merged.md から辿れる。概念（仕事で使う概念的道具）をつくるための工学として整備開始したもので、α版の扱いだが、売り込みに失敗し時期尚早と判断して中断した。具体的な方法は未整備だが、基本的な原則は整理しきれている
- 2025年: 応募を経て当事者意識が加速し、概念づくりの密度が増す。仕事のやり方・考え方に関する不満が大きくなり、仕事上のキャリアも停滞し、といった現状も糧にして、多数の作品を生み出していった
    - 仕事術2.0: workhack2.0/index.md から辿れる。VUCA で DEIB な時代に通用する仕事術を開発し、note の記事として計 400 以上を公開。それを 1-記事 1-markdown で変換したものを置いている。記事間はリンクにて繋がっており、知識ネットワークを意識している
    - Remotism: remotism/merged.md から辿れる。住み込み → 出社 → リモートと現代は第三パラダイムであるべきで、デフォルト・リモートと名付けた上で、これに必要な考え方とやり方を体系的に整備した
    - 知的生産に魅せられし者: neoterizer/index.md から辿れる。また読み方は neoterizer\docs\このサイトについて.md から辿れる。梅棹忠雄が夢見た「知的生産」を解釈し直し、実用的な概念を、容赦なくかつ楽しく開発してきた。Cosense にて書いていたものを markdown 化している。1-file 1-page であり、ページ間はリンクにて繋がっていて知識ネットワークを意識している
    - Soft Skills Engineering: soft-skills-engineering/index.md から辿れる。ソフトスキルを自分で開発できるよう工学を試みたもの。Workware Engineering や知的生産のような「概念をつくる営み」そのものの整備として、少し抽象性を落とした（ソフトスキルに絞った）ものとなる
- 2026年: 応募も通らず、作品も評価されず、居座るコミュニティから評価されることもなく、自分個人の限界と弱点を意識し始める。生成 AI に解釈してもらったり、生成 AI と連携して品質を高めたりといったアプローチを積極的に採用し始める。ただいま 2026-05-20、現在進行形
    - Collaboration Modules: collaboration-modules/index.md から辿れる。VUCA で DEIB な時代のコラボレーションを上手くやるための概念集。claude 利用を前提とした構成でつくっている。2025 年時代の焼き増しも含むが、新しい概念も含む。体系化まではしていないが、200 以上つくっており一区切りはついた認識
    - Solo-work Modules: 目次にあたるファイルはないが、根幹となるソロワークは solo-work-modules\modules\solo_work.md にて解説している。ひとりで仕事をすることの必要性に力点を置き、チームワークと対比してソロワークと名付けている。そのための考え方とやり方の整備を試みたが、Collaboration Modules ほど充実はしておらず、一区切りもついていない。自分のキャリアを上げる作品としては弱いと考えて、優先順位を落としたまま放置中

## ディレクトリ構成
- raw_gists/
    - 私の github gists 内容を取得して保存している
    - markdown
    - fetch_gists.py にて更新する。それ以外は read only
- raw_works/
    - 私の過去の成果物を保存している
    - markdown
    - 成果物ごとにフォルダで分けられている。1-folder 1-work。
    - 成果物は数百以上のテキストファイルや数十万文字以上のテキストファイルとして存在することもありえる
    - 更新は私自ら行う。基本的には read only
- wiki/
    - 日々の作業メモを書いている
    - scb 記法を用いて書かれている
    - 更新は私自身も行うし、AI にも行わせる

## scb 記法について
- 拡張子 .scb のファイルは scb 記法であり、Scrapbox をベースとしたフォーマットである
- 行指向的であり、1-space 1-indent の箇条書きを書く
- インデントは構造を示す
- 空行で区切られた個々の塊も構造を示す
- リンクは `[pageA]` で書き、pageA.scb にリンクしている
    - リンク記法上でリンク先を開いたり、リンク先がない場合はファイル新規をする
    - そのため scb 記法では気軽にページを切り出すことができ、ネットワーク構造をつくりやすい
- コードブロックは code:xxx の行と :c の行で囲った部分になる

リンク時のファイルは以下のとおり修正する。これは不正なファイル名にさせないための対策である:

```ts
function fixInvalidFilename(filename: string) {
    let newFilename = filename;
    const after = '_';
    newFilename = newFilename.replace(/\\/g, after);
    newFilename = newFilename.replace(/\//g, after);
    newFilename = newFilename.replace(/:/g, after);
    newFilename = newFilename.replace(/\*/g, after);
    newFilename = newFilename.replace(/\?/g, after);
    newFilename = newFilename.replace(/"/g, after);
    newFilename = newFilename.replace(/>/g, after);
    newFilename = newFilename.replace(/</g, after);
    newFilename = newFilename.replace(/\|/g, after);
    // スペースはファイル名としては有効だが何かとウザイので潰す
    newFilename = newFilename.replace(/ /g, after);
    return newFilename;
}
```

厳密な文法は、以下の scb.tmLanguage.json を見よ

```json
{
	"$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
	"name": "vscode-scb",
	"scopeName": "text.scb",
	"patterns": [
		{
			"include": "#content"
		}
	],
	"repository": {
		"content": {
			"patterns": [{
				"include": "#lines"
			}]
		},
		"lines": {
			"patterns": [
				{ "include": "#line" },
				{ "include": "#block" }
			]
		},
		"line": {
			"patterns": [
				{ "include": "#indent" },
				{ "include": "#line-body" }
			]
		},
		"block": {
			"patterns": [
				{ "include": "#codeblock" }
			]
		},


		"indent": {
			"patterns": [
				{ "include": "#indent9over" },
				{ "include": "#indent8" },
				{ "include": "#indent7" },
				{ "include": "#indent6" },
				{ "include": "#indent5" },
				{ "include": "#indent4" },
				{ "include": "#indent3" },
				{ "include": "#indent2" },
				{ "include": "#indent1" }
			]
		},
		"indent1": {
			"patterns": [{
				"name": "indent.1.scb",
				"match": "^( )"
			}]
		},
		"indent2": {
			"patterns": [{
				"name": "indent.2.scb",
				"match": "^(  )"
			}]
		},
		"indent3": {
			"patterns": [{
				"name": "indent.3.scb",
				"match": "^(   )"
			}]
		},
		"indent4": {
			"patterns": [{
				"name": "indent.4.scb",
				"match": "^(    )"
			}]
		},
		"indent5": {
			"patterns": [{
				"name": "indent.5.scb",
				"match": "^(     )"
			}]
		},
		"indent6": {
			"patterns": [{
				"name": "indent.6.scb",
				"match": "^(      )"
			}]
		},
		"indent7": {
			"patterns": [{
				"name": "indent.7.scb",
				"match": "^(       )"
			}]
		},
		"indent8": {
			"patterns": [{
				"name": "indent.8.scb",
				"match": "^(        )"
			}]
		},
		"indent9over": {
			"patterns": [{
				"name": "indent.over9.scb",
				"match": "^( ){9,}"
			}]
		},

		"line-body": {
			"patterns": [
				{ "include": "#plain-parts" },
				{ "include": "#quote-parts" }
			]
		},

		"codeblock": {
			"begin": "(?<=^( )*)code\\:",
			"end": "\\:c$",
			"name": "block.code.scb"
		},

		"plain-parts": {
			"patterns": [
				{ "include": "#parts" }
			]
		},
		"quote-parts": {
			"begin": "(?<=^( )*)>",
			"end": "$",
			"beginCaptures": {
				"0": { "name": "quote.line.start.scb" }
			},
			"endCaptures": {
				"0": { "name": "quote.line.end.scb" }
			},
			"name": "quote.line.scb",
			"patterns": [
				{ "include": "#parts" }
			]
		},

		"parts": {
			"patterns": [
				{ "include": "#part" }
			]
		},
		"part": {
			"patterns": [
				{ "include": "#link" },
				{ "include": "#literal" }
			]
		},
		"link": {
			"patterns": [{
				"name": "link.scb",
				"match": "\\[[^\\]]+\\]"
			}]
		},
		"literal": {
			"patterns": [{
				"name": "literal.scb",
				"match": "`[^`]+`"
			}]
		},

		"dummy": {}

	}		
}
```

また文中の🐰は私を示すアイコンであり、私のコメントを書いている。文頭に書いたり、文末に置いたり、行に置いた上でインデントにてぶら下げたりするが、いずれもその範囲が私のコメントであることを示す。

## Claude Mention について
.scb ファイル中の @claude 記法については .claude/rules/claude_mention.md を参照
