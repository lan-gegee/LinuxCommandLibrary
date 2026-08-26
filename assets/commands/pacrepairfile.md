# TAGLINE

重置 alpm 所管理文件的属性

# TLDR

搜索所属软件包并**重置文件属性**

```pacrepairfile path/to/file --package```

**静默地**重置一个文件

```pacrepairfile package_name --quiet --package```

重置指定的**文件属性**（mode、uid、gid 或 mtime）

```pacrepairfile package_name --mode --package```

显示**帮助**

```pacrepairfile --help```

# SYNOPSIS

**pacrepairfile** [_options_] _target_

# PARAMETERS

**--package**
> 查找拥有该文件的软件包

**--mode**
> 重置文件权限模式

**--uid**
> 重置文件所有者 UID

**--gid**
> 重置文件所属组 GID

**--mtime**
> 重置文件修改时间

**--quiet**
> 抑制非必要的输出

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pacrepairfile** 重置 alpm（Arch Linux 软件包管理器）所管理文件的属性。它可以将文件的权限、所有权和修改时间恢复为软件包数据库中记录的原始值。

当文件属性被意外更改或损坏时，该命令很有用。

# CAVEATS

仅对已安装软件包跟踪的文件有效。无法修复从未属于任何软件包的文件。

# HISTORY

**pacutils** 的一部分，这是一个基于 libalpm 构建的 Arch Linux 软件包管理实用工具集。

# SEE ALSO

[pacman](/man/pacman)(8), [pacrepairdb](/man/pacrepairdb)(1)
