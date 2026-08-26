# TAGLINE

比较或打印 terminfo 描述

# TLDR

**显示当前终端的能力**

```infocmp```

**显示特定的终端类型**

```infocmp [xterm-256color]```

**比较两个终端描述**（显示差异）

```infocmp -d [xterm] [xterm-256color]```

**以 terminfo 源格式输出**（可用 tic 编译）

```infocmp -I [xterm]```

**每行显示一项能力**

```infocmp -1 [xterm]```

**以 termcap 格式输出**

```infocmp -C [xterm]```

**利用 use= 字段生成相对描述**

```infocmp -u [xterm-256color] [xterm]```

# SYNOPSIS

**infocmp** [_options_] [_termname_...]

# PARAMETERS

_termname_
> 要显示或比较的终端类型。

**-d**
> 显示两个终端描述之间的差异。

**-c**
> 显示两个终端之间的共同能力。

**-n**
> 显示两者共同的能力，并列出不同的部分。

**-u**
> 使用 **use=** 字段生成相对于其他条目的 terminfo 源。

**-I**
> 以 terminfo 源格式输出。

**-C**
> 以 termcap 格式输出。

**-L**
> 输出中使用长的 C 变量名。

**-1**
> 每行打印一项能力。

**-r**
> 显示 terminfo 条目的解析后路径。

**-E**
> 将能力导出为 TERMTYPE 结构的 C 初始化表。

**-e**
> 将能力导出为 TERMTYPE 结构的 C 初始化器。

**-F**
> 比较 terminfo 文件，报告各条目之间的相同与不同之处。

**-A** _dir_
> 为第一个终端使用指定的 terminfo 数据库目录。

**-B** _dir_
> 为第二个终端使用指定的 terminfo 数据库目录。

# DESCRIPTION

**infocmp** 对来自 terminfo 数据库的终端能力描述进行比较或打印。它可以改写描述，使其通过 **use=** 字段共享共同能力；可以比较不同终端类型之间的二进制条目；还能以多种格式输出，包括 terminfo 源和 termcap。

该命令读取已编译的 terminfo 条目并以可读格式输出。它可用于调试终端问题、了解终端特性，以及准备待用 **tic** 编译的 terminfo 源文件。

# CAVEATS

terminfo 数据库位置因系统而异（常见为 **/usr/share/terminfo** 或 **/usr/lib/terminfo**）。某些能力可能在终端条目中缺失。现代终端支持的许多扩展超出了标准 terminfo 集合。比较模式（**-d**）下只显示有差异的能力。

# HISTORY

**infocmp** 是 **ncurses** 库的一部分，后者实现了 terminfo 数据库。terminfo 系统取代了较旧的 termcap 格式，为终端能力提供了更可扩展的二进制格式。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tic](/man/tic)(1), [tput](/man/tput)(1), [toe](/man/toe)(1)
