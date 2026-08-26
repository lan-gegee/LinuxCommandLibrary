# TAGLINE

将 termcap 描述转换为 terminfo 格式

# TLDR

**将 termcap 文件转换**为 terminfo 格式

```captoinfo [path/to/termcap_file]```

一步完成**转换并编译**进 terminfo 数据库

```captoinfo [path/to/termcap_file] | tic```

带**详细输出**转换，便于调试

```captoinfo -v [path/to/termcap_file]```

**每行输出一个字段**而不是自动换行

```captoinfo -1 [path/to/termcap_file]```

启用**扩展能力**支持进行转换

```captoinfo -x [path/to/termcap_file]```

**显示版本**信息

```captoinfo -V```

# SYNOPSIS

**captoinfo** [**-v**_n_] [**-V**] [**-1**] [**-w** _width_] [**-x**] [_file_...]

# PARAMETERS

**-v**_n_
> 将详细注释和调试信息输出到标准错误。数值越大越详细。

**-V**
> 显示 ncurses 库的版本号并退出。

**-1**
> 每行输出一个字段，而不是将多个字段折行到最多 60 字符宽度内。

**-w** _width_
> 设置折行字段的最大输出宽度。

**-x**
> 启用对现代终端特性的扩展 terminfo 能力的解析和输出。

# DESCRIPTION

**captoinfo** 将 termcap 终端能力描述转换为 terminfo 格式。对于输入文件中的每个 termcap 条目，都会向标准输出写出等价的 terminfo 描述。它还会把一些过时的非标准能力翻译为标准（SVr4/XSI Curses）terminfo 能力。

未指定文件时，captoinfo 读取 **TERMCAP** 环境变量所指定的文件，并只提取 **TERM** 所指定终端的条目。若 TERMCAP 未设置，则默认读取 /etc/termcap。

该工具实现为指向 **tic**(1) 的链接，隐含了 **-I** 选项。其他 tic 选项如 **-1**、**-f**、**-v**、**-w** 和 **-x** 均可使用。

# CAVEATS

某些 termcap 能力可能没有直接的 terminfo 对应项。复杂或非标准的 termcap 条目在转换后可能需要手动调整。输出为 terminfo 源格式，必须用 **tic** 编译后才能供应用使用。

# HISTORY

termcap 数据库是 Unix 中最早的终端描述机制，在 1970 年代和 1980 年代初广泛使用。其局限（固定大小缓冲区、缺乏强类型）促成了 1980 年代中期 terminfo 的开发。**captoinfo** 作为 ncurses 项目的一部分被创建，用于简化从 termcap 到 terminfo 的迁移，让管理员可以转换现有的终端定义而不必从零重写。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tic](/man/tic)(1), [infocmp](/man/infocmp)(1), [infotocap](/man/infotocap)(1), [tput](/man/tput)(1)
