# TAGLINE

Python 快速静态错误检查器

# TLDR

**检查 Python 文件**中的错误

```pyflakes [file.py]```

**检查多个文件**

```pyflakes [file1.py] [file2.py]```

**从 stdin 检查**

```cat [file.py] | pyflakes```

**递归检查目录**

```pyflakes [path/to/directory]```

# SYNOPSIS

**pyflakes** [_options_] [_files_or_directories_]

# PARAMETERS

_FILES_
> 要检查的 Python 文件或目录

**--version**
> 显示程序版本并退出

**-h**, **--help**
> 显示帮助信息并退出

# DESCRIPTION

**pyflakes** 是一个快速轻量的静态分析工具，无需执行代码即可检查 Python 源文件中的常见错误。它能检测未定义名称、未使用的导入、重复定义的变量等会导致运行时失败的逻辑问题。

与 **pylint** 或 **flake8** 不同，pyflakes 只专注于错误检测，不检查代码风格或格式。这种狭窄的范围使其速度显著更快，且不会对风格选择产生误报，非常适合集成到编辑器和 pre-commit 钩子等注重速度的场景。

# CAVEATS

只检查逻辑错误，不检查代码风格或格式。不支持通过配置文件自定义规则。通常作为 **flake8** 的组件使用而非独立运行。

# HISTORY

Pyflakes 由 Divmod 创建，用于对 Python 代码进行**快速静态**分析。现由 PyCQA（Python Code Quality Authority）组织维护。

# INSTALL

```apk: sudo apk add py3-pyflakes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pylint](/man/pylint)(1), [flake8](/man/flake8)(1), [mypy](/man/mypy)(1), [ruff](/man/ruff)(1)
