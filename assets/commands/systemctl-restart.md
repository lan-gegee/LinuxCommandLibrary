# TAGLINE

停止并重启 systemd 单元

# TLDR

**重启**一个单元

```systemctl restart [unit]```

重启**多个**单元

```systemctl restart [unit1] [unit2]```

重启一个**用户**单元

```systemctl restart [unit] --user```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **restart** _PATTERN_...

# PARAMETERS

**--user**
> 重启用户服务管理器的单元而不是系统单元

**--no-block**
> 不等待操作完成

**--job-mode=**_MODE_
> 指定如何处理已排队的任务

# DESCRIPTION

**systemctl restart** 先停止再启动 systemd 单元。当服务需要完全重启才能应用配置更改或从错误状态恢复时，此命令非常有用。

与 **systemctl reload** 不同，restart 会完全停止服务进程并启动新进程。这会造成短暂中断，但能确保干净的重启。它也可用于已停止的单元，但为避免意外重启正在运行的服务，使用 **systemctl start** 更稳妥。

# CAVEATS

对系统单元操作需要 root 权限。重启期间服务会中断。如果服务支持且需要无中断地应用配置，请使用 **systemctl reload**。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-start](/man/systemctl-start)(1), [systemctl-reload](/man/systemctl-reload)(1)
