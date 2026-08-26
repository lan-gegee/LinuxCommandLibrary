# TAGLINE

Signal 即时通讯软件的简易终端用户界面

# TLDR

**启动 Signal TUI**

```scli```

**启动时保存会话历史**

```scli -s```

**将 scli 与现有 Signal 账户关联**

```scli link --name "[my-laptop]"```

# SYNOPSIS

**scli** [_options_]

# PARAMETERS

**-s**, **--save-history**
> 启用会话历史保存。

**--enable-notifications**
> 开启桌面通知。

**--color**
> 以标准或 256 色模式为消息着色。

**--wrap-at** _NUM_
> 文本换行宽度。

**--editor-command** _CMD_
> 用于撰写消息的自定义编辑器命令。

# DESCRIPTION

**scli** 是 Signal 即时通讯软件的 TUI，以 **signal-cli** 为后端、urwid 为界面。它具备类 Vim 导航、emoji 表情回应、远程删除消息、带发送者头像的桌面通知，以及撰写消息的外部编辑器支持等功能。

# CAVEATS

需要已安装并注册的 **signal-cli**。受 signal-cli 限制，无法引用消息或添加提及（mention）。不支持语音通话和已读回执。数据以未加密方式存储；建议启用全盘加密。

# HISTORY

**scli** 由 **isamert** 创建，使用 **Python** 编写。

# INSTALL

```nix: nix profile install nixpkgs#scli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toot](/man/toot)(1)
