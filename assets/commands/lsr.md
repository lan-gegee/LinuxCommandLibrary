# TAGLINE

带 Git 集成和 Lua 扩展性的彩色 ls 替代品

# TLDR

**列出当前目录**中的文件

```lsr```

以树状结构**递归列出文件**

```lsr -R```

带 Git 状态**列出文件**

```lsr -g```

列出所有文件，包括隐藏文件

```lsr -a```

**列出特定目录**中的文件

```lsr [/path/to/directory]```

# SYNOPSIS

**lsr** [_options_] [_path_...]

# PARAMETERS

**-R**, **--recursive**
> 以递归的树状结构显示文件。

**-g**, **--git**
> 显示已暂存和未暂存更改的 Git 状态指示符。

**-a**, **--all**
> 显示隐藏文件。

# DESCRIPTION

**lsr**（又名 Laser）是一个注重可读性和易用性的 **ls** 命令行替代品。它提供色彩化的文件列表、更佳的视觉组织、递归树状显示、Git 状态指示符，并通过视觉标志标识文件/符号链接。

配色方案可自定义，该工具还可通过 **Lua 脚本**扩展，显示标准 ls 之外的自定义信息。

# CAVEATS

Lua 脚本扩展要求系统上可用 Lua。

# HISTORY

**lsr** 由 **jmattaa** 创建，使用 **C** 编写。支持 macOS、Linux、BSD 和 Windows。

# INSTALL

```brew: brew install lsr```

```nix: nix profile install nixpkgs#lsr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [eza](/man/eza)(1), [tree](/man/tree)(1), [lsd](/man/lsd)(1), [exa](/man/exa)(1)
