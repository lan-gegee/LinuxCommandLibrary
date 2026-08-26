# TAGLINE

PXELINUX 专用 DHCP 选项参考

# TLDR

**查看 pxelinux-options man 手册**

```man pxelinux-options```

# SYNOPSIS

This is a documentation reference, not an executable command.

# PARAMETERS

**DHCP Option 208** (pxelinux.magic)
> 标识 PXELINUX 感知型 DHCP 配置的幻数。必须设置为 F1:00:74:7E。

**DHCP Option 209** (pxelinux.configfile)
> 指定相对于 TFTP 服务器前缀的 PXELINUX 配置文件路径。

**DHCP Option 210** (pxelinux.pathprefix)
> 加在 PXELINUX 配置文件中所有文件引用之前的路径前缀。

**DHCP Option 211** (pxelinux.reboottime)
> 以秒为单位的重启时间，编码为 32 位无符号整数。控制 PXELINUX 在失败后等待多久再重启。

# DESCRIPTION

**pxelinux-options** 是一份 man 文档，记录 **PXELINUX**（SYSLINUX 引导加载器的网络 PXE 启动变体）专用的 DHCP 选项。这些选项通过 DHCP 传递给 PXELINUX 客户端，用于配置其启动行为。

这些选项使用 DHCP 选项号 208-211（站点专属选项空间），允许 DHCP 服务器为进行 PXE 启动的客户端指定配置文件、路径前缀和重启超时。必须在 DHCP 服务器上（如 ISC dhcpd 或 dnsmasq）配置这些选项，才能将其传递给正在启动的客户端。

# CAVEATS

这是一份文档参考，不是可执行程序。DHCP 选项 208-211 位于站点本地选项空间中，可能与这些选项号的其他用途冲突。必须正确设置选项 208（pxelinux.magic），PXELINUX 才能识别其余选项。

# HISTORY

pxelinux-options 是 **H. Peter Anvin** 创建的 **SYSLINUX** 项目的一部分。PXELINUX 使 Linux 系统能够使用 PXE（Preboot Execution Environment）标准通过网络启动。

# INSTALL

```apt: sudo apt install syslinux-utils```

```dnf: sudo dnf install syslinux```

```pacman: sudo pacman -S syslinux```

```apk: sudo apk add syslinux```

```zypper: sudo zypper install syslinux```

```nix: nix profile install nixpkgs#syslinux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[syslinux](/man/syslinux)(1), [pxelinux](/man/pxelinux)(1), [tftp](/man/tftp)(1), [dhcpd](/man/dhcpd)(1), [dnsmasq](/man/dnsmasq)(1)
