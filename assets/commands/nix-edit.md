# TAGLINE

在编辑器中打开软件包的 Nix 表达式

# TLDR

**编辑软件包定义**

```nix edit nixpkgs#[package]```

**使用指定编辑器编辑**

```EDITOR=vim nix edit nixpkgs#[package]```

# SYNOPSIS

**nix edit** _installable_ [_options_]

# PARAMETERS

_installable_
> 要编辑的软件包（例如 nixpkgs#hello）。

# DESCRIPTION

**nix edit** 在你的编辑器中打开某个软件包的 Nix 表达式。适用于查看或修改软件包定义。使用的编辑器由 $EDITOR 环境变量决定。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-search](/man/nix-search)(1)
