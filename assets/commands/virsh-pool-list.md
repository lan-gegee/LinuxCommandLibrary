# TAGLINE

列出 libvirt 存储池

# TLDR

**列出活动存储池**

```virsh pool-list```

**列出所有存储池（包括非活动池）**

```virsh pool-list --all```

**仅列出非活动存储池**

```virsh pool-list --inactive```

**列出所有存储池及容量详情**

```virsh pool-list --all --details```

# SYNOPSIS

**virsh** **pool-list** [_options_]

# PARAMETERS

**--all**
> 同时列出活动和非活动存储池。

**--inactive**
> 仅列出非活动存储池。

**--details**
> 显示详细信息，包括容量、已分配空间和可用空间。

**--uuid**
> 显示存储池 UUID。

**--name**
> 仅显示存储池名称。

**--autostart**
> 显示自启动状态。

# DESCRIPTION

**virsh pool-list** 显示由 libvirt 管理的存储池。默认只显示活动存储池。输出包括存储池名称、状态和自启动配置。使用 --details 可查看容量与分配信息。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-pool-info](/man/virsh-pool-info)(1), [virsh-pool-define-as](/man/virsh-pool-define-as)(1), [virsh-pool-start](/man/virsh-pool-start)(1), [virsh-pool-destroy](/man/virsh-pool-destroy)(1)

