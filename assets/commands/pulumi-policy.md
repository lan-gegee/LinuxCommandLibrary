# TAGLINE

管理基础设施策略包

# TLDR

**列出策略包**

```pulumi policy ls```

**创建新策略包**

```pulumi policy new [template]```

**发布策略包**

```pulumi policy publish [org]```

**启用策略包**

```pulumi policy enable [org/pack] [version]```

**禁用策略包**

```pulumi policy disable [org/pack]```

**移除策略包**

```pulumi policy rm [org/pack] [version]```

**校验策略包配置**

```pulumi policy validate-config [org/pack] [version] --config [policy-config.json]```

# SYNOPSIS

**pulumi** **policy** _command_ [_options_]

# PARAMETERS

**ls**
> 列出策略包。

**new** _template_
> 创建策略包。

**publish** _org_
> 发布策略包。

**enable** _pack_ _version_
> 启用策略包。

**disable** _pack_
> 禁用策略包。

**rm** _pack_ _version_
> 从组织中移除策略包。必须先在所有 Policy Group 中将其禁用。

**group**
> 管理策略组。

**validate-config** _pack_ _version_
> 根据配置模式校验策略包配置。

# DESCRIPTION

**pulumi policy** 管理 Policy as Code（CrossGuard）。策略对基础设施实施合规规则。创建、发布和启用策略包以校验部署。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-preview](/man/pulumi-preview)(1), [pulumi-stack](/man/pulumi-stack)(1)
