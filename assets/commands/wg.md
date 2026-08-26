# TAGLINE

WireGuard VPN 配置工具

# TLDR

**检查**当前活动接口的状态

```sudo wg```

**生成**新的私钥

```wg genkey```

从私钥**生成**公钥

```wg pubkey < [path/to/private_key] > [path/to/public_key]```

同时**生成**公钥和私钥

```wg genkey | tee [path/to/private_key] | wg pubkey > [path/to/public_key]```

**显示**接口当前的配置

```sudo wg showconf [wg0]```

# SYNOPSIS

**wg** [_command_] [_arguments_]

# PARAMETERS

**show**
> 显示当前配置和状态

**showconf _interface_**
> 以配置文件格式显示配置

**genkey**
> 生成新的私钥

**pubkey**
> 从标准输入的私钥生成公钥

**genpsk**
> 生成预共享密钥

**set _interface_ _options_**
> 修改接口的配置

**setconf _interface_ _file_**
> 应用来自文件的配置

**addconf _interface_ _file_**
> 添加来自文件的配置

# DESCRIPTION

**wg** 是 WireGuard 的配置工具。WireGuard 是一种现代 VPN 隧道。它管理 WireGuard 接口，包括密钥生成、对端配置和状态监控。

WireGuard 采用最先进的密码学技术，设计上比 OpenVPN 或 IPsec 等传统 VPN 协议更简单、更快速、更安全。

# CAVEATS

大多数操作需要 root 权限。私钥应以受限的文件权限妥善保管。必须先创建接口（例如用 **ip link add**）再进行配置。若想简化设置流程，可以考虑使用 **wg-quick**。

# INSTALL

```apt: sudo apt install wireguard-tools```

```dnf: sudo dnf install wireguard-tools```

```pacman: sudo pacman -S wireguard-tools```

```apk: sudo apk add wireguard-tools-wg```

```zypper: sudo zypper install wireguard-tools```

```brew: brew install wireguard-tools```

```nix: nix profile install nixpkgs#wireguard-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg-quick](/man/wg-quick)(8), [ip](/man/ip)(8)
