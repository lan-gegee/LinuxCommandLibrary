# TAGLINE

只读的 AWS 成本浪费与卫生状况扫描器

# TLDR

**安装**并启动交互式向导

```npm install -g @cloudrift/cli && cloudrift```

在一个或多个区域**分析**浪费情况

```cloudrift analyze -r us-east-1 eu-west-1```

**导出** PDF 报告

```cloudrift analyze -r us-east-1 --pdf```

**扫描**僵死/未使用资源（通常为 $0 成本的卫生检查）

```cloudrift dead-resources -r us-east-1```

**扫描**安全配置错误

```cloudrift resource-security -r us-east-1```

**比较**月度支出或绘制趋势图（Cost Explorer — 会产生计费）

```cloudrift cost```

```cloudrift trend --months 12```

# SYNOPSIS

**cloudrift** [_command_] [_options_]

# DESCRIPTION

**cloudrift** 是一个开源、只读的 AWS 成本优化 CLI。它能发现闲置、孤立和过度配置的资源，估算每月浪费，且从不删除、修改或停止任何东西 — 仅生成报告。在交互式终端中不带子命令运行时，它会启动一个引导式向导。

核心领域：

- **analyze** — 成本浪费与优化机会（EBS、EIP、闲置 NAT、利用率不足的 EC2/RDS，以及更多扫描器）。
- **dead-resources** — 可能花费 $0 但会弄乱账户的废弃资产（未使用的密钥对、空的 S3、不活跃的 IAM 等）。
- **resource-security** — 配置风险（开放的安全组、公开的 S3、缺失 MFA、未加密的卷等）。
- **cost** / **trend** — Cost Explorer 支出比较与月度图表（**每次 CE 请求 $0.01**；除非使用 **-y**，否则需要确认）。
- **history** — 位于 **~/.cloudrift/trends/** 下的本地 SQLite 快照。
- **mcp** — 用于智能体集成的 stdio MCP 服务器。

需要 Node.js 20+ 以及具备文档所述只读 IAM 策略的 AWS 凭证。也可通过 Homebrew 安装（**elleVas/cloudrift/cloudrift**）。

# COMMANDS

**analyze** [**-r** _region_...] [**--pdf**] [other flags]

> 运行浪费/优化扫描器。默认区域通常为 **us-east-1**。

**dead-resources** [**-r** _region_...] [**--scanners** _id_]

> 针对僵死或未使用资源的卫生扫描。

**resource-security** [**-r** _region_...] [**--scanners** _id_]

> 安全态势检查。

**cost** / **trend**

> 账单比较与多月趋势（会产生 Cost Explorer 费用）。

**history** [**--domain** _name_] [**--limit** _n_]

> 读取本地先前的扫描快照。

**mcp**

> 以本地 Model Context Protocol 服务器形式通过 stdio 运行。

# CAVEATS

发现结果仅为估算值 — 采取行动前请先行验证。合理化调整启发式规则（例如仅基于 CPU 的低利用率判断）不能替代 AWS Compute Optimizer。**cost**/**trend** 是唯一会刻意产生 AWS API 费用的命令。排除标签 **cloudrift:ignore** 是一种信任边界，而非安全控制手段。

# SEE ALSO

[aws](/man/aws)(1), [aws-cli](/man/aws-cli)(1)

# RESOURCES

```[Source code](https://github.com/elleVas/cloudrift)```

```[Homepage](https://www.npmjs.com/package/@cloudrift/cli)```

```[Documentation](https://github.com/elleVas/cloudrift/tree/main/docs/en)```

<!-- verified: 2026-07-30 -->
