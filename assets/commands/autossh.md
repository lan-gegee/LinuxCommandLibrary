# TAGLINE

自动维持持久的 SSH 连接

# TLDR

**创建**持久 SSH 隧道

```autossh -M [20000] -N -L [8080:localhost:80] [user@remote]```

隧道**不使用监控端口**

```autossh -M 0 -N -L [8080:localhost:80] [user@remote]```

**反向**隧道

```autossh -M [20000] -N -R [8080:localhost:80] [user@remote]```

在**后台**运行

```autossh -f -M [20000] -N -L [8080:localhost:80] [user@remote]```

# SYNOPSIS

**autossh** -M _monitor_port_ [_ssh_options_] _destination_

# DESCRIPTION

**autossh** 为 SSH 连接提供自动重连功能。它会监控连接并在连接断开时重启，使 SSH 隧道和连接保持持久。

对于维持长时间运行的 SSH 隧道、远程端口转发和 SOCKS 代理，这个工具必不可少。

# PARAMETERS

**-M** _port_[:_port_]
> 监控端口。使用 -M 0 可禁用端口监控

**-f**
> 认证完成后转入后台

**-N**
> 不执行命令（仅做转发）

**-L** _port_:_host_:_port_
> 本地端口转发

**-R** _port_:_host_:_port_
> 远程端口转发

**-D** _port_
> SOCKS 代理

其余所有 **ssh** 选项均受支持。

# ENVIRONMENT VARIABLES

**AUTOSSH_GATETIME**
> 第一次连接检查前的等待秒数（默认：30）

**AUTOSSH_POLL**
> 轮询间隔秒数（监控禁用时生效）

**AUTOSSH_DEBUG**
> 启用调试日志

# CAVEATS

监控端口在两端都必须空闲。SSH 配置中的 ServerAliveInterval 可以替代监控功能。可能无法检测到所有类型的断连。较新的 SSH 版本已内置保活机制。

# HISTORY

**autossh** 由 Carson Harding 创建，用于解决 SSH 连接无提示中断的问题，于 **2002 年**前后首次发布。

# INSTALL

```apt: sudo apt install autossh```

```dnf: sudo dnf install autossh```

```pacman: sudo pacman -S autossh```

```apk: sudo apk add autossh```

```zypper: sudo zypper install autossh```

```brew: brew install autossh```

```nix: nix profile install nixpkgs#autossh```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ssh](/man/ssh)(1), [tmux](/man/tmux)(1)
