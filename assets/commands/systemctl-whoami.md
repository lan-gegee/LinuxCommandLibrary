# TAGLINE

显示进程所属的单元

# TLDR

显示**当前** Shell 所在的单元

```systemctl whoami```

查询**用户**服务管理器

```systemctl whoami --user```

显示**特定 PID** 所属的单元

```systemctl whoami [pid]```

显示**多个** PID 所属的单元

```systemctl whoami [pid1 pid2 ...]```

# SYNOPSIS

**systemctl whoami** [_PID_...]

# PARAMETERS

**--user**
> 查询用户服务管理器

**--system**
> 查询系统服务管理器（默认）

# DESCRIPTION

**systemctl whoami** 显示某个进程属于哪个 systemd 单元。不带参数时，它显示当前 Shell（运行 systemctl 的那个进程）所属的单元。

指定 PID 时，它会显示这些进程所属的单元。这有助于识别特定进程由哪个服务或 scope 拥有。

# CAVEATS

不受 systemd 管理的进程可能显示为属于 root slice，或没有关联的单元。容器中的进程显示方式可能不同。

# HISTORY

**whoami** 子命令提供了一种快速识别进程运行于哪个单元之下的方法，可用于调试和理解 cgroup 归属关系。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl-status](/man/systemctl-status)(1), [systemctl](/man/systemctl)(1), [ps](/man/ps)(1)
