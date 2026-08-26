# TAGLINE

可扩展的终端聊天客户端

# TLDR

**启动 WeeChat**

```weechat```

**连接 IRC 服务器**

```/connect [irc.libera.chat]```

**加入频道**

```/join [#channel]```

**发送私信**

```/msg [nickname] [message]```

**以指定的配置目录启动**

```weechat -d [~/.config/weechat]```

**启动时运行命令**

```weechat -r "/connect libera"```

**设置昵称**

```/set irc.server.libera.nicks "[mynick]"```

**退出 WeeChat**

```/quit```

# SYNOPSIS

**weechat** [_-d directory_] [_-r command_] [_-p_] [_options_]

# PARAMETERS

**-a**, **--no-connect**
> 禁用自动连接服务器。

**-c**, **--colors**
> 在终端中显示颜色。

**-d**, **--dir** _DIR_
> 设置配置目录。

**-p**, **--no-plugin**
> 不加载插件。

**-P**, **--plugins** _LIST_
> 只加载指定的插件。

**-r**, **--run-command** _CMD_
> 启动后运行命令。

**-s**, **--no-script**
> 不加载脚本。

**-t**, **--temp-dir**
> 使用临时目录。

**-u**, **--upgrade**
> 从上一次会话升级恢复。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# COMMANDS

**/connect** _SERVER_
> 连接服务器。

**/disconnect**
> 断开与服务器的连接。

**/join** _CHANNEL_
> 加入频道。

**/part** [_CHANNEL_]
> 离开频道。

**/msg** _TARGET_ _MESSAGE_
> 发送消息。

**/query** _NICK_
> 打开私聊会话。

**/nick** _NEWNICK_
> 更改昵称。

**/set** _OPTION_ [_VALUE_]
> 设置配置选项。

**/save**
> 保存配置。

**/quit**
> 退出 WeeChat。

**/help** [_COMMAND_]
> 显示帮助。

# DESCRIPTION

**WeeChat**（Wee Enhanced Environment for Chat）是一款可扩展的终端聊天客户端。虽然它主要是一个 IRC 客户端，但通过插件可以扩展支持 Matrix、Slack、Discord 以及其他协议。

界面使用多个缓冲区来管理频道、私信和服务器控制台。使用 Alt+方向键或缓冲区编号进行导航。窗口可以水平或垂直分割。

通过 /set 进行的配置覆盖一切：颜色、按键绑定、网络设置和插件选项。更改立即生效；/save 将其持久化。

脚本可用 Python、Perl、Ruby、Lua 等语言扩展功能。流行的脚本提供通知、自动加入频道、URL 处理和协议桥接等功能。脚本仓库汇集了社区贡献。

relay 插件允许从其他客户端或移动应用远程访问。这提供了一个持久连接，移动设备可以随时断开和重连。

安全特性包括 SASL 身份验证、SSL/TLS 和代理支持。密码处理与系统钥匙串集成。

# CAVEATS

命令和配置有一定学习曲线。某些功能需要插件/脚本。移动端使用需要设置 relay。默认配色未必适合所有终端。尽管支持多协议，仍以 IRC 为核心。

# HISTORY

**WeeChat** 由 **Sébastien Helleu**（FlashCode）于 **2003 年**创建。名称中的 "wee" 意为"小巧"，后来演变为"可扩展环境"之意。它使用 C 语言编写以保证性能，并提供丰富的脚本支持，逐渐成为 irssi 之外广受欢迎的终端聊天选择。

# INSTALL

```apt: sudo apt install weechat-curses```

```dnf: sudo dnf install weechat```

```pacman: sudo pacman -S weechat```

```apk: sudo apk add weechat```

```zypper: sudo zypper install weechat```

```brew: brew install weechat```

```nix: nix profile install nixpkgs#weechat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[irssi](/man/irssi)(1), [hexchat](/man/hexchat)(1), [matrix-commander](/man/matrix-commander)(1)
