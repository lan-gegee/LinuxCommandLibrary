# TAGLINE

终端中的 Twitch 聊天客户端

# TLDR

**启动 Twitch 聊天 TUI**

```twt```

**显示帮助**

```twt --help```

**显示版本**

```twt --version```

**连接到指定频道**

```twt -c [channel_name]```

**使用自定义配置文件**

```twt --config [path/to/config.toml]```

# SYNOPSIS

**twt** [_options_]

# PARAMETERS

**-c** _CHANNEL_, **--channel** _CHANNEL_
> 启动时连接的频道（覆盖配置文件设置）。

**-C** _PATH_, **--config** _PATH_
> 自定义配置文件的路径。

**-t** _TOKEN_, **--token** _TOKEN_
> Twitch OAuth token（覆盖配置文件中的 token）。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**twitch-tui** 是一个用于阅读和参与 Twitch 聊天的终端用户界面。它的按键绑定受 Vim 和 Emacs 启发，设计上与 streamlink 配合使用，让你观看 Twitch 直播时无需打开浏览器。

配置通过首次运行时生成的 TOML 配置文件管理。配置文件控制频道、外观和按键绑定。

# CONFIGURATION

**~/.config/twt/config.toml**
> 主配置文件，包含频道、外观和按键绑定设置。

# HISTORY

**twitch-tui** 由 **Xithrius** 开发，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S twitch-tui```

```nix: nix profile install nixpkgs#twitch-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[streamlink](/man/streamlink)(1), [irssi](/man/irssi)(1), [weechat](/man/weechat)(1)
