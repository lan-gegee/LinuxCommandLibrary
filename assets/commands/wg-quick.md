# TAGLINE

快速搭建 WireGuard VPN 隧道

# TLDR

**启动 WireGuard 隧道**

```sudo wg-quick up [wg0]```

**关闭 WireGuard 隧道**

```sudo wg-quick down [wg0]```

**从指定的配置文件启动隧道**

```sudo wg-quick up [/etc/wireguard/wg0.conf]```

**将当前接口状态保存到配置文件**

```sudo wg-quick save [wg0]```

# SYNOPSIS

**wg-quick** [**up**|**down**|**save**|**strip**] _interface_

# PARAMETERS

**up _interface_**
> 使用配置文件启动 WireGuard 接口

**down _interface_**
> 关闭 WireGuard 接口

**save _interface_**
> 将当前配置保存到配置文件

**strip _interface_**
> 输出不含 wg-quick 专属选项的配置

# DESCRIPTION

**wg-quick** 是一个便捷的封装工具，用于快速搭建 WireGuard VPN 隧道。它从 **/etc/wireguard/** 读取配置文件，并自动处理接口创建、路由和 DNS 配置。

配置文件命名为 **[interface].conf**（例如 **/etc/wireguard/wg0.conf**），其中既包含 WireGuard 设置，也包含 Address、DNS 和路由规则等 wg-quick 专属选项。

# CAVEATS

需要 root 权限。配置文件必须存在于 **/etc/wireguard/** 中。该脚本会修改路由表，可能影响网络连接。DNS 更改需要 resolvconf 或 systemd-resolved 支持。

# HISTORY

**wg-quick** 是 WireGuard 工具的一部分，由 **Jason A. Donenfeld** 创建。WireGuard 最初作为 Linux 内核模块开发，并在 **5.6** 版本（2020 年 3 月）合入主线 Linux 内核。wg-quick 脚本简化了原本需要多条 **wg** 和 **ip** 命令才能完成的设置工作。

# INSTALL

```apt: sudo apt install wireguard-tools```

```dnf: sudo dnf install wireguard-tools```

```pacman: sudo pacman -S wireguard-tools```

```apk: sudo apk add wireguard-tools-wg-quick```

```zypper: sudo zypper install wireguard-tools```

```brew: brew install wireguard-tools```

```nix: nix profile install nixpkgs#wireguard-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg](/man/wg)(8), [ip](/man/ip)(8)
