# TAGLINE

列出 terminfo 终端类型条目

# TLDR

**列出所有终端类型**

```toe```

**列出包括不完整在内的所有条目**

```toe -a```

**带目录标题列出**

```toe -h```

**只显示主名称**

```toe -s```

**扫描指定目录**

```toe [/usr/share/terminfo]```

**列出多个目录中的条目**

```toe [/usr/share/terminfo] [~/.terminfo]```

# SYNOPSIS

**toe** [_options_] [_directory_...]

# PARAMETERS

**-a**
> 列出所有条目，包括不完整的条目。

**-h**
> 进入每个目录时显示目录标题。

**-s**
> 简短列表：每个条目只显示第一个别名。

**-u** _file_
> 将带有依赖排序列表的报告写入文件。

**-v**
> 显示版本并退出。

**-V**
> 显示版本和设置后退出。

# DESCRIPTION

**toe**（Table Of Entries）列出 terminfo 数据库中可用的终端类型描述。它是 ncurses 软件包的一部分，帮助识别系统上安装了哪些终端能力。

terminfo 数据库包含终端能力的编译描述，应用程序借助它们与不同类型的终端正确交互。每个条目描述光标移动、颜色支持、功能键等终端特有行为。

不带参数时，toe 扫描默认的 terminfo 目录。给定目录参数时，则扫描那些目录。输出显示终端类型名称及简要描述。

# CAVEATS

仅列出 terminfo 格式的条目，不包括旧的 termcap 文件。默认目录位置因发行版而异。某些精简安装可能只有有限的 terminfo 条目。无法移植到非 ncurses 系统。

# HISTORY

**toe** 作为 ncurses 库的一部分开发，ncurses 是 curses 的自由软件模拟。命令名是开发者的文字游戏：tic、tac（现在的 tack）、toe，构成了经典游戏的梗。terminfo 系统取代了较旧的 termcap 数据库，克服了大小限制并提升了性能。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tic](/man/tic)(1), [infocmp](/man/infocmp)(1), [tput](/man/tput)(1), [tset](/man/tset)(1)
