# TAGLINE

easside-ng WEP 攻击的配套服务器

# TLDR

**启动 buddy-ng 服务器**

```buddy-ng```

**启动后不放弃特权**

```buddy-ng -p```

**显示帮助**

```buddy-ng -h```

# SYNOPSIS

**buddy-ng** [_options_]

# DESCRIPTION

**buddy-ng** 是 easside-ng 的配套工具，运行在可访问互联网的远程计算机上。它接收解密后的数据包并回传，使 easside-ng 无需知道密钥即可访问受 WEP 保护的无线网络。

其原理是让接入点自身解密数据包，然后通过 buddy-ng 转发。

# PARAMETERS

**-h**
> 显示帮助界面

**-p**
> 启动后不放弃特权

# NETWORK

Buddy-ng 默认监听端口 **6969**，这是 easside-ng 通信使用的标准端口。

# WORKFLOW

1. 在可访问互联网的远程服务器上启动 buddy-ng
2. 在攻击机上运行 easside-ng，指定 buddy-ng 服务器
3. Easside-ng 与 buddy-ng 建立 TCP 连接
4. 数据包由 AP 解密并经 buddy-ng 转发
5. 无需知道 WEP 密钥即可实现互联网访问

# COMPILATION

构建 buddy-ng 需要在编译 aircrack-ng 时加上 **--with-experimental** 标志：

```./configure --with-experimental```

还需要 libpcap 开发包。

# CAVEATS

仅配合 easside-ng 用于 WEP 网络攻击时有用。需要一台可公开访问的服务器来运行 buddy-ng。只能在你拥有所有权或获得明确授权的网络上使用。WEP 已被弃用，不应再用于安全防护。

# INSTALL

```apt: sudo apt install aircrack-ng```

```dnf: sudo dnf install aircrack-ng```

```pacman: sudo pacman -S aircrack-ng```

```apk: sudo apk add aircrack-ng```

```zypper: sudo zypper install aircrack-ng```

```brew: brew install aircrack-ng```

```nix: nix profile install nixpkgs#aircrack-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[easside-ng](/man/easside-ng)(1), [aircrack-ng](/man/aircrack-ng)(1), [wesside-ng](/man/wesside-ng)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

<!-- verified: 2026-06-22 -->
