# TAGLINE

预览 Terraform 基础设施变更

# TLDR

**创建执行计划**

```terraform plan```

**将计划保存到文件**

```terraform plan -out=[plan.tfplan]```

**带变量的计划**

```terraform plan -var="[key]=[value]"```

**计划销毁**

```terraform plan -destroy```

**针对特定目标的计划**

```terraform plan -target=[resource]```

# SYNOPSIS

**terraform** **plan** [_options_]

# PARAMETERS

**-out** _file_
> 将计划保存到文件。

**-var** _name=value_
> 设置变量。

**-var-file** _file_
> 变量文件。

**-target** _resource_
> 针对特定资源。

**-destroy**
> 规划销毁操作。

**-refresh-only**
> 仅刷新状态。

**-detailed-exitcode**
> 若有变更计划则退出码为 2。

# DESCRIPTION

**terraform plan** 创建显示拟议变更的执行计划。它将当前状态与配置进行比较。在应用前先审阅计划，以了解基础设施的变更内容。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-apply](/man/terraform-apply)(1)
