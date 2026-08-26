# TAGLINE

显示 Varnish 缓存统计信息

# TLDR

**实时显示统计信息**

```varnishstat```

**打印一次统计信息后退出**

```varnishstat -1```

**以 JSON 格式输出**

```varnishstat -j```

**以 XML 格式输出**

```varnishstat -x```

**显示特定字段**

```varnishstat -f [MAIN.cache_hit,MAIN.cache_miss]```

**列出可用字段**

```varnishstat -l```

**连接指定实例**

```varnishstat -n [instance_name]```

# SYNOPSIS

**varnishstat** [_options_]

# PARAMETERS

**-1**
> 打印一次统计信息后退出。

**-j**
> 以 JSON 格式输出。

**-x**
> 以 XML 格式输出。

**-f** _field_
> 过滤到特定字段（glob 模式）。

**-I** _glob_
> 包含匹配 glob 的字段。

**-X** _glob_
> 排除匹配 glob 的字段。

**-l**
> 列出可用的字段名。

**-n** _name_
> 连接到指定的 varnishd 实例。

**-t** _seconds_
> 获取共享内存锁的超时时间。

# CURSES INTERFACE

默认的 curses 模式以下列各栏实时显示统计信息：

**Current**: 当前值。

**Change**: 每秒变化率。

**Average**: 运行期平均值。

**Avg_10/100/1000**: 各更新区间内的移动平均。

# DESCRIPTION

**varnishstat** 显示正在运行的 Varnish 缓存服务器的实时统计信息，包括缓存命中率、连接数、后端健康状况以及大量性能计数器。

在 curses 模式下，统计信息持续更新，底部显示当前所选计数器的说明。一次性模式（-1）打印所有计数器一次，便于脚本处理。JSON 和 XML 输出便于与监控系统集成。

关键指标包括客户端请求数、缓存命中率、后端连接数和内存使用量。监控这些指标有助于发现性能瓶颈和容量问题。

# CAVEATS

需要访问 Varnish 共享内存。Varnish 重启后统计信息会重置。字段名可能因版本而异。部分计数器需要正确解读（区分平均值和总量）。

# HISTORY

**varnishstat** 由 Poul-Henning Kamp 开发，是 Varnish Cache 项目的一部分。Varnish 于 2006 年为挪威报纸 VG 创建，如今已是部署最广泛的 HTTP 加速器之一。

# INSTALL

```apt: sudo apt install varnish```

```dnf: sudo dnf install varnish```

```apk: sudo apk add varnish```

```brew: brew install varnish```

```nix: nix profile install nixpkgs#varnish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[varnishd](/man/varnishd)(1), [varnishhist](/man/varnishhist)(1), [varnishlog](/man/varnishlog)(1)
