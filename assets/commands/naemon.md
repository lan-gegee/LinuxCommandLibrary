# TAGLINE

监视主机与服务并在异常时告警的网络监控应用

# TLDR

**启动 Naemon**

```sudo naemon /etc/naemon/naemon.cfg```

**验证配置**

```naemon -v /etc/naemon/naemon.cfg```

**以守护进程方式启动**

```sudo systemctl start naemon```

**查看状态**

```sudo systemctl status naemon```

# SYNOPSIS

**naemon** [_options_] _config-file_

# PARAMETERS

**-v**
> 验证配置。

**-d**
> 以守护进程方式运行。

**-s**
> 显示调度信息。

**-p** _file_
> PID 文件位置。

**--help**
> 显示帮助。

# DESCRIPTION

**Naemon** 是一个网络监控应用，用于监视主机和服务并在出现问题时发出告警。它是 Nagios 的一个分支，专注于性能和现代化特性。

Naemon 使用插件执行检查，并通过 Thruk 提供 Web 界面。

# CONFIGURATION

```
/etc/naemon/
├── naemon.cfg       # Main config
├── conf.d/          # Object definitions
└── resource.cfg     # Macros
```

# COMPONENTS

```
naemon        - Core daemon
naemonstats   - Statistics
livestatus    - Status API
thruk         - Web interface
```

# CAVEATS

兼容 Nagios 的插件和配置。需要配置插件。Web 界面是单独的软件包。

# HISTORY

Naemon 由 op5 和 Consol 于 **2013 年**从 Nagios Core 分支而来，旨在打造更快、更社区驱动的监控方案。

# INSTALL

```aur: yay -S naemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nagios](/man/nagios)(8), [icinga2](/man/icinga2)(8), [check_mk](/man/check_mk)(1)
