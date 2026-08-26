# TAGLINE

运行 Nix 软件包中的程序

# TLDR

**运行 nixpkgs 中的软件包**

```nix run nixpkgs#[hello]```

**从 flake 运行**

```nix run [.#default]```

**带参数运行**

```nix run nixpkgs#[cowsay] -- "[Hello]"```

**从 GitHub 运行**

```nix run [github:owner/repo]```

**运行指定的应用**

```nix run [.#apps.x86_64-linux.default]```

# SYNOPSIS

**nix** **run** [_options_] _installable_ [-- _args_]

# PARAMETERS

_INSTALLABLE_
> 要运行的 flake 引用。

_ARGS_
> 要传给程序的参数。

**--impure**
> 允许非纯求值。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix run** 直接运行 Nix 软件包中的程序，无需安装。

该工具会获取并运行软件包，只是临时执行，不会污染系统。

# CAVEATS

需要启用 flakes。首次运行时需要下载软件包。依赖网络连接。

# HISTORY

nix run 是**新 Nix CLI** 的一部分，可在不安装的前提下运行软件包。

# INSTALL

```nix: nix profile install nixpkgs#nix-run```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1), [nix-build](/man/nix-build)(1)
