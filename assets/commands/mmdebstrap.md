# TAGLINE

从一个或多个镜像源创建 Debian chroot

# TLDR

创建 **Debian Stable** 目录型 chroot

```sudo mmdebstrap stable [path/to/debian-root]/```

使用镜像源创建 **Debian Bookworm** tar 包形式的 chroot

```mmdebstrap bookworm [path/to/debian-bookworm.tar] [http://mirror.example.org/debian]```

创建带**额外软件包**的 Debian Sid tar 包

```mmdebstrap sid [path/to/debian-sid.tar] --include=[pkg1,pkg2]```

使用**用户命名空间**创建 chroot（无需 root）

```mmdebstrap --mode=unshare stable [path/to/debian.tar]```

仅包含必要软件包、创建**最小化 chroot**

```mmdebstrap --variant=essential stable [path/to/minimal.tar]```

**模拟运行**，不下载也不安装

```mmdebstrap --simulate stable```

# SYNOPSIS

**mmdebstrap** [_options_] [_suite_ [_target_ [_mirror_...]]]

# PARAMETERS

**--mode _name_**
> 运行模式：auto、sudo、root、unshare、fakeroot、fakechroot、proot、chrootless

**--format _name_**
> 输出格式：auto、directory、tar、squashfs、ext2、null

**--variant _name_**
> 软件包集合：extract、custom、essential、apt、required、minbase、buildd、important、debootstrap、-、standard

**--include _packages_**
> 要额外安装的软件包（逗号分隔）

**--components _list_**
> 软件仓库组件：main、contrib、non-free、non-free-firmware

**--architectures _list_**
> 支持的架构（本机架构和外部架构）

**--keyring _file_**
> 用于签名验证的 GPG 密钥环

**--aptopt _option_**
> 向 apt 传递选项

**--dpkgopt _option_**
> 向 dpkg 传递选项

**--setup-hook _cmd_**
> 初始设置完成后运行的命令

**--customize-hook _cmd_**
> 软件包安装完成后运行的命令

**--hook-directory _dir_**
> 从指定目录执行钩子脚本

**--simulate, --dry-run**
> 只测试，不下载也不安装

**-q, --quiet**
> 抑制输出

**-v, --verbose**
> 显示详细输出

# DESCRIPTION

**mmdebstrap** 从一个或多个镜像源创建 Debian chroot。它是 debootstrap 的替代品，使用 apt 解析依赖关系，支持同时使用多个镜像源，并且可以借助用户命名空间在没有 root 权限的情况下运行。

suite 可以是代号（bookworm、sid）或符号名称（stable、unstable）。target 可以是目录、tar 包、squashfs 镜像、ext2/ext4 镜像或 stdout。输出格式会根据文件扩展名自动检测。

# CAVEATS

chrootless 模式在使用不受支持的软件包时可能修改宿主系统。unshare 模式在命名空间之外创建的文件所有权看起来不正确；需要正确配置 /etc/subuid 和 /etc/subgid。只能用于基于 apt 的发行版。

# HISTORY

**mmdebstrap** 由 **Johannes Schauer Marin Rodrigues** 开发，是比 debootstrap 更快、更灵活的替代方案。在设置了 SOURCE_DATE_EPOCH 时它支持可复现构建，速度大约可达 debootstrap 的两倍。

# INSTALL

```aur: yay -S mmdebstrap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[debootstrap](/man/debootstrap)(8), [apt](/man/apt)(8), [dpkg](/man/dpkg)(1)
