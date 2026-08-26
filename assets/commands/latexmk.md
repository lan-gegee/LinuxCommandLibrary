# TAGLINE

自动完成 LaTeX 文档编译的 Perl 脚本

# TLDR

将 LaTeX 文档**编译为 PDF**

```latexmk -pdf [document.tex]```

**编译并持续监视**变化

```latexmk -pdf -pvc [document.tex]```

**使用 XeLaTeX 编译**

```latexmk -xelatex [document.tex]```

**使用 LuaLaTeX 编译**

```latexmk -lualatex [document.tex]```

**清理辅助文件**

```latexmk -c [document.tex]```

**清理所有生成文件**（包括输出）

```latexmk -C [document.tex]```

**启用 shell escape 编译**（用于 minted 等）

```latexmk -pdf -shell-escape [document.tex]```

**静默模式**（输出更少）

```latexmk -pdf -silent [document.tex]```

# SYNOPSIS

**latexmk** [_-pdf_|_-xelatex_|_-lualatex_] [_-pvc_] [_-c_|_-C_] [_options_] [_file.tex_]

# PARAMETERS

**-pdf**
> 通过 pdflatex 生成 PDF。

**-xelatex**
> 通过 xelatex 生成 PDF。

**-lualatex**
> 通过 lualatex 生成 PDF。

**-dvi**
> 生成 DVI 文件。

**-ps**
> 生成 PostScript 文件。

**-pvc**
> 持续预览（监视模式）。

**-pv**
> 编译完成后预览。

**-c**
> 清理辅助文件。

**-C**
> 清理所有生成的文件，包括输出。

**-f**
> 强制越过错误继续处理。

**-g**
> 强制完整处理（忽略时间戳）。

**-silent**
> 降低输出详细程度。

**-verbose**
> 提高输出详细程度。

**-interaction=**_mode_
> 设置交互模式：nonstopmode、batchmode、errorstopmode、scrollmode。

**-shell-escape**
> 启用 shell escape（供 minted 之类的宏包使用）。

**-outdir=**_dir_, **-output-directory=**_dir_
> 生成文件的输出目录。

**-auxdir=**_dir_
> 存放辅助文件的目录。

**-jobname=**_name_
> 设置输出的基础名称。

**-bibtex**, **-nobibtex**
> 强制运行或禁用 bibtex/biber。

**-recorder**
> 启用 recorder 以追踪文件依赖。

**-norc**
> 跳过读取初始化（rc）文件。

**-deps**
> 显示依赖文件列表（Make 兼容格式）。

**-diagnostics**
> 打印详细的诊断信息。

# DESCRIPTION

**latexmk** 是一个自动化 LaTeX 文档编译的 Perl 脚本。它会确定所需的正确运行顺序和次数，按需自动运行 latex、bibtex/biber、makeindex 等工具。

LaTeX 文档通常需要多轮处理：交叉引用、参考文献和索引都要求反复运行 latex/bibtex。Latexmk 通过分析日志文件和辅助文件来判断何时需要重新编译以及按什么顺序进行。

持续预览模式（-pvc）会监视源文件并在内容变化时重新编译。再搭配一个能自动刷新的 PDF 阅读器（如 Zathura、Skim 或 SumatraPDF），就能形成实时预览的工作流。

配置可以放在 **latexmkrc** 文件中（系统级、用户级或项目级）。常见的设置内容包括默认选项、面向特殊处理的自定义规则，以及阅读器偏好。

对于带有自定义构建步骤的复杂文档，latexmk 支持自定义依赖规则和处理脚本，因此可以适应大多数 LaTeX 工作流。

# CAVEATS

需要 Perl。某些宏包可能需要专门的 latexmkrc 规则。预览模式对阅读器的支持因平台而异。shell escape 允许执行任意代码——只应配合受信任的文档使用。可能检测不到所有的依赖变化。

# HISTORY

**latexmk** 由 John Collins 编写，在 Evan McLean 等人早期工作的基础上发展而来。该脚本自 **20 世纪 90 年代**以来一直得到持续的维护和更新，已成为 LaTeX 编译的标准自动化工具，随 TeX Live 和 MiKTeX 发行版一同提供。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [xelatex](/man/xelatex)(1), [lualatex](/man/lualatex)(1), [bibtex](/man/bibtex)(1), [biber](/man/biber)(1)
