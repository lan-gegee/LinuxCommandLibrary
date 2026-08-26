# TAGLINE

让配置保持 DRY 的 Terraform 包装器

# TLDR

**初始化模块**

```terragrunt init```

**预览变更**

```terragrunt plan```

**应用变更**

```terragrunt apply```

**销毁基础设施**

```terragrunt destroy```

**对所有模块运行**

```terragrunt run-all apply```

**对所有模块做计划**

```terragrunt run-all plan```

**显示输出**

```terragrunt output```

**绘制依赖图**

```terragrunt graph-dependencies```

# SYNOPSIS

**terragrunt** [_init_] [_plan_] [_apply_] [_destroy_] [_run-all_] [_options_]

# PARAMETERS

**init**
> 初始化 Terraform。

**plan**
> 显示执行计划。

**apply**
> 应用变更。

**destroy**
> 销毁基础设施。

**output**
> 显示输出值。

**run-all** _CMD_
> 对所有模块运行命令。

**graph-dependencies**
> 显示依赖图。

**--terragrunt-config** _FILE_
> 配置文件。

**--terragrunt-working-dir** _DIR_
> 工作目录。

**--terragrunt-source** _SOURCE_
> 覆盖模块来源。

**--terragrunt-non-interactive**
> 非交互模式。

**--terragrunt-parallelism** _N_
> 并行操作数。

# DESCRIPTION

**terragrunt** 是 Terraform 的轻量包装器，提供额外工具来保持配置 DRY（不重复）并管理多个模块。

DRY 配置可避免跨环境的重复。公共设置只定义一次，由各模块继承。

远程状态配置集中管理。backend 设置无需在每个模块中重复编写。

模块间的依赖被自动管理。run-all 按依赖顺序在多个模块间执行命令。

before 和 after 钩子可在 Terraform 操作前后运行自定义命令，从而实现校验、通知和清理。

锁文件管理负责处理并发访问，使多名团队成员可以安全地协作共享基础设施。

# CONFIGURATION

**terragrunt.hcl**
> 模块级配置文件，定义 Terraform 来源、输入、依赖和 backend 设置

**TERRAGRUNT_CONFIG**
> 用于覆盖默认配置文件路径的环境变量

**TERRAGRUNT_DOWNLOAD**
> 用于设置 Terragrunt 下载 Terraform 源码目录的环境变量

# CAVEATS

相比纯 Terraform 增加了复杂度。配置语法有学习曲线。某些 Terraform 功能需要变通处理。

# HISTORY

**Terragrunt** 由 **Gruntwork** 于 **2016** 年前后创建，旨在解决大规模管理 Terraform 的痛点。它被广泛用于多环境、多账号的基础设施管理。

# INSTALL

```pacman: sudo pacman -S terragrunt```

```zypper: sudo zypper install terragrunt```

```brew: brew install terragrunt```

```nix: nix profile install nixpkgs#terragrunt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [pulumi](/man/pulumi)(1), [aws](/man/aws)(1)
