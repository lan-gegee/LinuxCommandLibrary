# TAGLINE

移除 Terraform 资源实例的 tainted 状态

# TLDR

**移除资源的 taint 标记**，使其不会被替换

```terraform untaint aws_instance.example```

即使资源在状态中**缺失也照样解除标记**

```terraform untaint -allow-missing module.foo.resource.bar```

**解除标记时不获取状态锁**

```terraform untaint -lock=false aws_instance.example```

# SYNOPSIS

**terraform** **untaint** [_options_] _address_

# DESCRIPTION

**terraform untaint** 清除状态文件中资源实例的 tainted 标志。该资源在下一次 apply 时将被正常对待（不强制替换）。它不会修改远程基础设施——只修改状态。

与 `terraform taint` 一样，此命令已被弃用，建议改用更明确的机制，例如 apply 时的 `-replace`。

# PARAMETERS

**-allow-missing**
> 即使地址在状态中不存在也成功执行。

**-lock**=_true|false_
> 控制状态锁定（默认 true）。使用 `-lock=false` 禁用。

**-lock-timeout**=_duration_
> 等待获取锁的时长（例如 `3s`）。

**-no-color**
> 禁用输出中的终端颜色序列。

# CAVEATS

已弃用。需要强制替换时，请优先使用 `terraform apply -replace=...`。untaint 只移除状态中的标记；它不会修复远程对象。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-apply](/man/terraform-apply)(1), [terraform-taint](/man/terraform-taint)(1)

# RESOURCES

```[Documentation](https://developer.hashicorp.com/terraform/cli/commands/untaint)```

<!-- verified: 2026-07-11 -->
