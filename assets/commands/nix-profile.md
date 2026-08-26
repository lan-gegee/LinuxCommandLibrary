# TAGLINE

管理 Nix 中的用户软件包 profile

# TLDR

**列出已安装的软件包**

```nix profile list```

**安装软件包**

```nix profile install [nixpkgs#hello]```

**移除软件包**

```nix profile remove [hello]```

**升级软件包**

```nix profile upgrade '.*'```

**回滚 profile**

```nix profile rollback```

# SYNOPSIS

**nix profile** _command_ [_options_]

# PARAMETERS

**list**
> 列出已安装的软件包。

**install** _package_
> 安装软件包。

**remove** _package_
> 移除软件包。

**upgrade** _regex_
> 升级匹配的软件包。

**rollback**
> 回滚到上一个世代。

**history**
> 显示 profile 历史。

**diff-closures**
> 显示各世代之间的差异。

# DESCRIPTION

**nix profile** 管理 Nix 中用户的软件包 profile，是 nix-env 的现代化替代品。它以原子操作的方式安装、移除和升级软件包，并支持回滚。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-env](/man/nix-env)(1)
