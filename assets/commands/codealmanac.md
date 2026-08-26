# TAGLINE

由 AI 编程智能体维护、并服务于智能体的代码库活维基

# TLDR

**设置**智能体指令与自动化

```codealmanac setup --yes```

在当前仓库中**初始化**维基

```codealmanac init```

**搜索**维基

```codealmanac search "checkout timeout"```

**显示**特定页面

```codealmanac show getting-started```

将材料（文件、PR、对话记录）**摄取**进维基

```codealmanac ingest README.md --using codex```

**运行**本地 Web 查看器

```codealmanac serve```

# SYNOPSIS

**codealmanac** <command> [options]

# DESCRIPTION

CodeAlmanac 在你的仓库内维护一个纯 markdown 维基（`almanac/`），记录那些仅靠源码无法表达的决策、架构、不变量、坑点和工作流。AI 智能体（通过 Claude 或 Codex 等本地 harness）通过 `ingest` 和 `garden` 操作保持维基的更新。所有数据都保留在本地。

人类与智能体使用同一个本地 CLI 来搜索、阅读和校验维基。

# COMMANDS

**setup**
> 安装智能体指令和可选的自动化任务（sync、garden）。

**init**
> 创建初始的 almanac/ 目录树和主题。

**search**, **show**, **topics**, **health**, **validate**
> 阅读和检查维基。

**ingest**, **garden**
> 通过配置的 agent harness 从各种来源更新维基。

**sync**, **jobs**, **serve**
> 自动化状态、任务日志以及本地 Web 查看器。

# CAVEATS

- 写操作需要可用的本地 agent harness（Codex 或 Claude）及其凭证。
- 维基是纳入版本控制的 Markdown；CLI 还会在 ~/.codealmanac/ 下维护派生索引。
- 在当前契约下不是托管服务。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1)

# RESOURCES

```[Source code](https://github.com/AlmanacCode/codealmanac)```

```[Homepage](https://codealmanac.com)```

```[Documentation](https://github.com/AlmanacCode/codealmanac#readme)```

<!-- verified: 2026-07-11 -->
