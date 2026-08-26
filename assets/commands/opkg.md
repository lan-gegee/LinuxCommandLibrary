# TAGLINE

轻量级软件包管理器，主要用于 OpenWrt 和其他嵌入式 Linux

# TLDR

**安装**软件包

```opkg install [package]```

**移除**软件包

```opkg remove [package]```

**更新**可用软件包列表

```opkg update```

**升级**一个或多个指定的软件包

```opkg upgrade [package(s)]```

显示特定软件包的**信息**

```opkg info [package]```

**列出**所有可用软件包

```opkg list```

查找**哪个软件包拥有**某文件

```opkg search [/path/to/file]```

列出软件包**所属的所有文件**

```opkg files [package]```

# SYNOPSIS

**opkg** _command_ [_options_] [_packages_]

# PARAMETERS

**install**
> 安装软件包

**remove**
> 移除软件包

**update**
> 从软件仓库更新软件包列表

**upgrade**
> 升级已安装的软件包

**info**
> 显示软件包信息

**list**
> 列出可用软件包

**list-installed**
> 列出已安装的软件包

**search**
> 查找某个文件属于哪个软件包

**files**
> 列出某软件包安装的文件

**--force-depends**
> 忽略依赖错误

**--force-overwrite**
> 覆盖来自其他软件包的文件

# DESCRIPTION

**opkg** 是一款轻量级软件包管理器，主要用于 OpenWrt 和其他嵌入式 Linux 系统。它提供与 apt 或 yum 类似的功能，但资源需求极低，适合路由器和物联网设备。

该软件包管理器负责处理依赖、从配置好的软件仓库下载软件包并管理安装数据库。配置存储在 **/etc/opkg.conf** 中，软件仓库列表位于 **/etc/opkg/*.conf**。

嵌入式设备的存储空间通常有限，因此 opkg 支持将软件包安装到外部存储，并能高效地管理软件包状态。

# CAVEATS

安装新软件包前必须先更新软件包列表（**opkg update**）。嵌入式设备存储空间有限；安装前请检查可用空间。部分软件包需要重启设备才能生效。在资源受限的系统上，依赖可能需要手动解决。

# INSTALL

```nix: nix profile install nixpkgs#opkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(8), [ipkg](/man/ipkg)(8)
