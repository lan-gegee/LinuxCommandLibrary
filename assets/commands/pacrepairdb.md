# TAGLINE

修复 libalpm 数据库中损坏的数据库条目

# TLDR

对指定软件包执行**基础修复**

```pacrepairdb package_name```

**不进行解包**，仅更新数据库条目

```pacrepairdb package_name --dbonly```

**预览**将被修复的软件包，而不做任何更改

```pacrepairdb package_name --print-only```

显示额外的**进度和调试**信息

```pacrepairdb package_name --verbose```

显示**帮助**

```pacrepairdb --help```

# SYNOPSIS

**pacrepairdb** [_options_] _package(s)_

# PARAMETERS

**--dbonly**
> 仅更新数据库条目，不提取或移除软件包

**--print-only**
> 只显示将要执行的操作，不做任何更改

**--verbose**
> 显示额外的进度和调试信息

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pacrepairdb** 修复 libalpm 数据库中损坏的数据库条目。它可以修复软件包元数据、从缓存重新安装软件包，并恢复数据库一致性，而无需完整重装软件包。

当软件包数据库条目因事务中断或文件系统问题而损坏时，该工具非常有用。

# CAVEATS

要进行完整修复，相关软件包必须存在于缓存中。如果只需要修正数据库元数据，请使用 --dbonly。

# HISTORY

**pacutils** 的一部分，这是一个基于 libalpm 构建的 Arch Linux 软件包管理实用工具集。

# SEE ALSO

[pacman](/man/pacman)(8), [pacrepairfile](/man/pacrepairfile)(1)
