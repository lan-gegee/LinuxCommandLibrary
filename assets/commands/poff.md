# TAGLINE

断开 PPP 拨号连接

# TLDR

**断开 PPP 连接**

```poff```

**断开特定提供商的连接**

```poff [provider]```

**断开所有连接**

```poff -a```

# SYNOPSIS

**poff** [_options_] [_provider_]

# PARAMETERS

_PROVIDER_
> PPP 提供商名称。

**-a**, **--all**
> 断开所有连接。

**-r**, **--reconnect**
> 断开后重新连接。

# DESCRIPTION

**poff** 用于终止由 **pon** 建立的 PPP（点对点协议）连接。不带参数时断开默认提供商的连接；也可以指定提供商名称来针对特定连接。

**-a** 标志断开所有活动的 PPP 连接。**-r** 标志在断开后自动重连。它是对 pppd 守护进程发送信号的一个便捷封装。

# CAVEATS

仅适用于 PPP。与 pon 命令配套使用。

# HISTORY

poff 为 Linux 系统上的 **PPP 连接**终止而创建。

# INSTALL

```apt: sudo apt install ppp```

```dnf: sudo dnf install ppp```

```pacman: sudo pacman -S ppp```

```apk: sudo apk add ppp-daemon```

```zypper: sudo zypper install ppp```

```nix: nix profile install nixpkgs#ppp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pon](/man/pon)(1), [pppd](/man/pppd)(8), [pppconfig](/man/pppconfig)(8)
