# TAGLINE

显示一个软件包为何依赖另一个软件包

# TLDR

**显示依赖路径**

```nix why-depends nixpkgs#[hello] nixpkgs#[glibc]```

**显示所有路径**

```nix why-depends --all nixpkgs#[package] nixpkgs#[dep]```

**直接基于派生文件分析**

```nix why-depends [/nix/store/...package] [/nix/store/...dep]```

# SYNOPSIS

**nix** **why-depends** [_options_] _package_ _dependency_

# PARAMETERS

_PACKAGE_
> 要分析的软件包。

_DEPENDENCY_
> 要查找的依赖。

**--all**
> 显示全部依赖路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix why-depends** 显示一个软件包为什么依赖另一个软件包，并追踪具体的依赖路径。

该工具用于调试闭包（closure），帮助你理解并削减依赖关系。

# CAVEATS

属于 Nix CLI。需要先完成求值。分析对象是闭包。

# HISTORY

nix why-depends 属于**新 Nix CLI**，专门用来排查依赖关系。

# SEE ALSO

[nix](/man/nix)(1), [nix-store](/man/nix-store)(1), [nix-build](/man/nix-build)(1)
