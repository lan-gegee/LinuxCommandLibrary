# TAGLINE

从命令行读取、编辑 .docx 文件并添加批注，完整保留原有格式

# TLDR

以带结构定位符的 Markdown **读取文档**

```docx read document.docx```

从 Markdown **创建新文档**

```docx create report.docx --from content.md --title "Q3 Report"```

**替换文本**的同时保留格式和制表位

```docx replace invoice.docx "Amount Due" "$1,250.00"```

**查找文本并在匹配处添加批注**

```docx comments add contract.docx --at "$(docx find contract.docx 'liability' | head -1)" --text "Review this clause with legal."```

**开启修订模式**并进行红线修改

```docx track-changes contract.docx on
docx replace contract.docx "reasonable efforts" "best efforts" --track```

**可视化渲染页面**以便核对版式

```docx render proposal.docx --out pages/```

**独立安装**（经过校验的二进制文件）

```curl -fsSL https://raw.githubusercontent.com/kklimuk/docx-cli/main/install.sh | sh```

# SYNOPSIS

**docx** _<command>_ [options]

# DESCRIPTION

**docx** 是一款面向 AI 智能体和人类的命令行工具，可用于读取、编辑 Microsoft Word（.docx）文档、添加批注并进行审阅，且不会丢失格式或破坏 Word 无法再打开的文件。

它直接修改底层的 OOXML，而不是经由有损模型来回转换或重新序列化文档。智能体会获得一套稳定的定位符系统（例如 `p3:5-20`、`t1:r0c2:p0`）外加一份带注记的 Markdown 视图，从而实现精确而安全的编辑。

主要能力包括：

- 以 Markdown 或无损 JSON AST 形式读取
- 创建、插入、编辑、删除、替换内容
- 添加并管理批注、脚注、尾注、页眉/页脚、图片、超链接、表格
- 完整的修订（redline）支持，可接受/拒绝修订
- 样式管理与页面几何信息
- 通过 Word 或 LibreOffice 进行页面可视化渲染

该工具的设计原则是 `docx <command> --help` 始终是最权威的参考。它还附带一个可选的 Agent Skill，适用于 Claude Code、Codex 及类似的宿主环境。

# LOCATORS

定位符可以寻址段落（`pN`）、表格（`tN`）、节（`sN`）、单元格段落、字符区间（`pN:S-E`）以及实体 ID（`cN` 表示批注，`imgN` 表示图片等）。完整语法请使用 `docx info locators` 查看。

# COMMON COMMANDS

**create** FILE [--from PATH.md | --text "..."] [--title T] [--author A]

> 创建一个新的 .docx 文件。`--from` 接受与 insert/edit 相同的 Markdown 方言。

**read** FILE [--from LOC] [--to LOC] [--ast] [--comments] [--accepted|--current|--baseline]

> 将正文渲染为 Markdown（带定位符注记）或 JSON AST。支持多种修订视图。

**edit** / **insert** / **delete** / **replace** FILE ...

> 在定位符处修改内容，或通过批量 JSONL 处理。replace 会保留既有的 run 格式。

**find** FILE QUERY [--regex] [--all]

> 返回文本或格式匹配项的定位符（可供 --at 使用）。

**track-changes** on|off|list|accept|reject FILE

> 控制并审阅修订。

**comments** / **images** / **tables** / **styles** / **sections** ...

> 管理对应的文档部件。

**render** FILE [--out DIR]

> 生成页面图片，用于直观核对版式。

**wc** / **outline** / **info**

> 字数统计、标题树以及参考资料（schema、定位符）。

# CAVEATS

CLI 内部没有撤销功能——请使用 git 或文件副本兜底。会导致文件损坏的编辑（例如删除被引用的关系）会被拒绝执行。渲染依赖 Microsoft Word（macOS/Windows）或 LibreOffice。批量操作针对的是读取时刻的文档快照。

其 Markdown 方言能保留大部分格式，但对于会被 GFM 改动的内容，也提供了字面文本通道（`--text-file`）。

# SEE ALSO

[pandoc](/man/pandoc)(1), [libreoffice](/man/libreoffice)(1)

# RESOURCES

```[Source code](https://github.com/kklimuk/docx-cli)```

```[Homepage](https://kklimuk.github.io/docx-cli/)```

```[Documentation](https://kklimuk.github.io/docx-cli/)```

<!-- verified: 2026-07-11 -->
