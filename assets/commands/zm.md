# TAGLINE

管理 ZoneMinder 监控守护进程

# TLDR

**启动 ZoneMinder 系统**

```sudo zmpkg.pl start```

**停止 ZoneMinder 系统**

```sudo zmpkg.pl stop```

**检查系统状态**

```zmpkg.pl status```

**启动特定守护进程**

```sudo zmdc.pl start [zmc] -m [monitor_id]```

**检查守护进程状态**

```zmdc.pl status```

**查询监视器状态**

```zmu -m [monitor_id] -q```

# SYNOPSIS

**zm** [_subcommand_]

**zmpkg.pl** [**start**|**stop**|**restart**|**status**|**logrot**|**version**]

**zmdc.pl** [**start**|**stop**|**status**|**check**|**startup**|**shutdown**] [_daemon_]

# DESCRIPTION

**ZoneMinder** 是一套视频摄像头安防与监控系统。**zm** 命令家族负责管理 ZoneMinder 的守护进程与服务。

主要组件：
- **zmpkg.pl** - 包控制（启动/停止整个系统）
- **zmdc.pl** - 守护进程控制（管理单个守护进程）
- **zmu** - 监视器工具（查询监视器状态）
- **zmwatch.pl** - 看门狗守护进程
- **zmaudit.pl** - 数据库审计工具

ZoneMinder 由多个守护进程组成：每个摄像头对应一个采集守护进程，用于移动侦测的分析守护进程，以及为 Web 界面和事件处理提供支持的服务。

主界面基于 Web，这些命令则提供后端管理与故障排查能力。

# CAVEATS

ZoneMinder 需要数据库（MySQL/MariaDB）和 Web 服务器才能运行。命令行工具用于管理守护进程，但配置要通过 Web 界面完成。

摄像头配置、区域设置和事件管理都在 Web UI 中处理，而不是命令行。

守护进程管理通常需要 root 权限。

资源占用随摄像头数量和分析复杂度而增长。

# SEE ALSO

[motion](/man/motion)(1), [ffmpeg](/man/ffmpeg)(1), [systemctl](/man/systemctl)(1)
