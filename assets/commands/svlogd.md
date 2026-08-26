# TAGLINE

支持自动轮转的 Runit 日志守护进程

# TLDR

**开始向目录写日志**

```svlogd [/var/log/myservice]```

**以人类可读的时间戳记录日志**

```svlogd -tt [/var/log/myservice]```

**以 ISO 8601 时间戳记录日志**

```svlogd -ttt [/var/log/myservice]```

**记录到多个目录**

```svlogd [/var/log/service1] [/var/log/service2]```

**设置缓冲区长度**

```svlogd -b [8192] [/var/log/myservice]```

**替换不可打印字符**

```svlogd -r [?] [/var/log/myservice]```

# SYNOPSIS

**svlogd** [**-tttv**] [**-r** _c_] [**-R** _xyz_] [**-l** _len_] [**-b** _buflen_] _logs_...

# PARAMETERS

**-t**
> 在每行前面加 tai64n 时间戳。

**-tt**
> 在每行前面加人类可读的 UTC 时间戳（YYYY-MM-DD_HH:MM:SS.xxxxx）。

**-ttt**
> 在每行前面加 ISO 8601 UTC 时间戳（YYYY-MM-DDTHH:MM:SS.xxxxx）。

**-v**
> 详细输出模式。

**-r** _c_
> 用字符 c 替换不可打印字符。

**-R** _xyz_
> 字符替换规则说明。

**-l** _len_
> 设置最大行长度。

**-b** _buflen_
> 设置缓冲区长度（默认 1024）。

# DESCRIPTION

**svlogd** 是 runit（一种 UNIX init 方案）的日志守护进程。它持续从标准输入读取日志数据，可选地对日志消息进行过滤和变换，然后写入一个或多个自动轮转的日志目录。

每个日志目录中包含名为 **current** 的当前日志文件，以及文件名以 @ 加 tai64n 时间戳开头的轮转日志。日志轮转通过每个日志目录中的 **config** 文件配置。

该守护进程支持使用模式匹配过滤日志消息、将选定的消息告警到标准错误或 UDP 目的地，以及用外部程序处理轮转后的日志。

svlogd 会一直运行，直到在标准输入上收到文件结束符或 TERM 信号。

# SIGNALS

**HUP**：关闭并重新打开所有日志，重新加载配置。

**TERM**：停止读取输入，处理缓冲区后退出。

**ALRM**：强制立即轮转所有日志。

# CAVEATS

需要对日志目录设置合适的权限。配置通过日志目录中的文件完成，而非命令行选项。属于 runit 监管套件的一部分。缓冲区大小影响内存占用和日志延迟。

# HISTORY

**svlogd** 由 Gerrit Pape 作为 runit init 系统的一部分创建。它被设计为 syslog 风格日志的可靠替代品，提供自动日志轮转和时间戳处理。Runit 的灵感来自 daemontools，在提供类似功能的同时做了部分增强。

# INSTALL

```apt: sudo apt install runit```

```apk: sudo apk add runit```

```brew: brew install runit```

```nix: nix profile install nixpkgs#runit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sv](/man/sv)(8), [runsv](/man/runsv)(8), [chpst](/man/chpst)(8)
