# TAGLINE

捕获 PPPoE 数据包用于调试

# TLDR

**嗅探 PPPoE 流量**

```pppoe-sniff -I [eth0]```

**详细输出**

```pppoe-sniff -I [eth0] -V```

# SYNOPSIS

**pppoe-sniff** [_options_]

# PARAMETERS

**-I** _INTERFACE_
> 网络接口。

**-V**
> 详细输出。

# DESCRIPTION

**pppoe-sniff** 在网络接口上捕获并显示 PPPoE 发现包和会话包，用于诊断目的。它会显示 PPPoE 客户端与接入集中器之间交换的 PADI、PADO、PADR、PADS 和 PADT 包。

通过验证发现包是否已发送、应答是否已收到，该工具有助于排查 PPPoE 连接失败问题。详细模式会提供关于数据包内容的更多信息。

# CAVEATS

需要 root 权限。仅作为调试工具。

# HISTORY

pppoe-sniff 提供 **PPPoE 流量分析**功能，用于故障排查。

# INSTALL

```apt: sudo apt install pppoe```

```dnf: sudo dnf install rp-pppoe```

```pacman: sudo pacman -S rp-pppoe```

```apk: sudo apk add rp-pppoe```

```zypper: sudo zypper install rp-pppoe```

```nix: nix profile install nixpkgs#rp-pppoe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppoe](/man/pppoe)(8), [pppoe-discovery](/man/pppoe-discovery)(8), [tcpdump](/man/tcpdump)(1)
