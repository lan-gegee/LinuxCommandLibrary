# TAGLINE

开源网络启动固件

# TLDR

**从 iPXE 命令行启动**

```dhcp && chain http://server/boot.ipxe```

**启动指定内核**

```kernel http://server/vmlinuz initrd=initrd.img```

**加载 initrd**

```initrd http://server/initrd.img```

**启动已加载的内核**

```boot```

**显示网络配置**

```ifstat```

# SYNOPSIS

iPXE 命令行或脚本命令

# COMMANDS

**dhcp**
> 通过 DHCP 获取 IP。

**ifopen**
> 打开网络接口。

**ifstat**
> 显示接口统计信息。

**kernel** _url_
> 加载内核镜像。

**initrd** _url_
> 加载初始内存盘。

**boot**
> 启动已加载的内核。

**chain** _url_
> 加载并执行脚本。

**imgfree**
> 释放已加载的镜像。

**shell**
> 进入 iPXE shell。

**exit**
> 退出 iPXE。

# DESCRIPTION

**iPXE** 是一款开源网络启动固件。它替代或扩展 PXE（Preboot Execution Environment，预启动执行环境），支持 HTTP、iSCSI、FCoE 等多种网络启动协议。

iPXE 可以嵌入 BIOS/UEFI、烧录到 ROM，或从现有 PXE 链式加载。它支持灵活的基于网络的系统安装和无盘启动。

# BOOT SCRIPT EXAMPLE

```
#!ipxe
dhcp
kernel http://server/vmlinuz ip=dhcp
initrd http://server/initrd.img
boot
```

# CAVEATS

需要网络启动支持。HTTPS 需要证书。UEFI 和 BIOS 需要不同的构建版本。某些网卡可能缺少驱动支持。

# HISTORY

iPXE 由 Etherboot 和 gPXE 项目演化而来。它提供超越标准 PXE 的高级网络启动能力，支持现代协议和脚本功能。

# SEE ALSO

[pxelinux](/man/pxelinux)(1), [dnsmasq](/man/dnsmasq)(8), [tftp](/man/tftp)(1)
