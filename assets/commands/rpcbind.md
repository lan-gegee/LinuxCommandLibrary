# TAGLINE

RPC 端口映射服务守护进程

# TLDR

**启动 rpcbind**

```sudo rpcbind```

**在前台运行**

```sudo rpcbind -f```

**调试模式**

```sudo rpcbind -d```

**检查状态**

```rpcinfo -p```

# SYNOPSIS

**rpcbind** [_options_]

# PARAMETERS

**-d**
> 调试模式。

**-f**
> 前台运行。

**-w**
> 温启动（恢复状态）。

**-l**
> 记录日志。

**-h** _host_
> 绑定到主机。

**-i** _interface_
> 绑定到网络接口。

# DESCRIPTION

**rpcbind** 是 RPC 端口映射守护进程。它将 RPC 程序号转换为网络地址，使客户端能够找到 RPC 服务。NFS 和 NIS 都依赖它。

它是较旧的 portmap 守护进程的替代品。

# EXAMPLES

```bash
# Start service
sudo systemctl start rpcbind

# Check registered programs
rpcinfo -p

# Check specific host
rpcinfo -p hostname

# List NFS services
rpcinfo -p | grep nfs

# Debug mode
sudo rpcbind -df
```

# RPC INFO

```bash
# List all registered programs
rpcinfo -p localhost

# Test specific program
rpcinfo -u localhost nfs

# Show statistics
rpcinfo -m
```

# CAVEATS

NFS 必需。存在安全隐患——请用防火墙限制访问。端口为 111 TCP/UDP。

# HISTORY

rpcbind 取代了 Sun RPC 中较旧的 **portmap**，提供了更好的安全性和 IPv6 支持。

# INSTALL

```apt: sudo apt install rpcbind```

```dnf: sudo dnf install rpcbind```

```pacman: sudo pacman -S rpcbind```

```apk: sudo apk add rpcbind```

```zypper: sudo zypper install rpcbind```

```nix: nix profile install nixpkgs#rpcbind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpcinfo](/man/rpcinfo)(8)
