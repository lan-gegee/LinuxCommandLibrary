# TAGLINE

预览 OpenTofu 基础设施变更

# TLDR

**创建执行计划**

```tofu plan```

**将计划保存到文件**

```tofu plan -out=[plan.tfplan]```

**带变量生成计划**

```tofu plan -var="[key]=[value]"```

**规划销毁操作**

```tofu plan -destroy```

# SYNOPSIS

**tofu** **plan** [_options_]

# PARAMETERS

**-out** _file_
> 将计划保存到文件。

**-var** _name=value_
> 设置变量。

**-var-file** _file_
> 变量文件。

**-target** _resource_
> 定位到特定资源。

**-destroy**
> 规划销毁操作。

**-refresh-only**
> 只刷新状态而不提出变更。

**-refresh=false**
> 跳过与远程对象同步状态。

**-parallelism** _n_
> 限制并发操作数（默认：10）。

**-detailed-exitcode**
> 返回 0（无变更）、1（错误）或 2（存在变更）。

**-input=false**
> 禁用对未设置变量的提示输入。

**-json**
> 机器可读的 JSON 输出。

# DESCRIPTION

**tofu plan** 为 OpenTofu 创建执行计划。OpenTofu 是 Terraform 的开源分支。它在应用到基础设施之前展示提议的变更。

# INSTALL

```dnf: sudo dnf install opentofu```

```pacman: sudo pacman -S opentofu```

```apk: sudo apk add opentofu```

```zypper: sudo zypper install opentofu```

```brew: brew install opentofu```

```nix: nix profile install nixpkgs#opentofu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tofu](/man/tofu)(1), [terraform-plan](/man/terraform-plan)(1)
