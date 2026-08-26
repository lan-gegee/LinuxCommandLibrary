# TAGLINE

重放已捕获的网络流量

# TLDR

**重放 pcap**

```tcpreplay -i [eth0] [capture.pcap]```

**以指定速度重放**

```tcpreplay -i [eth0] -M [100] [capture.pcap]```

**循环重放**

```tcpreplay -i [eth0] --loop [10] [capture.pcap]```

**以最高速度重放**

```tcpreplay -i [eth0] --topspeed [capture.pcap]```

**倍速重放**

```tcpreplay -i [eth0] -x [2.0] [capture.pcap]```

# SYNOPSIS

**tcpreplay** [_-i interface_] [_-M mbps_] [_--loop n_] [_options_] _pcap_

# PARAMETERS

**-i** _IFACE_
> 输出接口。

**-M** _MBPS_
> 以 Mbps 表示的速率。

**-x** _MULT_
> 速度倍数。

**--loop** _N_
> 循环次数。

**--topspeed**
> 最高速度。

**-K**
> 预加载到内存。

# DESCRIPTION

**tcpreplay** 将先前从 pcap 文件捕获的网络流量重新发回到网络中。它读取 tcpdump 或 Wireshark 等工具生成的抓包文件，并以受控速率通过指定的网络接口发送。

该工具提供灵活的速度控制：流量可以按原始记录速度、固定 Mbps 速率、速度倍数或 **--topspeed** 的最大线速重放。**--loop** 选项可将抓包文件重复多次，**-K** 则把整个文件预加载到内存以保证高速重放的稳定性。

常见用例包括测试防火墙和 IDS/IPS 等网络设备、对网络基础设施做压力测试、复现网络问题以便调试，以及在真实流量条件下对网络应用进行基准测试。

# CAVEATS

原始套接字访问需要 root 权限。在生产网络上重放流量可能造成干扰。**-i** 指定的接口必须处于启用状态。若要在重放前编辑数据包，请使用 **tcprewrite**。

# HISTORY

**tcpreplay** 为重放已捕获的网络流量而创建，用于测试网络设备和应用程序。

# INSTALL

```apt: sudo apt install tcpreplay```

```dnf: sudo dnf install tcpreplay```

```pacman: sudo pacman -S tcpreplay```

```apk: sudo apk add tcpreplay```

```zypper: sudo zypper install tcpreplay```

```brew: brew install tcpreplay```

```nix: nix profile install nixpkgs#tcpreplay```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [tcprewrite](/man/tcprewrite)(1)
