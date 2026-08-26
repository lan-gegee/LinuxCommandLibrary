# TAGLINE

以人类可读形式显示 Terraform 状态或计划

# TLDR

**显示当前状态**

```terraform show```

**显示已保存的计划文件**

```terraform show [plan.tfplan]```

**以 JSON 输出状态**

```terraform show -json```

**以 JSON 输出计划文件**

```terraform show -json [plan.tfplan]```

**无颜色显示状态**

```terraform show -no-color```

# SYNOPSIS

**terraform** **show** [_options_] [_file_]

# PARAMETERS

**-json**
> 以机器可读的 JSON 格式输出状态或计划。敏感值会以明文显示。

**-no-color**
> 禁用输出中的终端颜色代码。

# DESCRIPTION

**terraform show** 以人类可读格式读取并显示 Terraform 状态或计划文件。不带文件参数调用时，它会渲染最新的状态快照，显示所有受管资源及其当前属性值。给定计划文件（由 **terraform plan -out** 创建）时，它显示拟议的变更，包括将被创建、修改或销毁的资源。

**-json** 标志生成结构化的 JSON 输出，适合外部工具、CI/CD 流水线或策略引擎处理。该 JSON 格式包含完整的资源状态、计划的变更以及 provider 配置。

# CAVEATS

**-json** 标志会**以明文暴露敏感值**，包括存储在状态中的密码、令牌和密钥。状态文件应被视为敏感数据。JSON 输出格式要求 Terraform **0.12 或更高版本**，且其模式可能在大版本之间变化。对计划文件使用 **-json** 时，该计划必须是在未使用 **-refresh=false** 的情况下创建的。

# HISTORY

**show** 子命令自 **HashiCorp** 早期的 Terraform 版本起即可用。JSON 输出支持加入于 **Terraform 0.12**（2019 年 5 月），是让所有命令提供机器可读输出这一更广泛工作的一部分。此后 JSON 输出模式被逐步扩展，覆盖了更多资源元数据和计划变更细节。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-plan](/man/terraform-plan)(1), [terraform-apply](/man/terraform-apply)(1), [terraform-output](/man/terraform-output)(1)
