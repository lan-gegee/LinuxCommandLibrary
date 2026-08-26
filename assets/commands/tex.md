# TAGLINE

最初的 TeX 排版引擎

# TLDR

**编译文档**

```tex [document.tex]```

**以指定作业名编译**

```tex -jobname=[output] [document.tex]```

**交互模式**

```tex -interaction=nonstopmode [document.tex]```

**初始化格式**

```tex -ini [format.tex]```

# SYNOPSIS

**tex** [_-interaction mode_] [_-jobname name_] [_options_] _file_

# PARAMETERS

**-interaction** _MODE_
> 设置交互模式：batchmode、nonstopmode、scrollmode 或 errorstopmode。

**-jobname** _NAME_
> 设置作业名，而不是从输入文件名派生。

**-ini**
> 以 INI 模式启动，用于转储（dump）格式；不预加载任何格式。

**-output-directory** _DIR_
> 将输出文件写入 DIR 而不是当前目录。

**-halt-on-error**
> 在第一个错误处停止处理。

**-file-line-error**
> 以 file:line:error 格式打印错误消息。

**-recorder**
> 启用文件名记录器，生成列出已打开文件的 .fls 文件。

**-fmt** _NAME_
> 使用 NAME 作为格式，而非默认值。

# DESCRIPTION

**tex** 是 Donald Knuth 创建的最初版 TeX 排版引擎。它读取纯 TeX 源文件并产生 DVI（设备无关）输出，随后可用 dvips 或 dvipdfm 等工具转换为 PostScript、PDF 或其他格式。

TeX 默认使用 plain TeX 宏格式，它只提供基础的排版命令，没有 LaTeX 那样的高层抽象。它在数学排版方面尤为出色，能为公式、方程和技术文档产出出版级质量的输出。TeX 是 LaTeX、ConTeXt 及其他宏包赖以构建的基础。

# CAVEATS

只产生 DVI 输出；需要直接输出 PDF 请使用 pdftex 或 pdflatex。默认使用 plain TeX 宏，没有 LaTeX 的高层抽象。

# HISTORY

**TeX** 由 **Donald Knuth** 从 1977 年开始创建，最初用于排版他自己的著作，尤其是数学内容。

# INSTALL

```apt: sudo apt install texlive-binaries```

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[latex](/man/latex)(1), [pdftex](/man/pdftex)(1), [xetex](/man/xetex)(1), [dvips](/man/dvips)(1)
