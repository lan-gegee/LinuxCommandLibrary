# TAGLINE

取消正在进行的 Pulumi 堆栈更新

# TLDR

**取消当前更新**

```pulumi cancel```

**在指定堆栈中取消**

```pulumi cancel -s [stack]```

**强制取消**

```pulumi cancel --yes```

# SYNOPSIS

**pulumi** **cancel** [_options_]

# PARAMETERS

**-s**, **--stack** _name_
> 目标堆栈。

**-y**, **--yes**
> 跳过确认。

# DESCRIPTION

**pulumi cancel** 取消正在进行的堆栈更新。当更新卡住或需要中止时很有用。取消后资源可能处于未知状态。

# CAVEATS

取消更新可能使资源处于不一致的状态，需要手动干预。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1)
