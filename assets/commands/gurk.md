# TAGLINE

终端上的 Signal Messenger 客户端

# TLDR

**启动 gurk** 并链接 Signal 账户

```gurk```

**使用指定的配置文件启动**

```gurk --config [path/to/config.toml]```

# SYNOPSIS

**gurk** [**--config** _path_]

# DESCRIPTION

**gurk** 是一款完全运行在终端中的 Signal Messenger 客户端。它提供 TUI 界面，通过 Signal 协议收发加密消息，同时支持单聊和群聊。

首次启动时，gurk 会显示一个**二维码**，用 Signal 手机应用扫描即可将该终端客户端绑定为附属设备。绑定成功后，消息会在设备间同步，你可以使用键盘快捷键管理会话。

该客户端将数据和配置存储在本地目录中，并支持通过 TOML 配置文件自定义按键绑定。

# CAVEATS

需要一个移动设备上已有的 Signal 账户用于绑定。不支持创建新的 Signal 账户。语音/视频通话和快照等部分 Signal 功能在终端客户端中不可用。绑定之前的历史消息不会同步。

# HISTORY

**gurk**（gurk-rs）由 **boxdot** 创建，使用 **Rust** 编写。其名称是德语俚语"黄瓜"的意思。它是唯一仍在活跃维护的终端 Signal 客户端，为无头系统和以终端为中心的工作流提供注重隐私的消息传递功能。

# INSTALL

```pacman: sudo pacman -S gurk```

```brew: brew install gurk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iamb](/man/iamb)(1), [weechat](/man/weechat)(1)
