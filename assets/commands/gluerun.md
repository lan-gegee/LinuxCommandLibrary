# TAGLINE

并行 AI 编程智能体的编排引擎

# TLDR

在当前仓库中**搭建初始配置与文档**

```gluerun init```

**校验**依赖和仓库配置

```gluerun doctor```

**运行一个编排周期**（import、recover、integrate、dispatch、snapshot）

```gluerun reconcile --actuate```

**通过智能体流水线执行单个任务**

```gluerun drive [TASK-0001]```

在限定时间内**运行自治循环**

```gluerun auto```

**固定**特定的引擎版本

```gluerun update [version]```

# SYNOPSIS

**gluerun** _command_ [_arguments_] [_options_]

# DESCRIPTION

**gluerun** 是一个编排引擎，用于协调多个 AI 编程智能体在同一个软件仓库上并行工作。它实现了一个多层级调度模型，包含租约管理、审计工作流，并通过 **git worktrees** 进行隔离执行，使并发运行的智能体互不干扰。

每个任务会被分派到受支持的 runner CLI（如 **claude** 或 **codex**），经由流水线驱动执行，然后带着所产生的证据审计记录集成回来。该引擎每台机器安装一次，并通过 **.gluerun-version** 文件按仓库固定版本，因此改进只需提升版本号即可传播，无需重新复制脚本。

# PARAMETERS

**init**
> 在使用方仓库中搭建初始配置与文档。

**doctor**
> 校验所需的依赖和仓库配置。

**reconcile** [**--actuate**]
> 运行一个编排周期：import、recover、integrate、dispatch 和 snapshot。不带 **--actuate** 时该周期仅为演练（dry run）。

**drive** _TASK-ID_
> 通过智能体流水线执行单个任务。

**auto**
> 运行自治循环，持续分派工作直到时间预算耗尽。

**update** _version_
> 为当前仓库固定新的引擎版本。

# CAVEATS

需要 Bash 4 或更高版本、Python 3、Git，以及 PATH 中至少一个受支持的智能体 runner CLI。由于该引擎赋予自主智能体编辑和提交代码的能力，请只在你可以审查其变更的仓库上运行它。

# HISTORY

gluerun（glueRun-go）是一个社区项目，主要以 Bash 和 Python 编写，围绕 git-worktree 隔离机制和任务证据构建，面向智能体编程工作流。它以 GPL-3.0 许可证发布。

# SEE ALSO

[git-worktree](/man/git-worktree)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/alex-reysa/glueRun-go)```

<!-- verified: 2026-06-22 -->
