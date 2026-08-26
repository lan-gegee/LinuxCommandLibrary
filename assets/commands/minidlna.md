# TAGLINE

DLNA/UPnP 媒体服务器

# TLDR

**启动服务器**

```minidlnad```

**指定配置文件**

```minidlnad -f [/etc/minidlna.conf]```

**前台模式**

```minidlnad -d```

**重新扫描媒体**

```minidlnad -R```

**指定端口**

```minidlnad -p [8200]```

**重建数据库**

```minidlnad -R -f [config.conf]```

# SYNOPSIS

**minidlnad** [_options_]

# PARAMETERS

**-f** _FILE_
> 配置文件。

**-d**
> 调试/前台模式。

**-R**
> 重新扫描媒体文件。

**-p** _PORT_
> HTTP 端口。

**-r**
> 强制重新扫描。

**--help**
> 显示帮助信息。

# DESCRIPTION

**minidlna** 是一个 DLNA/UPnP 媒体服务器。它向电视和设备流式传输媒体。

该工具提供音频、视频和图片服务。兼容大多数支持 DLNA 的设备。

# CAVEATS

需要配置文件。转码功能有限。数据库位于 /var/cache。

# HISTORY

MiniDLNA（ReadyMedia）作为面向嵌入式系统的轻量级 **DLNA** 服务器而创建。

# INSTALL

```dnf: sudo dnf install minidlna```

```pacman: sudo pacman -S minidlna```

```zypper: sudo zypper install minidlna```

```brew: brew install minidlna```

```nix: nix profile install nixpkgs#minidlna```

<!-- packages: 2026-07-22 -->

# SEE ALSO

