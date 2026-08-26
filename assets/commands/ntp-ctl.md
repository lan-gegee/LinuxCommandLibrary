# TAGLINE

控制 OpenNTPD

# TLDR

**显示 NTP 状态**

```ntpctl -s status```

**显示对等服务器**

```ntpctl -s peers```

**显示全部信息**

```ntpctl -s all```

**显示传感器**

```ntpctl -s sensors```

# SYNOPSIS

**ntpctl** [_options_]

# PARAMETERS

**-s** _TYPE_
> 要显示的信息类型。

**status**
> 显示同步状态。

**peers**
> 显示已配置的对等服务器。

**sensors**
> 显示时间传感器。

**all**
> 显示全部信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntpctl** 控制 OpenNTPD，查询时间同步状态。

该工具监控 NTP 守护进程的状态，是只读的控制接口。

# CAVEATS

OpenBSD 特有。配合 OpenNTPD 使用。只读查询。

# HISTORY

ntpctl 作为 OpenBSD 系统上 OpenNTPD 的**控制接口**被开发出来。

# INSTALL

```apt: sudo apt install ntpd-rs```

```dnf: sudo dnf install ntpd-rs```

```pacman: sudo pacman -S ntpd-rs```

```zypper: sudo zypper install ntpd-rs```

```nix: nix profile install nixpkgs#ntpd-rs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntpd](/man/ntpd)(1), [ntpq](/man/ntpq)(1), [chronyc](/man/chronyc)(1)
