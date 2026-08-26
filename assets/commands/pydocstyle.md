# TAGLINE

检查 Python docstring 规范

# TLDR

**检查 docstring**

```pydocstyle [module.py]```

**检查目录**

```pydocstyle [src/]```

**选择规范**

```pydocstyle --convention [google] [module.py]```

**忽略特定错误**

```pydocstyle --ignore [D100,D101] [module.py]```

**选择特定错误**

```pydocstyle --select [D200,D201] [module.py]```

**显示源码**

```pydocstyle --source [module.py]```

**仅统计错误数**

```pydocstyle --count [module.py]```

# SYNOPSIS

**pydocstyle** [_--convention name_] [_--ignore codes_] [_--select codes_] [_options_] _files_

# PARAMETERS

**--convention** _NAME_
> 规范（pep257、numpy、google）。

**--ignore** _CODES_
> 要忽略的错误。

**--select** _CODES_
> 要检查的错误。

**--source**
> 显示源代码。

**--explain**
> 解释错误。

**--count**
> 仅统计数量。

**--match** _PATTERN_
> 只检查文件名匹配正则表达式 _PATTERN_ 的文件（默认：`(?!test_).*\.py`）。

**--match-dir** _PATTERN_
> 只递归进入目录名匹配正则表达式 _PATTERN_ 的目录（默认：`[^\.].*`）。

**--add-ignore** _CODES_
> 向现有忽略列表追加错误码（不替换原列表）。

**--add-select** _CODES_
> 向现有选择列表追加错误码（不替换原列表）。

**--config** _FILE_
> 使用指定的配置文件而非自动发现。

**-d**, **--debug**
> 输出调试信息。

**-v**, **--verbose**
> 运行期间输出状态信息。

# CONVENTIONS

**pep257** - PEP 257 规范
**numpy** - NumPy docstring 风格
**google** - Google Python 风格

# DESCRIPTION

**pydocstyle** 检查 Python docstring 是否符合规范，强制执行统一的文档风格。

规范定义了期望的格式，支持 PEP 257、NumPy 和 Google 三种风格。

错误码标识具体问题：D100 系列针对模块，D200 针对格式，等等。

显示源码可定位有问题的代码，帮助快速发现并修复问题。

配置文件可设置项目级默认值，支持 pyproject.toml 和 setup.cfg。

# CONFIGURATION

**pyproject.toml**
> 项目配置文件，包含 `[tool.pydocstyle]` 段，用于设置规范、匹配模式以及忽略/选择规则。

**setup.cfg**
> 另一种项目配置文件，包含 `[pydocstyle]` 段，支持相同的选项。

**.pydocstyle**
> pydocstyle 专用的独立配置文件。

# CAVEATS

风格偏好因人而异，可能需要按项目需求调整。并非覆盖所有边缘情况。

**已弃用：** 自 2023 年底起 pydocstyle 不再积极维护；其检查已在 **Ruff** 中以 `D` 前缀重新实现，推荐改用 Ruff。

# HISTORY

**pydocstyle** 起源于 **pep257**，后来扩展支持多种规范（PEP 257、NumPy、Google）。随着 **Ruff** 的兴起，开发逐渐放缓——Ruff 提供了更快、可直接替代的 pydocstyle 规则实现。PyCQA 项目于 2023 年 11 月宣布弃用，建议迁移到 Ruff。

# SEE ALSO

[ruff](/man/ruff)(1), [pylint](/man/pylint)(1), [flake8](/man/flake8)(1), [mypy](/man/mypy)(1), [black](/man/black)(1)
