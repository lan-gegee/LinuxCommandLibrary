# TAGLINE

内核 CEC 设备控制工具

# TLDR

**列出** CEC 设备

```cec-ctl --list-devices```

**监视** CEC 流量

```sudo cec-ctl -m```

显示 **CEC 拓扑**

```cec-ctl -S```

# SYNOPSIS

**cec-ctl** [_options_]

# DESCRIPTION

**cec-ctl** 通过 Linux 内核原生的 CEC 框架控制 CEC（Consumer Electronics Control，消费电子控制）设备。它提供对 CEC 子系统的底层访问，可用于监视流量、配置适配器以及直接通过内核驱动发送命令。

与依赖用户态 libCEC 库且需要 USB CEC 适配器的 cec-client 不同，cec-ctl 可直接使用集成在显卡和 SoC 中、暴露 `/dev/cecN` 设备节点的 CEC 硬件。因此它是内置 CEC 支持平台（如许多基于 ARM 的媒体播放器和现代 Intel GPU）上的首选工具。

监视模式（`-m`）对调试 CEC 通信问题特别有用，它能实时显示总线上的所有 CEC 流量。

# PARAMETERS

**--list-devices**
> 列出可用的 CEC 设备

**-m, --monitor**
> 监视总线上的 CEC 流量

**-S, --show-topology**
> 显示 CEC 设备拓扑

**-d** _device_
> 使用指定的 CEC 设备

**-p** _addr_
> 设置物理地址

**-o** _addr_
> 设置逻辑地址

# CAVEATS

需要内核支持 CEC（CONFIG_CEC）。监视模式需要 root 权限。并非所有 HDMI 接口都支持 CEC。

# INSTALL

```apt: sudo apt install v4l-utils```

```dnf: sudo dnf install v4l-utils```

```pacman: sudo pacman -S v4l-utils```

```apk: sudo apk add v4l-utils```

```zypper: sudo zypper install v4l-utils```

```nix: nix profile install nixpkgs#v4l-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cec-client](/man/cec-client)(1)

# RESOURCES

```[Source code](https://git.linuxtv.org/v4l-utils.git)```

<!-- verified: 2026-06-22 -->
