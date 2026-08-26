# TAGLINE

初始化 libvirt 存储池

# TLDR

**构建存储池**

```virsh pool-build [pool]```

**以覆盖方式构建**

```virsh pool-build [pool] --overwrite```

# SYNOPSIS

**virsh** **pool-build** _pool_ [_options_]

# PARAMETERS

**--overwrite**
> 覆盖已有数据。

**--no-overwrite**
> 存在数据时失败。

# DESCRIPTION

**virsh pool-build** 初始化之前已定义的 libvirt 存储池。具体操作取决于存储池类型：对于基于目录的存储池，它会创建目录；对于磁盘、LVM 或逻辑存储池，它会格式化底层设备；对于 NFS 存储池，它可能会设置挂载点。构建完成后，可以用 **virsh pool-start** 启动存储池。

对某些存储池类型（例如目录已存在的 **dir**），build 步骤是无操作或不必要的，但无害。**--overwrite** 选项允许重新初始化，会销毁目标上的现有数据，因此请谨慎使用。

# CAVEATS

**--overwrite** 标志会擦除目标存储上的现有数据。构建前必须已定义存储池（通过 **virsh pool-define** 或 **pool-define-as**）。并非所有存储池类型都需要或支持构建。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-pool-define-as](/man/virsh-pool-define-as)(1), [virsh-pool-start](/man/virsh-pool-start)(1)

