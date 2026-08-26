# TAGLINE

Matrix 通信协议的 CLI 客户端

# TLDR

**登录并创建会话**

```matrix-commander --login password```

**发送文本消息**

```matrix-commander -m "[message]" -r "[!roomid:server]"```

**发送文件**

```matrix-commander -f [file.pdf] -r "[!roomid:server]"```

**发送图片**

```matrix-commander -i [image.jpg] -r "[!roomid:server]"```

**监听消息**

```matrix-commander --listen once```

**列出房间**

```matrix-commander --rooms```

# SYNOPSIS

**matrix-commander** [_options_]

# PARAMETERS

**--login** _method_
> 登录（password、sso）。

**-m**, **--message** _text_
> 发送文本消息。

**-r**, **--room** _id_
> 目标房间 ID。

**-f**, **--file** _file_
> 发送文件。

**-i**, **--image** _file_
> 发送图片。

**--listen** _mode_
> 监听消息。

**--rooms**
> 列出已加入的房间。

**--verify**
> 验证设备。

**--logout**
> 结束会话。

# DESCRIPTION

**matrix-commander** 是 Matrix 通信协议的 CLI 客户端。它可以在脚本和自动化中发送消息、文件和图片，并能监听传入的消息。

非常适合机器人、通知以及脚本化的 Matrix 交互。

# CONFIGURATION

```
~/.config/matrix-commander/
├── credentials.json
└── store/
```

# CAVEATS

需要 Python 3。必须先创建会话。加密需要验证。发消息需要房间 ID。

# HISTORY

matrix-commander 的创建目的是为 Matrix 提供一个简单的命令行界面，使 shell 脚本和自动化能够与 Matrix 协议交互。

# INSTALL

```nix: nix profile install nixpkgs#matrix-commander```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gomuks](/man/gomuks)(1), [weechat](/man/weechat)(1)
