# TAGLINE

基于终端的 Google Hangouts 客户端（已失效：Hangouts 已于 2022 年关停）

# TLDR

**启动 hangups**（首次运行时会提示 OAuth 登录，随后缓存刷新令牌）

```hangups```

**使用手动（复制粘贴）OAuth 登录流程**

```hangups --manual-login```

**使用自定义配置文件**

```hangups --config [hangups.conf]```

**启用详细调试日志**写入文件

```hangups --debug --log [hangups.log]```

**重新绑定键盘快捷键**，例如退出键

```hangups --key-quit [ctrl q]```

**显示已安装版本**

```hangups --version```

# SYNOPSIS

**hangups** [_options_]

# PARAMETERS

**-c**, **--config** _FILE_
> 配置文件路径。

**-d**, **--debug**
> 记录详细的调试信息。

**--manual-login**
> 使用手动（复制粘贴）OAuth 登录流程，而不是打开浏览器。

**--token-path** _PATH_
> 用于存储缓存 OAuth 刷新令牌的路径。

**--log** _FILE_
> 日志文件路径。

**-D**, **--discreet-notifications**
> 在桌面通知中隐藏消息详情。

**--notification-type** _TYPE_
> 要创建的桌面通知类型。

**--key-quit**, **--key-next-tab**, **--key-prev-tab**, **--key-close-tab**, **--key-menu** _KEY_
> 重新绑定对应操作的按键（默认值：ctrl e、ctrl d、ctrl u、ctrl w、ctrl n）。

**--col-scheme** _NAME_
> 要使用的配色方案。

**--keep-emoticons**
> 不将表情符号替换为对应的 emoji。

**-v**, **--version**
> 打印已安装的 hangups 版本。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**hangups** 是第一款第三方 Google Hangouts 即时通讯客户端，提供了一个 Python 库和一个终端参考客户端（基于 urwid）。它的实现方式是对 Google 私有的 Hangouts 协议进行逆向工程，因此得以支持群聊等基于 XMPP 的客户端所不具备的功能。

# CAVEATS

Google 已于 **2022 年 11 月**关停了消费版 Hangouts，并停用了 hangups 所依赖的 API；该客户端已无法登录或连接，此后项目也未再发布功能性更新（PyPI 上的最后一次发布是 2022 年 4 月的 0.4.18）。目前它仅作为参考资料保留，不再是可用的聊天客户端。

# HISTORY

hangups 由 **Tom Dryer** 创建，首个版本发布于 **2014 年**，是面向终端用户的非官方 Google Hangouts 客户端。在 Hangouts 本身退役之前，不少机器人和桥接工具（HangupsBot、telepathy-hangups）都构建在它的协议库之上。

# SEE ALSO

[weechat](/man/weechat)(1), [irssi](/man/irssi)(1), [finch](/man/finch)(1)

# RESOURCES

```[Source code](https://github.com/tdryer/hangups)```

```[Documentation](https://hangups.readthedocs.io/)```

<!-- verified: 2026-07-17 -->
