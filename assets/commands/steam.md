# TAGLINE

Valve 游戏平台客户端

# TLDR

**启动 Steam**

```steam```

**启动指定游戏**

```steam steam://rungameid/[app_id]```

**打开大屏幕模式**

```steam -bigpicture```

**以离线模式运行**

```steam -offline```

**清除下载缓存**

```steam steam://flushconfig```

**打开游戏商店页面**

```steam steam://store/[app_id]```

**验证游戏文件**

```steam steam://validate/[app_id]```

# SYNOPSIS

**steam** [_options_] [_steam://url_]

# PARAMETERS

**-bigpicture**
> 大屏幕模式。

**-offline**
> 离线模式。

**-silent**
> 启动时最小化。

**-login** _USER_ _PASS_
> 自动登录。

**-console**
> 启用控制台。

**-dev**
> 开发者模式。

**-noverifyfiles**
> 跳过验证。

**-tcp**
> 强制使用 TCP。

# STEAM URLS

**steam://rungameid/ID** - 启动游戏
**steam://store/ID** - 商店页面
**steam://validate/ID** - 验证文件
**steam://install/ID** - 安装游戏
**steam://flushconfig** - 清除缓存

# DESCRIPTION

**Steam** 是 Valve 面向 Linux 的游戏平台客户端，提供游戏库管理、自动更新、社交功能以及面向社区内容的 Steam 创意工坊。游戏和应用程序由 app ID 标识，可与 steam:// URL 配合实现直接启动、安装和文件验证。

大屏幕模式提供专为电视和 Steam Deck 设计的对手柄友好的全屏界面。在 Linux 上，Steam 包含 **Proton**——一个基于 Wine 的兼容层，使许多 Windows 游戏得以原生运行。离线模式允许在没有网络连接的情况下玩已下载的游戏。

# CAVEATS

专有软件。部分游戏不支持 Linux。磁盘占用较大。

# HISTORY

**Steam** 由 **Valve Corporation** 于 **2003 年**创建。Linux 支持于 **2013 年**加入，显著扩展了平台上的游戏阵容。

# INSTALL

```nix: nix profile install nixpkgs#steam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steamcmd](/man/steamcmd)(1), [proton](/man/proton)(1), [wine](/man/wine)(1)
