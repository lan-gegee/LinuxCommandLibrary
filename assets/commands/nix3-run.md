# TAGLINE

无需安装即可执行软件包

# TLDR

**运行软件包**

```nix3 run nixpkgs#[hello]```

**从 flake 运行**

```nix3 run [.#default]```

**带参数运行**

```nix3 run nixpkgs#[cowsay] -- "[text]"```

# SYNOPSIS

**nix3** **run** [_options_] _installable_ [-- _args_]

# PARAMETERS

_INSTALLABLE_
> flake 引用。

_ARGS_
> 程序参数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix3 run** 无需安装即可执行软件包。是 nix run 的别名。

该工具临时运行程序。从 store 下载并执行。

# CAVEATS

nix run 的别名。需要网络。属于临时执行。

# HISTORY

nix3 run 是 **新版 Nix CLI** 中用于在不安装到系统的情况下运行软件包的命令。

# SEE ALSO

[nix](/man/nix)(1), [nix-run](/man/nix-run)(1), [nix3-shell](/man/nix3-shell)(1)
