# TAGLINE

面向云、代码和 Kubernetes 基础设施的只读深度调研 CLI

# TLDR

提出一个**交互式**的基础设施调研问题

```cynative "what in my cloud is publicly exposed that shouldn't be?"```

运行**单次非交互**任务后退出

```cynative -p "which IAM roles can escalate to admin?"```

将 IaC 通过管道传入**一次性审查**

```cat main.tf | cynative -p "review this Terraform for misconfigurations"```

不启动会话即**校验**配置与连接器

```cynative doctor```

在 doctor 中探测已配置的 **LLM**

```cynative doctor --live-llm```

为**无人值守**运行自动批准工具调用

```cynative -p "live cloud resources absent from IaC" --auto-approve```

# SYNOPSIS

**cynative** [_options_] [_"task"_]

**cynative** **-p**|_--print_ _"task"_

**cynative** **doctor** [_--live-llm_]

# PARAMETERS

**-p**, **--print** _task_
> 非交互地运行一个任务后退出（适用于脚本和管道）

**--auto-approve**
> 跳过逐个工具的审批提示（无 TTY 时需要）

**-v**
> 详细模式（例如流式显示内部沙箱的工具调用）

**doctor**
> 校验配置和连接器的就绪状态

**--live-llm**
> 配合 **doctor** 使用，以一次不含工具的往返请求探测已配置的模型

**completion** _shell_
> Shell 补全辅助（参见 `cynative completion <shell> --help`）

**--version**
> 打印版本、提交哈希、构建日期、Go 版本和平台信息

# DESCRIPTION

**cynative** 是一个只读的基础设施调研代理。它将前沿大语言模型接入你的真实环境——AWS、GCP、Azure、Kubernetes（包括 EKS/GKE/AKS）、GitHub 和 GitLab——并返回有证据支撑、经过验证的答案。

与带 MCP 插件的通用编程代理不同，cynative 是**从构造上就是只读的**：每次调用都会先依据安全审计风格的策略进行授权，然后才附加凭据；调研代码在沙箱中运行；密钥会从模型上下文中脱敏；每个工具调用都会记录到一个默认拒绝（fail-closed）的 JSONL 审计日志（默认位于 `~/.cynative/audit.log`）。

它使用你的 Shell 中已有的凭据（没有单独的凭据存储）。对于批量工作，它可以编写并运行沙箱化的 JavaScript 来并发发起大量 API 调用。交互模式支持行编辑和历史记录；按一次 Esc 或 Ctrl-C 可优雅地停止正在运行的任务。

通过 `CYNATIVE_LLM_PROVIDER`、`CYNATIVE_LLM_MODEL` 等环境变量以及各提供商的 API 密钥来配置 LLM，也可以使用 `~/.cynative/config.yaml`。资源上限（`CYNATIVE_MAX_TOTAL_TOKENS`、`CYNATIVE_MAX_ITERATIONS` 等）可约束无人值守的运行。

# CAVEATS

务必使用最小权限的只读凭据。托管的 LLM 提供商会收到提示词和工具结果（脱敏之后）。Token 和迭代次数限制默认很高甚至无界——用于 cron/CI 时请设置上限。运维类页脚信息（耗时、token 数）输出到 **stderr**，因此 stdout 保持干净便于管道处理。

# HISTORY

开源 Go CLI（Apache-2.0），用于自主可控、证据支撑的基础设施调研，内置云/VCS 连接器，并带有对写操作默认拒绝的行动闸门。

# SEE ALSO

[aws](/man/aws)(1), [gcloud](/man/gcloud)(1), [az](/man/az)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/cynative/cynative)```

```[Documentation](https://github.com/cynative/cynative/tree/main/docs)```

<!-- verified: 2026-07-29 -->
