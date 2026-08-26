# TAGLINE

直接操作堆栈状态

# TLDR

**从状态中删除资源**

```pulumi state delete [urn]```

**取消资源保护**

```pulumi state unprotect [urn]```

**重命名资源**

```pulumi state rename [urn] [new_name]```

**升级状态 schema**

```pulumi state upgrade```

# SYNOPSIS

**pulumi** **state** _command_ [_options_]

# PARAMETERS

**delete** _urn_
> 从状态中移除资源。

**unprotect** _urn_
> 移除资源的保护标记。

**rename** _urn_ _name_
> 在状态中重命名资源。

**upgrade**
> 升级状态 schema。

**-s**, **--stack** _name_
> 目标堆栈。

**-y**, **--yes**
> 跳过确认。

**--force**
> 强制执行操作。

# DESCRIPTION

**pulumi state** 直接操作堆栈状态。当资源需要手动移除或修改时，可用于"状态手术"。这些是绕过正常资源生命周期的危险操作。

# CAVEATS

直接修改状态可能导致状态与实际基础设施之间出现漂移。请谨慎使用。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-stack](/man/pulumi-stack)(1), [pulumi-import](/man/pulumi-import)(1)
