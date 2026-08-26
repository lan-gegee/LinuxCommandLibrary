# TAGLINE

基于控制台的多协议聊天客户端

# TLDR

**启动** finch

```finch```

**退出** finch

```<Alt q>|<Ctrl c>```

显示**操作**菜单

```<Alt a>```

跳转到第 **n** 个窗口

```<Alt [Number]>```

**关闭**当前窗口

```<Alt c>```

开始**移动**窗口

```<Alt m>```

开始**调整窗口大小**

```<Alt r>```

# SYNOPSIS

**finch** [_options_]

# DESCRIPTION

**finch** 是一个基于控制台的模块化即时通讯客户端，使用 libpurple 库（与 Pidgin 相同）。它支持多种协议，包括 XMPP、IRC 以及各类专有服务。

它是 Pidgin 图形客户端的纯文本替代品。

# PARAMETERS

**-c, --config** _dir_
> 使用备用配置目录

**-d, --debug**
> 启用调试输出

**-v, --version**
> 显示版本

# CONFIGURATION

**~/.purple/prefs.xml**
> 与 Pidgin 共享的 libpurple 首选项。

**~/.purple/accounts.xml**
> 账户凭据与连接设置。

**~/.gntrc**
> GNT（finch）界面的按键绑定与窗口行为。

# CAVEATS

需要 ncurses 库。它与 Pidgin 使用相同的 libpurple 插件。若使用相同的配置目录，账户配置将与 Pidgin 共享。

# INSTALL

```apt: sudo apt install finch```

```dnf: sudo dnf install finch```

```apk: sudo apk add finch```

```zypper: sudo zypper install finch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[irssi](/man/irssi)(1), [weechat](/man/weechat)(1)
