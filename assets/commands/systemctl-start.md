# TAGLINE

启动 systemd 单元

# TLDR

立即**启动**一个系统单元

```systemctl start [unit]```

在**用户**管理器中启动一个单元

```systemctl --user start [unit]```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **start** _PATTERN_...

# PARAMETERS

**--user**
> 启动用户服务管理器的单元而不是系统单元

**--no-block**
> 不等待操作完成

**--job-mode=**_MODE_
> 指定如何处理已排队的任务（fail、replace 等）

# DESCRIPTION

**systemctl start** 激活 systemd 单元：启动服务、挂载文件系统或激活其他类型的单元。该命令会为指定单元及其依赖排入一个启动任务。

对于服务，这会启动服务进程；对于套接字，这会开始监听；对于挂载点，这会挂载文件系统。依赖项会按需自动启动。

# CAVEATS

对系统单元操作需要 root 权限。启动一个单元并不会让它开机自启；要实现持久化请使用 **systemctl enable**。某些单元可能存在必须先满足的依赖。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-stop](/man/systemctl-stop)(1), [systemctl-enable](/man/systemctl-enable)(1)
