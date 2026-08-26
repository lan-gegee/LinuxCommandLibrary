# TAGLINE

操纵网络接口的 MAC 地址

# TLDR

**查看**当前 MAC 地址与永久 MAC 地址

```macchanger -s [eth0]```

设置**随机** MAC 地址

```sudo macchanger -r [eth0]```

设置带有**烧录地址（burned-in address）**标志的随机 MAC

```sudo macchanger -r -b [eth0]```

设置一个**指定的** MAC 地址

```sudo macchanger -m [XX:XX:XX:XX:XX:XX] [eth0]```

从**同一厂商**的地址中随机设置 MAC

```sudo macchanger -a [eth0]```

**重置**为永久的硬件 MAC 地址

```sudo macchanger -p [eth0]```

列出已知厂商的 **MAC 前缀**

```macchanger -l```

# SYNOPSIS

**macchanger** [_OPTIONS_] _interface_

# DESCRIPTION

**macchanger** 用于操纵网络接口的 MAC 地址。它可以设置随机地址、厂商相关地址，或恢复原始硬件地址。适用于隐私保护、测试和网络故障排查。

# PARAMETERS

**-s, --show**
> 显示当前 MAC 地址与永久 MAC 地址

**-r, --random**
> 设置完全随机的 MAC 地址

**-b, --bia**
> 伪装成烧录地址（保留厂商位）

**-m, --mac** _address_
> 设置指定的 MAC 地址

**-p, --permanent**
> 重置为永久的硬件 MAC 地址

**-l, --list**
> 打印已知厂商的 MAC 前缀

**-e, --ending**
> 只改变末尾几个字节，保留厂商前缀

**-a, --another**
> 设置同类型的随机厂商 MAC 地址

**-A**
> 设置任意类型的随机厂商 MAC 地址

# CAVEATS

在大多数系统上，修改 MAC 前必须先关闭接口。更改在重启后不会保留。某些网络会检测并阻止 MAC 地址变更。

# HISTORY

**macchanger** 由 **Alvaro Lopez Ortega** 编写，常用于 Linux 系统上的隐私保护和网络测试。

# INSTALL

```apt: sudo apt install macchanger```

```dnf: sudo dnf install macchanger```

```pacman: sudo pacman -S macchanger```

```apk: sudo apk add macchanger```

```zypper: sudo zypper install macchanger```

```brew: brew install macchanger```

```nix: nix profile install nixpkgs#macchanger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip-link](/man/ip-link)(8), [ifconfig](/man/ifconfig)(8)
