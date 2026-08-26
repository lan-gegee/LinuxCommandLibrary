# TAGLINE

编辑 pcap 数据包头部

# TLDR

**重写源和目标 MAC 地址**

```tcprewrite --enet-smac=[00:11:22:33:44:55] --enet-dmac=[66:77:88:99:aa:bb] -i [input.pcap] -o [output.pcap]```

**重写 IP 地址**

```tcprewrite --srcipmap=[192.168.1.0/24:10.0.0.0/24] --dstipmap=[192.168.2.0/24:10.0.1.0/24] -i [input.pcap] -o [output.pcap]```

**重写端口号**

```tcprewrite --portmap=[80:8080,443:8443] -i [input.pcap] -o [output.pcap]```

**随机化 IP 地址**

```tcprewrite --seed=[42] --pnat=[192.168.0.0/16:10.0.0.0/8] -i [input.pcap] -o [output.pcap]```

**编辑后修复校验和**

```tcprewrite --fixcsum -i [input.pcap] -o [output.pcap]```

**更改 MTU 并截断**

```tcprewrite --mtu=[1400] --mtu-trunc -i [input.pcap] -o [output.pcap]```

# SYNOPSIS

**tcprewrite** [_options_] **-i** _input.pcap_ **-o** _output.pcap_

# PARAMETERS

**-i**, **--infile** _file_
> 要读取的输入 pcap 文件。

**-o**, **--outfile** _file_
> 要写入的输出 pcap 文件。

**-c**, **--cachefile** _file_
> 用于客户端/服务器分类的 tcpprep 缓存文件。

**--enet-smac** _mac_
> 重写源以太网 MAC 地址。

**--enet-dmac** _mac_
> 重写目标以太网 MAC 地址。

**--srcipmap** _cidr:cidr_
> 重写源 IP 地址。

**--dstipmap** _cidr:cidr_
> 重写目标 IP 地址。

**--pnat** _cidr:cidr_
> 伪 NAT：带随机化地重写 IP。

**--portmap** _port:port_
> 重写 TCP/UDP 端口号。

**--seed** _n_
> 伪 NAT 的随机化种子。

**--fixcsum**
> 重新计算 TCP/UDP/IP 校验和。

**--mtu** _bytes_
> 设置最大数据包尺寸。

**--mtu-trunc**
> 截断超过 MTU 的数据包。

**-C**
> 重新计算校验和。

# DESCRIPTION

**tcprewrite** 是一个 pcap 文件编辑器，可以重写第 2、3、4 层的数据包头部。它能修改捕获流量中的以太网 MAC 地址、IP 地址以及 TCP/UDP 端口号。

该工具是 Tcpreplay 套件的组成部分，用于把捕获的流量改造成适合在不同网络环境中重放的形式。重写之后，可以使用 **tcpreplay** 或 **tcpreplay-edit** 进行重放。

常见用例包括在共享前对抓包进行匿名化处理、让抓包适配不同的网络配置，以及在实验室环境中准备用于安全测试的流量。

会改变数据包大小或内容的重写操作需要使用 --fixcsum 或 -C 选项重新计算校验和。

# CAVEATS

以 "any" 接口（cooked 模式）捕获的数据包无法被正确编辑。某些重写操作可能需要 tcpprep 缓存文件来做客户端/服务器分类。大型 pcap 文件可能需要很长的处理时间。无法处理应用层协议数据（例如 HTTP 中内嵌的 IP）。

# HISTORY

**tcprewrite** 是 Tcpreplay 套件的一部分，最初由 Aaron Turner 于 2001 年开发。该项目现在由 AppNeta 维护并以 GPLv3 许可证发行。它已成为网络测试和安全分析的标准工具。

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

[tcpreplay](/man/tcpreplay)(1), [tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1)
