# TAGLINE

**restore** 的别名 —— 从 dump(8) 备份中提取文件

# TLDR

该命令通常是 **restore** 的别名/符号链接。完整文档请参阅：

```tldr restore```

从 dump 文件**交互式恢复**

```recover -if [backup.dump]```

**列出 dump 归档的内容清单**

```recover -tf [backup.dump]```

**恢复整个文件系统**（到当前目录）

```recover -rf [backup.dump]```

**提取指定文件**

```recover -xvf [backup.dump] [path/to/file]```

**比较归档与文件系统**

```recover -Cf [backup.dump]```

# SYNOPSIS

**recover** [**-irtxCR**] [_options_] [_files_]

# DESCRIPTION

**recover** 是 **dump/restore** ext2/3/4 备份系统中 **restore** 工具的别名或符号链接。它读取由 `dump(8)` 生成的备份归档，并将选定的文件写回磁盘。交互模式（`-i`）提供一个微型 shell 用于浏览归档：`ls`、`cd`、`pwd`、`add`、`delete`、`extract`、`quit`。

在某些系统（尤其是 **NSR/NetWorker**）上，`recover` 指向的是完全不同的工具——Legato/EMC NetWorker 备份服务器的客户端恢复界面。下面的标志和行为描述的是 dump/restore 一脉；对于 NetWorker，请查阅该系统上的 `recover(8)`。

# PARAMETERS

**-i**
> 交互式恢复：浏览归档并挑选文件。

**-r**
> 恢复整个文件系统。须在一个新建的空文件系统中运行。

**-R**
> 恢复之前被中断的 `-r` 恢复操作。

**-t**
> 打印归档的内容清单。

**-x**
> 提取指定的文件（未给出名称则提取整个归档）。

**-C**
> 将归档内容与文件系统进行比较。

**-f** _file_
> 归档文件或设备（如 `/dev/nst0` 或 `backup.dump`）。用 `-` 表示标准输入。

**-v**
> 详细输出：处理每个文件时都打印出来。

**-N**
> 执行所有操作但不真正将文件写入磁盘（试运行）。

**-y**
> 遇到磁带错误时不询问是否中止；总是尝试继续。

**-h**
> 提取时不递归进入目录层级。

**-m**
> 按 inode 号而不是按名称提取。

**-s** _n_
> 在多文件磁带上跳到第 _n_ 个 dump 文件。

**-b** _size_
> 读取时的块大小（以 KB 为单位）。

# INTERACTIVE COMMANDS

`ls` [_dir_] — 列出条目
`cd` _dir_ — 在归档内切换目录
`pwd` — 显示当前归档目录
`add` _name_ — 标记待提取
`delete` _name_ — 取消标记
`extract` — 提取已标记的文件
`setmodes` — 为提取出的目录设置所有者/权限
`verbose` — 切换详细输出
`quit` — 退出

# CAVEATS

只能识别 `dump(8)` 创建的归档；`tar`、`cpio`、`rsync` 归档需要各自的恢复工具。完全恢复（`-r`）必须在空文件系统中运行。恢复会保留 inode 号，因此向活动目录树中恢复可能覆盖或交错写入文件。

你的系统上可能不存在 `recover`；如果缺失，请直接使用 `restore`。在 NetWorker 系统上，`recover` 是完全不同的程序。

# SEE ALSO

[dump](/man/dump)(8), [tar](/man/tar)(1), [rsync](/man/rsync)(1), [dd](/man/dd)(1), [extundelete](/man/extundelete)(1)
