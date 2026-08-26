# TAGLINE

CDK for Terraform 命令行工具

# TLDR

**初始化一个新的 CDKTF 项目**

```cdktf init --template=[typescript] --local```

**生成 provider 绑定**

```cdktf get```

**合成（synthesize）Terraform 配置**

```cdktf synth```

**规划基础设施变更**

```cdktf diff```

**应用基础设施变更**

```cdktf deploy```

**销毁基础设施**

```cdktf destroy```

**将 HCL 转换为 CDKTF**

```cdktf convert < [main.tf]```

**列出栈**

```cdktf list```

# SYNOPSIS

**cdktf** _command_ [_options_]

# PARAMETERS

**init**
> 初始化一个新的 CDKTF 项目。

**get**
> 从 cdktf.json 生成 provider 绑定。

**synth**
> 合成（synthesize）Terraform JSON 配置。

**diff**
> 显示计划中的变更（terraform plan）。

**deploy** [_stacks_]
> 部署基础设施（terraform apply）。

**destroy** [_stacks_]
> 销毁基础设施。

**convert**
> 将 HCL Terraform 代码转换为 CDKTF。

**list**
> 列出应用程序中的所有栈。

**output** [_stacks_]
> 显示已部署栈的输出。

**watch** [_stacks_]
> 监视文件变化并自动触发部署。

**debug**
> 获取关于当前项目和环境的调试信息。

**provider** _subcommand_
> 管理 provider（添加、升级、列出）。

**--template** _name_
> 项目模板：typescript、python、java、csharp、go。

**--local**
> 使用本地 Terraform 状态。

**--auto-approve**
> 跳过交互式确认。

**-o**, **--output** _directory_
> 合成文件的输出目录。

**--log-level** _level_
> 设置日志级别（debug、info、warn、error）。

**--version**
> 显示版本号。

# DESCRIPTION

**CDK for Terraform (CDKTF)** 允许使用熟悉的编程语言而不是 HCL 来定义基础设施。它生成 Terraform JSON 配置，让你可以用 TypeScript、Python、Java、C# 或 Go 编写基础设施代码，同时充分利用整个 Terraform 生态。

CDKTF 项目通过定义 **construct** 来表示基础设施资源。**synth** 命令将代码编译为 **cdktf.out/** 中的 Terraform JSON，可供检查或手动应用。**deploy** 命令则一步完成合成与应用。

Provider 绑定由 Terraform provider 生成，提供类型安全和 IDE 自动补全。复杂逻辑、循环和条件判断使用编程语言的原生特性，而不受 HCL 的限制。

# CONFIGURATION

**cdktf.json**
> 项目配置文件，包含 Terraform provider、模块以及应用程序入口点。

# CAVEATS

CDKTF 已于 **2025 年 12 月 10 日** 停止维护并被归档。HashiCorp 不再维护或开发该项目。归档代码仍可在 GitHub 上获取，但为只读状态，不会再有更新或兼容性修复。

需要单独安装 Terraform CLI。对于资源较多的 provider，生成 provider 绑定可能较慢。状态管理遵循 Terraform 的模式；使用 CDKTF 前请先了解 Terraform 状态机制。

# HISTORY

CDK for Terraform 由 **HashiCorp** 与 **AWS** 合作于 **2020 年 7 月** 宣布，将 AWS CDK 的 CDK（Cloud Development Kit）方式引入 Terraform。它于 **2022 年 8 月** 正式发布。由于未能大规模找到产品市场契合点，该项目于 **2025 年 12 月 10 日** 停止维护，HashiCorp 选择专注于 Terraform 核心。

# INSTALL

```brew: brew install cdktf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [pulumi](/man/pulumi)(1)
