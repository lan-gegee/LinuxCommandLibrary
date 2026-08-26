# TAGLINE

判断远程 Windows 系统的操作系统架构

# TLDR

**检测远程 Windows 系统**的架构

```impacket-getarch -target [192.168.1.100]```

从文件中**检查多个目标**的架构

```impacket-getarch -targets [targets.txt]```

使用自定义超时**检测架构**

```impacket-getarch -target [192.168.1.100] -timeout [5]```

带调试输出**检测架构**

```impacket-getarch -target [192.168.1.100] -debug```

# SYNOPSIS

**impacket-getarch** [_-h_] [_-target IP_] [_-targets FILE_] [_-timeout SECONDS_] [_-debug_] [_-ts_]

# PARAMETERS

**-target** _IP_
> 要探测的目标系统 IP 地址

**-targets** _FILE_
> 包含目标 IP 地址列表的文件（每行一个）

**-timeout** _SECONDS_
> 连接目标时的套接字超时时间（默认：2）

**-debug**
> 启用调试输出

**-ts**
> 为每条日志输出添加时间戳

# DESCRIPTION

**impacket-getarch** 是一款侦察工具，用于判断远程 Windows 系统运行的是 32 位还是 64 位操作系统。它的工作原理是连接目标的 SMB 服务，并分析 32 位和 64 位 Windows 在响应某些 SMB 请求时的差异。这一技术由微软记录在案，且无需身份验证。

在渗透测试中准备特定架构的载荷或漏洞利用时，这些信息非常有价值。

# CAVEATS

需要能访问目标的 SMB 端口（通常为 445）。结果的可靠性取决于 SMB 可访问且未被防火墙拦截。对非 Windows 系统或运行 Samba 的系统无效。

# HISTORY

属于 **Impacket** 库，最初由 SecureAuth 开发，现由 Fortra 维护。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket-psexec](/man/impacket-psexec)(1), [impacket-smbclient](/man/impacket-smbclient)(1), [nmap](/man/nmap)(1), [smbclient](/man/smbclient)(1)
