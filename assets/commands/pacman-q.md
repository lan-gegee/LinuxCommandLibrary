# TAGLINE

**pacman --query** 的简写形式，查询本地软件包数据库

# TLDR

此命令是 **pacman --query** 的别名

查看原始命令的文档

```tldr pacman query```

# SYNOPSIS

**pacman -Q** [_options_] [_package(s)_]

# DESCRIPTION

**pacman -Q** 是 **pacman --query** 的简写形式，用于查询本地软件包数据库。它可以列出已安装的软件包、查看软件包信息以及查询软件包拥有的文件。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-query](/man/pacman-query)(8)
