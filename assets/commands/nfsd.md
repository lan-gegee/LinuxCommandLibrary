# TAGLINE

处理来自客户端的 NFS 请求

# TLDR

**启动 NFS 服务器**

```sudo systemctl start nfs-server```

**开机时启用**

```sudo systemctl enable nfs-server```

**以指定线程数启动**

```sudo rpc.nfsd [16]```

**禁用 NFS 版本 3**

```sudo rpc.nfsd -N 3```

**查看 NFS 服务器状态**

```sudo systemctl status nfs-server```

**以指定端口和 RDMA 支持启动**

```sudo rpc.nfsd -p [2049] -r```

# SYNOPSIS

**rpc.nfsd** [_options_] [_nprocs_]

# PARAMETERS

**nprocs**
> 服务器线程数量（默认：8）。

**-d**, **--debug**
> 调试模式。

**-H**, **--host** _addr_
> 指定接受 NFS 请求的主机名或地址。默认使用所有已知的网络地址。

**-p**, **--port** _port_
> 指定监听 NFS 请求的其他端口（默认：2049）。

**-r**, **--rdma** [_port_]
> 在指定端口启用 RDMA 传输（默认：20049）。

**-N**, **--no-nfs-version** _ver_
> 禁用特定的 NFS 版本（如 3、4、4.1、4.2）。

**-V**, **--nfs-version** _ver_
> 启用特定的 NFS 版本。

**-s**, **--syslog**
> 将错误消息记录到 syslog 而非 stderr。

**-t**, **--tcp**
> 监听 TCP 套接字（默认）。

**-T**, **--no-tcp**
> 禁止客户端的 TCP 连接。

**-u**, **--udp**
> 监听 UDP 套接字。

**-U**, **--no-udp**
> 禁止客户端的 UDP 连接（默认）。

**-L** _seconds_, **--lease-time** _seconds_
> 设置 NFSv4 租约时间（10–3600 秒）。

**-G** _seconds_, **--grace-time** _seconds_
> 设置 NFSv4/NLM 用于状态回收的宽限期。

**-S** _scope_, **--scope** _scope_
> 设置 NFSv4.1+ 的服务器作用域标识符。

# DESCRIPTION

**nfsd**（NFS 服务器守护进程）处理来自客户端的 NFS 请求。它实现 NFS 协议，通过网络共享文件系统。

线程数决定了可以同时处理的请求数量。

# CONFIGURATION

```
/etc/exports              - Exported filesystems
/etc/nfs.conf            - NFS configuration
/etc/default/nfs-kernel-server  # Debian
```

# EXPORTS FORMAT

```
# /etc/exports
/home       192.168.1.0/24(rw,sync,no_root_squash)
/data       *(ro,sync)
```

# CAVEATS

需要 rpcbind（仅 NFSv4 的配置除外）。防火墙必须放行 NFS 端口。NFSv4 只使用单一端口（2049）。安全性通过 /etc/exports 管理，也可选择 Kerberos 身份验证。默认的 8 个线程应根据实际负载进行调整。

# HISTORY

NFS 由 **Russel Sandberg** 领导的团队于 **1984 年**在 **Sun Microsystems** 开发，成为 Unix 的基础网络协议之一。

# SEE ALSO

[showmount](/man/showmount)(8), [rpcbind](/man/rpcbind)(8), [nfsstat](/man/nfsstat)(8)
