# TAGLINE

分析崩溃回溯的重复性与质量

# TLDR

以**详细日志模式**分析回溯

```abrt-action-analyze-backtrace -v```

分析**指定转储目录**中的问题数据

```abrt-action-analyze-backtrace -d [path/to/directory]```

分析**当前工作目录**下的转储目录

```abrt-action-analyze-backtrace```

# SYNOPSIS

**abrt-action-analyze-backtrace** [_-v_] [_-d DIR_]

# DESCRIPTION

**abrt-action-analyze-backtrace** 分析 C/C++ 回溯，生成重复性哈希值和回溯评级，并识别崩溃函数。这些数据作为新元素 **duphash**、**rating** 和 **crash_function** 保存在问题目录中。

该工具作为回溯生成之后的二级分析器工作。评级可防止低质量回溯被上报，而重复性哈希有助于识别之前已提交过的类似崩溃报告。

# PARAMETERS

**-d DIR**
> 指定问题目录的路径；默认为当前工作目录

**-v**
> 启用详细输出；可多次使用以提高详细程度

# CAVEATS

要求问题目录中已存在回溯文件。通常作为 ABRT 事件流水线的一部分使用，而非由用户直接调用。

# HISTORY

属于 **ABRT**（Automatic Bug Reporting Tool，自动错误报告工具），由 Red Hat 为 Fedora 系系统开发，用于检测、分析和报告应用程序崩溃。

# SEE ALSO

[abrt-cli](/man/abrt-cli)(1), [abrt-action-generate-backtrace](/man/abrt-action-generate-backtrace)(1), [abrt-action-analyze-c](/man/abrt-action-analyze-c)(1)

# RESOURCES

```[Source code](https://github.com/abrt/abrt)```

```[Documentation](https://abrt.readthedocs.io/)```

<!-- verified: 2026-06-10 -->
