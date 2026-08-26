# TAGLINE

现代化、自包含的 LaTeX 引擎

# TLDR

**编译 LaTeX 文档**

```tectonic [document.tex]```

**编译并指定输出目录**

```tectonic -o [output/] [document.tex]```

**带 synctex 编译**

```tectonic --synctex [document.tex]```

**保留中间文件**

```tectonic --keep-intermediates [document.tex]```

**打印模式**（不联网）

```tectonic --only-cached [document.tex]```

**监视模式**（V1 CLI）

```tectonic --watch [document.tex]```

**使用 bundle**

```tectonic -b [bundle.tar] [document.tex]```

**构建文档**，使用 V2 CLI（需要 Tectonic.toml）

```tectonic -X build```

**创建新的文档**工作区

```tectonic -X new [project_name]```

**编译独立文档**（V2 CLI）

```tectonic -X compile [document.tex]```

# SYNOPSIS

**tectonic** [_-o dir_] [_--synctex_] [_--keep-intermediates_] [_options_] _file.tex_

# PARAMETERS

**-o** _DIR_
> 输出目录。

**--synctex**
> 生成 SyncTeX 数据。

**--keep-intermediates**
> 保留 .aux、.log 等。

**--keep-logs**
> 保留日志文件。

**--only-cached**
> 不下载软件包。

**--watch**, **-w**
> 监视并重新编译。

**-b** _FILE_
> 使用 bundle 文件。

**--print**
> 打印模式（PDF 输出到 stdout）。

**--format** _FMT_
> 输出格式。

**--untrusted**
> 禁用 shell-escape。

**-c** _FILE_
> 配置文件。

**-h**, **--help**
> 显示帮助。

**-X** _SUBCOMMAND_
> 启用 V2 CLI（build、compile、new、init、dump、show、watch）。

# DESCRIPTION

**tectonic** 是一个现代化的自包含 LaTeX 引擎，它会自动下载所需的宏包、执行正确次数的编译轮次，并生成可复现的输出。与传统 TeX 发行版不同，它不需要单独安装 TeX Live——缺失的宏包会按需从网络获取。

该引擎会自动处理 LaTeX 通常需要的多次编译轮次，用于解析引用、目录、参考文献和交叉引用。监视模式（**--watch**）会在源文件变化时重新编译，配合 PDF 查看器即可实现实时预览。

Tectonic 使用 bundle——自包含的宏包集合——来确保构建可复现：相同的输入总是产生相同的输出。**--only-cached** 标志允许使用先前下载的宏包进行离线编译。

V2 CLI（通过 **-X** 启用）提供类似 cargo 的接口，以 **Tectonic.toml** 文件为核心。项目构建使用 `tectonic -X build`，独立文档编译使用 `tectonic -X compile`。这一方式使 Tectonic 非常适合 CI/CD 流水线和基于版本控制的协作写作项目。

# CAVEATS

首次编译会下载宏包。获取新宏包需要联网。一些冷门宏包可能缺失。与传统 TeX 工作流有所不同。

# HISTORY

**Tectonic** 由 **Peter Williams** 自 **2016 年**前后开始创建。它基于 XeTeX 引擎并辅以现代工具链，解决了传统 TeX 发行版的诸多痛点。

# INSTALL

```pacman: sudo pacman -S tectonic```

```apk: sudo apk add tectonic```

```brew: brew install tectonic```

```nix: nix profile install nixpkgs#tectonic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [xelatex](/man/xelatex)(1), [lualatex](/man/lualatex)(1), [latexmk](/man/latexmk)(1)
