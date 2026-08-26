# TAGLINE

终端 Matrix 客户端

# TLDR

**连接**到 Matrix 主服务器

```gomuks```

以指定用户身份**连接**

```gomuks -u [@user:example.com]```

**连接**到指定的服务器

```gomuks -s [https://matrix.example.com]```

# SYNOPSIS

**gomuks** [_options_]

# PARAMETERS

**-u, --user** _MXID_
> Matrix 用户 ID（@user:server）

**-s, --server** _URL_
> 主服务器 URL

**-c, --config** _FILE_
> 配置文件的路径

**-d, --debug**
> 启用调试日志

**--version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gomuks** 是一个基于终端的 Matrix 客户端。它为 Matrix 协议提供文本界面，支持端到端加密、房间、私信和文件分享。

该客户端专为偏好终端工作流、不需要 GUI 即可使用 Matrix 的用户设计。

# KEYBINDINGS

**↑/↓**
> 在消息之间导航

**Tab**
> 在房间之间切换

**Ctrl+N**
> 跳到下一个有未读消息的房间

**Ctrl+P**
> 上一个房间

**/**
> 搜索消息

**: or /**
> 命令模式

**q**
> 退出

**?**
> 显示帮助

# COMMANDS

**/join** _#room:server_
> 加入一个房间

**/part**
> 离开当前房间

**/nick** _name_
> 更改显示名称

**/me** _action_
> 发送动作消息

**/react** _emoji_
> 对消息添加表情回应

# CAVEATS

端到端加密需要完成设备验证。部分 Matrix 功能可能不受支持。终端中媒体内容的显示能力有限。需要拥有 Matrix 账户。

# HISTORY

**gomuks** 作为一款终端 Matrix 客户端诞生，面向偏好 CLI 类通信工具的用户。

# INSTALL

```apt: sudo apt install gomuks```

```pacman: sudo pacman -S gomuks```

```apk: sudo apk add gomuks```

```zypper: sudo zypper install gomuks```

```nix: nix profile install nixpkgs#gomuks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[element](https://element.io/), [fractal](https://gitlab.gnome.org/GNOME/fractal), [matrix-spec](https://spec.matrix.org/)
