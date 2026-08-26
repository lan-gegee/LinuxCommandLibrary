# TAGLINE

打印大型 ASCII 艺术文字

# TLDR

**打印**横幅文字

```banner [HELLO]```

以指定**宽度**打印

```banner -w [60] [HELLO]```

打印从**标准输入**读取的文字

```echo "[HELLO]" | banner```

# SYNOPSIS

**banner** [**-w** _cols_] _text_

# PARAMETERS

**-w** _cols_, **--width**=_cols_
> 设置最大输出宽度（字符数）。默认为 132。

# DESCRIPTION

**banner** 在终端上打印大型 ASCII 艺术横幅文字。它将文本转换成大号方块字母，适合在终端输出中创建醒目的消息或标题。每个参数会在 10 个字符处截断，并各占一行单独打印。

如果命令行上没有给出文字，则从标准输入读取。长文本会尽量在单词边界处拆分为多行。

# CAVEATS

默认设置下的输出宽度可能非常大。并非所有系统都安装了 banner。现代替代工具（figlet、toilet）提供更多字体和功能。

# HISTORY

**banner** 自早期起就是 Unix 系统的一部分，最初用于在 **20 世纪 70 年代**的行式打印机上打印大型横幅。

# INSTALL

```apt: sudo apt install sysvbanner```

```dnf: sudo dnf install banner```

```aur: yay -S sysvbanner```

```nix: nix profile install nixpkgs#banner```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[figlet](/man/figlet)(6), [toilet](/man/toilet)(1), [cowsay](/man/cowsay)(1)
