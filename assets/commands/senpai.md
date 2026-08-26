# TAGLINE

针对 bouncer 优化的现代终端 IRC 客户端

# TLDR

**启动 IRC 客户端**

```senpai```

**以调试日志启动**

```senpai -debug```

# SYNOPSIS

**senpai** [_options_]

# DESCRIPTION

**senpai** 是一款现代 IRC 客户端，专为配合 soju 等 bouncer 使用而设计。它通过 CHATHISTORY 从服务器获取历史记录，通过 bouncer-networks 发现网络，通过 SEARCH 支持消息搜索，并通过 FILEHOST 支持拖放上传文件。首次启动时会有配置向导引导完成设置。

# CAVEATS

主要面向基于 bouncer 的工作流设计。需要支持良好 Unicode 的终端。

# HISTORY

**senpai** 最初由 **taiite** 创建，现由 **delthas** 维护。它使用 **Go** 编写。

# INSTALL

```apt: sudo apt install senpai```

```pacman: sudo pacman -S senpai```

```apk: sudo apk add senpai```

```zypper: sudo zypper install senpai```

```brew: brew install senpai```

```nix: nix profile install nixpkgs#senpai```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[weechat](/man/weechat)(1), [irssi](/man/irssi)(1)
