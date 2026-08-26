# TAGLINE

分析 Python 代码的错误与风格问题

# TLDR

**检查 Python 文件**

```pylint [file.py]```

**使用指定配置检查**

```pylint --rcfile=[.pylintrc] [file.py]```

**禁用特定警告**

```pylint --disable=[C0114] [file.py]```

**生成配置文件**

```pylint --generate-rcfile > [.pylintrc]```

**以 JSON 格式输出**

```pylint --output-format=json [file.py]```

# SYNOPSIS

**pylint** [_options_] _modules_

# PARAMETERS

_MODULES_
> 要检查的 Python 模块。

**--rcfile** _FILE_
> 配置文件。

**--disable** _IDS_
> 禁用检查项。

**--enable** _IDS_
> 启用检查项。

**--output-format** _FORMAT_
> 输出格式。

**--generate-rcfile**
> 生成配置文件。

# DESCRIPTION

**pylint** 是一个功能全面的静态分析工具，用于检查 Python 代码中的编程错误、编码规范违规和代码坏味道。它在不运行代码的情况下检查模块，并按类别报告问题：约定（C）、重构建议（R）、警告（W）、错误（E）和致命问题（F），每条都带有数字代码以便精确过滤。

该工具可通过 **.pylintrc** 文件或 **pyproject.toml** 段落高度自定义，团队可以启用、禁用或定制各项检查以匹配项目规范。它还会给出一个 10 分制的整体代码质量评分，便于在 CI 流水线中长期跟踪代码健康度。插件可将分析扩展到 Django 和 SQLAlchemy 等框架。

# CONFIGURATION

**.pylintrc**
> 项目级配置文件，用于启用/禁用检查、设置阈值和定义编码规范。

**pyproject.toml**
> 项目配置文件，包含 `[tool.pylint]` 段，支持与 .pylintrc 相同的选项。

**setup.cfg**
> 另一种配置文件，包含 `[pylint]` 段用于检查设置。

**~/.pylintrc**
> 用户级默认配置，在未找到项目配置时应用。

# CAVEATS

在大型代码库上可能较慢。可高度自定义。

# HISTORY

Pylint 作为**全面的 Python** 代码分析工具而创建。

# INSTALL

```dnf: sudo dnf install pylint```

```apk: sudo apk add py3-pylint```

```brew: brew install pylint```

```nix: nix profile install nixpkgs#pylint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pyflakes](/man/pyflakes)(1), [flake8](/man/flake8)(1), [mypy](/man/mypy)(1), [ruff](/man/ruff)(1)
