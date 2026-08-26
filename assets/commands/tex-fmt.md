# TAGLINE

快速的 LaTeX 源码格式化工具

# TLDR

**格式化文件**

```tex-fmt [document.tex]```

**原地格式化**

```tex-fmt -w [document.tex]```

**检查格式**

```tex-fmt --check [document.tex]```

**从 stdin 格式化**

```cat [document.tex] | tex-fmt```

**使用配置文件**

```tex-fmt -c [tex-fmt.toml] [document.tex]```

# SYNOPSIS

**tex-fmt** [_-w_] [_--check_] [_-c config_] [_options_] _files_

# PARAMETERS

**-w**
> 原地写入。

**--check**
> 仅检查。

**-c** _FILE_
> 配置文件。

**--stdin**
> 读取 stdin。

**--tabsize** _N_
> 制表符宽度。

# DESCRIPTION

**tex-fmt** 是一款用 Rust 编写的快速 LaTeX 源码格式化工具，用于统一 .tex 文件中的缩进和空白。它对 LaTeX 环境、命令和结构应用可配置的缩进规则，确保文档之间、团队之间格式一致。

**-w** 标志将更改原地写入，而 **--check** 模式只验证格式而不修改文件，因此适合 CI 流水线。可通过 TOML 文件提供配置，自定义缩进宽度、制表符处理及其他样式偏好。

# CAVEATS

仅适用于 LaTeX。可能破坏手工排版。使用前请先测试。

# HISTORY

**tex-fmt** 是一款用 Rust 编写的快速 LaTeX 格式化工具，用于实现一致的文档格式。

# INSTALL

```apt: sudo apt install tex-fmt```

```brew: brew install tex-fmt```

```nix: nix profile install nixpkgs#tex-fmt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[latexindent](/man/latexindent)(1), [latex](/man/latex)(1), [pdflatex](/man/pdflatex)(1)
