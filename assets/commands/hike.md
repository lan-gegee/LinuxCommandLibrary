# TAGLINE

终端中的 Markdown 浏览器

# TLDR

**启动 hike**浏览 Markdown 文件

```hike```

**打开指定的 Markdown 文件**

```hike [path/to/file.md]```

# SYNOPSIS

**hike** [_options_] [_file_]

# DESCRIPTION

**hike** 是一个基于终端的 Markdown 浏览器，能够浏览和查看本地 Markdown 文件以及从网络下载的 Markdown 文件。它内置快捷方式，可快速访问 **GitHub**、**GitLab**、**Codeberg** 和 **Bitbucket** 等热门 git 托管平台上的 Markdown 文件。

Hike 支持使用内置编辑器编辑本地文件系统上的 Markdown 文档，也支持选用你自己的外部编辑器。可以通过命令面板（**Ctrl+P**）发现各种命令。

# CAVEATS

需要具备现代渲染能力的终端。获取网络上的 Markdown 文件需要互联网连接。

# HISTORY

**hike** 由 **Dave Pearson**（davep）创建，使用基于 **Textual** TUI 框架的 **Python** 编写。其设计目标是为浏览文档和 README 文件提供原生的终端体验。

# SEE ALSO

[glow](/man/glow)(1), [mdcat](/man/mdcat)(1), [bat](/man/bat)(1)
