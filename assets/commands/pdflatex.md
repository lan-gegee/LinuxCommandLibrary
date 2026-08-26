# TAGLINE

将 LaTeX 文档直接编译为 PDF 格式

# TLDR

**将 LaTeX 编译为 PDF**

```pdflatex [document.tex]```

**以 non-stop 模式编译**

```pdflatex -interaction=nonstopmode [document.tex]```

**启用 shell escape 编译**

```pdflatex -shell-escape [document.tex]```

**输出到指定目录**

```pdflatex -output-directory=[outdir] [document.tex]```

**指定输出名称**

```pdflatex -jobname=[output] [document.tex]```

# SYNOPSIS

**pdflatex** [_options_] _file_

# DESCRIPTION

**pdflatex** 将 LaTeX 文档直接编译为 PDF 格式。它是 TeX Live 和 MiKTeX 发行版的一部分，是从 LaTeX 源文件生成 PDF 的最常用方式。

该工具处理 .tex 文件，完成排版、交叉引用和插图包含等任务。完整的文档处理可能需要多次运行。

# PARAMETERS

**-interaction=** _mode_
> 交互模式（batchmode、nonstopmode、scrollmode、errorstopmode）。

**-output-directory=** _dir_
> 输出目录。

**-jobname=** _name_
> 设置输出名称。

**-shell-escape**
> 启用 shell 命令执行。

**-halt-on-error**
> 在第一个错误处停止。

**-file-line-error**
> 以 file:line:error 格式显示错误。

**-synctex=** _n_
> 生成 SyncTeX 数据（1 启用，-1 为压缩格式）。

**-draftmode**
> 跳过最终 PDF 输出的写入（用于更快的编译检查）。

**-no-shell-escape**
> 禁用 shell 命令执行（默认）。

**-shell-restricted**
> 仅允许一组受限的 shell 命令。

**-recorder**
> 启用文件名记录（写入 .fls 文件）。

**-fmt=** _name_
> 使用指定的格式文件。

**-output-format=** _fmt_
> 输出格式：pdf（默认）或 dvi。

**--help**
> 显示用法信息并退出。

**--version**
> 显示版本信息并退出。

# CAVEATS

引用通常需要多次编译才能解析。shell escape 有安全风险。宏包错误信息可能晦涩难懂。辅助文件会不断累积。

# HISTORY

**pdfTeX** 由 **Han The Thanh** 自 **1996** 年起开发，扩展 TeX 使其能直接输出 PDF。pdflatex 将其与 LaTeX 格式结合。它成为标准的 LaTeX 工作流，在很大程度上取代了 DVI 输出。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[latex](/man/latex)(1), [xelatex](/man/xelatex)(1), [lualatex](/man/lualatex)(1), [bibtex](/man/bibtex)(1)
