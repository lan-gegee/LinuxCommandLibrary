# TAGLINE

运行 PPPoE 接入集中器服务器

# TLDR

**启动 PPPoE 服务器**

```pppoe-server -I [eth0]```

**指定本地 IP 和起始远程 IP**（最多分配 N 个连续地址）

```pppoe-server -I [eth0] -L [10.0.0.1] -R [10.0.0.100] -N [100]```

**以特定服务名运行**

```pppoe-server -I [eth0] -S [myservice]```

# SYNOPSIS

**pppoe-server** [_options_]

# PARAMETERS

**-I** _INTERFACE_
> 要监听的以太网接口。可重复使用以服务多个接口。

**-L** _IP_
> 本地（服务器侧）IP 地址（默认 **10.0.0.1**）。

**-R** _IP_
> 远程 IP 地址池的起始地址（默认 **10.67.15.1**）；每个会话依次获得下一个地址。

**-p** _FILE_
> 从文本文件读取远程 IP 地址池（每行一个地址）。

**-S** _NAME_
> 对外通告的服务名。可重复使用以通告多个服务。

**-C** _AC_NAME_
> 在 PADO 应答中通告的接入集中器名称（默认：主机名）。

**-N** _NUM_
> 最大并发会话数（默认 **64**）。

**-x** _N_
> 限制来自单个对端 MAC 的并发会话数。

**-O** _FILE_
> 每个派生的会话所使用的 **pppd** 选项文件路径。

**-T** _SECONDS_
> 传递给 **pppoe** 的空闲超时时间。

**-m** _MSS_
> 将协商的 TCP MSS 钳制为 _MSS_。

**-D**
> 将 IP 地址分配委托给 **pppd**（不从本地地址池分配）。

**-k**
> 使用内核内建 PPPoE 驱动（Linux 2.4+）。

**-F**
> 以前台方式运行而不守护进程化。

**-X** _PIDFILE_
> 将守护进程 PID 写入 _PIDFILE_ 并加锁。

**-q** _PATH_
> **pppd** 二进制文件的路径。

**-Q** _PATH_
> 用户空间 **pppoe** 二进制文件的路径。

**-u**
> 以 **unit** 选项调用 **pppd**，获得可预测的接口命名。

**-i**
> 当没有剩余会话槽位时静默丢弃 PADI 广播。

**-r**
> 随机化 PPPoE 会话 ID。

**-h**
> 打印用法并退出。

# DESCRIPTION

**pppoe-server** 实现了一个 PPPoE 接入集中器，在指定的以太网接口上接受传入的 PPPoE 客户端（PADI/PADR）帧。对于每个被接受的会话，它会派生一个 **pppd** 实例并连接到用户空间 **pppoe** 插件（或使用 **-k** 时的内核驱动），除非用 **-D** 将地址分配委托给 **pppd**，否则会从本地地址池分配一个远程 IP。

典型部署是将 **pppoe-server** 作为小型实验性 DSL/PPPoE 环境的一部分；ISP 更常见的是通过 **pppd** 的 **radius** 插件将其用作基于 RADIUS 的 AAA 体系的前端。

# CAVEATS

**pppoe-server** 使用的以太网接口通常必须在不配置 IP 的情况下启用，因为 PPPoE 工作在第 2 层。若要实现真正的认证，请在 **pppd** 中配合 RADIUS 插件使用；内置的地址池分配仅适用于简单/实验环境。除非提高上限，默认的会话数上限（**-N 64**）是 **rp-pppoe** 每个接口的绝对最大值。

# HISTORY

**pppoe-server** 是 **Roaring Penguin Software** 的 **rp-pppoe**（最初由 **Dianne Skoll** 编写）的一部分，是 Linux 和 \*BSD 上标准的用户空间 PPPoE 实现。

# INSTALL

```apt: sudo apt install pppoe```

```dnf: sudo dnf install rp-pppoe```

```pacman: sudo pacman -S rp-pppoe```

```apk: sudo apk add rp-pppoe```

```zypper: sudo zypper install rp-pppoe```

```nix: nix profile install nixpkgs#rp-pppoe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppoe](/man/pppoe)(8), [pppoe-relay](/man/pppoe-relay)(8), [pppd](/man/pppd)(8)
