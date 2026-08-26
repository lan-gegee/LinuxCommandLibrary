# TAGLINE

跨平台系统监控工具

# TLDR

**启动 glances**

```glances```

**Web 服务器模式**

```glances -w```

**客户端模式**

```glances -c [server-ip]```

**导出为 CSV**

```glances --export csv --export-csv-file [output.csv]```

**每 CPU 统计**，5 秒刷新一次

```glances -1 -t 5```

在自定义端口上运行**服务器模式**

```glances -s -p [61210]```

**安静模式**

```glances -q```

# SYNOPSIS

**glances** [_options_]

# PARAMETERS

**-w**, **--webserver**
> 启动 Web 服务器。

**-c** _SERVER_, **--client** _SERVER_
> 连接到服务器。

**-s**, **--server**
> 启动服务器模式。

**-t** _SECONDS_
> 刷新时间。

**--export** _FORMAT_
> 导出为指定格式。

**-p** _PORT_, **--port** _PORT_
> 客户端/服务器/Web 模式使用的 TCP 端口（默认：61209）。

**-1**, **--percpu**
> 显示每个 CPU 的统计信息而非汇总值。

**-b**, **--byte**
> 以字节/秒而非比特/秒显示网络 I/O。

**-q**, **--quiet**
> 不显示界面，后台运行。

**--disable-plugin** _PLUGIN_
> 禁用指定插件（如 docker、gpu）。

**--stdout** _STATS_
> 将统计信息输出到 stdout（逗号分隔列表）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**glances** 是一款跨平台系统监控工具。它在统一的终端界面中实时显示 CPU、内存、磁盘、网络和进程信息。

相比 top 或 htop，该工具能在单一视图中呈现更多信息。它支持客户端-服务器模式、Web 界面，并可导出为多种格式用于监控和分析。

# CONFIGURATION

**~/.config/glances/glances.conf**
> 主配置文件，用于设置阈值、显示选项和导出配置。

# CAVEATS

需要 Python 和 psutil。某些功能（Web 模式、Docker、GPU 监控）需要可选依赖。Web 模式需要浏览器以及 bottle/fastapi 模块。过高的刷新频率可能增加 CPU 占用。

# HISTORY

glances 由 **Nicolas Hennion** 创建，旨在提供一个超越 top 等传统工具的全面系统监控方案。

# INSTALL

```dnf: sudo dnf install glances```

```pacman: sudo pacman -S glances```

```apk: sudo apk add glances```

```brew: brew install glances```

```nix: nix profile install nixpkgs#glances```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [top](/man/top)(1), [iotop](/man/iotop)(1), [nmon](/man/nmon)(1), [vmstat](/man/vmstat)(8)
