# TAGLINE

管理 Nix flake 注册表

# TLDR

**列出注册表**

```nix registry list```

**将 flake 固定到特定版本**

```nix registry pin [nixpkgs]```

**添加注册表条目**

```nix registry add [myflake] [github:owner/repo]```

**移除注册表条目**

```nix registry remove [myflake]```

# SYNOPSIS

**nix registry** _command_ [_options_]

# PARAMETERS

**list**
> 列出注册表条目。

**add** _name_ _flake_
> 添加 flake 别名。

**remove** _name_
> 移除别名。

**pin** _name_
> 将 flake 固定为当前版本。

# DESCRIPTION

**nix registry** 管理 Nix flake 注册表。注册表为 flake URL 提供简短的别名，并支持将 flake 固定到特定版本以保证可复现性。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-flake](/man/nix-flake)(1)
