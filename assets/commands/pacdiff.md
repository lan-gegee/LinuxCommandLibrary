# TAGLINE

管理 pacman 在软件包升级期间产生的配置文件冲突

# TLDR

在交互模式下**审查需要处理的文件**

```pacdiff```

使用 **sudo 和 sudoedit** 移除与合并文件

```pacdiff -s```

审查文件，覆盖时为原文件创建 **.bak 备份**

```pacdiff -s -b```

使用**指定的编辑器**查看和合并配置文件

```DIFFPROG=[editor] pacdiff```

用 **locate** 代替 pacman 数据库扫描文件

```pacdiff -l```

# SYNOPSIS

**pacdiff** [_options_]

# PARAMETERS

**-s**, **--sudo**
> 使用 sudo 和 sudoedit 移除并编辑文件

**-b**, **--backup**
> 覆盖时创建 .bak 备份

**-l**, **--locate**
> 使用 locate 而不是 pacman 数据库查找文件

**-f**, **--find**
> 使用 find 命令查找文件

**-p**, **--pacmandb**
> 使用 pacman 数据库扫描（默认）

**-o**, **--output**
> 将文件打印到标准输出而不是交互模式

**-3**, **--threeway**
> 以三方对比方式查看差异（原始版、新版、当前版）

**-m**, **--merge**
> 执行三方合并

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pacdiff** 管理 pacman 在软件包升级期间产生的配置文件冲突。当 pacman 遇到被修改过的配置文件时，会将新版本保存为 **.pacnew** 扩展名，将原版本保存为 **.pacorig** 或 **.pacsave**，需要人工审查。

该工具逐个交互式地呈现这些文件，让用户可以查看差异、编辑文件、用新版本覆盖或删除冲突文件。默认使用 **vim -d** 查看差异，但也尊重 **DIFFPROG** 环境变量以使用自定义 diff 工具。

# CAVEATS

交互模式需要对每个文件投入人工处理。默认的 diff 查看器（vim -d）要求安装 vim。使用 **-l**（locate）需要已更新的 mlocate 数据库。覆盖系统配置文件之前务必仔细审查更改。

# HISTORY

属于 **pacman-contrib**，这是一组 Arch Linux 维护脚本。它解决滚动发行版上最常见的维护任务之一——频繁的更新可能与用户自定义的配置文件发生冲突。

# SEE ALSO

[pacman](/man/pacman)(8), [paccache](/man/paccache)(8), [vimdiff](/man/vimdiff)(1)
