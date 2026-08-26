# TAGLINE

为 LaTeX 文档处理参考文献引用

# TLDR

**处理文档的参考文献**（传入不含 .aux 扩展名的基本名）

```bibtex [document]```

**处理指定的** .aux 文件

```bibtex [document.aux]```

**静默运行**，仅打印错误消息

```bibtex -terse [document]```

**设置自动收录所需的交叉引用最小数量**

```bibtex -min-crossrefs=[number] [document]```

# SYNOPSIS

**bibtex** [_options_] _auxname_[.aux]

# DESCRIPTION

**bibtex** 为 LaTeX 文档处理参考文献信息。它读取 LaTeX 生成的 .aux 文件，在 .bib 文献数据库中查找被引条目，按文献样式（.bst）排版，并生成一个由 LaTeX 包含进最终文档的 .bbl 文件。

该工具对学术写作和 LaTeX 中的引用管理至关重要。

# PARAMETERS

**-terse**
> 静默运行，仅打印错误消息。

**-min-crossrefs=**_number_
> crossref 基础条目被自动收录进参考文献所需的最小交叉引用数（默认：2）。设为很大的值可禁用自动收录。

**-help**
> 显示帮助并退出。

**-version**
> 显示版本信息并退出。

# WORKFLOW

```bash
# 1. Run LaTeX (generates .aux with citations)
pdflatex document.tex

# 2. Run BibTeX (processes bibliography)
bibtex document

# 3. Run LaTeX twice more (to resolve references)
pdflatex document.tex
pdflatex document.tex
```

# FILES

**document.tex**
> 含 \cite 命令的 LaTeX 源文件

**refs.bib**
> 文献数据库

**document.aux**
> 辅助文件（LaTeX 的输出）

**document.bbl**
> 排版后的参考文献（BibTeX 的输出）

**document.blg**
> BibTeX 日志文件

# BIBLIOGRAPHY STYLE

常用样式：

**plain**
> 数字编号引用，按字母排序。

**alpha**
> 字母数字混合的引用标签。

**abbrv**
> 类似 plain，但名字、月份和期刊名使用缩写。

**unsrt**
> 类似 plain，但条目按引用顺序排列。

**ieeetr**
> IEEE Transactions 样式。

# BIB FORMAT

```bibtex
@article{key2023,
  author = {Author, First},
  title = {Article Title},
  journal = {Journal Name},
  year = {2023},
  volume = {10},
  pages = {1-20}
}
```

# CAVEATS

需要多次运行 LaTeX/BibTeX。错误信息可能晦涩难懂。BibTeX 语法严格。现代替代方案：biblatex/biber。Unicode 支持有限（完整 Unicode 支持请使用 biber）。

# HISTORY

**BibTeX** 由 Oren Patashnik 于 **1985 年**创建，作为 LaTeX 文档制备系统的一部分，用于管理参考文献。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[biber](/man/biber)(1), [latex](/man/latex)(1), [pdflatex](/man/pdflatex)(1)

# RESOURCES

```[Homepage](https://www.tug.org/bibtex/)```

<!-- verified: 2026-06-19 -->
