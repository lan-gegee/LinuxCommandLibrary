# TAGLINE

查找没有 AppArmor 配置文件的网络监听进程

# TLDR

**列出持有开放网络套接字的未受约束进程**（默认使用 ss）

```sudo aa-unconfined```

改用 **netstat** 代替 ss 来检测开放的网络套接字

```sudo aa-unconfined --with-netstat```

**显示 /proc 中所有**监听 TCP/UDP 端口且未受约束的进程

```sudo aa-unconfined --paranoid```

**只显示服务类进程**（拥有监听套接字的进程）

```sudo aa-unconfined --show=server```

# SYNOPSIS

**aa-unconfined** [_--paranoid_] [_--with-ss_ | _--with-netstat_]

# DESCRIPTION

**aa-unconfined** 用于识别那些监听网络套接字但没有 AppArmor 安全配置文件的进程。它通过将持有开放 TCP 或 UDP 连接的进程与内核中已加载的 AppArmor 策略进行比对来实现这一点。

该工具有助于找出可能值得添加 AppArmor 约束的服务。

# PARAMETERS

**--paranoid**
> 检查 /proc 文件系统中所有持有活动 TCP 或 UDP 端口且未受 AppArmor 约束的进程。等价于 --show=all。

**--show=**_MODE_
> 决定要显示的进程集合：all（所有进程）、network（有任何套接字的进程）、server（有监听套接字的进程）、client（有非监听套接字的进程）。

**--with-ss**
> 使用 ss(8) 工具识别网络套接字监听者（默认）。

**--with-netstat**
> 使用 netstat(8) 命令而非 ss 来发现网络套接字。在 ss 不可用时作为后备方案。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

该工具必须以 **root 权限**运行，且存在一些局限：无法可靠处理已被删除的可执行文件，可能遗漏在配置文件加载之前启动的进程，并易受竞态条件影响。它只监控 TCP 和 UDP 协议。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-status](/man/aa-status)(8), [aa-genprof](/man/aa-genprof)(8), [ss](/man/ss)(8), [netstat](/man/netstat)(8), [apparmor](/man/apparmor)(7)
