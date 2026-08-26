# TAGLINE

销毁 Terraform 管理的基础设施

# TLDR

**销毁**当前配置中的所有资源

```terraform destroy```

**销毁**时不进行交互式确认

```terraform destroy -auto-approve```

仅**销毁特定资源**

```terraform destroy -target=[resource_type.resource_name]```

**预览**将销毁的内容而不执行

```terraform plan -destroy```

使用指定**变量值****销毁**

```terraform destroy -var '[name]=[value]'```

使用**变量文件****销毁**

```terraform destroy -var-file=[prod.tfvars]```

以受限的**并行度****销毁**，避免触发 API 速率限制

```terraform destroy -parallelism=[5]```

# SYNOPSIS

**terraform destroy** [_options_]

# PARAMETERS

**-auto-approve**
> 跳过交互式确认提示

**-target=**_RESOURCE_
> 仅销毁指定的资源及其依赖项。可多次指定。

**-var** '_NAME_=_VALUE_'
> 设置输入变量的值。可多次指定。

**-var-file=**_PATH_
> 从文件加载变量值

**-lock=**_BOOL_
> 控制 Terraform 是否锁定状态文件。默认：**true**。

**-lock-timeout=**_DURATION_
> 等待获取状态锁的时长。示例：**20s**。

**-parallelism=**_N_
> 限制并发资源操作数。默认：**10**。

**-refresh=**_BOOL_
> 是否在规划前刷新状态。默认：**true**。

**-state=**_PATH_
> 状态文件的路径。默认：**terraform.tfstate**。

**-no-color**
> 禁用彩色输出

# DESCRIPTION

**terraform destroy** 永久删除当前 Terraform 状态文件中跟踪的所有基础设施资源。它是 **terraform apply -destroy** 的便捷别名。

该命令读取状态文件以识别受管资源，针对云服务商 API 验证状态，构建依赖图以确定正确的反向销毁顺序，给出计划供确认，然后通过服务商 API 删除资源。完成后它会更新状态文件，反映这些资源已不存在。

它主要用于开发和测试环境中的临时基础设施。对于生产环境，只应在受控的下线场景中使用。

# CAVEATS

此命令**不可逆**。资源一旦被销毁，云服务商将其永久移除，Terraform 无法恢复它们。如果销毁操作在中途失败，你可能处于部分销毁的状态。该命令完全基于状态文件运行，不感知未在状态中跟踪的资源。在服务商层面启用了**删除保护**的资源，在手动解除保护之前无法销毁。配置了 **lifecycle { prevent_destroy = true }** 的资源会使销毁失败并报错。使用 **-target** 进行选择性销毁可能使基础设施处于不一致的状态，应仅用于例外情况。

# HISTORY

**Terraform** 由 **Mitchell Hashimoto** 和 **Armon Dadgar** 在 **HashiCorp** 创建，**v0.1.0** 于 **2014 年 7 月**发布。destroy 子命令自最早版本起就是 Terraform 核心工作流的一部分。在 **v0.15.2**（2021 年 4 月）中，**terraform apply -destroy** 作为显式形式加入，使 **terraform destroy** 成为官方认可的便捷别名。Terraform 于 **2021 年 6 月**随 **v1.0.0** 正式发布（GA）。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-plan](/man/terraform-plan)(1), [terraform-apply](/man/terraform-apply)(1)
