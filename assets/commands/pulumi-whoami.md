# TAGLINE

显示当前 Pulumi 用户和后端

# TLDR

**显示当前用户**

```pulumi whoami```

**显示详细信息**

```pulumi whoami -v```

**以 JSON 格式显示**

```pulumi whoami --json```

# SYNOPSIS

**pulumi** **whoami** [_options_]

# PARAMETERS

**-v**, **--verbose**
> 显示详细信息。

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**pulumi whoami** 显示当前登录的用户和后端。展示用户名、组织和后端 URL。可用于验证身份验证状态。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-login](/man/pulumi-login)(1), [pulumi-logout](/man/pulumi-logout)(1)
