# TAGLINE

自动崩溃报告与诊断系统

# TLDR

显示某个 PID 的**崩溃报告**

```apport-retrace -s [/var/crash/_bin_foo.1000.crash]```

**列出**待处理的崩溃报告

```ls /var/crash/```

**解包**崩溃报告

```apport-unpack [/var/crash/report.crash] [output_dir]```

**启用** apport 崩溃报告

```sudo systemctl enable apport```

从崩溃文件提交错误报告

```ubuntu-bug [/var/crash/report.crash]```

# SYNOPSIS

**apport** (system daemon)

# DESCRIPTION

**apport** 是 Ubuntu 的崩溃报告系统，在应用程序崩溃时自动收集数据，包括核心转储、软件包版本和系统信息。它将崩溃报告存储在 /var/crash/ 中，供之后提交。

启用后，apport 会拦截段错误和其他崩溃，生成可提交到 Launchpad 或在本地分析的 .crash 文件。

# CONFIGURATION

**/etc/default/apport**
> 主配置文件。设置 enabled=1 以收集崩溃报告，或设置 enabled=0 禁用。

**/var/crash/**
> 存储崩溃报告文件的目录。

# RELATED COMMANDS

**apport-cli**
> 命令行崩溃报告处理工具

**apport-unpack**
> 提取崩溃报告内容

**apport-retrace**
> 重新生成堆栈跟踪

**ubuntu-bug**
> 向 Launchpad 报告错误

# CAVEATS

核心转储可能占用大量磁盘空间。崩溃报告可能包含敏感信息。在生产环境中默认禁用。

# HISTORY

**Apport** 为 Ubuntu 而创建，最早出现于 **2006** 年。它与 Launchpad 集成，以便从桌面和服务器的崩溃中自动报告错误。

# SEE ALSO

[apport-cli](/man/apport-cli)(1), [apport-unpack](/man/apport-unpack)(1), [ubuntu-bug](/man/ubuntu-bug)(1), [coredumpctl](/man/coredumpctl)(1), [dmesg](/man/dmesg)(1)
