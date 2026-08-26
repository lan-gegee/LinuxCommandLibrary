# TAGLINE

Debian 打包用的 debhelper 序列执行器

# TLDR

**按顺序执行 debhelper 命令**

```dh [sequence]```

**用 debhelper 构建软件包**

```dh build```

**清理构建产物**

```dh clean```

**以详细输出模式运行**

```dh [sequence] --verbose```

**列出序列中的所有命令**

```dh [sequence] --no-act```

**跳过特定命令**

```dh [sequence] --until [dh_auto_configure]```

# SYNOPSIS

**dh** _sequence_ [_options_] [_debhelper-options_]

# PARAMETERS

_SEQUENCE_
> 构建序列：build、clean、install、binary 等。

**--verbose**
> 为所有命令启用详细模式。

**--no-act**, **-n**
> 显示将要执行的操作但不实际执行。

**--with** _ADDON_
> 使用指定的 addon（如 python3、systemd）。

**--without** _ADDON_
> 禁用指定的 addon。

**--until** _CMD_
> 运行到指定命令为止。

**--after** _CMD_
> 从指定命令之后开始运行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dh** 是 debhelper 的序列执行器，按正确顺序运行一系列 dh_* 命令来构建 Debian 软件包。它自动判断需要运行哪些命令，从而简化 debian/rules 文件。

该工具读取 debian/rules 中的 override 来自定义行为。debian/rules 中的 override 目标（override_dh_*）让维护者修改特定步骤。addon 支持则为特定打包场景扩展功能。

dh 大幅减少了 debian/rules 的样板代码，用简单的序列调用取代显式的命令列表，自动处理大部分打包任务。

# CAVEATS

行为取决于 debhelper 兼容级别（在 debian/compat 或 Build-Depends 中设置）。override 语法在不同兼容级别之间有所差异。某些软件包需要显式的命令序列。

# HISTORY

dh 由 **Joey Hess** 在 **debhelper v7**（2008 年）中引入，用于简化 Debian 打包。它催生了"dh 短格式"rules 文件，显著降低了打包复杂度。

# SEE ALSO

[debhelper](/man/debhelper)(7), [dpkg-buildpackage](/man/dpkg-buildpackage)(1), [lintian](/man/lintian)(1)
