# TAGLINE

创建临时的开发环境

# TLDR

**携带软件包进入 Shell**

```nix-shell -p [hello]```

**从 default.nix 进入 Shell**

```nix-shell```

**从指定文件进入 Shell**

```nix-shell [shell.nix]```

**在 Shell 中运行命令**

```nix-shell -p [jq] --run "[jq --version]"```

**纯 Shell 环境**

```nix-shell --pure -p [python3]```

**同时加入多个软件包**

```nix-shell -p [python3] [nodejs] [git]```

# SYNOPSIS

**nix-shell** [_options_] [_path_]

# PARAMETERS

_PATH_
> Nix 表达式文件。

**-p** _PACKAGES_
> 要纳入的软件包。

**--run** _CMD_
> 要执行的命令。

**--pure**
> 清空环境。

**-A** _ATTR_
> 使用指定的属性。

**-I** _PATH_
> 向 Nix 表达式搜索路径添加路径（例如 `-I nixpkgs=/path/to/nixpkgs`）。

**--command** _CMD_
> 运行命令后仍停留在 Shell 中（与 `--run` 不同，后者执行完就退出）。

**--keep** _VAR_
> 使用 `--pure` 时保留指定的环境变量。

**--packages**
> `-p` 的长格式写法。

**-i** _INTERPRETER_
> 用作 shebang 解释器（参见 `#!nix-shell` 脚本）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix-shell** 创建临时开发环境，让你无需安装就能使用软件包。

该工具会搭建好带有依赖的 Shell。退出时不留痕迹，不会改动系统。

# CAVEATS

属于旧版命令。可以考虑改用 nix develop。环境只在单次调用期间有效。

# HISTORY

nix-shell 是一条核心的 **Nix** 命令，用于创建临时开发 Shell。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-develop](/man/nix-develop)(1), [nix](/man/nix)(1), [direnv](/man/direnv)(1)
