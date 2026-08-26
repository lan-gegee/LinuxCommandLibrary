# TAGLINE

查询众多 Linux 发行版中的软件包可用性

# TLDR

**在所有支持的发行版中搜索软件包**

```whohas [package_name]```

**将搜索限制在特定发行版**

```whohas -d [debian,ubuntu,arch] [package_name]```

**精确匹配软件包名称**

```whohas --strict [package_name]```

**以牺牲部分细节为代价加快搜索速度**

```whohas --shallow [package_name]```

**禁用多线程查询**

```whohas --no-threads [package_name]```

# SYNOPSIS

**whohas** [**--no-threads**] [**--shallow**] [**--strict**] [**-d** _Dist1_[,_Dist2_[,_Dist3_]]] _pkgname_

# DESCRIPTION

**whohas** 是一个命令行工具，可并行查询多个 Linux 和 BSD 发行版的软件包列表，并以统一的格式打印结果。它的目的是让你无需访问每个发行版的网站，就能轻松发现哪些发行版提供了某个软件包、版本是什么、体积有多大。

支持的发行版包括 **Arch Linux**、**Debian**、**Fedora**、**Gentoo**、**Mageia**、**Mandriva**、**openSUSE**、**Slackware**、**Source Mage**、**Ubuntu**、**FreeBSD**、**NetBSD**、**OpenBSD**、**Fink**、**MacPorts** 和 **Cygwin**。

默认情况下每个软件仓库都会被并发查询以降低延迟；如果不希望如此，可用 **--no-threads** 选项退回到顺序查询。

# PARAMETERS

**--no-threads**
> 禁用多线程查询（较慢，但更易于调试或进行速率控制）。

**--shallow**
> 限制每台服务器只调用一次。更快，但会丢失一些信息，例如软件包大小和发布日期。

**--strict**
> 仅列出名称与 _pkgname_ 完全一致的软件包。

**-d** _DIST_[,_DIST_...]
> 将查询限制在给定的发行版。接受的值包括 _archlinux_、_debian_、_ubuntu_、_fedora_、_opensuse_、_gentoo_、_mageia_、_mandriva_、_slackware_、_sourcemage_、_freebsd_、_netbsd_、_openbsd_、_fink_、_macports_、_cygwin_。

_pkgname_
> 要搜索的软件包名称（或子串，除非指定 **--strict**）。

# CAVEATS

**whohas** 抓取上游软件包索引；如果某个发行版更改了其索引格式，查询可能会暂时返回过期或不正确的数据，直到 **whohas** 更新为止。某些服务器可能对激进的并发查询进行限速——如果遇到此类限制，请使用 **--no-threads**。

# HISTORY

**whohas** 由 **Philipp L. Wesche** 编写为一个 Perl 脚本，旨在简化跨发行版的软件包查找。它已被打包进许多发行版，维护者在提交新软件包之前常用它来检查哪些发行版已经收录了该软件。

# INSTALL

```zypper: sudo zypper install whohas```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt-cache](/man/apt-cache)(8), [dpkg-query](/man/dpkg-query)(1), [pacman](/man/pacman)(8), [dnf](/man/dnf)(8)
