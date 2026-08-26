# TAGLINE

极快的 Python linter 和格式化工具

# TLDR

**检查当前目录**

```ruff check```

**检查特定文件**

```ruff check [file.py] [other.py]```

**自动修复问题**

```ruff check --fix```

**格式化代码**

```ruff format```

**显示可修复的问题**

```ruff check --show-fixes```

**监视模式**

```ruff check --watch```

**选择特定规则**

```ruff check --select [E,F,W]```

**忽略规则**

```ruff check --ignore [E501]```

# SYNOPSIS

**ruff** [_check_] [_format_] [_--fix_] [_--select rules_] [_options_] [_paths_]

# PARAMETERS

**check**
> 运行 lint 检查。

**format**
> 格式化代码。

**--fix**
> 自动修复违规项。

**--unsafe-fixes**
> 应用不安全的修复。

**--select** _RULES_
> 要启用的规则。

**--ignore** _RULES_
> 要忽略的规则。

**--extend-select** _RULES_
> 额外的规则。

**--config** _FILE_
> 配置文件。

**--show-fixes**
> 显示可用的修复。

**--watch**
> 监视变化。

**--output-format** _FMT_
> 输出格式（text、json 等）。

**--statistics**
> 显示统计信息。

**--diff**
> 显示修复的差异。

# DESCRIPTION

**ruff** 是一个用 Rust 编写、速度极快的 Python linter。它实现了来自 Flake8、isort、pyupgrade 以及其他工具的规则。

速度是其主要优势。Ruff 比传统的 Python linter 快 10 到 100 倍。这使得实时反馈和无延迟的 CI 集成成为可能。

规则选择控制哪些检查会执行。类别包括 E（pycodestyle 错误）、F（Pyflakes）、W（警告）、I（isort）、UP（pyupgrade）等等。

其格式化工具与 Black 兼容，提供一致的代码风格。它与 linter 集成在一起，构成统一的工具链。

pyproject.toml 或 ruff.toml 中的配置可以自定义行为。按文件忽略和 extend 支持能满足复杂项目的需求。

修复模式会自动修改文件。不安全的修复可能改变程序行为，因此需要单独启用。

# CONFIGURATION

**pyproject.toml** `[tool.ruff]`
> 标准 Python 项目文件中的 Ruff 配置节，定义规则选择、行长度、按文件忽略和目标 Python 版本。

**ruff.toml**
> 独立的 Ruff 配置文件，可作为 pyproject.toml 的替代。

**.ruff.toml**
> 独立配置文件的隐藏变体，会在各级父目录中查找。

# CAVEATS

基于 Rust 实现——需要独立于 Python 单独安装。并非所有 Flake8 插件都已实现。迭代非常迅速。

# HISTORY

**Ruff** 由 **Charlie Marsh** 于 **2022 年**创建。它凭借速度迅速走红，用一个快速工具取代了多个 Python 工具。

# INSTALL

```dnf: sudo dnf install ruff```

```pacman: sudo pacman -S ruff```

```apk: sudo apk add ruff```

```brew: brew install ruff```

```nix: nix profile install nixpkgs#ruff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flake8](/man/flake8)(1), [black](/man/black)(1), [pylint](/man/pylint)(1), [isort](/man/isort)(1)
