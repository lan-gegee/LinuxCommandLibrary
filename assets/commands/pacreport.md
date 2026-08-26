# TAGLINE

生成关于已安装软件包与系统状态的报告

# TLDR

生成已安装软件包的**摘要**

```pacreport```

列出**无归属文件**

```pacreport --unowned-files```

列出**缺失**的软件包文件

```pacreport --missing-files```

在 /etc 中搜索**未合并的备份文件**（.pacnew、.pacsave）

```pacreport --backups```

列出某个**软件组**中未安装的软件包

```pacreport --group group_name```

# SYNOPSIS

**pacreport** [_options_]

# PARAMETERS

**--unowned-files**
> 列出不属于任何软件包的文件

**--missing-files**
> 列出本应存在却缺失的文件

**--backups**
> 查找 /etc 中未合并的备份文件

**--group** _name_
> 显示指定软件组中未安装的软件包

**--config** _path_
> 设置替代的 pacman 配置文件

**--dbpath** _path_
> 设置替代的数据库位置

**--root** _path_
> 设置替代的安装根目录

**--cachedir** _path_
> 设置替代的软件包缓存位置

# DESCRIPTION

**pacreport** 生成关于已安装软件包与系统状态的报告。默认情况下，它会输出一份摘要，包括按大小排序的软件包、可选依赖以及软件组成员关系。它还能识别无归属文件、缺失的软件包文件，以及待合并的配置文件（.pacnew/.pacsave 文件）。

该工具适用于 Arch Linux 系统上的系统维护与清理任务。

# CAVEATS

在文件数量众多的系统上扫描无归属文件可能较慢。该工具只检查通常由软件包管理的路径。**--unowned-files** 选项不会检查家目录或临时目录内部。

# HISTORY

**pacutils** 的一部分，这是一个基于 libalpm 构建的 Arch Linux 软件包管理实用工具集。

# SEE ALSO

[pacman](/man/pacman)(8), [pacdiff](/man/pacdiff)(1), [pactree](/man/pactree)(1)
