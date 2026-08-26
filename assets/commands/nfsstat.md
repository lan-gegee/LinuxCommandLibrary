# TAGLINE

显示 NFS 活动的统计信息

# TLDR

**显示所有 NFS 统计信息**

```nfsstat```

**显示服务端统计信息**

```nfsstat -s```

**显示客户端统计信息**

```nfsstat -c```

**显示指定 NFS 版本**

```nfsstat -3```

**显示 RPC 统计信息**

```nfsstat -r```

**显示已挂载的文件系统**

```nfsstat -m```

**统计计数清零**

```sudo nfsstat -z```

# SYNOPSIS

**nfsstat** [_options_]

# PARAMETERS

**-s**, **--server**
> 仅显示服务端统计信息。

**-c**, **--client**
> 仅显示客户端统计信息。

**-n**, **--nfs**
> 仅显示 NFS 统计信息。

**-r**, **--rpc**
> 仅显示 RPC 统计信息。

**-2**, **-3**, **-4**
> NFS 版本（v2、v3、v4）。

**-m**, **--mounts**
> 显示挂载信息。

**-z**, **--zero**
> 将统计计数清零。

**-l**, **--list**
> 以列表格式打印统计信息。

**-o**, **--since**
> 显示自上次执行 nfsstat -z 重置以来的统计信息。

**-S**, **--sort** _field_
> 按字段对 NFS 统计信息排序。

# DESCRIPTION

**nfsstat** 显示 NFS（网络文件系统）活动的统计信息。它展示客户端和服务端操作的 RPC 与 NFS 统计数据。

统计内容包括操作次数、错误以及缓存性能。

# OUTPUT SECTIONS

```
Server RPC stats - Server RPC activity
Client RPC stats - Client RPC activity
Server NFS stats - NFS operations served
Client NFS stats - NFS operations made
```

# EXAMPLE OUTPUT

```
Server nfs v3:
null         getattr      setattr      lookup
1000         50000        1000         25000
```

# CAVEATS

重启后统计数据会清零。需要 NFS 内核模块。某些选项可能需要 root 权限。

# HISTORY

nfsstat 自 **20 世纪 80 年代** Sun Microsystems 的早期实现起就是 NFS 工具的组成部分。

# INSTALL

```apt: sudo apt install nfs-common```

```dnf: sudo dnf install nfs-utils```

```pacman: sudo pacman -S nfs-utils```

```apk: sudo apk add nfs-utils```

```nix: nix profile install nixpkgs#nfs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nfsd](/man/nfsd)(8), [showmount](/man/showmount)(8), [rpcinfo](/man/rpcinfo)(8)
