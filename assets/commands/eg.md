# TAGLINE

提供实用命令示例的命令行工具

# TLDR

**显示**某个命令的示例

```eg [command]```

**显示**子命令的示例

```eg git log```

**列出**所有可用的示例主题

```eg --list```

**使用自定义示例目录**

```eg --examples-dir [path/to/examples] [command]```

**使用自定义分页器**显示输出

```eg --pager-cmd [less] [command]```

# SYNOPSIS

**eg** [_options_] _command_

# PARAMETERS

**--list**
> 列出所有有示例的命令。

**--color**
> 为输出着色。

**--squeeze**
> 从输出中移除空行。

**--pager-cmd** _PAGER_
> 使用指定的分页程序显示输出。

**--examples-dir** _DIR_
> 使用自定义示例目录。

**--custom-dir** _DIR_
> 使用用户自定义的示例目录。

**-v**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助并退出。

# DESCRIPTION

**eg** 是一个为常用命令提供实用示例的命令行工具。与侧重全面文档的传统 man page 不同，eg 展示最常见、最有用的用法模式，并配有清晰的解释。

eg 用 Python 编写，开箱即用，无需任何配置。它只依赖 Python 标准库，同时支持 Python 2 和 3。用户可以把自定义示例文件放在自定义目录中，与内置示例配合使用。

该工具对那些知道自己想做什么但需要快速确认确切语法的开发者特别有帮助。它覆盖 git、docker 等热门工具以及许多 Unix 实用程序。

# CAVEATS

示例库可能无法覆盖所有命令变体。示例优先考虑常见用例而非边缘情况。更新内置示例需要更新工具本身。默认情况下，自定义示例只能补充而不能覆盖内置示例。

# HISTORY

**eg** 由 **Sam Sudar** 创建，旨在提供比 man page 更实用的替代方案，专注于开发者在日常工作中真正需要的真实用法示例。源代码可在 GitHub 的 **github.com/srsudar/eg** 获取。

# INSTALL

```dnf: sudo dnf install eg```

```brew: brew install eg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [tldr](/man/tldr)(1), [cheat](/man/cheat)(1)
