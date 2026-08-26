# TAGLINE

Groff 的 HP LaserJet 4 打印机驱动

# TLDR

**生成 HP LaserJet 输出**

```groff -Tlj4 [file.roff] | lpr -P[printer]```

**直接使用 grolj4**

```grolj4 [file] > output.lj4```

**指定份数**

```grolj4 -c [3] [file]```

# SYNOPSIS

**grolj4** [_options_] [_file_]

# PARAMETERS

_FILE_
> groff 中间输出。

**-c** _N_
> 份数。

**-d** _DUPLEX_
> 双面打印模式（1=长边装订，2=短边装订）。

**-F** _DIR_
> 字体目录。

**-l**
> 横向方向。

**-p** _SIZE_
> 纸张尺寸。

**-w** _WIDTH_
> 线条粗细（单位为千分之一 em，默认 40）。

**-v**, **--version**
> 显示版本信息并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grolj4** 是面向 HP LaserJet 4 系列及兼容打印机的 groff 输出驱动。它生成 PCL 5 输出，支持双面打印、多种纸张尺寸和方向。

通常 **grolj4** 由 **groff -Tlj4** 间接调用而非直接运行；它读取 groff 的中间输出格式并将其转换为 PCL5 打印机命令。

# CAVEATS

属于 groff 软件包。专用于 HP PCL5 兼容打印机。未指定时默认纸张格式为 "letter"；默认双面模式为长边装订。部分功能需要打印机支持。

# HISTORY

grolj4 作为 **GNU groff** 的一部分开发，用于支持 HP LaserJet 系列打印机。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [grops](/man/grops)(1), [grolbp](/man/grolbp)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

```[Documentation](https://www.gnu.org/software/groff/groff.html)```

<!-- verified: 2026-07-17 -->
