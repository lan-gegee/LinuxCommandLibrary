# TAGLINE

可视化展示被 ignore 规则匹配的文件

# TLDR

**可视化项目中被忽略的文件**

```vignore -d [/path/to/project]```

**可视化当前目录中被忽略的文件**

```vignore -d .```

# SYNOPSIS

**vignore** [**-h**] **-d** _DIFFPATH_

# PARAMETERS

**-d** _DIFFPATH_
> 要分析的项目目录路径。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**vignore** 可视化哪些文件被 .gitignore、.dockerignore 或 .fdignore 等 ignore 规则匹配。它提供即时视觉反馈，帮助开发者无需猜测即可理解自己的 ignore 模式。需要安装 **fd**。

# CAVEATS

需要安装 **fd**（fd-find）并确保其位于 PATH 中。仅支持 fd 能识别的 ignore 文件格式。

# HISTORY

**vignore** 由 **James4Ever0** 开发，使用 **Python** 编写。

# SEE ALSO

[fd](/man/fd)(1), [tree](/man/tree)(1), [git](/man/git)(1)
