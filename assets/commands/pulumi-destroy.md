# TAGLINE

删除 Pulumi 堆栈中的所有资源

# TLDR

**销毁所有资源**

```pulumi destroy```

**自动确认并销毁**

```pulumi destroy --yes```

**销毁指定堆栈**

```pulumi destroy -s [stack]```

**预览销毁操作**

```pulumi destroy --preview-only```

**销毁指定目标**

```pulumi destroy --target [urn]```

# SYNOPSIS

**pulumi** **destroy** [_options_]

# PARAMETERS

**-s**, **--stack** _name_
> 目标堆栈。

**-y**, **--yes**
> 跳过确认。

**--preview-only**
> 仅预览而不执行。

**--target** _urn_
> 销毁指定的资源。

**-p**, **--parallel** _n_
> 并行度。

**--refresh**
> 在销毁前刷新状态。

# DESCRIPTION

**pulumi destroy** 删除堆栈中的所有资源。它会移除由 Pulumi 管理的云基础设施。在生产环境中执行销毁前务必先预览变更。

# CAVEATS

此操作会永久销毁云资源。在生产环境中请先使用 --preview-only。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-preview](/man/pulumi-preview)(1)
