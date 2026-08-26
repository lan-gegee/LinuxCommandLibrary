# TAGLINE

面向 BIOS 系统的网络 PXE 引导加载器

# TLDR

**基本 PXELINUX 设置**

```cp pxelinux.0 [/tftproot/]```

**创建配置目录**

```mkdir -p [/tftproot/pxelinux.cfg/]```

**创建默认配置**

```vi [/tftproot/pxelinux.cfg/default]```

# SYNOPSIS

PXELINUX bootloader configuration

# DESCRIPTION

**PXELINUX** 是用于 PXE 网络启动的 SYSLINUX 衍生版本。它通过 TFTP 加载，允许通过网络启动 Linux 内核及其他操作系统。

# CONFIGURATION

```
# /tftproot/pxelinux.cfg/default
DEFAULT linux
TIMEOUT 50
PROMPT 1

LABEL linux
  KERNEL vmlinuz
  APPEND initrd=initrd.img root=/dev/nfs nfsroot=server:/path ip=dhcp

LABEL local
  LOCALBOOT 0
```

# EXAMPLES

```bash
# Setup TFTP root
mkdir -p /tftproot/pxelinux.cfg
cp /usr/lib/PXELINUX/pxelinux.0 /tftproot/
cp /usr/lib/syslinux/modules/bios/*.c32 /tftproot/

# DHCP config (dhcpd.conf)
next-server 192.168.1.1;
filename "pxelinux.0";
```

# CONFIG FILE SEARCH ORDER

```
/pxelinux.cfg/01-88-99-aa-bb-cc-dd  # MAC address
/pxelinux.cfg/C0A80001              # IP in hex
/pxelinux.cfg/default               # Fallback
```

# CAVEATS

需要 TFTP 和 DHCP 服务器。仅支持 BIOS/legacy 启动（UEFI 请使用 SYSLINUX）。SYSLINUX 项目的一部分。

# HISTORY

PXELINUX 由 **H. Peter Anvin** 开发，是 SYSLINUX 项目中负责 PXE 网络启动的部分。

# SEE ALSO

[syslinux](/man/syslinux)(1), [dhcpd](/man/dhcpd)(8)
