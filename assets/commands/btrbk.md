# TAGLINE

btrfs 快照与子卷备份工具

# TLDR

打印子卷和快照的**统计**信息

```sudo btrbk stats```

**列出**已配置的子卷和快照

```sudo btrbk list```

以**试运行（dry run）**方式打印将要执行的操作

```sudo btrbk -v dryrun```

**执行备份**流程并显示进度

```sudo btrbk --progress -v run```

仅为已配置的子卷创建**快照**

```sudo btrbk snapshot```

**续传**未完成的备份

```sudo btrbk resume```

使用指定的**配置**文件

```sudo btrbk -c [/path/to/btrbk.conf] run```

# SYNOPSIS

**btrbk** [_options_] _command_ [_filter_]

# DESCRIPTION

**btrbk** 是一个面向 btrfs 文件系统的备份工具，用于创建和管理快照及远程备份。它利用 btrfs send/receive 实现高效的增量备份，并支持复杂的保留策略。

配置定义在 **/etc/btrbk/btrbk.conf** 中，指定源子卷、快照位置以及备份目标，包括通过 SSH 访问的远程主机。

# SUBCOMMANDS

**run**
> 创建快照并执行备份流程

**snapshot**
> 仅创建快照（不做备份）

**resume**
> 续传未完成的备份

**dryrun**
> 只显示将要执行的操作，不实际修改

**stats**
> 显示统计信息

**list**
> 列出已配置的项目

**prune**
> 按保留策略删除过期的备份和快照

**clean**
> 删除不完整（损坏）的备份

**archive** _source_ _target_
> 将备份整合到单个目标目录

# PARAMETERS

**-v**, **--verbose**
> 增加详细输出

**-q**, **--quiet**
> 抑制非错误输出

**--progress**
> 在 send/receive 传输期间显示进度

**-n**, **--dry-run**
> 与 dryrun 命令相同

**-c** _file_
> 使用其他配置文件

**-p**, **--preserve**
> 保留所有快照和备份（不清理）

**-t**, **--table**
> 以表格形式打印输出

**-l**, **--loglevel** _level_
> 设置日志详细程度

**-h**, **--help**
> 打印用法概要和命令列表

# CONFIGURATION

**/etc/btrbk/btrbk.conf**
> 主配置文件，定义源子卷、快照位置、备份目标和保留策略。

# CAVEATS

仅适用于 btrfs 文件系统。远程备份需要 SSH 访问权限，且远程主机上也要有 btrfs。保留策略应先用 dryrun 测试。

# INSTALL

```dnf: sudo dnf install btrbk```

```pacman: sudo pacman -S btrbk```

```apk: sudo apk add btrbk```

```nix: nix profile install nixpkgs#btrbk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-send](/man/btrfs-send)(8), [snapper](/man/snapper)(8)
