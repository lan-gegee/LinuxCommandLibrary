# TAGLINE

从 coredump 生成人类可读的回溯

# TLDR

从问题目录**生成回溯**

```abrt-action-generate-backtrace -d [/var/spool/abrt/ccpp-2024-01-15]```

以详细输出模式**生成回溯**

```abrt-action-generate-backtrace -v -d [/var/spool/abrt/ccpp-2024-01-15]```

为 gdb 设置超时时间来**生成回溯**

```abrt-action-generate-backtrace -d [problem_dir] -t [300]```

# SYNOPSIS

**abrt-action-generate-backtrace** [**-v**] [**-d** _DIR_] [**-t** _NUM_]

# PARAMETERS

**-d** _DIR_
> 包含 coredump 文件的问题目录的路径。默认为当前工作目录

**-v**
> 输出更详细的信息；可多次指定以提高详细程度

**-t** _NUM_
> 若 gdb 运行超过 NUM 秒则将其终止（超时）

# DESCRIPTION

**abrt-action-generate-backtrace** 是 ABRT（Automatic Bug Reporting Tool，自动错误报告工具）套件的一部分。它分析 coredump 文件，生成人类可读的回溯，展示应用程序崩溃那一刻的状态。

该工具对指定问题目录中名为 "coredump" 的文件运行 **gdb**。GDB 生成回溯及其他诊断信息，随后作为名为 "backtrace" 的新元素保存到问题目录中。该回溯可用于调试、提交错误报告或崩溃分析。

要获得最佳结果，应为崩溃的应用程序及其依赖库安装相应的 debuginfo 软件包。缺少调试符号时，回溯中将只有内存地址，而没有函数名和行号。

该工具与 libreport 事件集成，通常由 ABRT 在分析 C/C++ 应用程序崩溃时自动调用。

# CAVEATS

需要安装 **gdb**。回溯的质量取决于 debuginfo 软件包是否可用。处理大型 coredump 可能非常消耗内存且耗时；如有需要，可使用 **-t** 选项设置超时。仅适用于应用程序产生的 coredump，不支持内核崩溃。

# HISTORY

ABRT（Automatic Bug Reporting Tool）由 **Red Hat** 自 **2009** 年前后开始为 Fedora 和 RHEL 系统开发，提供自动化的崩溃检测与报告基础设施。回溯生成组件旨在简化从应用程序崩溃中收集诊断信息的流程，以便提交到 Bugzilla 等缺陷跟踪系统。

# SEE ALSO

[gdb](/man/gdb)(1), [abrt-cli](/man/abrt-cli)(1), [coredumpctl](/man/coredumpctl)(1), [abrt](/man/abrt)(1)

# RESOURCES

```[Source code](https://github.com/abrt/abrt)```

```[Documentation](https://abrt.readthedocs.io/)```

<!-- verified: 2026-06-10 -->
