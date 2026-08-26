# TAGLINE

显示默认引导 target

# TLDR

显示**默认 target**

```systemctl get-default```

# SYNOPSIS

**systemctl get-default**

# DESCRIPTION

**systemctl get-default** 显示系统启动时进入的默认 target（等价于运行级别）。常见 target 包括 `graphical.target`（图形界面环境）、`multi-user.target`（文本模式多用户）和 `rescue.target`（单用户恢复）。

默认 target 由 `/etc/systemd/system/default.target` 处的符号链接决定。

# CAVEATS

只显示已配置的默认值，而非当前活动的 target。使用 `systemctl list-units --type=target` 查看当前活动的 target。

# HISTORY

**get-default** 子命令提供了一种查看系统引导 target 的简单方式，取代了传统的 `/etc/inittab` 运行级别配置检查。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-set-default](/man/systemctl-set-default)(1), [systemctl-default](/man/systemctl-default)(1)
