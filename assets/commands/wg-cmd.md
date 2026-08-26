# TAGLINE

管理 WireGuard 配置的 TUI 工具

# TLDR

为新接口**启动设置向导**

```wg-cmd new```

**管理已有的 WireGuard 接口**

```wg-cmd [wg0]```

不打开 UI 直接**生成配置**

```wg-cmd [wg0] make```

# SYNOPSIS

**wg-cmd** [_command_] [_interface_]

# DESCRIPTION

**wg-cmd**（WG Commander）提供一个文本用户界面来管理 WireGuard 配置文件。它包含初始设置向导、支持查看二维码的对端管理，以及 sysctl、systemd 和 NAT 规则的自动配置。需要 root 权限，并假定系统为带有 iptables 和 systemd 的 Linux。

# HISTORY

**wg-cmd** 由 **Andrian Budantsov**（AndrianBdn）创建，使用 **Go** 编写。

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

[wg](/man/wg)(1), [vortix](/man/vortix)(1)
