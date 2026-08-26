# TAGLINE

查询 OpenNTPD 守护进程的同步状态

# TLDR

**显示同步状态**

```ntpctl -s status```

**显示所有对等服务器**

```ntpctl -s peers```

**显示所有传感器**

```ntpctl -s sensors```

**显示全部信息**

```ntpctl -s all```

# SYNOPSIS

**ntpctl** [_-s command_]

# PARAMETERS

**-s status**
> 显示同步状态。

**-s peers**
> 显示对等服务器状态。

**-s sensors**
> 显示传感器状态。

**-s all**
> 显示全部信息。

# DESCRIPTION

**ntpctl** 查询 OpenNTPD 守护进程的同步状态，显示关于时间源和同步状态的信息。

状态视图显示时钟是否已同步、stratum 层级以及相对参考时间的偏移量。时钟已同步意味着系统时间正在被校正。

对等服务器视图列出已配置的 NTP 服务器及其状态、stratum 和偏移量，有助于识别哪些服务器可达并提供良好的时间。

传感器视图显示可能已配置的硬件时间源，例如 GPS 接收器或无线电时钟。它们提供独立于网络的本地参考时间。

该工具通过控制套接字与 ntpd 通信。守护进程必须在启用控制套接字的情况下运行，ntpctl 才能工作。

OpenNTPD 强调安全性和简单性而非功能完备性。ntpctl 也体现了这一点：只提供必要的状态信息而不提供复杂查询。

# CAVEATS

OpenNTPD 特有——不兼容 ISC ntpd。控制套接字必须在 ntpd 配置中启用。相比 ntpq 功能有限。

# HISTORY

**ntpctl** 是 **OpenNTPD** 的一部分，由 **OpenBSD** 项目于约 **2004 年**开始开发。OpenNTPD 的创建目的是作为参考 NTP 实现之外更简单、更安全的替代方案。

# INSTALL

```apt: sudo apt install openntpd```

```pacman: sudo pacman -S openntpd```

```apk: sudo apk add openntpd```

```nix: nix profile install nixpkgs#openntpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntpd](/man/ntpd)(8), [ntpq](/man/ntpq)(1), [chronyc](/man/chronyc)(1), [timedatectl](/man/timedatectl)(1)
