# TAGLINE

显示 flake 元数据

# TLDR

**显示 flake 信息**

```nix flake info```

**显示远程 flake 的信息**

```nix flake info [github:NixOS/nixpkgs]```

**以 JSON 格式显示信息**

```nix flake info --json```

# SYNOPSIS

**nix** **flake** **info** [_options_] [_flake-url_]

# PARAMETERS

_FLAKE-URL_
> Flake 引用 URL。

**--json**
> 以 JSON 格式输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix flake info** 显示 flake 元数据，包括其输入和描述。

该命令会展示 flake URL，并列出锁定的输入项及对应的修订版本。

# CAVEATS

在较新版本中已更名为 metadata。必须启用 flakes。访问远程 flake 需要网络。

# HISTORY

nix flake info 属于早期的 **flakes** 实现，现已被 metadata 子命令取代。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-flake](/man/nix-flake)(1), [nix-flake-show](/man/nix-flake-show)(1), [nix](/man/nix)(1)
