# TAGLINE

用于崩溃报告和错误提交的命令行界面。

# TLDR

以交互方式**处理待处理的崩溃报告**

```apport-cli```

针对特定软件包**报告错误**

```apport-cli --file-bug --package [package-name]```

针对正在运行的进程**报告错误**

```apport-cli --file-bug --pid [1234]```

使用症状脚本**报告问题**

```apport-cli --file-bug --symptom [audio]```

**上传现有的崩溃报告**文件

```apport-cli --crash-file [/path/to/report.crash]```

**用更多信息更新现有的错误报告**

```apport-cli --update-report [bug-number]```

**将报告保存到文件**而不提交

```apport-cli --file-bug --package [package-name] --save [report.apport]```

# SYNOPSIS

**apport-cli** [_options_] [_symptom_|_package_|_pid_|_crash-file_]

# PARAMETERS

**-f**, **--file-bug**
> 报告非崩溃类问题；如果未指定 package/pid，会提示选择症状

**-p** _package_, **--package=**_package_
> 指定要报告问题的软件包

**-P** _pid_, **--pid=**_pid_
> 按 PID 针对正在运行的进程报告问题

**-s** _symptom_, **--symptom=**_symptom_
> 使用症状脚本引导问题报告（audio、video、network 等）

**-c** _report_, **--crash-file=**_report_
> 从文件上传已存储的崩溃报告

**-u** _number_, **--update-report=**_number_
> 为现有的错误报告收集补充信息

**--save** _filename_
> 将报告保存到文件而不是提交

**-w**, **--window**
> 点击应用程序窗口以针对它报告错误

# DESCRIPTION

**apport-cli** 是 Ubuntu 的 Apport 崩溃报告系统的命令行界面。它处理收集在 **/var/crash/** 中的崩溃报告，并允许用户将它们连同相关调试信息一起提交到缺陷跟踪系统。

不带参数调用时，它会以交互方式处理待处理的崩溃报告。它还可以针对软件包或正在运行的进程提交新的错误报告，或者使用症状脚本引导用户诊断特定类型的问题。

Apport 会自动收集系统信息、软件包版本、堆栈跟踪和其他调试数据。这些全面的信息比手动编写的错误报告更能帮助开发者高效地诊断和修复问题。

该工具主要用于无法使用 **apport-gtk** 等图形界面的服务器环境。

# CAVEATS

如果软件包或其依赖已过时，Apport 会拒绝创建报告；可设置 **APPORT_IGNORE_OBSOLETE_PACKAGES** 来忽略此限制。提交报告需要网络连接以及 Ubuntu 缺陷跟踪器（Launchpad）的身份验证。核心转储和日志可能包含敏感信息。

# HISTORY

**Apport** 由 Canonical 的 **Martin Pitt** 开发，于 **2006** 年随 **Ubuntu 6.10**（Edgy Eft）推出。它的设计目标是通过自动收集相关调试信息来提高错误报告的质量。该系统已成为 Ubuntu 质量保障基础设施的标准组成部分，并被其他基于 Debian 的发行版采用。

# SEE ALSO

[apport-unpack](/man/apport-unpack)(1), [ubuntu-bug](/man/ubuntu-bug)(1)
