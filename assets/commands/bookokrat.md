# TAGLINE

终端 EPUB、PDF 和 DJVU 电子书阅读器

# TLDR

**打开** EPUB 文件

```bookokrat [path/to/book.epub]```

**打开** PDF 文件

```bookokrat [path/to/book.pdf]```

**打开** DJVU 文件

```bookokrat [path/to/book.djvu]```

以**禅模式**打开一本书（无干扰阅读）

```bookokrat --zen-mode [path/to/book.epub]```

# SYNOPSIS

**bookokrat** [_--zen-mode_] [_file_]

# PARAMETERS

**--zen-mode**
> 以禅模式启动，隐藏侧边栏和状态栏，实现无干扰阅读。

# DESCRIPTION

**bookokrat** 是一款基于终端的电子书阅读器，支持 **EPUB**、**PDF** 和 **DJVU** 格式。它直接在终端中渲染书籍内容，具备完整的 HTML 渲染、内联图像和 MathML 支持，无需图形环境即可获得无干扰的阅读体验。

该阅读器具有 Vim 风格键绑定、带书库/目录面板和阅读面板的分屏布局、搜索、书签、跳转列表历史、内联注释和阅读统计等功能。在应用内按 **?** 可打开内置帮助。

# CAVEATS

PDF 中复杂的版式和富格式在纯文本环境下可能无法良好呈现。最适合以文字为主的书籍。由于 EPUB 格式具有可重排特性，其支持通常优于 PDF。

# INSTALL

```brew: brew install bookokrat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zathura](/man/zathura)(1), [mupdf](/man/mupdf)(1), [calibre](/man/calibre)(1)
