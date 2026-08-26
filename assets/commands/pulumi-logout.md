# TAGLINE

移除已存储的 Pulumi 后端凭据

# TLDR

**从当前后端登出**

```pulumi logout```

**从指定后端登出**

```pulumi logout [url]```

**从所有后端登出**

```pulumi logout --all```

# SYNOPSIS

**pulumi** **logout** [_options_] [_url_]

# PARAMETERS

**--all**
> 从所有后端登出。

**--local**
> 从本地后端登出。

# DESCRIPTION

**pulumi logout** 移除 Pulumi 后端的已存储凭据。不影响已部署的资源或状态，仅影响本地身份验证。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-login](/man/pulumi-login)(1)
