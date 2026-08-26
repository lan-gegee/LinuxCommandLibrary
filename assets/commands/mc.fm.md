# TAGLINE

Midnight Commander 的文件管理器模式

# TLDR

**启动文件管理器**

```mc```

**浏览目录**

```mc [/path/to/dir]```

**打开两个目录**

```mc [left_dir] [right_dir]```

**使用内置查看器查看**

```mc -v [file]```

**使用内置编辑器编辑**

```mc -e [file]```

# SYNOPSIS

**mc** [_options_] [_path1_] [_path2_]

# PARAMETERS

_PATH1_ _PATH2_
> 两个面板显示的目录。

**-v** _FILE_
> 仅查看文件。

**-e** _FILE_
> 仅编辑文件。

**-b**
> 黑白模式。

**-c**
> 彩色模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mc** 是 Midnight Commander 的文件管理器模式。它提供双面板文件导航。

该工具支持键盘驱动的操作、归档浏览以及远程文件系统访问。

# CAVEATS

基于终端。需要使用功能键。与 mc 命令相同。

# HISTORY

Midnight Commander 文件管理器由 **Miguel de Icaza** 创建，是 Norton Commander 的克隆。

# SEE ALSO

[mc](/man/mc)(1), [ranger](/man/ranger)(1), [nnn](/man/nnn)(1)
