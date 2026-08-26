# TAGLINE

旨在从零开始创建全新的系统安装

# TLDR

安装 **base** 软件包、Linux 内核和固件

```sudo pacstrap /mnt base linux linux-firmware```

安装带 **LTS 内核**和构建工具的基础系统

```sudo pacstrap /mnt base base-devel linux-lts```

将主机的 **pacman 配置**复制到目标

```sudo pacstrap -P /mnt [packages]```

使用**替代的配置**文件

```sudo pacstrap -C [path/to/pacman.conf] /mnt [packages]```

使用主机的**软件包缓存**

```sudo pacstrap -c /mnt [packages]```

在目标中初始化**空的密钥环**

```sudo pacstrap -K /mnt [packages]```

以**交互式**模式安装

```sudo pacstrap -i /mnt [packages]```

# SYNOPSIS

**pacstrap** [**-C** _config_] [**-c**] [**-G**] [**-i**] [**-K**] [**-M**] [**-N**] [**-P**] _root_ [_packages_...]

# PARAMETERS

**-C _config_**
> 使用替代的 pacman 配置文件

**-c**
> 使用主机上的软件包缓存而不是目标的

**-G**
> 避免将主机的 pacman 密钥环复制到目标

**-i**
> 提示确认要安装的软件包（交互模式）

**-K**
> 在目标中初始化空的 pacman 密钥环

**-M**
> 避免将主机的 mirrorlist 复制到目标

**-N**
> 以普通用户身份在 unshare 模式下运行

**-P**
> 将主机的 pacman 配置复制到目标

# DESCRIPTION

**pacstrap** 旨在从零开始创建全新的系统安装。它将软件包安装到指定的新根目录中，通常在安装 Arch Linux 时用于引导基础系统。

该工具负责挂载目标文件系统、使用 pacman 安装软件包，并可选择性地复制主机的配置。它是 arch-install-scripts 软件包的一部分。

# CAVEATS

除非使用 -N 标志，否则需要 root 权限。运行前必须先挂载目标目录。默认使用主机的密钥环验证软件包签名。下载软件包需要网络连接。

# HISTORY

**pacstrap** 是 Arch Linux 团队开发的 **arch-install-scripts** 软件包的一部分。它以一个精简的工具取代了手动基于 chroot 的安装方法，处理引导 Arch 系统过程中的各种复杂操作。

# INSTALL

```dnf: sudo dnf install arch-install-scripts```

```pacman: sudo pacman -S arch-install-scripts```

```apk: sudo apk add arch-install-scripts```

```zypper: sudo zypper install arch-install-scripts```

```nix: nix profile install nixpkgs#arch-install-scripts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [arch-chroot](/man/arch-chroot)(1), [genfstab](/man/genfstab)(8)
