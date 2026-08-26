# TAGLINE

终端初始化与重置工具

# TLDR

根据 $TERM **初始化终端**

```tset```

**将终端重置**为正常状态

```reset```

**显式设置终端类型**

```tset [xterm-256color]```

**输出设置 TERM 的 shell 命令**

```tset -s```

**将擦除字符**设为退格键

```tset -e ^H```

**设置中断字符**

```tset -i ^C```

**跳过发送初始化**字符串

```tset -I```

**安静模式**（抑制输出）

```tset -q```

# SYNOPSIS

**tset** [**-IQVcqrsw**] [**-**] [**-e** _ch_] [**-i** _ch_] [**-k** _ch_] [**-m** _mapping_] [_terminal_]

# PARAMETERS

**-c**
> 设置控制字符和终端模式

**-e** _ch_
> 将擦除字符设置为 ch

**-i** _ch_
> 将中断字符设置为 ch

**-k** _ch_
> 将行终止（kill）字符设置为 ch

**-I**
> 不发送终端和制表符初始化字符串

**-m** _mapping_
> 将端口类型和波特率映射到终端类型

**-Q**
> 不显示擦除、中断和 kill 字符

**-q**
> 将终端类型输出到标准输出，但不初始化终端

**-r**
> 将终端类型打印到标准错误

**-s**
> 输出用于设置 TERM 环境变量的 shell 命令

**-V**
> 打印 ncurses 版本并退出

**-w**
> 调整窗口大小以匹配通过 setupterm 推断出的尺寸

# DESCRIPTION

**tset** 根据 **$TERM** 环境变量或命令行中指定的终端类型初始化终端。它设置终端模式、发送初始化字符串，并可配置擦除、kill 等特殊字符。如果既未指定 **-c** 也未指定 **-w**，则默认两者都生效。

以 **reset** 方式调用时，该命令会将终端模式恢复为"正常"值：启用 cooked 和 echo 模式、禁用 raw 模式、启用换行转换，并将特殊字符重置为默认值。这可用于从把终端弄乱的程序中恢复。

命令按以下顺序确定终端类型：命令行参数、$TERM 变量、/etc/ttys 条目（BSD 系统），最后是默认类型 "unknown"。随后它会从 terminfo 数据库发送相应的初始化序列。

**-s** 选项会输出设置 TERM 的 shell 命令，在登录脚本中终端类型可能变化的场景下很有用。

# CAVEATS

当终端显示混乱时，你可能需要输入 **\<LF\>reset\<LF\>**（用 Ctrl+J 代替回车），因为此时回车符可能不起作用。在现代系统上，终端模拟器通常会自动处理初始化，因此 tset 已较少需要。

# HISTORY

**tset** 由 **Eric Allman** 编写，于 **1977 年**首次出现在 **1BSD** 中，当时使用 termcap 数据库。ncurses 版本则使用 terminfo。**reset** 功能历史上是一个独立命令，现在通常是指向 tset 的链接。该命令早于 POSIX 标准，并未被标准化。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[reset](/man/reset)(1), [stty](/man/stty)(1), [clear](/man/clear)(1), [tput](/man/tput)(1), [infocmp](/man/infocmp)(1)
