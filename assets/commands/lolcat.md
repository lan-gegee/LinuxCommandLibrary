# TAGLINE

终端文本显示的彩虹着色效果

# TLDR

**以彩虹色输出文本**

```echo "Hello World" | lolcat```

**以彩虹色显示文件**

```lolcat [file]```

**让彩虹效果动起来**

```echo "Animated!" | lolcat -a```

**调整动画速度**（数值越小越快）

```echo "Fast rainbow" | lolcat -a -d [1]```

**设置彩虹跨度**（越大渐变越紧密）

```lolcat -p [3.0] [file]```

**强制彩色输出**，即使通过管道传输

```lolcat -f [file] | less -R```

# SYNOPSIS

**lolcat** [_options_] [_file ..._]

# PARAMETERS

**-a**, **--animate**
> 让彩虹效果动起来

**-d** _duration_, **--duration** _duration_
> 每行动画时长（秒）（默认：12）

**-s** _speed_, **--speed** _speed_
> 动画速度（默认：20.0）

**-p** _spread_, **--spread** _spread_
> 彩虹跨度（默认：3.0）

**-F** _freq_, **--freq** _freq_
> 彩虹频率（默认：0.1）

**-S** _seed_, **--seed** _seed_
> 彩虹种子，0 表示随机（默认：0）

**-i**, **--invert**
> 交换前景色与背景色

**-t**, **--truecolor**
> 使用 24 位真彩色（在支持的终端上默认启用）

**-f**, **--force**
> 即使标准输出不是终端也强制彩色输出

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 输出版本并退出

# DESCRIPTION

**lolcat** 将文件或标准输入拼接后输出到标准输出，并添加彩虹色渐变。它的作用类似 **cat**，但会附加 ANSI 颜色代码，为终端输出增添缤纷色彩。

lolcat 常与 **figlet**、**cowsay** 等 ASCII 艺术生成器搭配使用，因能打造醒目的终端输出、系统横幅并为 Shell 脚本增添个性而广受欢迎。

# CAVEATS

需要支持 ANSI 颜色代码的终端。对大文件运行动画模式可能占用大量 CPU。当输出通过管道传给不保留 ANSI 代码的命令时，颜色可能无法正确显示（可使用 **-f** 标志，并确保接收程序支持原始控制字符）。

# HISTORY

**lolcat** 由 **busyloop** 创建，于 **2011 年**作为 Ruby gem 发布。它受同类着色工具启发，凭借简单有趣的终端输出方式迅速在 Unix 社区流行起来。如今已有 C、Python、Rust 等多种语言的实现，其中 C 版本（**c-lolcat**）处理大文件的性能更佳。

# INSTALL

```dnf: sudo dnf install lolcat```

```pacman: sudo pacman -S lolcat```

```brew: brew install lolcat```

```nix: nix profile install nixpkgs#lolcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(1), [cowsay](/man/cowsay)(1), [toilet](/man/toilet)(1), [cmatrix](/man/cmatrix)(1), [cat](/man/cat)(1)
