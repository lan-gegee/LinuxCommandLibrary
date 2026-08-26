# TAGLINE

面向 Linux、Windows 和 macOS 的图形化 IRC 客户端

# TLDR

**启动 HexChat**

```hexchat```

**连接到服务器**

```hexchat [irc://irc.libera.chat/channel]```

**以最小化方式启动**

```hexchat --minimize=2```

**指定配置目录**

```hexchat -d [~/.config/hexchat]```

# SYNOPSIS

**hexchat** [_options_] [_url_]

# PARAMETERS

_url_
> 要连接的 IRC URL。

**-d**, **--cfgdir** _dir_
> 配置目录。

**-n**, **--no-plugins**
> 不加载插件。

**--minimize**=_level_
> 以最小化窗口启动：**0** = 不最小化，**1** = 最小化窗口，**2** = 仅最小化到托盘。

**-a**, **--no-auto**
> 启动时不自动连接任何服务器。

**-e**, **--existing**
> 在已有实例中打开。

**--url** _url_
> 连接到指定的 IRC URL。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**HexChat** 是一款面向 Linux、Windows 和 macOS 的图形化 IRC 客户端。它为多个频道和服务器提供标签页界面，具备 DCC 文件传输、脚本扩展和丰富的自定义功能。

HexChat 支持 C、Perl、Python 和 Lua 插件。它是 XChat 的分支，在现代特性上持续开发并获得活跃维护。

# FEATURES

- 频道标签页界面
- DCC 文件传输
- SSL/TLS 支持
- 脚本扩展（Python、Perl、Lua）
- 拼写检查
- 桌面通知
- 自动加入频道和重新连接

# CAVEATS

配置保存在 ~/.config/hexchat 中。IRC 连接可能需要 SSL。某些网络要求注册。插件兼容性因实现而异。

# HISTORY

HexChat 于 **2009 年**从 **XChat** 分支而来，当时 XChat 的 Windows 版本转为共享软件。它由开发者社区维护，是 Linux 上最受欢迎的图形化 IRC 客户端。

# INSTALL

```apt: sudo apt install hexchat```

```dnf: sudo dnf install hexchat```

```zypper: sudo zypper install hexchat```

```nix: nix profile install nixpkgs#hexchat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[irssi](/man/irssi)(1), [weechat](/man/weechat)(1)
