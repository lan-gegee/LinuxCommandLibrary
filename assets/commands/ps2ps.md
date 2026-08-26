# TAGLINE

优化并规范化 PostScript 文件

# TLDR

**优化 PostScript 文件**

```ps2ps [input.ps] [output.ps]```

**以指定选项转换**

```ps2ps -dSAFER [input.ps] [output.ps]```

# SYNOPSIS

**ps2ps** [_options_] _input_ _output_

# PARAMETERS

_INPUT_
> 输入的 PostScript 文件。

_OUTPUT_
> 输出的 PostScript 文件。

**-dSAFER**
> 更安全的模式。

# DESCRIPTION

**ps2ps** 通过 Ghostscript 解释器读取 PostScript 文件，并将输出重写为干净、规范的 PostScript，从而实现优化和规范化。这一过程可以减小文件体积、解决兼容性问题，并简化复杂的 PostScript 代码，以便在难以处理原始文件的打印机或其他工具上使用。

该工具是 Ghostscript 套件的一部分，本质上是一个启用了 PostScript 输出的 **gs** 封装。如果未指定输出文件名，结果将写入 stdout。

# CAVEATS

Ghostscript 套件的一部分。可能改变排版格式。

# HISTORY

ps2ps 是 **Ghostscript** 中负责 PostScript 优化的工具。

# INSTALL

```apt: sudo apt install ghostscript```

```dnf: sudo dnf install ghostscript```

```pacman: sudo pacman -S ghostscript```

```apk: sudo apk add ghostscript```

```zypper: sudo zypper install ghostscript```

```brew: brew install ghostscript```

```nix: nix profile install nixpkgs#ghostscript```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gs](/man/gs)(1), [ps2pdf](/man/ps2pdf)(1), [ps2epsi](/man/ps2epsi)(1)
