# TAGLINE

Bluesky 社交网络的 TUI 客户端

# TLDR

**启动 Bluesky TUI 客户端**

```tuisky```

**指定配置文件**

```tuisky -c [path/to/config.toml]```

**设置最大列数**

```tuisky -n [3]```

**显示版本**

```tuisky -V```

# SYNOPSIS

**tuisky** [_options_]

# PARAMETERS

**-c**, **--config** _CONFIG_
> 配置文件路径。

**-n**, **--num-columns** _NUM_
> 最大显示列数（未设置时根据终端宽度自动确定）。

**-h**, **--help**
> 打印帮助信息。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**tuisky** 是 Bluesky 的终端用户界面客户端。它支持多栏布局、多会话管理、置顶信息流选择、自动刷新、带文本和图片的帖子发布、通知和聊天，以及可自动保存与恢复的可配置设置。

# HISTORY

**tuisky** 由 **sugyan** 创建，用 **Rust** 和 ratatui TUI 框架编写。

# INSTALL

```brew: brew install tuisky```

```nix: nix profile install nixpkgs#tuisky```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toot](/man/toot)(1), [servitor](/man/servitor)(1)
