# TAGLINE

Steam 命令行专用服务器工具

# TLDR

**启动交互模式**

```steamcmd```

**匿名登录**

```steamcmd +login anonymous```

**安装游戏服务器**

```steamcmd +login anonymous +app_update [740] +quit```

**安装到指定目录**

```steamcmd +force_install_dir [/path/to/server] +login anonymous +app_update [740] +quit```

**校验安装**

```steamcmd +login anonymous +app_update [740] validate +quit```

**使用凭据登录**

```steamcmd +login [username] [password]```

# SYNOPSIS

**steamcmd** [_+command_]...

# PARAMETERS

**+login** _USER_ [_PASS_]
> 登录 Steam。

**+app_update** _APPID_
> 安装/更新应用。

**+force_install_dir** _PATH_
> 安装目录。

**+quit**
> 执行完命令后退出。

**+validate**
> 校验文件。

**+app_info_print** _APPID_
> 显示应用信息。

**+workshop_download_item** _APPID_ _ITEMID_
> 下载创意工坊物品。

# DESCRIPTION

**steamcmd** 是 Valve 的命令行 Steam 客户端，专为自动化管理专用游戏服务器而设计。它支持在不使用完整 Steam 图形客户端的情况下下载、安装、更新和校验游戏服务器文件。

命令以 **+** 为前缀，可以串联起来进行批量操作。对大多数专用服务器的下载而言，匿名登录就足够了；但某些内容需要用拥有该游戏的 Steam 账户进行身份验证。**+app_update** 命令既处理初次安装也处理后续更新，**validate** 用于校验文件完整性并修复损坏的安装。

# COMMON APP IDS

**740** - Counter-Strike: Global Offensive
**232250** - Team Fortress 2
**258550** - Rust
**376030** - ARK

# CAVEATS

某些应用要求拥有对应游戏。下载体积可能很大。SteamGuard 可能需要验证码。

# HISTORY

**SteamCMD** 由 **Valve** 发布，用于无界面（headless）服务器管理。它使游戏服务器的自动化部署无需完整的 Steam 客户端。

# INSTALL

```nix: nix profile install nixpkgs#steamcmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steam](/man/steam)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1)
