# TAGLINE

验证 Terraform 配置的语法与内部一致性

# TLDR

**校验**当前目录中的配置

```terraform validate```

以 **JSON****输出**校验结果

```terraform validate -json```

**校验**时无颜色

```terraform validate -no-color```

在无 backend 的 init 之后进行**校验**（CI / 模块）

```terraform init -backend=false && terraform validate```

# SYNOPSIS

**terraform** **validate** [_options_]

# PARAMETERS

**-json**
> 生成机器可读的 JSON 输出（禁用颜色）。适合编辑器集成和 CI。

**-no-color**
> 禁用人类可读输出中的颜色。

**-var** _'NAME=VALUE'_
> 设置单个根模块输入变量。可重复使用。

**-var-file** _FILENAME_
> 从 **.tfvars** 文件加载变量值。可重复使用。

# DESCRIPTION

**terraform validate** 检查工作目录中的 Terraform 配置文件在语法上是否有效、内部是否一致。它验证属性名、值类型和模块结构，而不连接远程状态 backend 或 provider API 等远程服务。

校验要求工作目录已初始化，且引用的 provider 和模块已安装。若要在不配置 backend 的情况下本地检查，请先运行 **terraform init -backend=false**。要在特定 workspace、变量和状态的上下文中校验配置，请使用 **terraform plan**，它包含一个隐式的校验步骤。

该命令可以安全地作为编辑器保存后检查或可复用模块的 CI 步骤自动运行。配合 **-json** 时，结果包括 **valid**、**error_count**、**warning_count** 以及描述每个问题的 **diagnostics** 数组。

# CAVEATS

不能替代 **terraform plan**：远程资源是否存在、provider API 行为以及运行时变量约束都不会被完整检验。未初始化的目录在插件和模块安装完成前会校验失败。检测到错误时退出码非零；仅有警告并不会使配置无效。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-24 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-init](/man/terraform-init)(1), [terraform-plan](/man/terraform-plan)(1), [terraform-fmt](/man/terraform-fmt)(1)

# RESOURCES

```[Documentation](https://developer.hashicorp.com/terraform/cli/commands/validate)```

```[Homepage](https://www.terraform.io)```

```[Source code](https://github.com/hashicorp/terraform)```

<!-- verified: 2026-07-24 -->
