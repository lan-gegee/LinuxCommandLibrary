# TAGLINE

带自动重启功能的 collectd 监控守护进程包装器

# TLDR

**以守护进程方式启动 collectd**

```collectdmon```

**使用指定的配置文件启动**

```collectdmon -c [/etc/collectd.conf]```

**在前台启动**

```collectdmon -f```

**崩溃时重启 collectd**

```collectdmon -P [/var/run/collectd.pid]```

# SYNOPSIS

**collectdmon** [_options_]

# DESCRIPTION

**collectdmon** 是 collectd 的监控守护进程包装器。它监视 collectd 进程，并在其意外终止时自动重启。

该守护进程通过维持 collectd 的持续运行来确保指标收集不间断。它会恰当地处理信号并将其转发给子 collectd 进程。

# PARAMETERS

**-c** _file_
> collectd 配置文件路径。

**-P** _file_
> PID 文件路径。

**-f**
> 在前台运行（不守护进程化）。

**-h**
> 显示帮助信息。

# CONFIGURATION

**/etc/collectd.conf**
> 传递给被监控 collectd 进程的配置文件。

# CAVEATS

需要已安装 collectd。collectd 的配置问题会导致反复重启循环。PID 文件位置需要适当的权限。

# HISTORY

**collectdmon** 属于 **collectd** 项目——一个由 **Florian Forster** 于 **2005 年**创建的系统统计信息收集守护进程。该监控包装器为生产环境中对指标连续性要求苛刻的部署提供了可靠性保障。

# INSTALL

```apt: sudo apt install collectd-core```

```dnf: sudo dnf install collectd```

```apk: sudo apk add collectd```

```zypper: sudo zypper install collectd```

```brew: brew install collectd```

```nix: nix profile install nixpkgs#collectd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[collectd](/man/collectd)(1)
