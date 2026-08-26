# TAGLINE

**pacman --deptest** 的简写形式，检查指定的依赖是否满足要求

# TLDR

此命令是 **pacman --deptest** 的别名

查看原始命令的文档

```tldr pacman deptest```

# SYNOPSIS

**pacman -T** [_options_] [_package(s)_]

# DESCRIPTION

**pacman -T** 是 **pacman --deptest** 的简写形式，用于检查指定的依赖在系统上是否满足。它会返回未安装或不符合版本要求的软件包名称。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-deptest](/man/pacman-deptest)(8)
