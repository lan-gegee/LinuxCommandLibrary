# TAGLINE

groff 命令行选项推测工具

# TLDR

**推测处理某个文件所需的 groff 命令**

```grog [file.roff]```

**推测并立即运行 groff**

```grog [file.roff] | sh```

**一次处理多个文件**

```grog [file1.roff] [file2.roff]```

**从标准输入读取**

```cat [file.roff] | grog```

# SYNOPSIS

**grog** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要分析的文件；若省略或给定为 "-"，则读取标准输入。

**-C**
> 启用 AT&T troff 兼容模式（同时也会传递给推测出的命令）。

**-v**, **--version**
> 显示版本信息并退出。

**-h**, **--help**
> 显示用法消息并退出。

其他任何 **groff**(1) 选项（例如 **-T**、**-k**）都会原样传递给推测出的命令行。

# DESCRIPTION

**grog** 分析 roff 输入文件并给出合适的 groff 命令行。它通过检查文档内容中宏的使用情况，检测需要哪些宏包和预处理器。

该工具输出带有正确选项的完整 groff 命令，可以通过管道交给 shell 执行。

# CAVEATS

属于 groff 软件包。可能无法检测出所有需求。建议先验证其给出的结果。

# HISTORY

grog 作为 **GNU groff** 的一部分开发，用于简化为复杂文档确定正确选项的过程。

# INSTALL

```apt: sudo apt install groff-base```

```dnf: sudo dnf install groff-base```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [nroff](/man/nroff)(1), [troff](/man/troff)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

```[Documentation](https://www.gnu.org/software/groff/groff.html)```

<!-- verified: 2026-07-17 -->
