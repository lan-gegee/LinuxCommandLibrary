# TAGLINE

管理 Nix 用户环境

# TLDR

**安装软件包**

```nix-env -iA nixpkgs.[package]```

**卸载软件包**

```nix-env -e [package]```

**列出已安装的软件包**

```nix-env -q```

**搜索软件包**

```nix-env -qaP [pattern]```

**升级所有软件包**

```nix-env -u```

**回滚到上一个世代**

```nix-env --rollback```

**列出世代**

```nix-env --list-generations```

# SYNOPSIS

**nix-env** [_options_] _operation_

# PARAMETERS

**-i**, **--install**
> 安装软件包。

**-e**, **--uninstall**
> 移除软件包。

**-u**, **--upgrade**
> 升级软件包。

**-q**, **--query**
> 查询软件包。

**-A**, **--attr**
> 按属性路径进行安装。

**--rollback**
> 回滚到上一个世代。

**-p** _profile_
> 使用指定的 profile。

# DESCRIPTION

**nix-env** 管理 Nix 用户环境。它可以在用户 profile 中安装、升级和移除软件包，并且能够回滚到先前的状态。

每次操作都会创建一个新的世代，同时保留之前的状态。

# PROFILES

```
~/.nix-profile        - Default profile
/nix/var/nix/profiles - System profiles
```

# CAVEATS

建议改用声明式配置（如 home-manager）。世代会占用磁盘空间。使用 -A 按属性路径定位更快。

# HISTORY

nix-env 是 **Nix** 的一部分。Nix 是一款纯函数式的软件包管理器，由 **Eelco Dolstra** 在其 2006 年于乌得勒支大学完成的博士论文中提出。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1), [nix-store](/man/nix-store)(1), [home-manager](/man/home-manager)(1)
