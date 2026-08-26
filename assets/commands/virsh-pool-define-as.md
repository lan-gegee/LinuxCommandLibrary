# TAGLINE

定义新的 libvirt 存储池

# TLDR

**定义目录存储池**

```virsh pool-define-as [name] dir --target [/path/to/pool]```

**定义 LVM 存储池**

```virsh pool-define-as [name] logical --source-name [vgname] --target [/dev/vgname]```

**定义 NFS 存储池**

```virsh pool-define-as [name] netfs --source-host [server] --source-path [/export] --target [/mnt]```

# SYNOPSIS

**virsh** **pool-define-as** _name_ _type_ [_options_]

# PARAMETERS

**dir**
> 目录存储池类型。

**logical**
> LVM 卷组。

**netfs**
> 网络文件系统。

**--target** _path_
> 挂载/目标路径。

**--source-path** _path_
> 源路径。

**--source-host** _host_
> 源主机名。

**--source-name** _name_
> 源名称（VG 名称）。

# DESCRIPTION

**virsh pool-define-as** 根据参数定义一个新的存储池。只创建存储池配置而不启动它。支持目录、LVM、NFS、iSCSI 等多种存储池类型。

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-pool-build](/man/virsh-pool-build)(1), [virsh-pool-start](/man/virsh-pool-start)(1)

