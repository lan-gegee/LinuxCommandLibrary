# TAGLINE

带服务监督的跨平台 Unix init 方案

# TLDR

**启动 runit init**

```runit```

**作为阶段 2 运行**

```runsvdir -P [/etc/service]```

**检查服务状态**

```sv status [service_name]```

**启动服务**

```sv start [service_name]```

**停止服务**

```sv stop [service_name]```

**重启服务**

```sv restart [service_name]```

# SYNOPSIS

**runit** [_options_]

**sv** _command_ _service_

# COMMANDS

**sv start** _SERVICE_
> 启动服务。

**sv stop** _SERVICE_
> 停止服务。

**sv restart** _SERVICE_
> 重启服务。

**sv status** _SERVICE_
> 检查状态。

**sv reload** _SERVICE_
> 发送 SIGHUP 信号。

**sv once** _SERVICE_
> 只运行一次，不自动重启。

# DESCRIPTION

**runit** 是一个带服务监督功能的 Unix init 方案。它是 systemd 和 SysV init 的替代品。

系统启动由三个阶段处理。阶段 1 进行初始化，阶段 2 运行服务，阶段 3 执行关机。

服务目录中包含 run 脚本。一个简单的可执行脚本即可定义一个服务。

监督机制会重启崩溃的服务。自动恢复维持了系统的可用性。

日志与 svlogd 集成。每个服务都有独立的日志轮转和管理。

# SERVICE STRUCTURE

- `/etc/service/name/run` - 服务脚本
- `/etc/service/name/log/run` - 日志脚本
- `/etc/service/name/supervise/` - 状态目录

# CONFIGURATION

**/etc/service/**
> 默认的服务目录，指向服务定义的符号链接放在这里。每个子目录代表一个受监督的服务。

**/etc/sv/**
> 服务定义目录，包含每个服务的 run 脚本以及可选的 log/run 脚本。

**/etc/runit/1**
> 阶段 1 脚本，在系统初始化期间、服务启动之前执行。

**/etc/runit/2**
> 阶段 2 脚本，用于启动服务监督器（通常是 runsvdir）。

**/etc/runit/3**
> 阶段 3 脚本，在系统关机期间执行清理任务。

# CAVEATS

语法与 systemd 不同。编写 run 脚本有一定学习曲线。普及程度不如 systemd。

# HISTORY

**runit** 由 **Gerrit Pape** 于 **2004 年**前后创建，是一个轻量级 init 系统。Void Linux 将其用作默认 init，许多发行版也提供该软件。

# INSTALL

```apt: sudo apt install runit```

```apk: sudo apk add runit```

```brew: brew install runit```

```nix: nix profile install nixpkgs#runit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sv](/man/sv)(1), [runsv](/man/runsv)(1), [runsvdir](/man/runsvdir)(1), [svlogd](/man/svlogd)(8)
