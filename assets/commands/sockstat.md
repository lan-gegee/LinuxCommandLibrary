# TAGLINE

列出打开的 Internet 和 Unix 域套接字

# TLDR

显示**所有套接字**（IPv4 和 IPv6，监听和已连接）

```sockstat```

显示特定端口上的 **IPv4 监听**套接字

```sockstat -4 -l -p [port1,port2]```

显示**已连接**和 **Unix** 套接字

```sockstat -cu```

按**进程** ID 或名称过滤

```sockstat -P [pid|process]```

按**用户**过滤

```sockstat -U [uid|user]```

按**组**过滤

```sockstat -G [gid|group]```

按**协议**过滤

```sockstat -R [tcp|udp|raw|unix]```

# SYNOPSIS

**sockstat** [**-46clouh**] [**-p** _ports_] [**-P** _pid|process_] [**-U** _uid|user_] [**-G** _gid|group_] [**-R** _protocol_]

# PARAMETERS

**-4**
> 只显示 IPv4 套接字

**-6**
> 只显示 IPv6 套接字

**-u**
> 包含 Unix 域套接字

**-c**
> 只显示已连接的套接字

**-l**
> 只显示监听中的套接字

**-o**
> 各过滤器之间用 OR 逻辑而非 AND

**-p** _ports_
> 按端口过滤（逗号分隔或范围如 80-443）

**-P** _pid|process_
> 按进程 ID 或进程名过滤

**-U** _uid|user_
> 按用户 ID 或用户名过滤

**-G** _gid|group_
> 按组 ID 或组名过滤

**-R** _protocol_
> 按协议过滤（tcp、udp、raw、unix）

**-h**
> 显示帮助

# DESCRIPTION

**sockstat** 列出系统上打开的 Internet 和 Unix 域套接字。它显示哪些进程打开了哪些套接字的信息，对网络排障和安全审计很有用。

对于 Internet 套接字，输出包括 USER、COMMAND、PID、FD（文件描述符）、PROTO（协议）、LOCAL ADDRESS 和 FOREIGN ADDRESS。多个过滤器可以组合使用以缩小结果范围。

# CAVEATS

查看所有套接字需要相应的权限；root 可以看到全部。在 Linux 上，类似功能由 **ss** 或 **netstat** 提供。sockstat 命令起源于 BSD 系统，并非所有 Linux 发行版都有提供。

# HISTORY

**sockstat** 起源于 **FreeBSD** 及其他 BSD 系统，作为解析 /proc 或使用 netstat 的友好替代方案而出现。Linux 版本提供了类似功能。该工具自 **20 世纪 90 年代末**以来一直是 BSD 的一部分，后来作为各种实用工具包的一部分被移植到 Linux。

# INSTALL

```apt: sudo apt install sockstat```

```nix: nix profile install nixpkgs#sockstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss](/man/ss)(8), [netstat](/man/netstat)(8), [lsof](/man/lsof)(8), [fuser](/man/fuser)(1)
