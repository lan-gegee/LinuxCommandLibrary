# TAGLINE

以可脚本化和可定制主题著称的终端 IRC 客户端

# TLDR

**启动 irssi**

```irssi```

**连接到服务器**

```irssi -c [irc.libera.chat]```

**使用指定昵称连接**

```irssi -c [irc.libera.chat] -n [nickname]```

**通过 SSL 连接到服务器**

```irssi -c [irc.libera.chat] -p [6697] --ssl```

**使用指定的配置文件**

```irssi --config=[path/to/config]```

**启动时执行命令**

```irssi -c [server] -e "/join #[channel]"```

# SYNOPSIS

**irssi** [_-c server_] [_-p port_] [_-n nick_] [_--ssl_] [_--config file_] [_-e command_]

# PARAMETERS

**-c**, **--connect** _server_
> 启动时连接到服务器。

**-p**, **--port** _port_
> 服务器端口号。

**-n**, **--nick** _nick_
> 要使用的昵称。

**-w**, **--password** _password_
> 服务器密码。

**--ssl**
> 使用 SSL/TLS 连接。

**--ssl-verify**
> 验证 SSL 证书。

**--config** _file_
> 使用其他配置文件。

**--home** _dir_
> 使用其他 irssi 主目录。

**-e**, **--exec** _command_
> 启动时执行 irssi 命令。

**--noconnect**
> 启动时不连接任何服务器。

# IRSSI COMMANDS

**/connect** _server_
> 连接到服务器。

**/disconnect**
> 断开当前服务器的连接。

**/join** _#channel_
> 加入频道。

**/part** [_#channel_]
> 离开频道。

**/msg** _nick message_
> 发送私信。

**/query** _nick_
> 打开私聊窗口。

**/quit** [_message_]
> 退出 irssi。

**/window** _number_
> 切换到指定编号的窗口。

**/wc**
> 关闭当前窗口。

**/names**
> 列出频道中的用户。

**/whois** _nick_
> 获取用户信息。

**/set** _option value_
> 修改设置。

**/save**
> 保存配置。

**/script load** _name_
> 加载 Perl 脚本。

# DESCRIPTION

**irssi** 是一款终端 IRC 客户端，以可脚本化、可定制主题和高效著称。它完全运行在终端中，支持多个并发连接、窗口和频道。

界面采用多窗口系统：按 Alt+数字（或 Ctrl+N/P）可在窗口间切换。每个频道、私聊和服务器状态都拥有自己的窗口。状态栏用不同颜色的高亮显示窗口活动。

配置保存在 **~/.irssi/config** 中，可通过 /set 命令或直接编辑文件修改。设置项包括昵称、备用昵称、退出消息、高亮规则和服务器配置。可以预定义网络和服务器以便快速连接。

irssi 的 Perl 脚本接口支持深度自定义。脚本可以添加命令、修改行为、与外部服务集成或实现机器人。社区已有大量脚本可供常见需求使用。

为了保持连接不断，irssi 通常在服务器上的终端复用器（screen、tmux）中运行，这样即使断开连接也不会丢失聊天会话。

# CAVEATS

键盘导航有一定学习成本。默认按键绑定可能与 terminal/screen 冲突。部分脚本需要额外的 Perl 模块。没有内置 GUI——纯终端程序。在较旧的系统上可能需要显式配置 UTF-8 支持。

# HISTORY

**irssi** 由 Timo Sirainen 于 **1999 年**前后创建，是一款模块化、可脚本化的 IRC 客户端。其名称来自 IRC 加上芬兰语的 "ii" 词尾。它已成为最受欢迎的终端 IRC 客户端之一，以稳定性和可扩展性著称。开发仍在继续，定期发布维护版本。

# INSTALL

```apt: sudo apt install irssi```

```dnf: sudo dnf install irssi```

```pacman: sudo pacman -S irssi```

```apk: sudo apk add irssi```

```zypper: sudo zypper install irssi```

```brew: brew install irssi```

```nix: nix profile install nixpkgs#irssi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[weechat](/man/weechat)(1), [screen](/man/screen)(1), [tmux](/man/tmux)(1), [hexchat](/man/hexchat)(1)
