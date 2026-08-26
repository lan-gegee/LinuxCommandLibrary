# TAGLINE

终端中的 Slack 客户端

# TLDR

**使用默认配置启动**

```slack-term```

**使用自定义配置文件启动**

```slack-term -config [/path/to/config]```

**直接使用 Slack token 启动**

```slack-term -token [xoxp-your-slack-token]```

**启用调试模式启动**

```slack-term -debug```

# SYNOPSIS

**slack-term** [**-config** _path_] [**-token** _token_] [**-debug**]

# PARAMETERS

**-config** _path_
> 配置文件的位置。默认为 ~/.config/slack-term/config。

**-token** _token_
> Slack 身份验证 token。会覆盖配置文件中的 token。

**-debug**
> 启用调试模式。

# DESCRIPTION

**slack-term** 为 Slack 提供完整的基于终端的界面。它支持三种模式：使用类 Vim 按键绑定进行导航的命令模式、用于撰写消息的插入模式，以及用于查找内容的搜索模式。它通过 API token 连接到 Slack，提供频道导航、消息收发和通知功能。

# CONFIGURATION

**~/.config/slack-term/config**
> 默认的 JSON 配置文件，包含 Slack API token 和各项设置。

# HISTORY

**slack-term** 由 **J.P. Bruins Slot**（erroneousboat）创建，采用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#slack-term```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[weechat](/man/weechat)(1), [irssi](/man/irssi)(1), [scli](/man/scli)(1), [screen](/man/screen)(1)
