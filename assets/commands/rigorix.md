# TAGLINE

将意图编译为可执行 DAG 的确定性编程智能体运行时

# TLDR

**初始化项目**

```rigorix init```

**在执行前生成并审查计划**

```rigorix plan "Add a new API endpoint"```

**运行任务**

```rigorix run "Refactor the user module"```

**显示仪表盘 / 交互式 TUI**

```rigorix```

# SYNOPSIS

**rigorix** [_options_] <command> [_args_...]

常用命令：init、plan、run、update

# DESCRIPTION

Rigorix 将自然语言开发任务转化为确定性的、可审计的有向无环图（DAG）。规划与执行相分离：LLM 按照模板生成计划，Rigorix 对计划进行校验，然后在策略、权限和预算控制下执行。

与开放式智能体循环相比的主要优势：

- 可重复的执行图
- 明确的质量关卡与策略强制
- 完整的审计追踪
- 可安全地在 CI/CD 环境中运行

它支持 Rust、TypeScript、Python 和 Go 代码库（TypeScript 支持最为成熟）。

# INSTALL

```bash
cargo install --git https://github.com/arman-jalili/rigorix-oss rigorix-cli
```

也可以从源码构建，并将 rigorix 二进制文件放入 PATH 中。

设置你的 LLM API 密钥，例如：

```bash
export RIGORIX__LLM__API_KEY="sk-ant-..."
# or: export ANTHROPIC_API_KEY="sk-ant-..."
```

# PARAMETERS

大部分配置在 `rigorix init` 之后保存在项目内。命令行选项用于控制规划与执行、选择提供商，以及非交互模式。

**init**
> 生成项目配置与模板的脚手架。

**plan** _task_
> 对意图进行分类，构建可审查的 DAG，并可选择提示是否运行。

**run** _task_
> 端到端地规划并执行任务。

# CAVEATS

Rigorix 有意设计得不如自由对话式智能体灵活。它擅长可重复、受管控的工作流，而非探索式对话。规划和生成步骤需要 LLM API 密钥。

# RESOURCES

```[Source code](https://github.com/arman-jalili/rigorix-oss)```

<!-- verified: 2026-07-11 -->
