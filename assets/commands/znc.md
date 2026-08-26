# TAGLINE

高级 IRC bouncer 守护进程

# TLDR

运行**初始设置**

```znc -c```

**启动**守护进程

```znc```

为 **systemd** 做设置

```sudo -u znc znc -c -d /var/lib/znc```

设置**开机**自启

```systemctl enable znc --now```

# SYNOPSIS

**znc** [_OPTIONS_]

# PARAMETERS

**-c, --makeconf**
> 运行初始配置向导

**-d, --datadir** _DIR_
> 使用指定的数据目录

**-f, --foreground**
> 在前台运行（不作为守护进程）

**-D, --debug**
> 启用调试输出

# DESCRIPTION

**znc** 是一个 IRC bouncer，替你与 IRC 服务器保持持久连接。当你的 IRC 客户端断开连接时，ZNC 保持在线并缓存所有消息、频道动态和通知，等你重新连接后再回放。

ZNC 支持同时连接多个 IRC 网络和多个用户账户，因此既适合个人使用，也适合多人共用的部署。它提供 SSL/TLS 加密、基于 Web 的管理界面，以及丰富的模块系统，可用于日志记录、自动回复和客户端脚本等功能。

初始配置通过 **-c** 标志交互式完成，它会引导你逐步设置网络、用户和端口。配置完成后，ZNC 默认作为后台守护进程运行。

# CAVEATS

需要先通过 -c 标志完成初始设置。Web 界面可通过配置的端口访问。持续运行需要一台常驻服务器。

# INSTALL

```apt: sudo apt install znc```

```dnf: sudo dnf install znc```

```pacman: sudo pacman -S znc```

```apk: sudo apk add znc```

```zypper: sudo zypper install znc```

```brew: brew install znc```

```nix: nix profile install nixpkgs#znc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[irssi](/man/irssi)(1), [weechat](/man/weechat)(1)
