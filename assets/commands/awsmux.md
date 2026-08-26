# TAGLINE

跨多个账户并行运行一条 AWS CLI 命令

# TLDR

**检查**环境、aws CLI 与 profile 发现情况

```awsmux doctor```

**列出已验证的目标**（带 STS 身份的 profile/区域）

```awsmux targets --regions [us-east-1,us-west-2]```

在匹配的 profile 上**执行只读命令**

```awsmux run --profiles '[prod-*]' --format jsonl -- ec2 describe-instances --query 'Reservations[].Instances[].InstanceId'```

以并发数和排除模式进行**批量展开**

```awsmux run --profiles '[prod-*]' --exclude '[*-sandbox]' --concurrency [100] -- ec2 describe-vpcs```

**为变更/破坏性操作制定计划**（不实际执行）

```awsmux plan -- ssm put-parameter --name [/app/flag] --value [on] --type String```

**批准一个计划**（输出一次性令牌）

```awsmux approve [plan-01k...]```

使用令牌**应用已批准的计划**

```awsmux apply [plan-01k...] --approval-token [token]```

通过 stdio 为 AI 代理**提供 MCP 服务**

```awsmux mcp```

# SYNOPSIS

**awsmux** _command_ [_options_] [**--** _aws-cli-args_...]

# PARAMETERS

**doctor**

> 检查 aws CLI 是否存在、共享配置/凭证文件以及 profile 的发现情况。

**targets**

> 列出由 profile 和区域筛选条件选出的、经 STS 验证的账户/区域目标。

**run**

> 在选定的目标上并行执行 aws CLI 调用。只读操作可直接运行；变更和破坏性操作需要确认、**--yes**（仅限变更操作）或计划。

**plan**

> 为变更或破坏性的 aws CLI 操作构建不可变计划，但不执行它。

**approve** _PLAN_ID_

> 批准计划并打印一次性批准令牌（从不存储）。

**apply** _PLAN_ID_ **--approval-token** _TOKEN_

> 执行已批准的计划。令牌与计划的 SHA-256 哈希绑定；若被篡改则拒绝应用。

**replay**

> 从 **history** 中重新执行过去的一次运行，并重新选定其目标。

**history**

> 显示过去的运行及结果。

**mcp**

> 通过 stdio 提供代理接口服务（Model Context Protocol）。不需要额外凭证；使用与 Shell 相同的 AWS profile。

常用选择与执行选项（用于 **run**、**plan**、**targets** 及相关命令）：

**--profiles** _GLOB_

> 包含匹配 shell 风格通配符的 profile（逗号分隔）。

**--exclude** _GLOB_

> 排除匹配的 profile。

**--regions** _LIST_

> 要展开到的区域，逗号分隔。

**--dedupe**

> 合并解析到相同账户、主体和区域的目标（会运行 STS 预检）。

**--concurrency** _N_

> 并行的 aws CLI 工作进程数（默认 **100**）。

**--timeout** _DURATION_

> 每个目标的超时时间（例如 **30s**）。

**--format** _jsonl_|_table_

> 结果流格式。

**--output-dir** _DIR_

> 为每个目标写入一个结果文件。

**--interactive**

> 目标的复选框选择器（仅限 **run**）。

**--max-errors** _N_ / **--stop-on-access-denied**

> 达到错误阈值时停止展开。

# DESCRIPTION

**awsmux** 将单条 **aws** CLI 命令并行展开到多个账户和区域。它会从标准的共享配置和凭证文件（**~/.aws/config**、**~/.aws/credentials** 以及 **AWS_CONFIG_FILE** / **AWS_SHARED_CREDENTIALS_FILE**）发现 profile，原样支持 SSO、静态密钥和 **credential_process** 类型的 profile，并且始终通过已安装的 **aws** CLI 执行。每个目标在工作开始前都会经过 STS 身份校验。

操作会被分类为 **read_only**、**mutating**、**destructive** 和 **unknown**（按变更处理）。只读操作（如 describe/list/get、**s3 ls**）可以直接运行。变更操作需要 **--yes**、交互式确认或已批准的计划。破坏性操作（delete/terminate/revoke、**s3 rm**、**s3 mv**、**s3 sync --delete** 等）绝不接受 **--yes**；必须输入确认文本或走 plan/approve/apply 流程。某些看似只读的操作会被强制归为变更操作（铸造凭证的 STS 调用、**s3 presign**、将 s3api get-object 输出到本地 outfile）。

退出码对自动化是稳定的：**0** 全部成功，**1** 部分失败，**2** 选择/配置错误，**3** 需要批准或批准被拒绝，**4** 因达到阈值而停止。**awsmux mcp** 通过 MCP 将同样的安全模型暴露给 AI 代理；代理可以列出目标并执行只读操作，但变更操作会返回一个必须由人在真实终端中批准的计划。

# CAVEATS

需要在 **PATH** 中有可用的 **aws** CLI（或对于 GUI 环境下 PATH 不完整的 MCP 客户端，需要位于已知安装路径）。awsmux 不取代 **aws-vault** 之类的凭证工具；它通过这些工具管理的 profile 运行。破坏性命令无法用 **--yes** 强制执行。计划令牌与计划内容绑定：批准之后修改计划文件会使 apply 失效。默认并发数 100 会派生大量 aws 子进程——请根据速率限制和本地资源进行调整。

# SEE ALSO

[aws](/man/aws)(1), [aws-vault](/man/aws-vault)(1), [go](/man/go)(1)

# RESOURCES

```[Source code](https://github.com/0hardik1/awsmux)```

```[Documentation](https://github.com/0hardik1/awsmux/blob/main/docs/ARCHITECTURE.md)```

<!-- verified: 2026-07-26 -->
