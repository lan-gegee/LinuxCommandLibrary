# TAGLINE

停止 systemd 单元

# TLDR

**停止**一个正在运行的系统单元

```systemctl stop [unit]```

停止由**用户**实例管理的单元

```systemctl --user stop [unit]```

停止时**抑制**某些警告

```systemctl stop --no-warn [unit]```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **stop** _PATTERN_...

# PARAMETERS

**--user**
> 停止用户服务管理器的单元而不是系统单元

**--no-block**
> 不等待操作完成

**--no-warn**
> 抑制关于停止正在运行单元的警告

**--job-mode=**_MODE_
> 指定如何处理已排队的任务

# DESCRIPTION

**systemctl stop** 停用 systemd 单元：停止服务、卸载文件系统或停用其他类型的单元。该命令会为指定单元排入一个停止任务。

对于服务，这会发送停止命令（通常是先发 SIGTERM，超时后再发 SIGKILL）。单元会转换为 inactive 状态。依赖它的单元不会被自动停止，除非它们离开被停单元便无法工作。

# CAVEATS

对系统单元操作需要 root 权限。停止一个单元并不会禁用它；如果它已被启用，下次开机时仍可能重启。某些服务的优雅停止需要一些时间。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-start](/man/systemctl-start)(1), [systemctl-restart](/man/systemctl-restart)(1)
