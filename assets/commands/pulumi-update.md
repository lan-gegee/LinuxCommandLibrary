# TAGLINE

部署基础设施变更的别名

# TLDR

**更新堆栈（up 的别名）**

```pulumi update```

**自动确认并更新**

```pulumi update --yes```

**更新指定堆栈**

```pulumi update --stack [stack_name]```

**以 JSON 预览变更**

```pulumi update --json```

# SYNOPSIS

**pulumi** **update** [_options_]

# DESCRIPTION

**pulumi update** 是 **pulumi up** 的别名。通过将期望状态与当前资源进行比较并应用变更，来创建或更新基础设施。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-preview](/man/pulumi-preview)(1), [pulumi-destroy](/man/pulumi-destroy)(1)
