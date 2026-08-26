# TAGLINE

面向 BibLaTeX 的现代参考文献处理器

# TLDR

**处理 BibLaTeX 参考文献**

```biber [document]```

**用指定输出目录处理**

```biber -O [output_dir] [document]```

**对照数据模型校验数据**

```biber --validate-datamodel [document]```

**以静默输出处理**

```biber -q [document]```

**启用追踪**以便调试

```biber --trace [document]```

**指定输出格式**

```biber --output-format [bbl] [document]```

**将 .bib 数据库转换为 BibLaTeXML**

```biber --tool --output-format=biblatexml [references.bib]```

# SYNOPSIS

**biber** [_options_] _file_[.bcf]

# DESCRIPTION

**biber** 是一款设计用来取代 BibTeX 的现代参考文献处理器，作为 LaTeX 文档中 biblatex 软件包的后端。它提供高级排序、过滤和 Unicode 支持。

Biber 读取由 LaTeX 生成的 **.bcf**（biblatex 控制文件），并生成包含已格式化参考文献的 **.bbl** 文件。它支持多个文献数据库，并提供丰富的配置选项。

# PARAMETERS

**--output-directory** _dir_
> 输出文件的写入目录

**-O, --output-file** _file_
> 输出到指定文件，而不是 basename.bbl

**--output-format** _format_
> 输出格式：bbl（默认）、dot、bibtex、biblatexml、bblxml

**-e, --input-encoding** _encoding_
> 输入文件的字符编码（默认：UTF-8）

**-E, --output-encoding** _encoding_
> 输出文件的字符编码（默认：UTF-8）

**--tool**
> 以工具模式运行，在没有 .bcf 控制文件的情况下转换/处理单个数据源（.bib）

**-V, --validate-datamodel**
> 对照数据模型校验数据

**--validate-control**
> 对 .bcf 控制文件做 schema 校验

**-q, --quiet**
> 仅记录错误；使用两次可抑制所有输出

**-T, --trace**
> 启用底层追踪以便调试（同时开启 --debug）

**--logfile** _file_
> 将日志消息写入指定文件

**--nolog**
> 不写任何日志文件

**-v, --version**
> 显示版本号

# CAVEATS

Biber 需要先用 LaTeX 配合 biblatex 运行生成 **.bcf** 文件。典型工作流程是：pdflatex -> biber -> pdflatex -> pdflatex。Biber 不是 BibTeX 的直接替代品；它必须搭配 biblatex 软件包使用。

# HISTORY

Biber 最初由 **Francois Charette** 编写；**Philip Kime** 于 **2009 年**加入开发，并将其打磨成今天功能完备的后端。它以 Perl 编写，解决了 BibTeX 的诸多局限，尤其是 Unicode 支持和高级排序方面。它成为 biblatex 的推荐后端，如今已是现代 LaTeX 参考文献处理的标准工具。

# INSTALL

```dnf: sudo dnf install biber```

```pacman: sudo pacman -S biber```

```apk: sudo apk add biber```

```brew: brew install biber```

```nix: nix profile install nixpkgs#biber```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bibtex](/man/bibtex)(1), [pdflatex](/man/pdflatex)(1), [latex](/man/latex)(1)

# RESOURCES

```[Source code](https://github.com/plk/biber)```

```[Homepage](https://sourceforge.net/projects/biblatex-biber/)```

<!-- verified: 2026-06-19 -->
