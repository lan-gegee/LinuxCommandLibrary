# TAGLINE

查询 NFS 服务器的导出信息

# TLDR

**显示导出列表**

```showmount -e [server]```

**显示已挂载的目录**

```showmount -d [server]```

**显示所有挂载**

```showmount -a [server]```

**显示本机导出**

```showmount -e```

**不输出表头**

```showmount --no-headers -e [server]```

# SYNOPSIS

**showmount** [_-e_] [_-d_] [_-a_] [_options_] [_host_]

# PARAMETERS

**-e**, **--exports**
> 显示导出列表。

**-d**, **--directories**
> 显示已挂载的目录。

**-a**, **--all**
> 显示所有挂载点。

**--no-headers**
> 不显示表头。

**--version**
> 显示版本。

# DESCRIPTION

**showmount** 查询 NFS 服务器的挂载守护进程，显示导出文件系统和活动挂载的相关信息。**-e** 选项列出所有导出目录及其访问权限和允许访问的客户端主机，这是发现可用 NFS 共享时最常见的用法。

**-d** 选项只显示客户端当前挂载的目录，而 **-a** 以 host:directory 对的形式显示所有活动挂载点，可用于审计 NFS 使用情况和识别已连接的客户端。不带主机参数时，命令查询本机的 NFS 服务器。

# CAVEATS

需要 rpcbind/portmapper。防火墙可能阻止查询。NFSv4 可能不会报告所有信息。

# HISTORY

**showmount** 属于 NFS 工具集，可追溯至最早的 NFS 实现。它为 NFS 管理提供重要信息。

# INSTALL

```apt: sudo apt install nfs-common```

```dnf: sudo dnf install nfs-utils```

```pacman: sudo pacman -S nfs-utils```

```apk: sudo apk add nfs-utils```

```nix: nix profile install nixpkgs#nfs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [exports](/man/exports)(5), [nfsd](/man/nfsd)(8)
