# TAGLINE

macOS 上管理 iOS 模拟器的 TUI

# TLDR

**启动模拟器浏览器**

```simtool```

**以全部应用视图启动**

```simtool --apps```

**显示可用的配色主题**

```simtool --list-themes```

# SYNOPSIS

**simtool** [**--apps**] [**--generate-config**] [**--list-themes**]

# DESCRIPTION

**simtool** 是一个终端用户界面，用于在 macOS 上浏览和管理 iOS 模拟器。它让你可以导航模拟器、浏览已安装的应用、探索文件系统并以语法高亮预览内容。它具有 Vim 风格导航、60 多个配色主题、SQLite 检查和懒加载等功能。

# CAVEATS

仅限 macOS。需要安装了模拟器运行时的 Xcode。

# HISTORY

**simtool** 由 **Aziz Uysal**（azizuysal）创建，使用 **Go** 编写。

# SEE ALSO

[xcrun](/man/xcrun)(1)
