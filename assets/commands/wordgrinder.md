# TAGLINE

面向专注写作的终端文字处理器

# TLDR

**启动 WordGrinder**

```wordgrinder```

**打开文档**

```wordgrinder [document.wg]```

**导入文件**

```wordgrinder --import=[file.txt]```

**导出为其他格式**

```wordgrinder --export=[output.html]```

# SYNOPSIS

**wordgrinder** [_--import file_] [_--export file_] [_document_]

# PARAMETERS

**--import** _FILE_
> 导入文档。

**--export** _FILE_
> 导出文档。

_document_
> 打开文档。

# KEY BINDINGS

**Ctrl+S** - Save
**Ctrl+O** - Open
**Ctrl+Q** - Quit
**Ctrl+F** - Find
**Ctrl+R** - Replace
**Ctrl+K** - Style menu
**F1** - Help

# DESCRIPTION

**wordgrinder** 是一款基于终端的文字处理器，专为专注、无干扰的写作而设计。它强调内容而非外观，通过标题、段落和列表等样式来组织文档结构，而不是提供视觉排版控制。

文档以原生的 .wg 格式保存，可以完整保留结构，并可导出为 HTML、LaTeX、Markdown、ODT 和纯文本。全屏编辑环境让注意力集中在写作本身，并提供键盘快捷键进行导航和样式切换。

# CAVEATS

基于终端，没有所见即所得。排版功能有限。专注于散文写作场景。

# HISTORY

**WordGrinder** 为专注的终端写作而生。它提供了一个无干扰的文字处理环境。

# INSTALL

```apt: sudo apt install wordgrinder-ncurses```

```dnf: sudo dnf install wordgrinder```

```apk: sudo apk add wordgrinder```

```brew: brew install wordgrinder```

```nix: nix profile install nixpkgs#wordgrinder```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [nano](/man/nano)(1), [joe](/man/joe)(1)
