# TAGLINE

移除存储池定义

# TLDR

**取消定义存储池**

```virsh pool-undefine [pool]```

# SYNOPSIS

**virsh** **pool-undefine** _pool_

# DESCRIPTION

**virsh pool-undefine** 移除存储池的 libvirt 配置，使其变为瞬态。如果存储池当前正在运行，运行时实例会继续存在直到被停止，但不再在 libvirtd 重启后保留。磁盘上的存储池内容不受影响；要销毁底层存储请使用 `virsh pool-delete`。

# PARAMETERS

_pool_
> 存储池名称或 UUID。

# CAVEATS

不会删除底层存储上的文件。运行中的存储池会变为瞬态，并在守护进程下次重启时消失。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-pool-destroy](/man/virsh-pool-destroy)(1), [virsh-pool-delete](/man/virsh-pool-delete)(1)

