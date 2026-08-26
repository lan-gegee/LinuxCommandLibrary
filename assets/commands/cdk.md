# TAGLINE

AWS Cloud Development Kit 命令行工具

# TLDR

**初始化新的 CDK 项目**

```cdk init app --language [typescript]```

**列出应用中的堆栈**

```cdk list```

**合成 CloudFormation 模板**

```cdk synth```

**部署堆栈**

```cdk deploy [StackName]```

**部署所有堆栈**

```cdk deploy --all```

**显示与已部署堆栈的差异**

```cdk diff [StackName]```

**销毁堆栈**

```cdk destroy [StackName]```

# SYNOPSIS

**cdk** [_global_options_] _command_ [_arguments_] [_command_options_]

# DESCRIPTION

**cdk** 是 AWS Cloud Development Kit 的命令行工具，用于使用熟悉的编程语言以代码方式定义云基础设施。它从 TypeScript、Python、Java、C# 或 Go 代码合成 CloudFormation 模板并部署到 AWS。

开发者无需手写 CloudFormation YAML 或 JSON，而是使用 construct——可复用、可组合的类来定义基础设施，每个 construct 代表 AWS 资源。CDK 将这些 construct 合成为 CloudFormation 模板，随后部署以创建和管理实际的 AWS 资源。

典型工作流包括：用 `cdk init` 初始化项目、编写基础设施代码、用 `cdk diff` 预览更改、再用 `cdk deploy` 部署。`cdk watch` 命令可在开发期间实现热重载。

# COMMANDS

**init**
> 从模板创建新的 CDK 项目

**list** (ls)
> 列出 CDK 应用中的堆栈

**synth**
> 合成 CloudFormation 模板

**deploy**
> 将堆栈部署到 AWS

**destroy**
> 从 AWS 删除堆栈

**diff**
> 显示堆栈之间的差异

**bootstrap**
> 部署 CDK 引导堆栈

**watch**
> 监视变更并部署

**context**
> 管理缓存的上下文值

**docs**
> 打开 CDK 文档

# PARAMETERS

**--all**
> 部署/销毁所有堆栈

**--hotswap**
> 尽可能使用快速部署

**--require-approval** _level_
> 审批级别：never、any-change、broadening

**--profile** _name_
> 要使用的 AWS profile

**--region** _region_
> AWS 区域

**--output** _dir_
> 合成模板的输出目录

**--verbose**, **-v**
> 详细输出

# CONFIGURATION

**cdk.json**
> 项目配置，包括应用入口点、上下文值和特性开关。

# CAVEATS

需要 Node.js 和已配置的 AWS 凭据。首次部署前需对每个账户/区域运行一次 `cdk bootstrap`。

# INSTALL

```dnf: sudo dnf install cdk```

```brew: brew install cdk```

```nix: nix profile install nixpkgs#cdk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [terraform](/man/terraform)(1), [pulumi](/man/pulumi)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cdk)```

```[Documentation](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)```

<!-- verified: 2026-06-22 -->
