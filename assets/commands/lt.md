# TAGLINE

以树形结构列出目录内容

# TLDR

**以树形列出文件**

```lt```

**列出指定目录**

```lt [directory/]```

**显示隐藏文件**

```lt -a```

**限制深度**

```lt -L [2]```

**显示文件详情**

```lt -l```

**彩色输出**

```lt --color```

# SYNOPSIS

**lt** [_options_] [_path_]

# PARAMETERS

_PATH_
> 要列出的目录。

**-a**
> 显示隐藏文件。

**-L** _DEPTH_
> 最大深度。

**-l**
> 长列表格式。

**--color**
> 启用彩色输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lt** 以树形格式列出目录内容。它通常是一个 shell 别名而非独立命令，一般配置为 **lsd --tree**、**exa --tree** 或 **eza --tree** 的别名。

具体行为和可用选项取决于底层命令。运行 **type lt** 或 **alias lt** 可查看你系统上的实际定义。

# CAVEATS

并非标准命令。行为和可用标志完全取决于别名的配置方式。此处显示的选项对应于 lsd 或 eza 等常见实现。

# HISTORY

**lt** 通常被配置为 shell 别名，借助 **lsd**、**exa** 或 **eza** 等现代 ls 替代品实现树形目录列表。

# INSTALL

```apt: sudo apt install looptools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [lsd](/man/lsd)(1), [exa](/man/exa)(1), [eza](/man/eza)(1), [ls](/man/ls)(1)
