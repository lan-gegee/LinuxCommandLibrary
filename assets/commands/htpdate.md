# TAGLINE

利用 Web 服务器的 HTTP 头同步本地系统时间

# TLDR

**同步**日期和时间

```sudo htpdate [host]```

执行**模拟**而不做任何实际操作

```htpdate -q [host]```

**补偿**系统性的时钟漂移

```sudo htpdate -x [host]```

同步后**立即**设置时间

```sudo htpdate -s [host]```

# SYNOPSIS

**htpdate** [_options_] _host_...

# PARAMETERS

**-q**
> 仅查询；不设置时间

**-s**
> 立即设置时间（步进调整）

**-x**
> 补偿系统性漂移

**-a**
> 平滑调整时间（渐进式）

**-d**
> 以守护进程方式运行

**-l**
> 使用 syslog 记录日志

**-t**
> 关闭时间合理性检查

**-u** _USER_
> 以指定用户身份运行

**-p** _FILE_
> 创建 PID 文件

# DESCRIPTION

**htpdate** 利用来自 Web 服务器的 HTTP 头来同步本地系统时间。它从 HTTP 响应中提取 Date 头，从而在不依赖专用 NTP 端口的情况下实现时间同步。

这在受限的网络环境中非常有用，例如：
- NTP（端口 123）被防火墙屏蔽
- 只允许 HTTP/HTTPS 流量
- 需要时间同步但无法访问 NTP 服务器

htpdate 可以查询多台服务器并对结果取平均值以提高精度。它既支持一次性同步，也支持持续调整的守护进程模式。

# CAVEATS

精度不如 NTP（HTTP 时间戳只有秒级分辨率）。依赖 Web 服务器本身拥有准确的时间。网络延迟会影响精度。HTTPS 需要额外的处理过程，可能影响精度。

# HISTORY

htpdate 由 Eddy Vervest 创建，用于在 NTP 流量受限的环境中替代 NTP。它利用 HTTP 访问的普遍性来提供基本的时间同步。

# INSTALL

```apt: sudo apt install htpdate```

```apk: sudo apk add htpdate```

```brew: brew install htpdate```

```nix: nix profile install nixpkgs#htpdate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntpd](/man/ntpd)(8), [chrony](/man/chrony)(8), [date](/man/date)(1)
