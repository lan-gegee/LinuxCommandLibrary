# TAGLINE

管理 Pulumi Cloud 组织

# TLDR

**设置默认组织**

```pulumi org set-default [org]```

**获取默认组织**

```pulumi org get-default```

**列出组织**

```pulumi org search```

# SYNOPSIS

**pulumi** **org** _command_ [_options_]

# PARAMETERS

**set-default** _org_
> 设置默认组织。

**get-default**
> 显示默认组织。

**search**
> 列出可用的组织。

# DESCRIPTION

**pulumi org** 管理 Pulumi Cloud 组织。组织用于对用户、堆栈和设置进行分组。可为新堆栈和操作设置默认组织。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-whoami](/man/pulumi-whoami)(1)
