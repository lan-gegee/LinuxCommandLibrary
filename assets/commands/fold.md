# TAGLINE

将输入行折行以适应指定宽度

# TLDR

按特定宽度**折行**（默认：80 列）

```fold -w [60] [path/to/file]```

折行并在空格处**断行**（单词边界）

```fold -s -w [60] [path/to/file]```

以**字节**而非列数计算宽度

```fold -b -w [60] [path/to/file]```

以**字符**而非列数计算宽度

```fold -c -w [60] [path/to/file]```

对 **stdin** 输入折行

```echo "long line of text" | fold -w [40]```

# SYNOPSIS

**fold** [_options_] [_file..._]

# PARAMETERS

**-w, --width** _width_
> 使用指定宽度而非默认的 80 列

**-s, --spaces**
> 在宽度限制内于空格处断行（单词边界）

**-b, --bytes**
> 按字节而非列计数

**-c, --characters**
> 按字符而非列计数

**--help**
> 显示帮助并退出

**--version**
> 输出版本信息并退出

# DESCRIPTION

**Fold** 将每条输入行折行以适应指定宽度，并将结果写入标准输出。默认按列计数并在恰好 80 个字符处折行，这可能把单词从中间截断。

**-s** 选项通过在宽度限制内最右侧的空格处断行来提升可读性，尽可能保留完整单词。不指定文件参数（或使用 **-**）时，fold 从标准输入读取。

宽度计数方式因模式而异：**列**（默认）考虑制表符展开和多字节字符；**-b** 计算原始字节数；**-c** 按字符计数而不考虑显示宽度。

# CAVEATS

不加 **-s** 时，fold 会在指定的宽度处精确断行，可能把单词拆开。制表符在计算列数前会展开为空格，可能产生意外结果。如需带段落处理的更精细文本排版，请改用 **fmt**。

# HISTORY

**fold** 命令起源于早期 Unix 系统，并被 POSIX 标准化。由 **David MacKenzie** 编写的 GNU 版本是 **coreutils** 软件包的一部分，包含并非所有实现都有的扩展，例如 **-c** 字符计数选项。

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

[fmt](/man/fmt)(1), [pr](/man/pr)(1), [cut](/man/cut)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/coreutils/)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html)```

<!-- verified: 2026-07-15 -->
