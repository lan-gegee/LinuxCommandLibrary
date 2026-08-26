# TAGLINE

向服务管理器通知状态变化

# TLDR

**通知** systemd 服务已完成初始化

```systemd-notify --booted```

**告知** systemd 服务已就绪

```systemd-notify --ready```

**提供**自定义状态消息给 systemd

```systemd-notify --status "[Add custom status message here...]"```

# SYNOPSIS

**systemd-notify** [_options_] [_variable=value_...]

# PARAMETERS

**--ready**
> 向 systemd 发出服务就绪信号

**--booted**
> 检查系统是否以 systemd 启动

**--status _text_**
> 向服务管理器发送状态文本

**--pid _pid_**
> 告知守护进程的主 PID

**--uid _user_**
> 指定发送通知所用的用户

**--reloading**
> 发出服务正在重新加载配置的信号

**--stopping**
> 发出服务正在停止的信号

# DESCRIPTION

**systemd-notify** 向服务管理器通知启动完成及其他守护进程状态变化。它主要用于 **Type=notify** 类型服务的 systemd 服务脚本中。

通过 **--status** 提供的状态文本会显示在 **systemctl status** 中。这使服务能够向管理员传达其当前状态与进度。

# CAVEATS

仅在 systemd 服务上下文中有用。服务必须在其单元文件中配置为 **Type=notify** 或 **Type=notify-reload**。在 systemd 服务之外运行时不起作用。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1)
