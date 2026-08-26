# TAGLINE

查询 RPC 服务注册信息

# TLDR

**显示 localhost 上所有 RPC 服务的完整表格**

```rpcinfo```

**探测 portmapper** 并列出所有已注册的程序

```rpcinfo -p [hostname]```

**显示 RPC 服务的简明表格**

```rpcinfo -s [hostname]```

**显示 rpcbind 统计信息**

```rpcinfo -m```

**列出远程主机上特定服务和版本的条目**

```rpcinfo -l [hostname] [mountd] [2]```

**通过 TCP 检查某项服务是否可用**

```rpcinfo -t [hostname] [nfs]```

**删除某个服务版本的注册**（需要 root）

```rpcinfo -d [mountd] [1]```

# SYNOPSIS

**rpcinfo** [_options_] [_host_]

# PARAMETERS

**-p** _host_
> 探测主机上的 portmapper，并列出所有已注册的 RPC 程序。

**-s** _host_
> 显示所有已注册服务的简明表格。

**-m**
> 显示 rpcbind 操作统计信息。

**-l** _host_ _program_ _version_
> 列出匹配给定程序和版本的所有条目。

**-t** _host_ _program_ [_version_]
> 通过 TCP 使用针对过程 0 的 RPC 调用来探测服务。

**-u** _host_ _program_ [_version_]
> 通过 UDP 使用针对过程 0 的 RPC 调用来探测服务。

**-b** _program_ _version_
> 发起 RPC 广播并报告所有响应的主机。

**-d** _program_ _version_ [_transport_]
> 删除指定程序和版本的注册。若指定了传输协议，则仅在该传输协议上注销；否则在所有传输协议上注销（仅限 root）。

**-a** _serv_address_ **-T** _transport_ _program_ [_version_]
> 在指定传输协议上，按给定的通用地址 ping 指定程序的过程 0。

**-T** _transport_
> 指定要使用的传输协议（例如 tcp、udp）。

**-n** _portnum_
> 在 -t 和 -u 探测中使用 portnum 而非由 portmapper 分配的端口。

# DESCRIPTION

**rpcinfo** 查询 RPC 服务器并报告已注册的服务。它主要用于诊断 RPC 连接问题，以及查看 NFS、mountd 和其他基于 RPC 的可用网络服务。

该工具提供已注册 RPC 服务的程序号、版本、协议和端口等信息。它可以探测特定服务以检查其可用性、通过广播发现网络中的服务，还可以管理服务注册。

# CAVEATS

要求目标主机上正在运行 rpcbind。**-d** 选项需要 root 权限。**-b** 广播选项需要网络广播支持。

# HISTORY

标准 Unix 网络工具的组成部分，用于 RPC 服务管理。是 NFS 故障排查和配置的必备工具。

# INSTALL

```apt: sudo apt install rpcbind```

```dnf: sudo dnf install rpcbind```

```pacman: sudo pacman -S rpcbind```

```apk: sudo apk add rpcbind```

```zypper: sudo zypper install rpcbind```

```nix: nix profile install nixpkgs#rpcbind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpcbind](/man/rpcbind)(8), [nfsstat](/man/nfsstat)(8), [showmount](/man/showmount)(8)
