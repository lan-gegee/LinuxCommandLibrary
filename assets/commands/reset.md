# TAGLINE

将终端重新初始化到正常状态

# TLDR

**重新初始化**当前终端

```reset```

**显示**终端类型而不重新初始化

```reset -q```

**重置并打印设置 TERM 的 shell 命令**

```reset -s```

**重置但不发送**终端初始化字符串

```reset -I```

# SYNOPSIS

**reset** [**-IQVcqrsw**] [**-e** _ch_] [**-i** _ch_] [**-k** _ch_] [**-m** _mapping_] [_terminal_]

# PARAMETERS

**-q**
> 显示终端类型而不重新初始化

**-c**
> 设置控制字符和模式

**-e** _ch_
> 将擦除字符设为 _ch_

**-i** _ch_
> 将中断字符设为 _ch_

**-k** _ch_
> 将行删除字符设为 _ch_

**-I**
> 不发送终端初始化字符串

**-Q**
> 不显示擦除、中断和行删除字符的值

**-r**
> 将终端类型输出到 stderr

**-s**
> 打印设置 TERM 的 shell 命令

**-V**
> 报告 ncurses 版本并退出

**-w**
> 调整窗口大小以匹配通过 setupterm 推断出的大小

**-m** _mapping_
> 指定从端口类型到终端的映射

# DESCRIPTION

**reset** 将终端重新初始化到默认状态。当以 **reset**（而非 **tset**）调用时，它会先设置 cooked 和 echo 模式、关闭 cbreak 和 raw 模式、开启换行转换，并将未设置的特殊字符恢复为默认值，然后再发送终端初始化字符串。当因查看二进制文件或其他损坏导致终端显示混乱时，该命令非常有用。

该命令读取对应终端类型（来自 TERM 环境变量）的 terminfo 数据并发送适当的初始化序列。如果既未给出 **-c** 也未给出 **-w**，则两者都被假定。

# CAVEATS

可能无法修复所有终端损坏；某些情况下需要关闭并重新打开终端。在某些系统上，**reset** 是指向 **tset** 的符号链接。必须在 TERM 变量中正确设置终端类型。

# HISTORY

属于 **ncurses** 软件包的一部分，源自最初的 BSD **tset** 命令。自早期 Unix 以来就是恢复终端的必备工具，用于在显示二进制数据或转义序列破坏显示状态后还原终端。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tset](/man/tset)(1), [clear](/man/clear)(1), [stty](/man/stty)(1), [tput](/man/tput)(1)
