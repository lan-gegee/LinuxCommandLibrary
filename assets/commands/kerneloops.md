# TAGLINE

收集并提交内核崩溃信息

# TLDR

**启动 kerneloops 守护进程**

```sudo kerneloops```

**以调试模式运行**而不转为守护进程

```kerneloops --debug```

**解析指定文件**中的内核 oops 消息

```kerneloops --file [/var/log/messages]```

**在前台运行**而不成为守护进程

```kerneloops --nodaemon```

# SYNOPSIS

**kerneloops** [_options_]

# PARAMETERS

**--debug**
> 启用调试模式，输出额外的诊断信息。

**--file** _filename_
> 将指定文件当作 /var/log/messages 来解析。

**--nodaemon**
> 不转为守护进程；在前台运行。

# DESCRIPTION

**kerneloops** 收集内核崩溃信息（oops 消息），并把提取出的签名提交到 oops.kernel.org 网站，用于统计分析并向 Linux 内核开发者展示。

该守护进程监控 /var/log/messages 中的内核 oops 数据并自动提交。配置存储在 /etc/kerneloops.conf 中。

# CAVEATS

提交的 oops 数据可能包含内核状态信息。提交报告到 oops.kernel.org 需要网络连接。该守护进程通常以 root 身份运行。

# HISTORY

kerneloops 由 **Intel** 创建，用于收集内核崩溃数据，帮助发现 Linux 内核中的缺陷。

# SEE ALSO

[dmesg](/man/dmesg)(1), [journalctl](/man/journalctl)(1)
