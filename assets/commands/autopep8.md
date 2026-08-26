# TAGLINE

自动将 Python 代码格式化为 PEP 8 风格

# TLDR

**原地格式化 Python 文件**

```autopep8 --in-place [file.py]```

**应用激进修复进行格式化**（重复 -a 可提高激进程度）

```autopep8 --in-place --aggressive --aggressive [file.py]```

**显示 diff 而不修改文件**

```autopep8 --diff [file.py]```

递归**格式化目录中的所有 Python 文件**

```autopep8 --in-place --recursive [directory/]```

**只修复特定错误代码**

```autopep8 --select E501,W293 --in-place [file.py]```

**使用多个并行任务格式化**

```autopep8 --in-place --recursive --jobs 4 [directory/]```

**设置自定义最大行宽**

```autopep8 --max-line-length 120 --in-place [file.py]```

# SYNOPSIS

**autopep8** [_--in-place_] [_--aggressive_] [_options_] _files_

# DESCRIPTION

**autopep8** 自动将 Python 代码格式化为符合 PEP 8 风格指南的形式。它在保持代码语义的前提下修复空白、缩进、行宽等问题。

该工具可集成到编辑器和 CI 流水线中以强制统一的 Python 风格。它使用 pycodestyle 检测风格违规并相应地应用修复。

# PARAMETERS

**-i**, **--in-place**
> 原地修改文件。

**-d**, **--diff**
> 打印更改的统一 diff 而不修改文件。

**-r**, **--recursive**
> 递归处理目录。需要配合 `--in-place` 或 `--diff`。

**-a**, **--aggressive**
> 启用空白之外的更激进修复。可重复使用以提高激进程度（如 -aa）。

**-j** _n_, **--jobs** _n_
> 并行任务数。小于 1 的值表示使用所有可用 CPU。

**--select** _errors_
> 只修复指定的错误代码（如 E501,W293）。

**--ignore** _errors_
> 忽略指定的错误代码（默认：E226,E24,W50,W690）。

**--max-line-length** _n_
> 允许的最大行宽（默认：79）。

**--range** _start_ _end_
> 只修复指定行范围内的错误。

**--exclude** _patterns_
> 排除匹配指定逗号分隔 glob 模式的文件和目录。

**--experimental**
> 启用实验性的代码缩短特性。

**--list-fixes**
> 列出可与 `--select` 和 `--ignore` 一起使用的错误代码。

**-v**, **--verbose**
> 打印详细消息。可重复使用以获得更多信息。

**-p** _n_, **--pep8-passes** _n_
> 额外格式化遍数的最大次数（默认：无限次，直到不再有变化）。

**--hang-closing**
> 让闭括号悬挂缩进，而不是与起始行对齐。

**--exit-code**
> 当使用 `--diff` 或 `--in-place` 且有更改时返回退出码 2。

**--global-config** _filename_
> 指定 pycodestyle 规则的自定义全局配置文件。

**--ignore-local-config**
> 不读取本地配置文件。

**--version**
> 显示版本号并退出。

**--help**
> 显示帮助信息。

# ERROR CODES

基于 PEP 8：
- **E**: 错误（如 E501 行过长、E302 缺少空行）
- **W**: 警告（如 W291 行尾空白、W293 注释前有空白）

# CONFIGURATION

**setup.cfg**
> 项目级配置，位于 `[pycodestyle]` 小节下。

**pyproject.toml**
> 项目级配置，位于 `[tool.autopep8]` 小节下。

**~/.config/pycodestyle**
> pycodestyle 规则的用户级默认配置。

# CAVEATS

可能与 **black** 等其他格式化工具冲突。激进模式在极少数情况下可能改变代码逻辑；提交前请检查更改。若偏好强风格约束，**black** 目前更为流行。

# HISTORY

**autopep8** 由 Hideo Hattori 创建，于 **2010 年**前后发布，用于自动实现 PEP 8 合规。

# INSTALL

```pacman: sudo pacman -S autopep8```

```apk: sudo apk add py3-autopep8```

```brew: brew install autopep8```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[black](/man/black)(1), [isort](/man/isort)(1), [flake8](/man/flake8)(1), [yapf](/man/yapf)(1), [pycodestyle](/man/pycodestyle)(1), [pylint](/man/pylint)(1)
