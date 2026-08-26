# TAGLINE

将崩溃报告中的字段解包为单独的文件。

# TLDR

**将崩溃报告解包**到目录

```apport-unpack [/var/crash/_usr_bin_app.1000.crash] [output_directory]```

从标准输入**解包崩溃报告**

```cat [report.crash] | apport-unpack - [output_directory]```

**解包核心转储**以便调试

```apport-unpack [crash_file.crash] [extracted/] && gdb [/usr/bin/app] [extracted/CoreDump]```

# SYNOPSIS

**apport-unpack** _report_ _target-directory_

# PARAMETERS

_report_
> apport 崩溃报告文件（.crash）的路径，或用 '-' 从标准输入读取

_target-directory_
> 解包出的文件写入的目标目录；必须不存在或为空

# DESCRIPTION

**apport-unpack** 将 Apport 问题报告中的各个字段提取为单独的文件。崩溃报告中的每个键值对都会变成一个单独的文件：键作为文件名，值作为文件内容。

Apport 崩溃报告使用 RFC822 语法，打包了多种信息，包括堆栈跟踪、系统信息、软件包详情和核心转储。此工具可将它们拆分开来逐一检查。

主要用途是提取 **CoreDump** 文件，供 **gdb** 或其他调试工具分析。其他解包出的文件还包括 **ProcMaps**、**ProcStatus**、**Stacktrace**、**Package** 以及各种系统信息字段。

崩溃报告通常存储在 **/var/crash/** 中，命名遵循 **_usr_bin_program.uid.crash** 模式。

# CAVEATS

目标目录必须为空或不存在；该工具不会覆盖已有文件。仅适用于有效的 Apport 崩溃报告；直接提供原始二进制文件（如核心转储）会失败。CoreDump 等二进制字段可能很大。

# HISTORY

**apport-unpack** 由 **Martin Pitt** 开发，是 Ubuntu 的 Apport 崩溃报告系统的组成部分，于 **2006** 年推出。该工具满足了从打包的崩溃报告中提取并分析单个组件的需求，尤其是用于深入调试的核心转储。

# SEE ALSO

[apport-cli](/man/apport-cli)(1), [apport](/man/apport)(1), [apport-bug](/man/apport-bug)(1), [gdb](/man/gdb)(1), [coredumpctl](/man/coredumpctl)(1)
