# TAGLINE

在线时长记录跟踪守护进程

# TLDR

**启动守护进程**

```sudo systemctl start uptimed```

**设置开机自启**

```sudo systemctl enable uptimed```

**查看在线时长记录**

```uprecords```

**显示前 20 条记录**

```uprecords -m 20```

**显示重启之间的停机时间**

```uprecords -d```

**以简短格式显示记录**

```uprecords -s```

# SYNOPSIS

**uptimed** [_options_]

**uprecords** [_options_]

# UPTIMED PARAMETERS

**-f** _file_
> 使用指定的配置文件。

**-p** _file_
> 使用指定的 PID 文件。

**-e** _email_
> 在达到里程碑和刷新纪录时发送邮件。

**-i** _interval_
> 设置循环间隔（秒）。

**-m** _count_
> 最多记录 count 条条目。

**-t** _timespec_
> 设置可被记为纪录的最低在线时长。

**-b**
> 创建 bootid 后退出。

**-v**
> 显示版本信息。

# UPRECORDS PARAMETERS

**-m** _count_
> 显示指定数量的记录。

**-d**
> 显示重启之间的停机时间。

**-s**
> 简短的输出格式。

**-a**
> 显示全部记录。

**-b**
> 按启动时间排序。

**-w**
> 宽幅输出格式。

**-v**
> 显示版本。

# DESCRIPTION

**uptimed** 是一个负责跟踪和记录系统在线时长历史的守护进程。它维护着一个由各次启动会话及其持续时长组成的数据库，让你能够查看系统的历史在线时长记录。

配套的 **uprecords** 命令以排名形式展示所记录的数据，列出系统最长的一段段在线时长。当前会话在排行榜中的位置会用箭头标出。

通过配置可以设定计入纪录的最低在线时长阈值、里程碑通知，以及刷新纪录时的邮件提醒。守护进程依据启动时间来区分不同会话。

# CONFIGURATION

配置文件：/etc/uptimed.conf

**LOG_MINIMUM_UPTIME**: 记录所需的最低在线时长（默认：1h）。

**MILESTONE**: 定义里程碑，例如 "7d:One week uptime"。

**EMAIL**: 接收里程碑通知的地址。

# CAVEATS

只记录安装之后的在线时长。必须保持守护进程运行才能跟踪当前会话。系统时钟的变动会影响准确性。邮件通知需要事先配置好 MTA。

# HISTORY

**uptimed** 由 Rob Kaper 创建，现由 Radek Podgorny 维护。其灵感来自 'ud' 工具，但采用了不同的设计——基于启动时间而非 PID 文件来区分会话。

# INSTALL

```apt: sudo apt install uptimed```

```dnf: sudo dnf install uptimed```

```pacman: sudo pacman -S uptimed```

```apk: sudo apk add uptimed```

```brew: brew install uptimed```

```nix: nix profile install nixpkgs#uptimed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uprecords](/man/uprecords)(1), [uptime](/man/uptime)(1), [last](/man/last)(1), [who](/man/who)(1)
