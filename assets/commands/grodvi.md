# TAGLINE

Groff 的 DVI 输出驱动

# TLDR

**将 groff 转换为 DVI**

```groff -Tdvi [file.roff] > output.dvi```

**直接使用 grodvi**

```grodvi [file] > output.dvi```

**指定字体路径**

```grodvi -F [fontdir] [file]```

# SYNOPSIS

**grodvi** [_options_] [_file_]

# PARAMETERS

_FILE_
> groff 中间输出文件。

**-d**
> 启用调试模式。

**-F** _DIR_
> 字体目录。

**-l**
> 横向（landscape）模式。

**-p** _SIZE_
> 纸张尺寸。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grodvi** 是一个 groff 输出驱动，生成 DVI（DeVice Independent，设备无关）格式，可与 dvips、xdvi 等 TeX 生态工具配合使用。

该驱动将 groff 中间输出转换为 DVI 格式，使其能够集成到基于 TeX 的工作流中，并支持标准的 groff 字体特性。

# CAVEATS

属于 groff 软件包。与 PDF 相比 DVI 格式存在局限。要获得最佳效果需要 TeX 字体。

# HISTORY

grodvi 作为 **GNU groff** 的一部分开发，用于提供 DVI 输出能力，在 groff 与 TeX 生态之间架起桥梁。

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

[groff](/man/groff)(1), [grops](/man/grops)(1), [dvips](/man/dvips)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

<!-- verified: 2026-07-17 -->
