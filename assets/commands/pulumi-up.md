# TAGLINE

部署基础设施变更

# TLDR

**部署堆栈**

```pulumi up```

**自动确认并部署**

```pulumi up --yes```

**部署指定堆栈**

```pulumi up -s [stack]```

**带预览地部署**

```pulumi up --diff```

**部署指定目标**

```pulumi up --target [urn]```

# SYNOPSIS

**pulumi** **up** [_options_]

# PARAMETERS

**-s**, **--stack** _name_
> 目标堆栈。

**-y**, **--yes**
> 跳过确认。

**--diff**
> 显示详细差异。

**--target** _urn_
> 更新指定的资源。

**--refresh**
> 在更新前刷新状态。

**-p**, **--parallel** _n_
> 并行度。

**--skip-preview**
> 跳过预览步骤。

**--replace** _urn_
> 强制替换资源。

**-f**, **--skip-preview**
> 跳过预览。

# DESCRIPTION

**pulumi up** 创建或更新基础设施。它将期望状态与当前基础设施进行比较，并应用必要的变更。这是部署 Pulumi 程序的主要命令。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-preview](/man/pulumi-preview)(1), [pulumi-destroy](/man/pulumi-destroy)(1)
