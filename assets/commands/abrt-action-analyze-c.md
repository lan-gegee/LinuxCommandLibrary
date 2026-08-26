# TAGLINE

从 coredump 生成 UUID 用于崩溃去重

# TLDR

为**当前转储目录**中 C/C++ 崩溃计算并存储 UUID

```abrt-action-analyze-c```

对**指定的转储目录**执行同样操作

```abrt-action-analyze-c -d [path/to/directory]```

以**详细输出**模式运行

```abrt-action-analyze-c -v```

# SYNOPSIS

**abrt-action-analyze-c** [_-v_] [_-d DIR_]

# DESCRIPTION

**abrt-action-analyze-c** 处理来自问题数据目录的 coredump 文件，并生成全局唯一标识符（UUID）。该 UUID 作为新元素保存在目录结构中。

该工具与 ABRT 事件集成，主要用于在新 coredump 保存时生成 UUID。

# PARAMETERS

**-d DIR**
> 指定 coredump 所在问题目录的路径；默认为当前工作目录

**-v**
> 启用详细输出；可多次指定以提高详细程度

# CAVEATS

要求问题目录中存在 coredump 文件。通常作为 ABRT 事件流水线的一部分使用，而非由用户直接调用。

# HISTORY

属于 **ABRT**（Automatic Bug Reporting Tool，自动错误报告工具），由 Red Hat 为 Fedora 系系统开发，用于检测、分析和报告应用程序崩溃。

# SEE ALSO

[abrt-cli](/man/abrt-cli)(1), [abrt-action-analyze-backtrace](/man/abrt-action-analyze-backtrace)(1), [abrt-action-generate-backtrace](/man/abrt-action-generate-backtrace)(1)

# RESOURCES

```[Source code](https://github.com/abrt/abrt)```

```[Documentation](https://abrt.readthedocs.io/)```

<!-- verified: 2026-06-10 -->
