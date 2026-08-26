# TAGLINE

将文本文件中的空格转换为制表符

# TLDR

**将文件中的行首空格转换为制表符**

```unexpand [file]```

**转换所有空格**（不仅是行首）为制表符

```unexpand -a [file]```

**使用指定的制表符宽度**

```unexpand -t [4] [file]```

**转换并保存到新文件**

```unexpand [input.txt] > [output.txt]```

**处理多个文件**

```unexpand [file1] [file2]```

**从 stdin 读取**

```cat [file] | unexpand```

# SYNOPSIS

**unexpand** [_options_] [_file ..._]

# PARAMETERS

**-a**, **--all**
> 转换所有两个及以上连续空格的序列，而不仅限于行首空格。

**-t** _n_, **--tabs=**_n_
> 每 n 列设置一个制表位（默认：8）。

**-t** _list_, **--tabs=**_list_
> 在指定的列位置设置制表位（逗号分隔）。

**--first-only**
> 仅转换行首空白（默认行为）。

**--help**
> 显示帮助信息并退出。

**--version**
> 显示版本信息并退出。

# DESCRIPTION

**unexpand** 将文件中的空格转换为制表符，并写入标准输出。默认情况下，它只将行首空格（每行开头处）转换为尽可能多的制表符，再加上填满相同列数所需的最少空格。

使用 **-a** 时，所有空格序列（不仅是行首）都会被转换。制表位默认为每 8 列一个，可用 **-t** 更改。

未指定文件或文件为 **-** 时，unexpand 从标准输入读取。

# CAVEATS

默认情况下，unexpand 只转换行首空格，这与 **expand** 默认转换所有制表符的行为不同。这种不对称性可能导致在两个命令之间来回转换时出现意外结果。要一致地转换所有空格，请使用 **-a**。

# HISTORY

unexpand 是 **GNU coreutils** 的一部分，由 **David MacKenzie** 编写。该命令起源于早期 Unix 系统，作为 expand 工具的配套命令。这两个命令都是为了满足在不同终端和打印机需求之间转换制表符与空格的历史需要。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[expand](/man/expand)(1), [cat](/man/cat)(1), [pr](/man/pr)(1), [col](/man/col)(1)
