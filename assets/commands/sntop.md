# TAGLINE

用于监控主机连通性的简单网络 top 工具

# TLDR

**监控默认配置中定义的主机**

```sntop```

每 10 秒从自定义配置轮询主机

```sntop -r 10 -f [/path/to/hosts.conf]```

**生成 HTML 状态页**

```sntop -w -e [/var/www/status.html]```

# SYNOPSIS

**sntop** [**-d**] [**-o**] [**-c**] [**-r** _time_] [**-f** _file_] [**-a** _file_] [**-l** _file_]

# PARAMETERS

**-r** _TIME_
> 设置轮询间隔，单位秒。

**-f** _FILE_
> 使用自定义的主机配置文件。

**-w**
> 启用 HTML 输出模式。

**-d**
> 以守护进程模式运行。

# DESCRIPTION

**sntop** 是一个基于 ncurses 的控制台工具，定期使用 fping 或 ping 轮询主机列表，并以类似 top 的表格显示它们的在线/离线状态。它支持生成 HTML、守护进程模式、在主机状态变化时执行告警脚本以及彩色输出。

# HISTORY

**sntop** 由 **Robert M. Love** 和 **Chris M. Rivera** 创建，使用 **C** 编写。

# INSTALL

```apt: sudo apt install sntop```

```brew: brew install sntop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fping](/man/fping)(1), [ping](/man/ping)(1), [trippy](/man/trippy)(1)
