# TAGLINE

生成用于备份和复制的 btrfs 子卷变更流

# TLDR

将快照**发送到 stdout**

```btrfs send [/path/to/snapshot]```

**发送到文件**

```btrfs send [/path/to/snapshot] -f [backup.send]```

**增量发送**（只传输与父快照的差异）

```btrfs send -p [/path/to/parent] [/path/to/snapshot]```

**使用多个克隆源发送**

```btrfs send -c [/path/to/clone1] -c [/path/to/clone2] [/path/to/snapshot]```

在一条管道中完成**发送与接收**

```btrfs send [/path/to/snapshot] | btrfs receive [/path/to/destination]```

**通过 SSH 增量发送**

```btrfs send -p [/snapshots/old] [/snapshots/new] | ssh [user@host] btrfs receive [/backup]```

**静默模式**（不显示进度）

```btrfs send -q [/path/to/snapshot]```

# SYNOPSIS

**btrfs send** [**-v**] [**-p** _parent_] [**-c** _clone-src_] [**-f** _outfile_] _subvolume_

# DESCRIPTION

**btrfs send** 生成一个指令流，表示某个 btrfs 子卷或快照。该流可由 **btrfs receive** 接收，在另一个文件系统上重建子卷，从而实现备份和复制工作流。

send 操作作用于只读快照，生成的二进制流包含文件数据、元数据和结构信息。指定父快照时，只传输差异（增量发送），可显著减小常规备份的传输量。

流的格式具有前向兼容性，可以直接通过管道传输、保存到文件，或经由 SSH 等网络连接传送。

# PARAMETERS

**-f** _file_
> 将流写入文件而非 stdout。

**-p** _parent_
> 用于增量发送的父子卷。

**-c** _clone-src_
> 克隆源（用于去重的额外参考）。

**-v**
> 详细输出模式。

**-q**
> 静默模式（不显示进度）。

**--no-data**
> 发送时不带文件数据（仅元数据）。

**-e**
> 在子卷数据之后结束流。

**--proto** _N_
> 使用版本号为 N 的 send stream 协议。

# CAVEATS

源子卷必须是只读的。接收端必须存在父快照才能进行增量恢复。流内容不是人类可读的。中断 send/receive 可能留下不完整的子卷。恢复文件权限和所有权需要相应权限。压缩的 send 流需要协议版本 2 及以上。

# HISTORY

**btrfs send/receive** 于 Linux 内核 **3.6**（**2012 年 9 月**发布）中引入，是 btrfs 开发的一部分。其设计目标类似于 ZFS send/receive，实现高效的基于快照的备份与复制。该功能此后不断增强，增加了压缩传输（协议 v2）并提升了大文件系统场景下的性能。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs-subvolume](/man/btrfs-subvolume)(8), [btrfs](/man/btrfs)(8), [rsync](/man/rsync)(1)
