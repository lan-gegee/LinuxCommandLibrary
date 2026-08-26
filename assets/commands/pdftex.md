# TAGLINE

直接产生 PDF 输出的 TeX 引擎

# TLDR

**将 TeX 编译为 PDF**

```pdftex [document.tex]```

**以指定输出名编译**

```pdftex -jobname=[output] [document.tex]```

**交互模式**

```pdftex -interaction=nonstopmode [document.tex]```

**草稿模式（无输出）**

```pdftex -draftmode [document.tex]```

**显示版本**

```pdftex --version```

# SYNOPSIS

**pdftex** [_-interaction mode_] [_-jobname name_] [_options_] _file_

# PARAMETERS

**-interaction** _MODE_
> 设置交互方式（nonstopmode、batchmode、scrollmode）。

**-jobname** _NAME_
> 设置输出名称。

**-draftmode**
> 不产生 PDF 输出。

**-output-directory** _DIR_
> 输出目录。

**-halt-on-error**
> 在第一个错误处停止。

**-ini**
> 初始化（创建）格式文件以加快加载。

**-fmt** _FORMAT_
> 使用指定的格式文件代替默认值。

**-file-line-error**
> 打印带文件名和行号的错误消息。

**-synctex** _NUMBER_
> 生成用于编辑器集成的 SyncTeX 数据（1 启用）。

**-shell-escape**
> 启用 \write18 以运行外部命令。

**-no-shell-escape**
> 禁用 \write18（默认）。

# DESCRIPTION

**pdfTeX** 是一个直接从 TeX 源文件产生 PDF 输出的 TeX 引擎，无需中间的 DVI 阶段。它在 Knuth 的原始 TeX 之上扩展了 PDF 专属的原语和微排版特性，例如边缘字距调整（字符突出）和字体伸缩（hz 优化），以改善文本外观。

pdfTeX 默认处理纯 TeX。对于 LaTeX 文档，请改用 **pdflatex**——它是预加载了 LaTeX 格式的 pdfTeX。

# CAVEATS

默认处理纯 TeX；LaTeX 文档请使用 pdflatex。含交叉引用、目录或参考文献的大型文档可能需要多次编译。`-shell-escape` 标志允许执行任意命令，应谨慎使用。

# HISTORY

**pdfTeX** 由 **Han The Thanh** 在捷克马萨里克大学攻读博士期间开发，于 **1996** 年首次发布。它扩展了 TeX 使其直接输出 PDF，并引入了微排版特性。pdfTeX 已成为大多数 TeX 发行版中的默认引擎。

# INSTALL

```apt: sudo apt install texlive-binaries```

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [tex](/man/tex)(1), [xetex](/man/xetex)(1), [luatex](/man/luatex)(1)
