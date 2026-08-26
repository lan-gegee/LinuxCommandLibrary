# TAGLINE

通过网络传输 ALSA MIDI 音序器事件

# TLDR

**启动** MIDI 网络服务器

```aseqnet```

连接到**远程服务器**

```aseqnet [hostname]```

指定**端口**

```aseqnet -p [40002] [hostname]```

启动时自动连接**读取**端口

```aseqnet -s [client:port] [hostname]```

启动时自动连接**写入**端口

```aseqnet -d [client:port] [hostname]```

# SYNOPSIS

**aseqnet** [_options_] [_hostname_]

# DESCRIPTION

**aseqnet** 通过网络连接传输 ALSA 音序器事件。它让机器之间能够进行 MIDI 通信，可用于远程 MIDI 控制或分布式音乐系统。

不带参数运行时启动服务器；指定主机名则以客户端身份连接。aseqnet 创建的端口可以通过 [aconnect](/man/aconnect)(1) 连接到其他音序器端口。

# PARAMETERS

**hostname**
> 连接到此服务器（客户端模式）

**-p** _port_
> TCP 端口号或服务名（默认：40002）

**-s** _addr_
> 自动订阅给定地址用于读取（client:port）

**-d** _addr_
> 自动订阅给定地址用于写入（client:port）

**-n** _name_
> 指定该进程的 MIDI 名称

**-v**
> 详细输出

# CAVEATS

没有加密；需要安全时请使用 SSH 隧道。网络延迟会影响 MIDI 时序。

# HISTORY

**aseqnet** 是 ALSA 实用工具的一部分，为分布式音频系统提供网络 MIDI 功能。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aconnect](/man/aconnect)(1), [aseqdump](/man/aseqdump)(1), [aplaymidi](/man/aplaymidi)(1)
