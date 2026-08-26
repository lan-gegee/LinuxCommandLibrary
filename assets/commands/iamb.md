# TAGLINE

为 Vim 爱好者打造的 Matrix 聊天客户端

# TLDR

**启动 iamb**

```iamb```

以指定配置文件**启动**

```iamb -P [profile_name]```

# SYNOPSIS

**iamb** [**-P** _profile_] [_options_]

# DESCRIPTION

**iamb** 是一款基于终端、采用 **Vim** 按键绑定的 **Matrix** 聊天客户端。它支持话题串（threads）、空间（spaces）、端到端加密（E2EE）、图片预览（在支持 sixel、Kitty 或 iTerm2 协议的终端中），以及完整的房间管理，包括创建、加入、退出房间和处理邀请。

该客户端提供消息编辑、撤回、表情回应以及房间导航，均使用熟悉的 Vim 动作和命令。支持自定义按键绑定和多配置文件。

# CAVEATS

需要 Matrix 主服务器账户。端到端加密的密钥管理可能比较复杂。图片预览质量取决于终端能力。

# HISTORY

**iamb** 由 **Ulyssa** 创建，用 **Rust** 编写，基于 **matrix-rust-sdk**。它面向偏好模态编辑的用户，让他们无需离开终端即可使用键盘驱动的 Matrix 客户端。

# INSTALL

```apk: sudo apk add iamb```

```zypper: sudo zypper install iamb```

```brew: brew install iamb```

```nix: nix profile install nixpkgs#iamb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[weechat](/man/weechat)(1), [gurk](/man/gurk)(1)
