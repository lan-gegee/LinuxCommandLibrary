# TAGLINE

显示 flake 输出

# TLDR

**显示 flake 输出**

```nix flake show```

**显示远程 flake**

```nix flake show [github:NixOS/nixpkgs]```

**以 JSON 格式显示**

```nix flake show --json```

**显示所有系统平台**

```nix flake show --all-systems```

# SYNOPSIS

**nix** **flake** **show** [_options_] [_flake-url_]

# PARAMETERS

_FLAKE-URL_
> Flake 引用。

**--json**
> 以 JSON 格式输出。

**--all-systems**
> 显示所有系统平台上的输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix flake show** 显示 flake 的输出内容，包括软件包、应用（apps）和 devShells。

该命令会列出可用的属性，以树状视图呈现 flake 的结构。

# CAVEATS

必须先启用 flakes。执行时会对 flake 求值。访问远程 flake 需要网络连接。

# HISTORY

nix flake show 是 **Nix flakes** 的一部分，用于检查 flake 的输出结构。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-flake](/man/nix-flake)(1), [nix-flake-info](/man/nix-flake-info)(1), [nix](/man/nix)(1)
