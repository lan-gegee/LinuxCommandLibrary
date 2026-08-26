# TAGLINE

将 Terraform 资源标记为 tainted，强制在下一次 apply 时替换

# TLDR

**将资源标记为 tainted**，使其在下次 apply 时被重建

```terraform taint aws_instance.example```

即使资源在状态中**缺失也照样标记**

```terraform taint -allow-missing module.foo.aws_instance.bar[0]```

**不锁定状态进行标记**

```terraform taint -lock=false aws_instance.example```

# SYNOPSIS

**terraform** **taint** [_options_] _address_

# DESCRIPTION

**terraform taint** 将 Terraform 状态中的一个资源实例标记为 "tainted"。在下一次 `terraform apply` 时，Terraform 将销毁现有对象并创建替代对象。

过去常用于强制替换变得不一致或已损坏的资源。

**注意：** 此命令已被弃用。推荐的做法是在 `terraform apply` 或 `terraform plan` 上使用 `-replace` 标志，例如 `terraform apply -replace="aws_instance.example"`。

# PARAMETERS

**-allow-missing**
> 即使资源地址不在状态中也成功执行。

**-lock**=_true|false_
> 获取状态锁（默认 true）。使用 `-lock=false` 禁用。

**-lock-timeout**=_duration_
> 重试获取状态锁的时长（例如 `3s`）。

**-var** '_NAME=VALUE_'
> 设置输入变量的值（可重复）。

**-var-file**=_filename_
> 从 `.tfvars` 文件加载变量值（可重复）。

# CAVEATS

在现代 Terraform 版本中，tainting 已被弃用。更推荐在规划/应用时使用 `-replace`，因为它更明确且一步完成。taint/untaint 只影响状态，还需要单独执行一次 apply。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-apply](/man/terraform-apply)(1), [terraform-untaint](/man/terraform-untaint)(1)

# RESOURCES

```[Documentation](https://developer.hashicorp.com/terraform/cli/commands/taint)```

<!-- verified: 2026-07-11 -->
