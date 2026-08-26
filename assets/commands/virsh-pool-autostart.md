# TAGLINE

配置存储池自启动

# TLDR

**启用存储池自启动**

```virsh pool-autostart [pool]```

**禁用存储池自启动**

```virsh pool-autostart [pool] --disable```

# SYNOPSIS

**virsh** **pool-autostart** _pool_ [_options_]

# PARAMETERS

**--disable**
> 禁用自启动。

# DESCRIPTION

**virsh pool-autostart** 配置 libvirt 存储池是否随 libvirt 守护进程自动启动。启用后，存储池会在守护进程启动时变为活动状态；禁用后则需要通过 `virsh pool-start` 手动启动。该设置会持久保存在存储池的 XML 定义中。

# CAVEATS

仅适用于持久化存储池。瞬态存储池无法标记为自启动。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-pool-start](/man/virsh-pool-start)(1), [virsh-pool-list](/man/virsh-pool-list)(1)

