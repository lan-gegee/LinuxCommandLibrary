# TAGLINE

设置默认启动 target

# TLDR

设置**默认**启动 target

```systemctl set-default [target.target]```

以**图形界面**模式启动

```systemctl set-default graphical.target```

以**命令行**模式启动

```systemctl set-default multi-user.target```

# SYNOPSIS

**systemctl set-default** _TARGET_

# DESCRIPTION

**systemctl set-default** 通过在 `/etc/systemd/system/default.target` 创建指向指定 target 的符号链接，来设置系统开机默认进入的 target。

常见的 target 包括 `graphical.target`（带显示管理器的图形界面环境）和 `multi-user.target`（带网络功能的文本模式多用户环境）。

# COMMON TARGETS

**graphical.target** - 完整的图形用户界面

**multi-user.target** - 文本模式多用户环境

**rescue.target** - 单用户救援 Shell

**emergency.target** - 最小化的紧急 Shell

# CAVEATS

需要 root 权限。在下次启动时生效，不影响当前正在运行的系统。若要立即切换 target，请使用 `systemctl isolate`。

# HISTORY

**set-default** 子命令取代了传统的运行级别配置，提供了一种简单方式来控制系统开机进入哪个 target（相当于运行级别）。

# SEE ALSO

[systemctl-get-default](/man/systemctl-get-default)(1), [systemctl-isolate](/man/systemctl-isolate)(1), [systemctl](/man/systemctl)(1)
