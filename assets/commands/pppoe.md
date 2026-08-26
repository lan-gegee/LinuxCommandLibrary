# TAGLINE

管理以太网上的 PPP 连接

# TLDR

**启动 PPPoE 连接**

```pppoe -I [eth0]```

**调试模式**

```pppoe -I [eth0] -D [/tmp/pppoe.log]```

**指定 AC 名称**

```pppoe -I [eth0] -A [ac_name]```

# SYNOPSIS

**pppoe** [_options_]

# PARAMETERS

**-I** _INTERFACE_
> 以太网接口。

**-D** _FILE_
> 调试日志文件。

**-A** _NAME_
> 接入集中器名称。

**-S** _NAME_
> 服务名称。

**-T** _SECONDS_
> 超时时间。

# DESCRIPTION

**pppoe** 是一个用户态的以太网上的 PPP（PPP over Ethernet）客户端，用于为 DSL 宽带连接建立 PPPoE 会话。它处理 PPPoE 协议的发现阶段和会话阶段，通过指定的以太网接口与 ISP 的接入集中器通信。

该工具通常不直接调用，而是通过 **pppoe-connect** 或 **pppoe-start** 包装脚本间接使用。它与 **pppd** 配合工作，后者在以太网会话建立后处理 PPP 协商。

# CAVEATS

通常由 pppoe-connect 管理。需要 root 权限。

# HISTORY

pppoe 为 DSL 连接实现了 **PPP over Ethernet**。

# INSTALL

```apt: sudo apt install pppoe```

```dnf: sudo dnf install rp-pppoe```

```pacman: sudo pacman -S rp-pppoe```

```apk: sudo apk add rp-pppoe```

```zypper: sudo zypper install rp-pppoe```

```nix: nix profile install nixpkgs#rp-pppoe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppoe-connect](/man/pppoe-connect)(1), [pppoe-setup](/man/pppoe-setup)(8), [pppd](/man/pppd)(8)
