#!/usr/bin/env python3
import json
import os
import re

# Paths
IN  = "neoterizer.json"
MID = "neoterizer_masked.json"

# --- Preprocess: mask sensitive fields ---
with open(IN, encoding="utf-8") as f:
    data = json.load(f)
for u in data.get("users", []):
    for key in ("id", "email"):
        if key in u:
            u[key] = "X" * len(u[key])
with open(MID, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# --- Helpers ---
def writable(name):
    # Windows forbid: \ / : * ? " < > | and space
    return re.sub(r'[\\/:*?"<>| ]', "_", name)

# Build title → filename map
pages = data.get("pages", [])
title2file = {
    p["title"]: writable(p["title"]) + ".md"
    for p in pages
}

# Build title → first Gyazo image URL
first_img_url = {}
for p in pages:
    for ln in p.get("lines", []):
        m = re.match(r'^\[https://gyazo\.com/([0-9A-Fa-f]+)\]$', ln.strip())
        if m:
            first_img_url[p["title"]] = f"https://gyazo.com/{m.group(1)}.png"
            break

def convert_lines(lines):
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        text_line = line.strip()

        # Blank line
        if not text_line:
            out.append("")
            i += 1
            continue

        # Code block
        m = re.match(r'^code:(\S+)$', text_line)
        if m:
            ext = m.group(1).split(".")[-1]
            out.append(f"```{ext}")
            i += 1
            while i < n and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                out.append(lines[i].lstrip())
                i += 1
            out.append("```")
            continue

        # Table block
        m_tab = re.match(r'^([ \t　]*)(table:\S+)', line)
        if m_tab:
            base_indent = len(m_tab.group(1))
            i += 1
            rows = []
            while i < n:
                next_line = lines[i]
                indent_i = len(next_line) - len(next_line.lstrip(" \t　"))
                if indent_i <= base_indent:
                    break
                cells = re.split(r'\t+', next_line.strip())
                rows.append(cells)
                i += 1
            if rows:
                out.append("") # 表として認識させるために前後に空行をはさむ
                out.append("| " + " | ".join(rows[0]) + " |")
                out.append("| " + " | ".join("---" for _ in rows[0]) + " |")
                for r in rows[1:]:
                    out.append("| " + " | ".join(r) + " |")
                out.append("")
            continue

        # Gyazo image
        gy = re.match(r'^\[https://gyazo\.com/([0-9A-Fa-f]+)\]$', text_line)
        if gy:
            url = f"https://gyazo.com/{gy.group(1)}.png"
            out.append(f'<img src="{url}" />')
            # 空行をはさまないと次行以降のmarkdownが認識されないので、はさむ
            out.append(f'')
            i += 1
            continue

        # Project link [/project] or [/project/page]
        pr = re.match(r'^\[/([^\]]+)\]$', text_line)
        if pr:
            path = pr.group(1)
            parts = path.split('/', 1)
            proj = parts[0]
            if len(parts) > 1:
                page = parts[1]
                # スペース含まれてるとMarkdownとして破綻するね
                # 実装甘い可能性ある（他のパターンが漏れてる気がする🐰
                page = page.replace(' ', '_') 
                url = f"https://scrapbox.io/{proj}/{page}"
            else:
                url = f"https://scrapbox.io/{proj}"
            out.append(f'🌎️[{path}]({url})')
            i += 1
            continue

        # External links [text URL] or [URL text]
        ex = re.match(r'^\[([^\]]+)\]$', text_line)
        if ex:
            parts = ex.group(1).split()
            url = None
            # URL at start
            if parts and (parts[0].startswith("http://") or parts[0].startswith("https://")):
                url = parts[0]
                txt = " ".join(parts[1:])
            # URL at end
            elif parts and (parts[-1].startswith("http://") or parts[-1].startswith("https://")):
                url = parts[-1]
                txt = " ".join(parts[:-1])
            if url:
                out.append(f'🌎️[{txt}]({url})')
                i += 1
                continue

        # Internal link [title]
        def repl_int(m0):
            t = m0.group(1)
            if t.endswith(".icon"):
                return m0.group(0)
            if t in title2file:
                return f'[{t}]({title2file[t]})'
            return m0.group(0)
        line = re.sub(r'\[([^\]\.]+)\]', repl_int, line)

        # Icon [xxxx.icon]
        def repl_icon(m0):
            name = m0.group(1)
            href = title2file.get(name, name + ".md")
            src = first_img_url.get(name, "")
            return f'<a href="{href}"><img src="{src}" alt="{name}" width="16"/></a>'
        line = re.sub(r'\[([^\]]+)\.icon\]', repl_icon, line)

        # Heading or List
        indent = len(line) - len(line.lstrip(" \t　"))
        txt = line.strip()
        if indent == 0:
            out.append(f"# {txt}")
        else:
            if indent == 1:
                spaces = ""
            else:
                spaces = " " * ((indent - 1) * 4)
            out.append(f"{spaces}- {txt}")
        i += 1

    return out

# Write each page to docs/
odir = "docs"
os.makedirs(odir, exist_ok=True)
for p in pages:
    fname = title2file[p["title"]]
    content = convert_lines(p.get("lines", []))
    with open(os.path.join(odir, fname), "w", encoding="utf-8") as f:
        f.write("\n".join(content))

print("Generated docs/ with Markdown files.")
