# TAGLINE

Varnish 请求延迟实时直方图

# TLDR

**显示请求直方图**

```varnishhist```

**连接指定实例**

```varnishhist -n [instance_name]```

**从日志文件读取**

```varnishhist -r [/var/log/varnish.log]```

**设置更新延迟**

```varnishhist -d [2]```

**按模式过滤**

```varnishhist -q "[RespStatus == 200]"```

**排除匹配模式**

```varnishhist -x "[BogoHeader]"```

# SYNOPSIS

**varnishhist** [_options_]

# PARAMETERS

**-n** _name_
> 指定 varnishd 实例名。

**-r** _file_
> 从文件而非共享内存读取日志。

**-d** _delay_
> 更新之间的间隔秒数（默认：1）。

**-q** _query_
> 使用 VSL 查询过滤日志条目。

**-x** _regex_
> 排除匹配正则表达式的条目。

**-T** _seconds_
> 事务超时时间（默认：120 秒）。

**-h**
> 显示帮助。

**-V**
> 显示版本。

# DISPLAY

直方图展示请求处理时间的分布。横轴采用对数刻度。纵轴刻度和请求数（N）显示在左上角。

**|**: 缓存命中。

**#**: 缓存未命中。

# DESCRIPTION

**varnishhist** 读取 Varnish 共享内存日志，并实时显示请求处理时间的直方图。它将缓存命中与未命中的分布可视化，帮助识别性能模式。

显示内容持续更新，展示请求延迟在对数时间桶上的分布情况。缓存命中（|）和未命中（#）使用不同字符表示，便于比较两者的性能特征。

该工具适用于实时监控 Varnish 缓存性能以及发现延迟问题。过滤选项可用于聚焦特定请求类型或排除干扰。

# CAVEATS

需要访问 Varnish 共享内存（通常需要加入相应的用户组）。大量日志可能影响系统资源。历史分析需要已记录的日志数据。

# HISTORY

**varnishhist** 由 Poul-Henning Kamp 开发，是 Varnish Cache 项目的一部分。Varnish 于 2006 年为 Verdens Gang（VG.no）创建，如今已是最流行的 HTTP 加速器之一，而 varnishhist 提供了重要的可视化性能监控功能。

# INSTALL

```apt: sudo apt install varnish```

```dnf: sudo dnf install varnish```

```apk: sudo apk add varnish```

```brew: brew install varnish```

```nix: nix profile install nixpkgs#varnish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[varnishd](/man/varnishd)(1), [varnishstat](/man/varnishstat)(1), [varnishlog](/man/varnishlog)(1)
