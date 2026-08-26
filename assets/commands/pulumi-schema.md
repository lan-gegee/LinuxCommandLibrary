# TAGLINE

校验 Pulumi 包模式（schema）

# TLDR

**检查 schema 有效性**

```pulumi schema check [schema.json]```

# SYNOPSIS

**pulumi** **schema** _command_ [_options_]

# PARAMETERS

**check** _file_
> 校验 schema 文件。

# DESCRIPTION

**pulumi schema** 管理 Pulumi 包的 schema。schema 为 provider 定义资源类型及其属性。主要由 provider 作者用于校验。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-plugin](/man/pulumi-plugin)(1)
