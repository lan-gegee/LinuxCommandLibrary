# TAGLINE

Knot DNS 服务器的控制工具

# TLDR

**查看服务器状态**

```knotc status```

**重新加载服务器配置**

```knotc reload```

**停止 DNS 服务器**

```knotc stop```

**强制区域传送**

```knotc zone-retransfer [zone]```

**用 DNSSEC 对区域签名**

```knotc zone-sign [zone]```

**将区域刷入文件**

```knotc zone-flush [zone]```

# SYNOPSIS

**knotc** [_options_] _action_ [_args_...]

# PARAMETERS

**status**
> 检查服务器是否正在运行。

**reload**
> 重新加载配置和区域。

**stop**
> 停止服务器。

**zone-retransfer** _zone_
> 强制从主服务器进行区域传送。

**zone-sign** _zone_
> 触发 DNSSEC 重新签名。

**zone-flush** _zone_
> 将区域日志刷入文件。

**-c** _file_
> 配置文件路径。

**-s** _path_
> 控制套接字路径。

**-t** _seconds_
> 控制超时时间。

# DESCRIPTION

**knotc** 是 Knot DNS 服务器的控制工具。它通过控制套接字与正在运行的 knotd 守护进程通信，以管理区域、检查状态并触发操作。支持带有命令补全的交互模式。

# INSTALL

```apt: sudo apt install knot```

```dnf: sudo dnf install knot```

```pacman: sudo pacman -S knot```

```apk: sudo apk add knot```

```zypper: sudo zypper install knot```

```brew: brew install knot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kdig](/man/kdig)(1)
