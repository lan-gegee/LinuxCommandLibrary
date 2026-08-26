# TAGLINE

Google Python 代码格式化工具

# TLDR

**格式化一个 Python 文件**并将结果打印到标准输出

```yapf [file.py]```

**就地格式化文件**

```yapf -i [file.py]```

**显示**格式化更改的 **diff**

```yapf -d [file.py]```

**按 Google 风格格式化**

```yapf --style=google [file.py]```

递归**格式化所有 Python 文件**

```yapf -r -i [directory/]```

**并行格式化**以加快处理速度

```yapf -p -r -i [directory/]```

**显示可用的风格选项**

```yapf --style-help```

**使用自定义风格配置**

```yapf --style='{based_on_style: pep8, indent_width: 4}' [file.py]```

# SYNOPSIS

**yapf** [_options_] [_files_...]

# PARAMETERS

**-i**, **--in-place**
> 就地修改文件

**-d**, **--diff**
> 打印更改的 diff，但不修改文件

**-r**, **--recursive**
> 递归格式化目录中的文件

**-p**, **--parallel**
> 多文件时并行执行格式化

**-s**, **--style** _style_
> 风格：pep8、google、chromium、facebook，或配置文件的路径

**--style-help**
> 显示所有风格选项的文档

**-l**, **--lines** _range_
> 仅格式化指定的行（例如 1-10,15-20）

**-e**, **--exclude** _pattern_
> 排除匹配模式的文件

**--version**
> 显示版本并退出

# DESCRIPTION

**yapf**（Yet Another Python Formatter）是由 Google 开发的 Python 代码格式化工具。与只警告风格违规的 linter 不同，yapf 会重新编排代码使其符合配置的风格，无论原始格式如何都能产生一致的输出。

该算法分析代码结构，并根据配置的风格计算最优格式。内置风格包括 **pep8**（默认）、**google**、**chromium** 和 **facebook**。可以通过继承基础风格并覆盖特定选项来定义自定义风格。

源代码目录或其父目录中的配置文件（**.style.yapf**、**setup.cfg** 或 **pyproject.toml**）会被自动检测。配置文件使用 INI 格式，包含 **[style]** 段。

yapf 可以通过 **--lines** 格式化特定的行范围，适合在版本控制工作流中只格式化已更改的代码。

# CAVEATS

yapf 的输出可能与 black 等其他格式化工具不同。**-i** 选项会直接修改文件；建议先用 **-d** 预览更改。某些复杂表达式可能以意想不到的方式被格式化。注释会影响格式化的决策。

# HISTORY

**yapf** 由 **Google** 开发，于 **2015 年**首次作为开源项目发布。其灵感来自 **clang-format**（面向 C/C++），将类似的算法化格式化方法应用于 Python。命名遵循了 Unix "Yet Another" 工具的传统，承认其他 Python 格式化工具的存在。

# INSTALL

```pacman: sudo pacman -S yapf```

```apk: sudo apk add py3-yapf```

```brew: brew install yapf```

```nix: nix profile install nixpkgs#yapf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[black](/man/black)(1), [autopep8](/man/autopep8)(1), [isort](/man/isort)(1), [flake8](/man/flake8)(1)
