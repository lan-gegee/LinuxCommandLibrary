# TAGLINE

测试管理与执行框架

# TLDR

**列出**测试、计划和故事

```tmt```

**初始化**项目结构

```tmt init```

**使用模板创建**测试

```tmt test create -t [beakerlib] --link [verifies:issue#1234]```

列出**测试/计划/故事**

```tmt [test|plan|story] ls [pattern]```

结合上下文显示测试**元数据**

```tmt -c [arch=aarch64] test show```

**校验** tmt 文件

```tmt lint```

在容器中**运行**所有测试

```tmt run```

使用**过滤器**

```tmt tests ls -f [tag:foo] -f [tier:0]```

# SYNOPSIS

**tmt** [_OPTIONS_] _COMMAND_ [_ARGS_]

# COMMANDS

**init**
> 初始化 tmt 项目结构

**test** [create|ls|show]
> 管理测试

**plan** [ls|show]
> 管理测试计划

**story** [ls|show]
> 管理故事

**run**
> 执行测试

**lint**
> 校验 tmt 文件

**try**
> 交互式试用测试

# PARAMETERS

**-c, --context** _KEY=VALUE_
> 为操作设置上下文

**-f, --filter** _EXPRESSION_
> 过滤条目

**-t, --template** _NAME_
> 创建时使用模板

# DESCRIPTION

**tmt**（Test Management Tool）是用于创建、组织和执行测试的框架。它使用 YAML 格式的元数据定义测试、计划和故事，从而在不同环境中实现可复现的测试执行。

# CAVEATS

需要正确的 tmt 文件结构。测试默认在容器中运行。复杂的计划可能需要额外的资源调配配置。

# HISTORY

**tmt** 由 **Red Hat** 开发，用于管理 Fedora 和 RHEL 的测试，提供了统一的测试元数据格式和执行框架。

# INSTALL

```dnf: sudo dnf install tmt```

```brew: brew install tmt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[beakerlib](/man/beakerlib)(1), [podman](/man/podman)(1)
