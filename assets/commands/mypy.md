# TAGLINE

Python 静态类型检查器

# TLDR

**对文件做类型检查**

```mypy [script.py]```

**对目录做类型检查**

```mypy [src/]```

**严格模式**

```mypy --strict [script.py]```

**忽略缺失的导入**

```mypy --ignore-missing-imports [script.py]```

**显示错误代码**

```mypy --show-error-codes [script.py]```

**按指定 Python 版本检查**

```mypy --python-version [3.10] [script.py]```

**生成 HTML 报告**

```mypy --html-report [report/] [script.py]```

# SYNOPSIS

**mypy** [_options_] _files_

# PARAMETERS

_FILES_
> 要检查的 Python 文件。

**--strict**
> 启用所有可选的错误检查标志（严格模式）。

**--ignore-missing-imports**
> 消除无法解析的导入所引起的错误提示。

**--show-error-codes**
> 在错误信息中显示错误代码（近期版本默认开启）。

**--python-version** _X.Y_
> 按指定的 Python 版本进行类型检查。

**--disallow-untyped-defs**
> 禁止定义没有类型注解的函数。

**--follow-imports** _MODE_
> 如何处理导入（normal、silent、skip、error）。

**--html-report** _DIR_
> 生成 HTML 类型检查覆盖率报告（需要 lxml）。

**--install-types**
> 自动安装缺失的第三方类型存根。

**--namespace-packages**
> 支持 PEP 420 命名空间包。

**--config-file** _FILE_
> 使用指定的 mypy 配置文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mypy** 是 Python 的静态类型检查器。它用于验证类型注解。

该工具能在运行前捕获类型错误。支持渐进式采用类型标注。

# CAVEATS

需要类型注解。可能需要第三方类型存根。提供可选的严格模式。

# HISTORY

mypy 由 **Jukka Lehtosalo** 创建，在 Dropbox 开发，是 Python 首屈一指的类型检查器。

# INSTALL

```pacman: sudo pacman -S mypy```

```apk: sudo apk add py3-mypy```

```brew: brew install mypy```

```nix: nix profile install nixpkgs#mypy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [pyright](/man/pyright)(1), [pylint](/man/pylint)(1), [ruff](/man/ruff)(1), [black](/man/black)(1), [flake8](/man/flake8)(1)
