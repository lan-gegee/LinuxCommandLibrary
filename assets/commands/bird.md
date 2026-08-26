# TAGLINE

动态 IP 路由守护进程

# TLDR

**以指定配置文件启动** BIRD

```bird -c [/etc/bird/bird.conf]```

**解析配置**并检查错误

```bird -p```

以前台方式**运行**并输出调试消息

```bird -d```

以指定用户在前台**运行**

```bird -f -u [bird] -g [bird]```

**以自定义控制套接字路径启动**

```bird -s [/run/bird/bird.ctl]```

# SYNOPSIS

**bird** [_options_]

# DESCRIPTION

**bird**（BIRD Internet Routing Daemon）是一个动态 IP 路由守护进程，支持 BGP、OSPF、RIP、Babel 等多种路由协议。它为类 Unix 系统上的高性能路由而设计。

该守护进程被广泛用于互联网路由，尤其受到 ISP 和数据中心的青睐。

# PARAMETERS

**-c** _file_
> 使用给定的配置文件而不是默认的 /etc/bird/bird.conf。

**-d**
> 启用输出到 stderr 的调试消息，并以前台方式运行。

**-D** _file_
> 将调试信息记录到给定文件而不是 stderr。

**-f**
> 以前台方式运行（不带调试消息）。

**-p**
> 仅解析配置文件然后退出。有效则返回零。

**-s** _socket_
> 使用给定的文件名作为控制套接字（默认：/run/bird/bird.ctl）。

**-P** _file_
> 以给定的文件名创建 PID 文件。

**-u** _user_
> 放弃特权，以给定用户身份运行而不是 root。

**-g** _group_
> 以给定的组 ID 运行。

**-l**
> 在当前工作目录中查找配置文件和控制套接字。

**-R**
> 启动后应用优雅重启恢复。

**--help**
> 显示命令行选项。

**--version**
> 显示 BIRD 版本。

# SUPPORTED PROTOCOLS

**BGP** - Border Gateway Protocol
**OSPF** - Open Shortest Path First（v2 和 v3）
**RIP** - Routing Information Protocol
**Babel** - Babel 路由协议
**BFD** - Bidirectional Forwarding Detection
**Static** - 静态路由
**Kernel** - 内核路由表同步
**Pipe** - 表间路由复制

# CONFIGURATION

**/etc/bird/bird.conf**
> 主配置文件，定义路由协议、过滤器和网络接口。

# CONTROL

使用 `birdc`（BIRD 客户端）与运行中的守护进程交互：
```bash
birdc show protocols
birdc show route
birdc configure
```

# CAVEATS

高级场景下配置较为复杂。需要 root 或网络管理权限（配合 **-u** 运行时使用 CAP_NET_ADMIN）。配置错误可能扰乱路由。在 BIRD 1.x 中，IPv4 与 IPv6 使用独立的守护进程（bird/bird6）；BIRD 2.x 已将它们统一为单一守护进程。

# HISTORY

**BIRD** 自 **1998 年**起由布拉格查理大学开发，逐渐成为 Unix 系统上流行的开源路由守护进程。

# INSTALL

```apt: sudo apt install bird2```

```dnf: sudo dnf install bird```

```pacman: sudo pacman -S bird```

```apk: sudo apk add bird```

```zypper: sudo zypper install bird```

```nix: nix profile install nixpkgs#bird2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[birdc](/man/birdc)(8), [bgpd](/man/bgpd)(8), [ip](/man/ip)(8), [route](/man/route)(8)
