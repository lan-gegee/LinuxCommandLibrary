# TAGLINE

以 Markdown 存储的终端日志工具

# TLDR

**启动**日志 TUI

```caps-log```

以指定的数据目录**打开**

```caps-log --dir [path/to/journal]```

# SYNOPSIS

**caps-log** [_options_]

# PARAMETERS

**--dir** _PATH_
> 日志数据目录的路径。

# DESCRIPTION

**caps-log** 是一款基于终端的日志应用，将条目保存为按日期组织的 **Markdown** 文件。它提供 TUI 用于撰写、浏览和搜索日志条目，并带有日历视图便于导航。

条目以纯 Markdown 文件的形式存储在按日期组织的目录结构中，方便在应用之外阅读、备份和版本控制。界面包含日历侧栏、条目编辑器和搜索功能。

# CONFIGURATION

日志条目以 Markdown 文件形式存储在可配置的目录中，按年份和月份子目录组织。

# CAVEATS

使用 TUI 内置的文本编辑器——习惯使用自己钟爱的终端编辑器的用户可能觉得受限。Markdown 文件是纯文本，可以在外部编辑。

# INSTALL

```aur: yay -S caps-log```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jrnl](/man/jrnl)(1), [nb](/man/nb)(1)
