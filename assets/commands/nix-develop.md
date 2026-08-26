# TAGLINE

进入开发 Shell

# TLDR

**进入开发 Shell**

```nix develop```

**基于 flake 进行开发**

```nix develop [path/to/flake]```

**在 Shell 中运行命令**

```nix develop --command [bash -c "make"]```

**进入指定输出的开发环境**

```nix develop [.#devShells.default]```

**以非纯模式开发**

```nix develop --impure```

**先构建再进入**

```nix develop --build```

# SYNOPSIS

**nix** **develop** [_options_] [_installable_]

# PARAMETERS

_INSTALLABLE_
> Flake 引用或路径。

**--command** _CMD_
> 在 Shell 中运行命令。

**--impure**
> 允许非纯（impure）求值。

**--build**
> 进入前先执行构建。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix develop** 进入一个开发 Shell，并提供构建所需的依赖。

该工具负责设置环境变量，环境内容基于 flake 的 devShell 或 shell.nix。

# CAVEATS

需要启用 flakes，或存在 shell.nix 兼容配置。环境之间相互隔离。

# HISTORY

nix develop 属于 **Nix 2.4+** 的 flakes 功能，用于提供可复现的开发环境。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1), [direnv](/man/direnv)(1)
