# TAGLINE

网络扫描仪共享守护进程

# TLDR

**以独立守护进程模式运行 saned**

```saned -a```

**以调试模式运行**，等待连接

```saned -d```

**以详细调试运行**

```saned -d128```

**以调试模式运行**并输出 SANE_DEBUG

```saned -s```

**指定自定义的数据端口范围**

```saned -a -b```

# SYNOPSIS

**saned** [_-a_] [_-d [n]_] [_-s [n]_] [_-b_] [_-u_] [_-e_]

# PARAMETERS

**-a**
> 以独立守护进程模式运行，脱离控制台

**-d** [_n_]
> 调试模式；显式等待连接。可选数字设置详细程度（数值越大越详细）

**-s** [_n_]
> 带 SANE_DEBUG 输出的调试模式；可选详细级别

**-b**
> 与客户端协商数据端口范围

**-u**
> 绑定端口后以指定用户身份运行

**-e**
> 第一个客户端断开后退出（仅限调试模式）

# DESCRIPTION

**saned** 是 SANE 网络守护进程，允许远程客户端访问本地连接的扫描仪。它监听 TCP 端口 6566 以接收扫描请求，与本地 SANE 后端通信，并将扫描数据返回给客户端。

该守护进程可以用 **-a** 独立运行，也可由 inetd/xinetd 管理。访问控制在 **/etc/sane.d/saned.conf** 中配置，其中列出允许的主机名、IP 地址或 CIDR 子网。来自 localhost 的连接始终被允许。

客户端在其 **/etc/sane.d/net.conf** 文件中配置服务器地址，即可通过网络后端透明地访问远程扫描仪。

# CONFIGURATION

**/etc/sane.d/saned.conf**
> 访问控制文件，列出允许连接扫描仪守护进程的主机名、IP 地址或 CIDR 子网。

**/etc/sane.d/net.conf**
> 客户端配置文件，列出用于网络扫描的远程 saned 服务器。

# CAVEATS

saned 并非为暴露在不受信任的网络中而设计。务必通过 saned.conf 和防火墙规则限制访问。在访问列表中使用单个 **+** 会允许任何主机连接，存在安全风险。防火墙配置可能需要为扫描数据连接指定数据端口范围。

# HISTORY

saned 是 **SANE**（Scanner Access Now Easy）项目的一部分，该项目始于 **1996 年**，旨在为 Unix 系统提供标准化的扫描仪访问。这个网络守护进程无需专有协议即可在局域网内共享扫描仪。

# INSTALL

```apt: sudo apt install sane-utils```

```apk: sudo apk add sane-saned```

```zypper: sudo zypper install sane-saned```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scanimage](/man/scanimage)(1), [sane-find-scanner](/man/sane-find-scanner)(1)
