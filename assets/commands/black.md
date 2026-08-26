# TAGLINE

固执己见的 Python 代码格式化工具

# TLDR

**格式化** Python 文件

```black [script.py]```

格式化**整个项目**

```black [src/]```

**检查**而不修改

```black --check [script.py]```

以 **diff** 显示而不重写文件

```black --diff [script.py]```

设置**行长度**

```black -l [100] [script.py]```

# SYNOPSIS

**black** [_options_] _files_

# DESCRIPTION

**black** 是一个固执己见的 Python 代码格式化工具。它通过以极少的配置自动重新排版代码来强制统一风格。Black 的理念是提供唯一正确的方式，从而消除关于格式的争论。

该工具可与编辑器和 CI 管道集成，确保 Python 代码风格的一致性。

# PARAMETERS

**--check**
> 检查文件是否会被重新排版（若会则退出码为 1）

**--diff**
> 显示 diff 而不重写文件

**-l**, **--line-length** _n_
> 行长度（默认：88）

**--target-version** _py_
> Python 版本（py37、py38、py39 等）

**--exclude** _pattern_
> 要排除的文件/目录

**--include** _pattern_
> 要包含的文件/目录

**--quiet**
> 最少输出

**--verbose**
> 详细输出

**--color**/**--no-color**
> 彩色输出

# CONFIGURATION

**pyproject.toml**
> 项目级配置，位于 `[tool.black]` 部分。支持 `line-length`、`target-version`、`include` 和 `exclude` 设置。

# CAVEATS

风格固定（配置选项有限）。可能与其他格式化工具冲突。默认 88 字符的行长与 PEP 8 的 79 不同。某些排版选择存在争议。需要 Python 3.6+。

# HISTORY

**Black** 由 Łukasz Langa 于 **2018 年**创建，旨在提供确定性的 Python 排版，消除格式之争并减少 diff 噪音。

# INSTALL

```apt: sudo apt install black```

```dnf: sudo dnf install black```

```apk: sudo apk add black```

```brew: brew install black```

```nix: nix profile install nixpkgs#black```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[autopep8](/man/autopep8)(1), [isort](/man/isort)(1), [flake8](/man/flake8)(1)
