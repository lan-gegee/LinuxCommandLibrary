# TAGLINE

Python 代码检查与风格检查工具

# TLDR

**检查 Python 文件**

```flake8 [file.py]```

**检查目录**

```flake8 [src/]```

**只显示指定错误**

```flake8 --select=[E,W] [file.py]```

**忽略指定错误**

```flake8 --ignore=[E501] [file.py]```

**设置最大行宽**

```flake8 --max-line-length=[120] [file.py]```

# SYNOPSIS

**flake8** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要检查的 Python 文件或目录。

**--select** _ERRORS_
> 只检查指定的错误代码。

**--ignore** _ERRORS_
> 忽略指定的错误代码。

**--max-line-length** _N_
> 最大行宽（默认 79）。

**--exclude** _PATTERNS_
> 排除匹配的文件/目录。

**--config** _FILE_
> 指定配置文件。

**--format** _FORMAT_
> 输出格式。

**--help**
> 显示帮助信息。

# CONFIGURATION

**setup.cfg**
> 项目级 flake8 配置，位于 [flake8] 小节。

**.flake8**
> 项目专用的 flake8 配置文件。

**~/.config/flake8**
> 用户级全局配置文件。

# DESCRIPTION

**flake8** 是一款 Python 代码检查工具，融合了 PyFlakes、pycodestyle 和 McCabe 复杂度检查。它能够发现编程错误、风格问题以及过度复杂的代码。

该工具执行 PEP 8 风格规范，并能捕获未定义变量、无用导入和语法问题等常见错误。通过插件可以针对更多框架和模式扩展检查功能。

flake8 可以集成到编辑器、CI 流水线和 pre-commit 钩子中，实现自动化的代码质量管控。

# CAVEATS

默认规则相当严格，可能需要自行调整。某些检查项与其他工具有重叠。插件生态的质量良莠不齐。

# HISTORY

flake8 由 **Tarek Ziadé** 创建，旨在统一各类 Python 代码检查工具。它把多个检查器整合到一个界面之下，提供一致的配置方式与输出格式。

# INSTALL

```apk: sudo apk add py3-flake8```

```brew: brew install flake8```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pylint](/man/pylint)(1), [black](/man/black)(1), [ruff](/man/ruff)(1)

# RESOURCES

```[Source code](https://github.com/PyCQA/flake8)```

```[Documentation](https://flake8.pycqa.org/)```

<!-- verified: 2026-07-15 -->
