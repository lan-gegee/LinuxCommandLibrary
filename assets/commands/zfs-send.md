# TAGLINE

生成 ZFS 快照复制流

# TLDR

**将快照发送到文件**

```zfs send [pool/dataset@snapshot] > [backup.zfs]```

**将快照发送到远程系统**

```zfs send [pool/dataset@snap] | ssh [host] zfs recv [pool/newdataset]```

**在快照之间发送增量**

```zfs send -i [pool/data@snap1] [pool/data@snap2] | ssh [host] zfs recv [pool/data]```

**在快照之间发送全部增量**

```zfs send -I [pool/data@snap1] [pool/data@snap5] > [backup.zfs]```

**发送复制流**（包含所有后代）

```zfs send -R [pool/dataset@snapshot] > [full-backup.zfs]```

**试运行估算大小**

```zfs send -nvP [pool/dataset@snapshot]```

**发送原始加密流**

```zfs send -w [pool/encrypted@snap] > [encrypted-backup.zfs]```

**使用 receive_resume_token 恢复中断的发送**

```zfs send -t [token] | ssh [host] zfs recv [pool/data]```

# SYNOPSIS

**zfs send** [_options_] _snapshot_

**zfs send** [_options_] **-i** _snapshot1_ _snapshot2_

# PARAMETERS

**-i** _snapshot_
> 从快照生成增量流。

**-I** _snapshot_
> 生成累计增量流。

**-R**
> 生成复制流（所有后代、克隆、属性）。

**-D**
> 生成去重流。在 OpenZFS 2.1 中已弃用并被忽略。

**-L**
> 如可用则在流中生成更大的块。

**-e**
> 生成更紧凑的流。

**-c**
> 生成压缩流。

**-w**
> 发送原始加密数据（用于加密数据集）。

**-p**
> 在流中包含数据集属性。

**-b**
> 只发送来源为 received 或 local 的属性。

**-h**
> 在复制流中包含 hold。

**-n**
> 试运行，不生成流。

**-P**
> 输出关于流的详细机器可解析信息。

**-v**
> 详细输出，包括进度报告。

**-t** _token_
> 使用指定的 receive_resume_token 恢复中断的发送。

# DESCRIPTION

**zfs send** 创建 ZFS 快照的流表示形式，可以保存到文件或通过管道传给另一系统上的 **zfs receive**。这使得 ZFS 数据集的备份、复制和迁移成为可能。

完整流包含完整的快照数据。增量流（-i）只包含两个快照之间的变化，可实现高效的持续复制。复制流（-R）包括所有后代数据集及其快照。

对于加密数据集，-w 标志发送保持加密状态的原始加密数据。不带 -w 时，流在发送过程中会被解密。

流可以被压缩、去重，并通过 SSH 管道进行远程复制。

# CAVEATS

增量接收要求目标端存在基础快照。复制流会销毁发送方不存在的快照。原始加密流只能按原样接收。大型传输可能需要大量网络带宽。

# HISTORY

**zfs send** 自 ZFS 在 Solaris 10 中引入以来就是其一部分。该命令随 OpenZFS 不断发展，加入了原始加密发送、redacted 发送和可恢复传输等特性。它仍然是 ZFS 备份和复制的首要方法。

# INSTALL

```apt: sudo apt install zfs-fuse```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zfs-receive](/man/zfs-receive)(8), [zfs](/man/zfs)(8), [zpool](/man/zpool)(8)
