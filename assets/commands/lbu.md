# TAGLINE

管理无盘 Alpine Linux 系统上的 APK overlay 文件

# TLDR

**提交**更改到持久化存储

```lbu commit```

**列出**将被保存的文件

```lbu status```

显示被跟踪文件的**变更**

```lbu diff```

将文件或目录**纳入** overlay

```lbu include [path/to/file_or_directory]```

将文件从 overlay 中**排除**

```lbu exclude [path/to/file_or_directory]```

列出**手动纳入/排除**的文件

```lbu include -l```

列出**备份**（先前的 overlay）

```lbu list-backup```

**恢复**到某个备份 overlay

```lbu revert [overlay_filename.tar.gz]```

# SYNOPSIS

**lbu** _command_ [_arguments_]

# PARAMETERS

**ci**, **commit**
> 将更改保存到持久化存储

**st**, **status**
> 列出将要提交的文件

**diff**
> 显示被跟踪文件的变更

**inc**, **include** _PATH_
> 将文件/目录添加到 overlay

**ex**, **exclude** _PATH_
> 从 overlay 中移除文件/目录

**lb**, **list-backup**
> 列出可用的备份

**revert** _FILE_
> 恢复某个备份 overlay

# DESCRIPTION

**lbu**（Local Backup Utility）管理无盘 Alpine Linux 系统上的 APK overlay 文件。在无盘模式下，根文件系统运行于内存中，lbu 会将配置更改保存到持久化存储。

默认情况下，只有 /etc 被包含在 overlay 中。其他文件可以手动纳入。在使用 lbu commit 提交之前，更改不会持久化。

# CAVEATS

仅适用于 Alpine Linux 无盘安装。内存中未提交的更改会在重启后丢失。overlay 存储必须正确配置。

# HISTORY

lbu 是 Alpine Linux 无盘系统运行方案的一部分，允许在保持基础系统只读的同时，让自定义配置在重启后得以保留。

# INSTALL

```apk: sudo apk add alpine-conf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apk](/man/apk)(1), [setup-alpine](/man/setup-alpine)(8)
