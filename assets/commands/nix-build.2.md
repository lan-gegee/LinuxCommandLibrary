# TAGLINE

构建 Nix 派生（derivation）

# TLDR

**构建 default.nix**

```nix-build```

**构建指定属性**

```nix-build -A [package]```

**从 nixpkgs 构建**

```nix-build '<nixpkgs>' -A [hello]```

**构建时不生成结果链接**

```nix-build --no-out-link```

# SYNOPSIS

**nix-build** [_options_] [_path_]

# PARAMETERS

_PATH_
> Nix 表达式路径。

**-A** _ATTR_
> 要构建的属性。

**--no-out-link**
> 不创建结果符号链接。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix-build** 用于构建 Nix 派生（derivation）。本文件是该命令的另一份文档版本。

该工具对 Nix 表达式求值，产出 store 路径和结果链接。

# CAVEATS

属于 Nix 工具集。属旧版接口。使用 flake 时请改用 nix build。

# HISTORY

nix-build 是一条核心 **Nix** 命令，用于从表达式构建派生。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-build](/man/nix-build)(1), [nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1)
