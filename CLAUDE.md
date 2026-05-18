# kws
このリポジトリは、私のナレッジワーク作業場である。

この作業場では、新しい概念をつくることに力点を置く。日々の作業は wiki/ 上で行い、結実したものは別途作品化を行う。作品は別のリポジトリなどで公開するだろう。そうして完了した作品が raw_works/ に入る。つまり kws とは、「過去の作品」を配置し、wiki ベースで日々次の作品を育てる場と言える。

作品をつくって kws に取り込むまでは、以下を想定する:

- 1: この作業場で日々 wiki/ を育てる
- 2: wiki/ の中で、新しい概念が出てきたり、体系的な整理が見えてきたりする
- 3: ある程度見えてきたら、別のリポジトリをつくって、そこで改めて整理をし、リリースする
- 4: 3 を終えた作品を、kws の raw_works/ として配置する

作品の粒度、時系列、その他ストーリーについて:

- TBD...

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
