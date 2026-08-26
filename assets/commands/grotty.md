# TAGLINE

Groff 的终端输出驱动

# TLDR

**在终端中显示**

```groff -Tutf8 [file.roff]```

**ASCII 输出**

```groff -Tascii [file.roff]```

**直接使用 grotty**

```grotty [file]```

**禁用 SGR 序列**

```grotty -c [file]```

# SYNOPSIS

**grotty** [_options_] [_file_]

# PARAMETERS

_FILE_
> groff 中间输出。

**-b**
> 在传统（**-c**）输出格式中抑制粗体字符的重打（overstriking）。

**-c**
> 使用 grotty 的传统输出格式（重打）而非 SGR 转义序列。

**-d**
> 忽略输入中的所有绘图命令。

**-f**
> 在最后一行没有输出的每页末尾发出换页符。

**-i**
> 使用 SGR 斜体属性渲染倾斜字体，而不是加下划线。

**-o**
> 抑制重打（粗体和/或下划线字符除外）。

**-u**
> 在传统输出格式中抑制斜体字符的下划线。

**-h**
> 在输出中使用字面水平制表符。

**-t**
> 假定输出设备支持 SGR 38/48（24 位色）转义序列。

**-F** _DIR_
> 将 _DIR_/devname 添加到字体和设备描述文件搜索路径的最前面。

**-v**, **--version**
> 显示版本信息并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grotty** 是用于终端显示的 groff 输出驱动。它生成适合在文本终端中查看的 ASCII 或 UTF-8 输出，通过 SGR 转义序列或重打方式支持粗体和下划线。

它是 man page 显示和终端文档查看所使用的驱动。

# CAVEATS

属于 groff 软件包。输出质量取决于终端能力。文本模式下会丢失部分格式。

# HISTORY

grotty 作为 **GNU groff** 的一部分开发，用于实现排版文档的终端查看。

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

[groff](/man/groff)(1), [nroff](/man/nroff)(1), [man](/man/man)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

```[Documentation](https://www.gnu.org/software/groff/groff.html)```

<!-- verified: 2026-07-17 -->
