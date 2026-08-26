# TAGLINE

自动安装缺失的 LaTeX 软件包

# TLDR

**编译并自动安装**

```texliveonfly [document.tex]```

**使用指定引擎**

```texliveonfly --compiler=[pdflatex] [document.tex]```

**附带参数**

```texliveonfly --arguments="[-shell-escape]" [document.tex]```

**试运行**

```texliveonfly --dry-run [document.tex]```

# SYNOPSIS

**texliveonfly** [_--compiler engine_] [_--arguments args_] [_options_] _file_

# PARAMETERS

**--compiler** _ENGINE_
> 要使用的 TeX 引擎。

**--arguments** _ARGS_
> 传给编译器的参数。

**--dry-run**
> 不实际安装。

**--terminal_only**
> 仅控制台输出。

**--help**
> 显示帮助。

# DESCRIPTION

**texliveonfly** 编译 LaTeX 文档的同时，会自动从 TeX Live 软件仓库安装缺失的软件包。当编译器遇到未定义的软件包时，texliveonfly 会检测该错误，使用 **tlmgr** 安装所需的软件包，然后重试编译，直到所有依赖都满足为止。

该工具适用于任何 TeX Live 引擎，包括 pdflatex、xelatex 和 lualatex，可通过 **--compiler** 标志选择。其他编译器参数可通过 **--arguments** 传入。**--dry-run** 标志只显示将安装哪些软件包，而不实际执行安装。

# CAVEATS

需要 TeX Live。需要网络访问。全局安装需要管理员权限。

# HISTORY

**texliveonfly** 的创建目的是在编译期间自动安装缺失的 LaTeX 软件包。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [tlmgr](/man/tlmgr)(1), [latexmk](/man/latexmk)(1)
