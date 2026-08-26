# TAGLINE

Groff 的 Canon LBP 打印机驱动

# TLDR

**生成 Canon LBP 输出**

```groff -Tlbp [file.roff] | lpr -P[printer]```

**直接使用 grolbp**

```grolbp [file] > output.lbp```

**指定字体**

```grolbp -F [fontdir] [file]```

# SYNOPSIS

**grolbp** [_options_] [_file_]

# PARAMETERS

_FILE_
> groff 中间输出文件。

**-c** _N_, **--copies** _N_
> 每页打印 N 份。

**-F** _DIR_, **--fontdir** _DIR_
> 将目录添加到字体搜索路径的最前面。

**-l**, **--landscape**
> 以横向格式排版文档。

**-o** _ORIENTATION_, **--orientation** _ORIENTATION_
> 设置方向为纵向或横向。

**-p** _SIZE_, **--papersize** _SIZE_
> 设置纸张尺寸（A4、letter、legal、executive）。

**-w** _WIDTH_, **--linewidth** _WIDTH_
> 设置默认线条粗细（单位为千分之一 em，默认：40）。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**grolbp** 是一个 groff 输出驱动，生成适用于 Canon LBP-4 和 LBP-8 系列激光打印机的 CAPSL 与 VDM 格式输出。它支持多种纸张尺寸、方向和份数。

该驱动处理 groff 中间输出，并生成打印机专用命令，可直接发送到 Canon LBP 硬件进行打印。

# CAVEATS

属于 groff 软件包。专用于 Canon LBP 打印机。可能需要特定于打印机的配置。

# HISTORY

grolbp 作为 **GNU groff** 的一部分开发，用于支持 Canon 激光束打印机。

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

[groff](/man/groff)(1), [troff](/man/troff)(1), [grops](/man/grops)(1), [grolj4](/man/grolj4)(1), [lpr](/man/lpr)(1)
