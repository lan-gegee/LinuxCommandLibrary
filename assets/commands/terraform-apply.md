# TAGLINE

应用 Terraform 基础设施变更

# TLDR

**应用变更**并进行交互式确认

```terraform apply```

**应用已保存的计划**文件

```terraform apply [plan.tfplan]```

**跳过确认提示**直接应用

```terraform apply -auto-approve```

**应用时传入变量**

```terraform apply -var="[key]=[value]"```

**替换特定资源**

```terraform apply -replace=[resource]```

**限制并行度进行应用**

```terraform apply -parallelism=[n]```

# SYNOPSIS

**terraform** **apply** [_options_] [_plan file_]

# PARAMETERS

**-auto-approve**
> 跳过应用前的交互式计划确认。

**-var** _name=value_
> 设置输入变量的值。可多次指定。

**-var-file** _file_
> 从文件加载变量值。

**-replace** _resource_
> 强制替换特定的资源实例。

**-target** _resource_
> 将操作限制在特定资源及其依赖项上。

**-parallelism** _n_
> 限制并发操作的数量。默认为 **10**。

**-compact-warnings**
> 以仅含摘要的紧凑形式显示警告消息。

**-input** _true|false_
> 启用或禁用交互式提示。默认为 **true**。

**-lock** _true|false_
> 操作期间锁定状态文件。默认为 **true**。

**-lock-timeout** _duration_
> 重试获取状态锁的时长。默认为 **0s**。

**-no-color**
> 禁用输出中的颜色代码。

**-json**
> 启用机器可读的 JSON 输出。隐含 **-input=false**。

**-destroy**
> 生成销毁所有资源的计划，然后执行它。

**-refresh-only**
> 仅更新状态以匹配远程对象。

**-state** _path_
> 状态文件的路径（旧式，仅限本地 backend）。

**-backup** _path_
> 备份先前状态文件的路径。

# DESCRIPTION

**terraform apply** 执行 Terraform 计划中提出的操作，以创建、更新或销毁基础设施。在不带已保存计划文件运行时，它会自动生成新计划，提示确认，然后执行所提议的变更。如果给定已保存的计划文件（来自 **terraform plan -out**），则直接执行该计划而不提示。

该命令将配置文件中定义的期望状态与当前状态进行比较，确定所需的最小变更集。在未提供已保存计划时，它支持 **terraform plan** 的所有规划模式和选项。

# CAVEATS

在非交互环境（CI/CD）中不带 **-auto-approve** 运行 **terraform apply** 会因等待输入而挂起。自动化场景请使用 **-auto-approve** 或管道传入已保存的计划文件。团队环境中不应禁用状态锁定，否则并发操作可能导致状态损坏。

# HISTORY

**Terraform** 由 **Mitchell Hashimoto** 创建，于 **2014** 年由 **HashiCorp** 发布。它开创了使用声明式配置语言（HCL）的基础设施即代码方法。apply 命令自首个版本起就是"先计划后应用"工作流的核心部分，JSON 输出支持在后续版本中加入。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-plan](/man/terraform-plan)(1), [terraform-init](/man/terraform-init)(1), [terraform-fmt](/man/terraform-fmt)(1)
