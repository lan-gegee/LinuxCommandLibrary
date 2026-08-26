# TAGLINE

连接并显示文件内容

# TLDR

将文件内容输出到 **stdout**

```cat [path/to/file]```

**连接**多个文件并写入输出文件

```cat [file1] [file2] > [output_file]```

**追加**多个文件到输出文件

```cat [file1] [file2] >> [output_file]```

为所有输出行**编号**

```cat -n [path/to/file]```

显示**所有字符**，包括制表符和行尾符

```cat -A [path/to/file]```

通过 **stdin** 将文件内容传给另一个程序

```cat [path/to/file] | [program]```

# SYNOPSIS

**cat** [_-n_] [_-A_] [_-b_] [_-s_] [_file_...]

# DESCRIPTION

**cat**（concatenate）按顺序读取文件并将其内容写到标准输出。它是最常用的 Unix 工具之一，是显示文件内容、合并多个文件以及在 Shell 管道中把数据传递给其他命令的标准方式。

给定多个文件参数时，cat 会按顺序连接它们，适合拼接分卷文件或追加内容。不带文件参数或使用连字符（-）时，它会从标准输入读取，因此可以在管道中充当简单的直通环节。各种标志可以控制输出格式，包括行号和非打印字符的显示。

# PARAMETERS

**-n, --number**
> 为所有输出行编号

**-b, --number-nonblank**
> 仅为非空输出行编号

**-s, --squeeze-blank**
> 压缩连续的空输出行

**-A, --show-all**
> 等价于 -vET；显示所有字符

**-E, --show-ends**
> 在每行末尾显示 $

**-T, --show-tabs**
> 将 TAB 字符显示为 ^I

**-v, --show-nonprinting**
> 对非打印字符使用 ^ 和 M- 记法

**-e**
> 等价于 -vE

**-t**
> 等价于 -vT

# CAVEATS

对于大文件，建议改用 **less** 或 **head/tail**。用 cat 把单个文件通过管道传给另一条命令（UUOC - Useless Use of Cat）通常没有必要。

# HISTORY

属于 **GNU Coreutils**。起源于 **1971** 年贝尔实验室 Ken Thompson 编写的第一版 Unix。是最古老、最基础的 Unix 工具之一。

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

[less](/man/less)(1), [more](/man/more)(1), [head](/man/head)(1), [tail](/man/tail)(1), [tac](/man/tac)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html)```

<!-- verified: 2026-06-22 -->
