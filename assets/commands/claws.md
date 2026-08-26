# TAGLINE

用于 AWS 资源管理的 TUI 工具

# TLDR

使用默认 AWS 凭证**启动**

```claws```

**使用**指定的 AWS profile

```claws -p [myprofile]```

**定位**到指定区域

```claws -r [us-west-2]```

直接**进入** EC2 视图

```claws -s ec2```

多 profile 与多区域模式

```claws -p [dev],[prod] -r [us-east-1],[ap-northeast-1]```

以无破坏性操作的**安全浏览**模式运行

```claws --read-only```

# SYNOPSIS

**claws** [_flags_]

# PARAMETERS

**-p**, **--profile** _name_
> 指定一个或多个 AWS profile；多个时用逗号分隔或重复该选项。

**-r**, **--region** _name_
> 指定一个或多个 AWS 区域；多个时用逗号分隔或重复该选项。

**-s**, **--service** _name_
> 直接在特定服务/视图上启动（如 dashboard、ec2、rds/snapshots）。

**--read-only**
> 禁用所有破坏性操作。

# DESCRIPTION

**claws** 是一个用于管理 AWS 资源的交互式终端 UI，其灵感来自 **k9s**（Kubernetes 集群 TUI）。它支持约 70 种 AWS 服务和 175 种资源类型，包括 EC2、S3、Lambda、RDS、ECS、EKS、IAM 和 CloudWatch。它采用 vim 风格的按键绑定进行导航。

主要功能包括启动和停止 EC2 实例、跨资源导航（从 VPC 到子网、从函数到日志组）、支持并行查询的多 profile 与多区域切换、模糊搜索与基于标签的过滤、并排 diff 的资源比较、由 AWS Bedrock 驱动的内置 AI 助手、6 种配色主题，以及复制资源 ID 和 ARN 的快捷键。

# KEY BINDINGS

```
j/k      Navigate up/down     Enter/d  View details
/        Fuzzy search         :        Command mode
a        Actions menu         A        AI Chat (Bedrock)
R        Select region(s)     P        Select profile(s)
Tab      Cycle resource type  m        Mark for comparison
y/Y      Copy ID / ARN        q        Quit
```

# CAVEATS

需要通过 **~/.aws/credentials**、环境变量或 SSO 配置有效的 AWS 凭证。AI 聊天功能需要访问 AWS Bedrock。浏览生产环境时建议使用 **--read-only** 选项，以防误操作造成破坏。

# HISTORY

**claws** 于 **2024 年 12 月**首次发布，并在 2025 年初快速迭代。它使用 Go 编写，基于 Bubbletea 和 Lipgloss TUI 框架以及适用于 Go v2 的 AWS SDK。基于 Apache License 2.0 授权。

# INSTALL

```nix: nix profile install nixpkgs#claws```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [k9s](/man/k9s)(1), [lazydocker](/man/lazydocker)(1)
