# TAGLINE

Nix 软件包管理器 CLI

# TLDR

**搜索软件包**

```nix search nixpkgs [package]```

**运行软件包**

```nix run nixpkgs#[package]```

**构建派生**

```nix build```

**进入开发 Shell**

```nix develop```

**显示 flake 信息**

```nix flake show```

**更新 flake**

```nix flake update```

**求值表达式**

```nix eval --expr "[1 + 1]"```

**回收未使用的 store 路径**

```nix store gc```

**把软件包安装到 profile**

```nix profile install nixpkgs#[package]```

**启动交互式 Nix REPL**

```nix repl```

**启动包含某软件包的临时 Shell**

```nix shell nixpkgs#[package]```

# SYNOPSIS

**nix** [_command_] [_options_]

# PARAMETERS

**search** _flakeref_ _query_
> 在 flake 中搜索软件包。

**run** _installable_
> 构建并运行软件包。

**build** [_installable_]
> 构建派生或获取 store 路径。

**develop** [_installable_]
> 基于 flake 进入开发 Shell。

**shell** _installable..._
> 运行一个可以使用指定软件包的 Shell。

**flake** _subcommand_
> 管理 Nix flakes（show、update、init、check、lock）。

**profile** _subcommand_
> 管理 Nix profiles（install、remove、list、upgrade）。

**store** _subcommand_
> 管理 Nix store（gc、verify、repair、optimise）。

**repl**
> 启动交互式的 Nix 表达式求值器。

**eval** _installable_
> 对 Nix 表达式求值。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**nix** 是统一的 Nix 软件包管理器 CLI，提供可复现的软件包管理、构建以及开发环境。它是 nix-env、nix-build 等旧式命令的现代替代品。

该工具使用 **flakes** 定义可复现的项目，并配合锁文件工作。Flakes 规范了 Nix 项目声明依赖与输出的方式。

**nix develop** 创建带项目依赖的开发 Shell。**nix run** 直接构建并运行软件包。**nix shell** 提供一个可以使用指定软件包的临时 Shell。

Nix store 让所有软件包彼此隔离存放，从而支持原子化的升级与回滚。用 **nix store gc** 做垃圾回收可以清除无用的路径。

# CAVEATS

学习曲线陡峭。Nix 表达式语言是函数式的且相当独特。许多新式 nix 命令仍被标记为实验性，需要启用实验特性。需要安装 Nix 守护进程。

# HISTORY

Nix 由 **Eelco Dolstra** 作为其在乌得勒支大学的博士论文项目创建，于 **2003 年**首次发布。统一的 nix CLI 随 Nix 2.0 引入。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-shell](/man/nix-shell)(1), [nix-env](/man/nix-env)(1), [nix-build](/man/nix-build)(1), [nix-store](/man/nix-store)(1), [nixos-rebuild](/man/nixos-rebuild)(1), [home-manager](/man/home-manager)(1)
