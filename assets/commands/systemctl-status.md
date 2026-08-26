# TAGLINE

显示单元的运行时状态

# TLDR

显示某个 systemd 单元的**状态**

```systemctl status [unit].service```

显示**系统总览**状态

```systemctl status```

显示**多个单元**的状态

```systemctl status [unit1] [unit2]```

按 **PID** 显示状态

```systemctl status [pid]```

显示更多**日志行数**的状态

```systemctl status -n [50] [unit]```

显示**用户单元**的状态

```systemctl status --user [unit]```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **status** [_PATTERN_...|_PID_...]

# PARAMETERS

**--user**
> 查询用户服务管理器而不是系统管理器

**-n**, **--lines=**_NUM_
> 要显示的日志行数

**-o**, **--output=**_MODE_
> 日志输出模式（short、verbose、json 等）

**--no-pager**
> 不将输出送入分页器

**-l**, **--full**
> 不省略单元名称、进程树条目或日志输出

# DESCRIPTION

**systemctl status** 显示 systemd 单元（包括服务、套接字、target 和定时器）的当前状态。它会展示单元是否处于活动状态、是否已启用或已失败，以及来自 journal 的最近日志条目。

不带参数时，它显示系统状态总览。带单元名称时，它提供详细状态，包括主 PID、内存占用、控制组和最近的日志行。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-start](/man/systemctl-start)(1), [systemctl-restart](/man/systemctl-restart)(1), [journalctl](/man/journalctl)(1)
