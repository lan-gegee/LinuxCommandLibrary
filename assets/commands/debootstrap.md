# TAGLINE

将基本 Debian 系统安装到子目录中

# TLDR

创建 **Debian stable** 系统

```sudo debootstrap stable [path/to/debian-root]/ http://deb.debian.org/debian```

创建**最小化**系统

```sudo debootstrap --variant=minbase stable [path/to/debian-root]/```

使用本地镜像创建 **Debian Unstable**

```sudo debootstrap sid [path/to/sid-root]/ file:///[path/to/mirror]/```

切换到**引导好的系统**

```sudo chroot [path/to/root]```

**列出**可用发行版

```ls /usr/share/debootstrap/scripts/```

# SYNOPSIS

**debootstrap** [_options_] _suite_ _target_ [_mirror_]

# DESCRIPTION

**debootstrap** 将一个基本的 Debian 系统安装到子目录中。它从镜像下载软件包并完成安装，创建出一个最小但可用的系统，可用于 chroot 环境、容器或全新安装。

得到的系统虽然精简但功能完整，适合进一步定制。

# PARAMETERS

**--variant** _variant_
> minbase（最小化）、buildd（构建依赖）、fakechroot

**--arch** _arch_
> 目标架构（amd64、i386、arm64 等）

**--include** _packages_
> 额外要安装的软件包

**--exclude** _packages_
> 要排除的软件包

**--foreign**
> 仅执行第一阶段（用于跨架构）

# CAVEATS

需要 root 权限。目标目录必须已存在。跨架构引导可能需要 qemu-user-static。debootstrap 之后通常还需要额外配置（网络、fstab 等）。

# INSTALL

```dnf: sudo dnf install debootstrap```

```pacman: sudo pacman -S debootstrap```

```apk: sudo apk add debootstrap```

```zypper: sudo zypper install debootstrap```

```nix: nix profile install nixpkgs#debootstrap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chroot](/man/chroot)(8), [schroot](/man/schroot)(1), [systemd-nspawn](/man/systemd-nspawn)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/installer-team/debootstrap)```

```[Documentation](https://manpages.debian.org/testing/debootstrap/debootstrap.8)```

<!-- verified: 2026-07-11 -->
