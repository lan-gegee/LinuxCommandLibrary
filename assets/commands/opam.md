# TAGLINE

OCaml 软件包管理器

# TLDR

**初始化 opam**

```opam init```

**安装软件包**

```opam install [package]```

**搜索软件包**

```opam search [query]```

**更新软件包列表**

```opam update```

**升级软件包**

```opam upgrade```

**创建 switch**

```opam switch create [name] [compiler_version]```

# SYNOPSIS

**opam** [_command_] [_options_]

# PARAMETERS

**init**
> 初始化 opam。

**install** _PACKAGE_
> 安装软件包。

**search** _QUERY_
> 搜索软件包。

**update**
> 更新软件仓库。

**upgrade**
> 升级软件包。

**switch** _COMMAND_
> 管理编译器 switch。

**--help**
> 显示帮助信息。

# DESCRIPTION

**opam** 是 OCaml 软件包管理器，用于管理 OCaml 库和编译器。

该工具负责软件包安装和依赖解析。支持 switch。

# CAVEATS

使用前需要初始化。switch 用于隔离环境。需要进行 Shell 配置。

# HISTORY

opam 为 **OCaml 软件包管理**而创建，支持编译器版本切换。

# INSTALL

```apt: sudo apt install opam```

```dnf: sudo dnf install opam```

```pacman: sudo pacman -S opam```

```apk: sudo apk add opam```

```zypper: sudo zypper install opam```

```brew: brew install opam```

```nix: nix profile install nixpkgs#opam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ocaml](/man/ocaml)(1), [dune](/man/dune)(1)
