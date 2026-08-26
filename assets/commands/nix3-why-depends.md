# TAGLINE

追踪依赖关系

# TLDR

**显示依赖路径**

```nix3 why-depends nixpkgs#[package] nixpkgs#[dep]```

**显示所有路径**

```nix3 why-depends --all [pkg] [dep]```

# SYNOPSIS

**nix3** **why-depends** [_options_] _package_ _dependency_

# PARAMETERS

_PACKAGE_
> 要分析的软件包。

_DEPENDENCY_
> 要追踪的依赖。

**--all**
> 显示所有路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix3 why-depends** 追踪依赖关系。显示软件包为何依赖其他软件包。

该工具用于调试软件包闭包（closure）。帮助减少不必要的依赖。

# CAVEATS

nix why-depends 的别名。用于闭包分析。需要求值。

# HISTORY

nix3 why-depends 是 **Nix 3.x** 中用于调试依赖图的一部分。

# SEE ALSO

[nix](/man/nix)(1), [nix-why-depends](/man/nix-why-depends)(1), [nix-store](/man/nix-store)(1)
