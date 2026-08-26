# TAGLINE

使用系统字体的 Unicode TeX 引擎

# TLDR

**编译文档**

```xetex [document.tex]```

**输出到指定名称**

```xetex -jobname=[output] [document.tex]```

**Non-stop 模式**

```xetex -interaction=nonstopmode [document.tex]```

**输出到指定目录**

```xetex -output-directory=[path/to/dir] [document.tex]```

# SYNOPSIS

**xetex** [_-interaction mode_] [_-jobname name_] [_options_] _file_

# PARAMETERS

**-interaction** _MODE_
> 错误处理模式。

**-jobname** _NAME_
> 输出名称。

**-output-directory** _DIR_
> 输出位置。

**-halt-on-error**
> 在第一个错误处停止。

**-no-pdf**
> 生成 XDV 输出而不是 PDF。

**-output-driver** _CMD_
> 运行 CMD 而不是 xdvipdfmx 将 XDV 转换为 PDF。

**-papersize** _STRING_
> 将 PDF 媒介尺寸设置为 STRING。

**-synctex=**_NUMBER_
> 启用 SyncTeX 以便与编辑器集成（1 表示启用）。

# DESCRIPTION

**XeTeX** 是一个扩展的 TeX 排版引擎，为传统 TeX 系统添加了原生 Unicode 和现代字体支持。与受限于 8 位编码的经典 TeX 引擎不同，XeTeX 原生处理全部 Unicode 字符，适用于多语言文档以及来自任何书写系统的文字。

XeTeX 最重要的特性之一是能够直接使用系统安装的字体，包括 OpenType 和 TrueType 字体，无需安装 TeX 专用字体。这使作者可以使用系统上所有可用字体，并利用连字、风格替换和字体变体等高级 OpenType 特性。

XeTeX 通过 xdvipdfmx 后端直接生成 PDF 输出。它通常通过 **xelatex** 包装器使用，后者在 XeTeX 引擎之上提供了熟悉的 LaTeX 宏层，将 LaTeX 的文档结构化能力与 XeTeX 的 Unicode 和字体处理结合起来。

# CAVEATS

输入文件必须使用 UTF-8 编码。使用 XeLaTeX 时推荐用 `fontspec` 宏包选择字体。某些 pdfTeX 特有的宏包（如 `microtype` 的部分特性）支持有限。-no-pdf 标志生成 XDV（扩展 DVI）输出，可以随后用 `xdvipdfmx` 单独处理。

# HISTORY

**XeTeX** 由 **Jonathan Kew** 于 **2004 年**创建，目的是为 TeX 添加原生 Unicode 和现代字体支持。它最初基于 Apple 的 AAT 字体技术面向 macOS 开发，后来通过 ICU 和 HarfBuzz 在所有平台上扩展了对 OpenType 的支持。

# INSTALL

```apt: sudo apt install texlive-binaries```

```dnf: sudo dnf install texlive-xetex```

```pacman: sudo pacman -S texlive-xetex```

```apk: sudo apk add texlive-xetex```

```zypper: sudo zypper install texlive-xetex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xelatex](/man/xelatex)(1), [pdflatex](/man/pdflatex)(1), [luatex](/man/luatex)(1), [pdftex](/man/pdftex)(1), [latex](/man/latex)(1)
