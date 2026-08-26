# TAGLINE

进入开发 Shell

# TLDR

**进入开发 Shell**

```nix3 develop```

**从 flake 开始开发**

```nix3 develop [.#devShell]```

**运行命令**

```nix3 develop --command [make]```

# SYNOPSIS

**nix3** **develop** [_options_] [_installable_]

# PARAMETERS

_INSTALLABLE_
> flake 引用。

**--command** _CMD_
> 在 Shell 中运行命令。

**--impure**
> 允许不纯求值。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix3 develop** 进入开发 Shell。是 nix develop 的别名。

该工具提供构建依赖。基于 flake 的 devShells 输出。

# CAVEATS

nix develop 的别名。需要启用 Flakes。用于环境搭建。

# HISTORY

nix3 develop 是 **新版 Nix CLI** 中用于可复现开发环境的命令。

# SEE ALSO

[nix](/man/nix)(1), [nix-develop](/man/nix-develop)(1), [nix-shell](/man/nix-shell)(1)
