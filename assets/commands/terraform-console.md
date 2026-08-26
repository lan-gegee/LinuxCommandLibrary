# TAGLINE

交互式 Terraform 表达式求值器

# TLDR

**打开**交互式控制台

```terraform console```

基于**计划状态****求值**表达式

```terraform console -plan```

**非交互式求值**表达式

```echo '[expression]' | terraform console```

**打开**控制台并指定**变量文件**

```terraform console -var-file=[path/to/vars.tfvars]```

# SYNOPSIS

**terraform console** [_options_]

# PARAMETERS

**-plan**
> 先生成执行计划，并基于计划状态而非当前状态对表达式求值。显示 Terraform 预期在计划应用之后的值

**-state=**_path_
> 用于表达式求值的本地状态文件路径（默认：terraform.tfstate；旧式，仅限本地 backend）

**-var** _'NAME=VALUE'_
> 在命令行设置变量值

**-var-file=**_FILE_
> 从文件加载变量定义

# DESCRIPTION

**terraform console** 提供一个用于求值 Terraform 表达式的交互式 **REPL**（读取-求值-打印循环）。它可用于测试表达式和插值、检查当前状态值、试用 **split()**、**lower()**、**length()** 等内置函数，以及交互式调试配置。

该控制台是**只读**的，不会修改状态、配置文件或基础设施资源。但它运行期间会锁定状态文件，阻止并发的 **plan** 或 **apply** 操作。

可以直接访问当前 Terraform 状态中的字段、输出、变量和本地值。输入 **exit** 或按 **Ctrl-C** / **Ctrl-D** 退出。

# CAVEATS

控制台运行期间会**锁定状态文件**，因此无法在同一 workspace 中并发运行 **terraform plan** 或 **terraform apply**。使用控制台前必须先运行 **terraform init**。尚未创建的资源会显示为 unknown，除非使用 **-plan** 标志。特殊的 **type()** 函数仅在控制台中可用（自 Terraform v1.1 起）。无法以交互方式定义新变量。

# HISTORY

由 HashiCorp 联合创始人 Mitchell Hashimoto 于 **2016 年 11 月**随 **Terraform v0.8** 推出。最初被描述为一个用于试验插值的交互式控制台。**-var** 和 **-var-file** 支持后来通过 **2019 年 9 月**的一次修复加入。**type()** 函数作为仅限控制台的功能加入于 **Terraform v1.1**。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-plan](/man/terraform-plan)(1), [terraform-apply](/man/terraform-apply)(1), [terraform-output](/man/terraform-output)(1), [terraform-login](/man/terraform-login)(1)
