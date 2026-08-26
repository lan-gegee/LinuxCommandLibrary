# TAGLINE

停止运行中的存储池

# TLDR

**按名称停止运行中的存储池**

```virsh pool-destroy [pool]```

# SYNOPSIS

**virsh** **pool-destroy** _pool_

# DESCRIPTION

**virsh pool-destroy** 停止（停用）一个运行中的存储池。尽管名字如此，它并不会删除存储池的数据或持久化配置。存储池必须处于活动状态此命令才能成功。停止存储池后，可用 **pool-start** 重新启动。要移除配置，请使用 **pool-undefine**。要删除底层存储数据，请使用 **pool-delete**（必须先停止存储池）。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-pool-start](/man/virsh-pool-start)(1), [virsh-pool-delete](/man/virsh-pool-delete)(1), [virsh-pool-undefine](/man/virsh-pool-undefine)(1)

