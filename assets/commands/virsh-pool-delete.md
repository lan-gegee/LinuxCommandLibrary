# TAGLINE

删除存储池数据

# TLDR

**删除池存储**

```virsh pool-delete [pool]```

# SYNOPSIS

**virsh** **pool-delete** _pool_

# DESCRIPTION

**virsh pool-delete** 销毁存储池的底层存储。移除存储池中的所有数据。必须先停止存储池。在运行 pool-undefine 之前配置仍然保留。

# CAVEATS

这会永久销毁存储池中的所有数据。无法撤销。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-pool-undefine](/man/virsh-pool-undefine)(1)

