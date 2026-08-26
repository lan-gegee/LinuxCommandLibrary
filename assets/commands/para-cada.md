# TAGLINE

用 glob 表达式自动化重复性的文件处理任务

# TLDR

**对每个匹配的文件运行命令**

```para-cada [glob_pattern] -- [command]```

**预览操作**而不实际执行（试运行）

```para-cada --dry-run [glob_pattern] -- [command]```

**解压当前目录下所有 .tgz 归档**

```para-cada '*.tgz' -- tar xzf {}```

# SYNOPSIS

**para-cada** [_options_] _glob_pattern_ **--** _command_

# PARAMETERS

**--dry-run**
> 预览操作但不实际执行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**para-cada**（西班牙语意为"for each"）是一个自动化重复性文件任务的 CLI 工具。它对每个匹配 glob 表达式的文件执行一条命令，并把 **{}** 替换为匹配到的文件名。它支持批处理、基于 Python 的过滤和值变换、并发执行、试运行预览，以及通过插件支持高级操作。

# CAVEATS

需要 Python。glob 模式应加引号，以防被 shell 展开。仅限于基于 glob 匹配的文件操作。

# HISTORY

**para-cada** 由 **gergelyk** 开发，使用 **Python** 编写。可通过 PyPI 用 **pip install para-cada** 安装。

# SEE ALSO

[find](/man/find)(1), [xargs](/man/xargs)(1), [fd](/man/fd)(1)
