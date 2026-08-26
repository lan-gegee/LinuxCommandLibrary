# TAGLINE

按字母顺序排序 Python 导入并将其分节

# TLDR

**就地排序文件中的导入**

```isort [file.py]```

**只检查而不修改（如需更改则退出码非零）**

```isort --check-only [file.py]```

**显示拟修改内容的 diff**

```isort --diff [file.py]```

**递归排序当前目录下所有 Python 文件**

```isort .```

**使用与 Black 兼容的 profile**

```isort --profile black [file.py]```

**设置行宽并并行运行**

```isort -l [100] -j [4] [path]```

# SYNOPSIS

**isort** [_options_] [_path_...]

# PARAMETERS

**-c**, **--check-only**
> 只检查导入是否已排序，不修改文件。如果会作出更改则退出码为 1。

**--diff**
> 打印 isort 将作出的更改的 diff，而不是直接应用。

**--profile** _NAME_
> 使用预定义的 profile（black、django、pycharm、google、open_stack、plone、attrs、hug、wemake、appnexus）。

**-l**, **--line-length** _LENGTH_
> 导入行折行时使用的最大长度。默认为 79。

**--force-single-line**, **--sl**
> 强制所有 `from` 导入各占一行。

**--skip**, **-s** _PATH_
> 要跳过的文件或目录。可多次指定。

**--atomic**
> 如果输出文件会包含语法错误，则放弃写入。

**-j**, **--jobs** _N_
> 并行处理的文件数。负值表示使用 CPU 核心数。

**--settings-path**, **--sp** _PATH_
> 显式指定设置文件或目录的路径（覆盖自动检测）。

**-v**, **--verbose**
> 打印处理过程的详细输出。

**-q**, **--quiet**
> 仅显示错误。

**--help**
> 显示帮助信息。

# DESCRIPTION

**isort** 按字母顺序排序 Python 导入并将它们分成不同的节。它遵循 PEP 8 中关于导入组织的准则。

该工具将导入分为标准库、第三方库和本地库三组。它可与编辑器和 CI 流水线集成。

# CAVEATS

仅针对 Python。可能与其他格式化工具冲突。可使用 profile 保持兼容性。

# HISTORY

isort 由 **Timothy Crosley** 创建，用于按照最佳实践自动排序和整理 Python 导入。

# INSTALL

```apk: sudo apk add py3-isort```

```brew: brew install isort```

```nix: nix profile install nixpkgs#isort```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[black](/man/black)(1), [ruff](/man/ruff)(1), [flake8](/man/flake8)(1), [autopep8](/man/autopep8)(1), [yapf](/man/yapf)(1), [pylint](/man/pylint)(1), [mypy](/man/mypy)(1)
