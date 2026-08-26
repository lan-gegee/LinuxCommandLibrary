# TAGLINE

在部署前预览基础设施变更

# TLDR

**预览变更**

```pulumi preview```

**预览指定堆栈**

```pulumi preview -s [stack]```

**以详细差异预览**

```pulumi preview --diff```

**以 JSON 格式预览**

```pulumi preview --json```

**预览指定目标**

```pulumi preview --target [urn]```

# SYNOPSIS

**pulumi** **preview** [_options_]

# PARAMETERS

**-s**, **--stack** _name_
> 目标堆栈名称。

**--diff**
> 为每个变更的资源显示属性级别的详细差异。

**--json**
> 输出机器可读的 JSON。

**--target** _urn_
> 仅对列出的资源 URN 进行预览操作（可重复使用）。

**--target-dependents**
> 同时包含依赖于这些目标的资源。

**--refresh**
> 在计算预览前从云提供商刷新状态。

**--expect-no-changes**
> 如果检测到任何变更则以非零状态退出。适用于 CI 中的漂移检测。

**-p**, **--parallel** _n_
> 并发运行的资源操作最大数量。

**--config** _key=value_
> 为本次预览覆盖一个配置值。

**--message** _text_
> 随更新一起记录的可选消息。

**--show-replacement-steps**
> 显示构成替换操作的底层创建/删除步骤。

# DESCRIPTION

**pulumi preview** 计算并显示 **pulumi up** 将执行的资源操作集合，但不实际进行任何更改。它将程序中描述的目标状态与堆栈记录的当前状态（可选先从云端刷新）进行比较，并报告由此产生的创建/更新/替换/删除操作。

使用 **--diff** 查看将要发生变化的完整属性级视图；在 CI 流水线中使用 **--expect-no-changes** 来检测程序与已部署基础设施之间的漂移。

# CAVEATS

预览仅反映 Pulumi 能静态确定的内容：provider 端的验证错误或运行时故障仍可能在 **pulumi up** 期间出现。不使用 **--refresh** 时，预览基于最后已知的状态计算，该状态可能已过时。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-destroy](/man/pulumi-destroy)(1)
