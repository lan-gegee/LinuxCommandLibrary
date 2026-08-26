# TAGLINE

基于某个 Nix 表达式启动交互式 Shell

# TLDR

来自 shell.nix 的**开发 Shell**

```nix-shell [shell.nix]```

不混入任何宿主环境的**纯 Shell**

```nix-shell --pure```

包含指定软件包的**临时 Shell**

```nix-shell -p [python3] [git]```

在 Shell 环境中**运行命令**后退出

```nix-shell --run "[make check]"```

从 Nix 表达式中**选择属性**

```nix-shell -A [dev]```

在纯 Shell 中**保留环境变量**

```nix-shell --pure --keep [HOME]```

# SYNOPSIS

**nix-shell** [_options_] [_path_]

# PARAMETERS

_PATH_
> Nix 表达式文件（默认：shell.nix 或 default.nix）。

**-p**, **--packages** _packages..._
> 使用来自 Nixpkgs 的指定软件包搭建环境。

**--pure**
> 启动 Shell 前清空环境，只保留 HOME、USER 和 DISPLAY。

**--run** _cmd_
> 在非交互式 Shell 中运行命令后退出。

**--command** _cmd_
> 在交互式 Shell 中运行命令后退出。

**-A**, **--attr** _attrPath_
> 从 Nix 表达式中选择一个属性。

**--keep** _name_
> 使用 --pure 时保留指定的环境变量。

**--exclude** _regexp_
> 跳过构建 store 路径匹配该正则表达式的依赖。

**-i** _interpreter_
> 为 nix-shell shebang 脚本指定解释器。

**-I** _path_
> 向 Nix 表达式搜索路径添加一个路径。

**-v**
> 详细输出。

# DESCRIPTION

**nix-shell** 会启动一个交互式 Shell，其中的环境根据某个 Nix 表达式来搭建。它会提供指定派生的全部构建依赖但不实际构建该派生，因此非常适合用作开发环境。

配合 **--packages/-p** 使用时，它会创建装有特定软件包的临时环境。配合 **--pure** 使用时，宿主环境会被清空，以尽量贴近真实的 Nix 构建环境。

nix-shell 还能借助 shebang 行（`#!/usr/bin/env nix-shell`）作为脚本解释器使用，从而编写声明了依赖、可复现执行的脚本。

# CAVEATS

不加 **--pure** 时，宿主环境会泄漏进 Shell，可能导致构建在本地成功、却在干净的 Nix 构建中失败。**--packages** 标志使用的是 Nixpkgs 的属性名，而不是软件包名。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-build](/man/nix-build)(1), [nix-shell](/man/nix-shell)(1), [nix-develop](/man/nix-develop)(1), [nix-store](/man/nix-store)(1)
