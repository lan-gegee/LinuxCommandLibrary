# TAGLINE

Groff 的 PostScript 输出驱动

# TLDR

**将 groff 转换为 PostScript**

```groff -Tps [file.roff] > output.ps```

**直接使用 grops**

```grops [file] > output.ps```

**指定纸张尺寸**

```grops -p [a4] [file] > output.ps```

**横向模式**

```grops -l [file] > output.ps```

# SYNOPSIS

**grops** [_options_] [_file_]

# PARAMETERS

_FILE_
> groff 中间输出。

**-c** _N_
> 份数。

**-F** _DIR_
> 字体目录。

**-l**
> 横向方向。

**-p** _SIZE_
> 纸张尺寸（letter、a4、legal）。

**-P** _PROLOGUE_
> 使用 prologue 文件。

**-b**
> 用于兼容性的 broken 标志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grops** 是一个生成 PostScript 的 groff 输出驱动。它是 groff 高质量打印输出的主要驱动，生成支持色彩、图形和内嵌字体的 Level 2 PostScript。

输出可以直接打印，也可以用 ps2pdf 等工具转换为 PDF。

# CAVEATS

属于 groff 软件包。PostScript 输出可能较大。需要 PostScript 查看器或打印机。

# HISTORY

grops 作为 **GNU groff** 的一部分由 **James Clark** 开发，是打印文档的主要输出驱动。

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

[groff](/man/groff)(1), [ps2pdf](/man/ps2pdf)(1)
