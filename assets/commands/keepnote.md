# TAGLINE

笔记应用

# TLDR

**启动 KeepNote**

```keepnote```

**打开笔记本**

```keepnote [notebook_path]```

**打开指定页面**

```keepnote [notebook_path] --page [page_id]```

# SYNOPSIS

**keepnote** [_options_] [_notebook_]

# PARAMETERS

_NOTEBOOK_
> 笔记本目录的路径。

**--page** _ID_
> 打开指定页面。

**--version**
> 显示版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**KeepNote** 是一个桌面笔记应用，它将笔记组织成层次化的树状笔记本，并支持富文本格式。笔记可以包含带样式的文本、图片、超链接和文件附件，因此适合研究文档、日志记录和技术笔记。基于 GTK 的界面呈现熟悉的三栏布局：笔记本树、页面列表和编辑器。

笔记本以 HTML 文件及相关资源组成的目录形式存储在磁盘上，因此很容易备份、进行版本控制或在应用之外浏览。每条笔记都是自包含的 HTML 文档，即使没有安装 KeepNote，数据格式依然可访问。该应用用 Python 编写，支持对笔记本中所有笔记的全文搜索。

# CAVEATS

Python/GTK 应用。开发已放缓。可以考虑 Joplin 等替代品。

# HISTORY

KeepNote 由 **Matt Rasmussen** 创建，是一个具有层次化组织的开源笔记应用。

# INSTALL

```aur: yay -S keepnote```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[joplin](/man/joplin)(1)
