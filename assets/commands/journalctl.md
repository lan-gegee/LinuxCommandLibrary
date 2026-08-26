# TAGLINE

查询并显示 systemd 日志中的消息

# TLDR

显示本次启动以来**优先级为 3 级**（错误）的所有消息

```journalctl -b -p 3```

**跟踪**新消息（类似 tail -f）

```journalctl -n 50 -f```

显示来自**指定 unit** 的所有消息

```journalctl -u [unit]```

按**时间范围**过滤消息

```journalctl --since yesterday --until today```

显示来自**特定进程**的所有消息

```journalctl _PID=[pid]```

在日志消息中 **grep 匹配**模式

```journalctl -g "[pattern]"```

**删除** 2 天前的日志

```journalctl --vacuum-time=2d```

显示来自特定**可执行文件**的消息

```journalctl [path/to/executable]```

# SYNOPSIS

**journalctl** [_-b_] [_-p priority_] [_-u unit_] [_-n lines_] [_-f_] [_-S since_] [_-U until_]

# DESCRIPTION

**journalctl** 用于查询和显示 systemd 日志中的消息。该日志以结构化、可索引的格式存储来自内核、系统服务和应用程序的日志数据。

# PARAMETERS

**-b, --boot**
> 显示本次启动（或指定某次启动）的消息

**-p, --priority level**
> 按优先级过滤（0=emerg 到 7=debug，也可用名称）

**-u, --unit unit**
> 显示来自指定 systemd unit 的消息

**-n, --lines n**
> 显示最近的 n 行

**-f, --follow**
> 实时跟踪新出现的消息

**-S, --since time**
> 显示指定时间之后的条目

**-U, --until time**
> 显示指定时间之前的条目

**-k, --dmesg**
> 仅显示内核消息

**-r, --reverse**
> 反转输出顺序（最新的在前）

**-o, --output format**
> 输出格式（short、verbose、json、cat 等）

**--vacuum-time time**
> 删除早于指定时间的日志文件

**--vacuum-size size**
> 将日志缩减到指定大小

**-g, --grep pattern**
> 按正则表达式（PCRE2）过滤条目

**--no-pager**
> 不将输出送入分页器

**--list-boots**
> 显示启动 ID 及其时间戳的列表

**--disk-usage**
> 显示日志当前占用的磁盘空间

**_PID=pid**
> 按进程 ID 过滤

**_SYSTEMD_UNIT=unit**
> 按 systemd unit 过滤

# CAVEATS

日志文件存储在 /var/log/journal/（持久化）或 /run/log/journal/（易失性）。部分选项需要 root 权限。

# HISTORY

属于 **systemd** 的组成部分，由 Lennart Poettering 于 **2011 年**推出。在使用 systemd 的系统上取代了传统 syslog。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmesg](/man/dmesg)(1), [systemctl](/man/systemctl)(1)
