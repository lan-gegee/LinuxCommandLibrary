# TAGLINE

交互式终端软件包浏览器

# TLDR

**启动** aptitude TUI

```sudo aptitude-curses```

# SYNOPSIS

**aptitude-curses** [_options_]

# DESCRIPTION

**aptitude-curses** 启动基于 curses 的 aptitude 文本用户界面。不带子命令运行时通常直接以 **aptitude** 调用。

该 TUI 提供交互式软件包浏览器，具备依赖跟踪、搜索和高级过滤功能。

# PARAMETERS

所有选项与 **aptitude** 相同。

# CAVEATS

等同于不带参数运行 **aptitude**。单独的命令是为了显式调用 TUI 模式。

# INSTALL

```apt: sudo apt install aptitude```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aptitude](/man/aptitude)(8), [apt](/man/apt)(8), [dpkg](/man/dpkg)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/apt-team/aptitude)```

<!-- verified: 2026-06-11 -->
