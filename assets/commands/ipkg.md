# TAGLINE

面向嵌入式 Linux 系统的轻量级软件包管理器

# TLDR

**更新软件包列表**

```ipkg update```

**安装软件包**

```ipkg install [package]```

**卸载软件包**

```ipkg remove [package]```

**列出已安装的软件包**

```ipkg list_installed```

**搜索软件包**

```ipkg list | grep [pattern]```

**升级所有软件包**

```ipkg upgrade```

# SYNOPSIS

**ipkg** _command_ [_options_] [_package_...]

# PARAMETERS

**update**
> 更新软件包列表。

**install** _package_
> 安装软件包。

**remove** _package_
> 卸载软件包。

**upgrade**
> 升级所有软件包。

**list**
> 列出可用的软件包。

**list_installed**
> 列出已安装的软件包。

**info** _package_
> 显示软件包信息。

**status** _package_
> 显示软件包状态。

**download** _package_
> 只下载而不安装。

# DESCRIPTION

**ipkg**（Itsy Package Management System）是面向嵌入式 Linux 系统的轻量级软件包管理器。它专为存储和内存有限的设备设计，使用与 Debian 的 dpkg 类似的格式。

在被 opkg 接替之前，ipkg 曾广泛用于 OpenWrt、NSLU2 及其他嵌入式设备。

# CAVEATS

已被 opkg 取代，属于弃用状态。仅限于嵌入式系统。软件包可用性取决于 feed 配置。某些版本不具备依赖解析功能。

# HISTORY

ipkg 为 NSLU2 Linux 社区而开发，并在 8.09 版本之前被 OpenWrt 使用。它的继任者是 **opkg**，这是一个功能更强且仍在活跃维护的分叉版本。

# INSTALL

```aur: yay -S ipkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[opkg](/man/opkg)(1), [apt](/man/apt)(8), [dpkg](/man/dpkg)(1)
