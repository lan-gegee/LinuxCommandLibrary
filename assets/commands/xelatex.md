# TAGLINE

支持 Unicode 的 LaTeX 到 PDF 编译器

# TLDR

**将 LaTeX 文档编译为 PDF**

```xelatex [document.tex]```

**启用 shell escape 进行编译**

```xelatex -shell-escape [document.tex]```

**编译到指定的输出目录**

```xelatex -output-directory=[build/] [document.tex]```

**以 non-stop 模式运行，跳过错误**

```xelatex -interaction=nonstopmode [document.tex]```

**使用自定义作业名编译**

```xelatex -jobname=[output] [document.tex]```

**启用 SyncTeX 编译以便与编辑器集成**

```xelatex -synctex=1 [document.tex]```

**生成 XDV 输出而不是 PDF**

```xelatex -no-pdf [document.tex]```

# SYNOPSIS

**xelatex** [_options_] [_file_]

# PARAMETERS

**-output-directory** _DIR_
> 将输出文件写入指定目录。

**-jobname** _NAME_
> 设置输出文件的基本名。

**-interaction** _MODE_
> 设置交互模式：batchmode、nonstopmode、scrollmode、errorstopmode。

**-shell-escape**
> 启用 \\write18 shell 命令执行。

**-no-shell-escape**
> 禁用 shell 命令执行（默认）。

**-synctex** _N_
> 生成用于编辑器同步的 SyncTeX 数据。

**-halt-on-error**
> 在第一个错误处停止处理。

**-file-line-error**
> 在错误消息中显示文件名和行号。

**-no-pdf**
> 生成 XDV（XeTeX DeVice-independent）输出而不是 PDF。

**-output-driver** _CMD_
> 使用 CMD 作为 XDV 转 PDF 的驱动程序，代替默认的 xdvipdfmx。

**-8bit**
> 使所有字符默认可打印。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**xelatex** 使用 XeTeX 引擎编译 LaTeX 文档并生成 PDF 输出。它原生支持 Unicode（UTF-8），可以通过 **fontspec** 宏包直接使用系统安装的任意 OpenType 或 TrueType 字体。

与 pdfLaTeX 不同，xelatex 无需特殊的编码宏包即可处理非拉丁文字和复杂排版。文档可以直接包含来自任何书写系统的字符。在内部，xelatex 先生成 XDV（XeTeX DeVice-independent）文件，然后用 xdvipdfmx 将其转换为 PDF。

交叉引用、参考文献和索引可能需要多次编译。**latexmk** 等构建系统可以自动化这一过程。

# CAVEATS

某些为 pdfLaTeX 设计的宏包可能不兼容。由于需要两阶段的 XDV 转 PDF 过程，编译比 pdfLaTeX 稍慢。对 Microtype 的支持不如 pdfLaTeX 或 LuaLaTeX 完善。属于 TeX Live 发行版的一部分。

# HISTORY

**XeTeX** 由 Jonathan Kew 创建，最初于 **2004 年**面向 Mac OS X。它于 **2006 年**被移植到 Linux，并被收入 TeX Live **2007**。XeTeX 为 TeX 带来了现代字体技术和 Unicode 支持，使其适用于多语言和专业排版文档。

# INSTALL

```dnf: sudo dnf install texlive-xetex```

```pacman: sudo pacman -S texlive-xetex```

```apk: sudo apk add texlive-xetex```

```zypper: sudo zypper install texlive-xetex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xetex](/man/xetex)(1), [pdflatex](/man/pdflatex)(1), [lualatex](/man/lualatex)(1), [latexmk](/man/latexmk)(1), [biber](/man/biber)(1)
