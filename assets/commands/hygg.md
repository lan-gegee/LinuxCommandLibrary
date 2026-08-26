# TAGLINE

极简的类 Vim TUI 文档阅读器

# TLDR

**阅读 PDF 文件**

```hygg [path/to/document.pdf]```

**阅读 EPUB 文件**

```hygg [path/to/book.epub]```

**阅读 DOCX 文件**

```hygg [path/to/document.docx]```

# SYNOPSIS

**hygg** [_options_] _file_

# DESCRIPTION

**hygg** 是一款极简的终端文档阅读器，采用 **Vim 风格**的按键绑定。它通过 **pandoc** 集成支持包括 **PDF**、**EPUB**、**DOCX** 在内的多种通用文档格式。该阅读器提供按终端宽度排版的智能文本对齐、带高亮的强大搜索、书签以及自动保存进度。

Hygg 采用管道式架构，各个组件（转换器、对齐器）都可以作为独立的 Unix CLI 工具复用。它在本地运行并尊重隐私，还支持可选的自托管同步。

# KEY BINDINGS

**j/k** — 向下/向上滚动
**g/G** — 跳到顶部/底部
**/** — 搜索
**n/N** — 下一个/上一个搜索结果
**m** — 设置书签
**q** — 退出

# CAVEATS

某些格式的转换需要安装 **pandoc**。复杂的文档版式（表格、图片）在终端中可能无法完美呈现。大型文档首次打开时的转换可能需要一些时间。

# HISTORY

**hygg** 由 **kruseio** 创建，用 **Rust** 编写。其名字让人联想到丹麦语/挪威语中的 "hygge"（惬意），体现了它对终端舒适阅读体验的追求。

# INSTALL

```nix: nix profile install nixpkgs#hygg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [bat](/man/bat)(1), [glow](/man/glow)(1)
