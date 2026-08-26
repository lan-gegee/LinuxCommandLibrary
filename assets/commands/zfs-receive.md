# TAGLINE

接收 ZFS 快照复制流

# TLDR

**从文件接收快照**

```zfs receive [pool/dataset] < [backup.zfs]```

**从远程系统接收**

```ssh [host] zfs send [pool/data@snap] | zfs receive [pool/newdata]```

**强制回滚后接收**

```zfs receive -F [pool/dataset] < [backup.zfs]```

**使用流中的完整路径接收**

```zfs receive -d [pool] < [backup.zfs]```

**试运行以测试接收**

```zfs receive -nv [pool/dataset] < [backup.zfs]```

**接收并覆盖属性**

```zfs receive -o mountpoint=[/mnt/data] [pool/dataset] < [backup.zfs]```

**接收时排除属性**

```zfs receive -x compression [pool/dataset] < [backup.zfs]```

**恢复中断的接收**

```zfs receive -s [pool/dataset] < [backup.zfs]```

# SYNOPSIS

**zfs receive** [_options_] _filesystem_|_volume_|_snapshot_

# PARAMETERS

**-F**
> 在接收前强制回滚到最近的快照。

**-d**
> 使用发送的快照路径中除第一个元素外的所有元素。

**-e**
> 只使用发送的快照路径的最后一个元素。

**-u**
> 不挂载接收到的文件系统。

**-o** _property=value_
> 在接收的数据集上设置属性。

**-x** _property_
> 排除（继承）接收数据集上的属性。

**-s**
> 启用可恢复接收。

**-n**
> 试运行，不真正接收。

**-v**
> 详细输出。

**-h**
> 跳过与 hold 相关的错误（配合 -F）。

# DESCRIPTION

**zfs receive**（或 **zfs recv**）从标准输入提供的流创建快照。该流通常由 **zfs send** 生成。完整流会创建新数据集；增量流则更新现有数据集。

对于增量接收，目标端必须拥有基础快照。-F 标志强制回滚以便执行接收。复制流（send 的 -R）可能会销毁目标端多余的快照。

接收过程中可以用 -o 覆盖属性，或用 -x 使属性被继承。这对于在目标端设置不同的挂载点或压缩方式很有用。

-s 标志启用可恢复接收，允许中断的传输从中断处继续。

# CAVEATS

增量流要求目标端存在基础快照。强制（-F）会销毁中间快照。加密原始流必须按原样接收。属性覆盖对复制流会作用于整个子树。

# HISTORY

**zfs receive** 自 Solaris 10 起就是 ZFS 的组成部分，支撑着 ZFS 复制工作流。OpenZFS 通过可恢复接收、属性覆盖以及对加密数据集更好的处理增强了它。

# INSTALL

```apt: sudo apt install zfs-fuse```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zfs-send](/man/zfs-send)(8), [zfs](/man/zfs)(8), [zpool](/man/zpool)(8)
