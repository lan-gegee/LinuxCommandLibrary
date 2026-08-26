# TAGLINE

管理块设备上的持久预留

# TLDR

**注册**预留

```blkpr -c register -k reservation_key /dev/sda```

**保留**独占访问权

```blkpr -c reserve -k key -t exclusive-access /dev/sda```

**抢占**已有预留

```blkpr -c preempt -K old_key -k new_key -t write-exclusive /dev/sda```

**释放**预留

```blkpr -c release -k key -t type /dev/sda```

**清除**所有预留

```blkpr -c clear -k key /dev/sda```

# SYNOPSIS

**blkpr** [_OPTIONS_] _device_

# DESCRIPTION

**blkpr** 管理支持 SCSI 持久预留（Persistent Reservations）的块设备上的持久预留。它允许通过注册、保留、释放、抢占和清除预留来控制共享存储的访问。

# PARAMETERS

**-c, --command** _cmd_
> 命令：register、reserve、release、preempt、clear

**-k, --key** _key_
> 预留密钥

**-K, --oldkey** _key_
> preempt 操作使用的旧密钥

**-t, --type** _type_
> 预留类型（exclusive-access、write-exclusive 等）

# CAVEATS

需要支持 SCSI 持久预留的设备。用于集群存储环境中协调访问。密钥通常为 64 位值。

# HISTORY

**blkpr** 是 **util-linux** 的一部分，提供块设备持久预留管理功能。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blockdev](/man/blockdev)(8)
