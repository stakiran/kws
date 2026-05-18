import os

def main():
    # docs ディレクトリのパスを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(base_dir, "docs")

    # Markdown ファイルを取得し、index.md 自身を除外
    files = [
        f for f in os.listdir(docs_dir)
        if f.endswith(".md") and f.lower() != "index.md"
    ]
    files.sort()

    # 目次コンテンツを生成
    lines = ["# 目次", ""]
    for filename in files:
        title = os.path.splitext(filename)[0]
        lines.append(f"- [{title}]({filename})")

    content = "\n".join(lines) + "\n"

    # docs/index.md に書き込み
    index_path = os.path.join(docs_dir, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
