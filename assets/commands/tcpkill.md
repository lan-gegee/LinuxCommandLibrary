# TAGLINE

用 RST 包终止 TCP 连接

# TLDR

**按**接口、主机和端口**切断**连接

```tcpkill -i [eth1] host [192.95.4.27] and port [2266]```

# SYNOPSIS

**tcpkill** [_OPTIONS_] _EXPRESSION_

# PARAMETERS

**-i** _INTERFACE_
> 使用的网络接口

**-1** 到 **-9**
> 激进程度（默认为 3）

# DESCRIPTION

**tcpkill** 通过注入 TCP RST（重置）数据包来终止进行中的 TCP 连接。它监视匹配指定过滤表达式的流量，并向两端发送伪造的重置包。

过滤表达式使用 libpcap 语法，可按主机、端口、网络或任意组合进行过滤。

# CAVEATS

需要 root 权限。属于 dsniff 软件包。只对网络上可见的未加密连接有效。对活跃连接可能需要多次尝试。请负责任地使用——未经授权的使用可能违法。

# HISTORY

**tcpkill** 是 **Dug Song** 创建的 **dsniff** 网络审计工具套件的一部分，用于安全测试和紧急连接终止。

# INSTALL

```apt: sudo apt install dsniff```

```dnf: sudo dnf install dsniff```

```pacman: sudo pacman -S dsniff```

```nix: nix profile install nixpkgs#dsniff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(8), [dsniff](/man/dsniff)(8)
