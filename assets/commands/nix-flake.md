# TAGLINE

管理 Nix flakes

# TLDR

**显示 flake 信息**

```nix flake show```

**更新 flake 输入**

```nix flake update```

**锁定 flake 输入**

```nix flake lock```

**初始化新的 flake**

```nix flake init```

**检查 flake**

```nix flake check```

**显示 flake 元数据**

```nix flake metadata```

**克隆 flake**

```nix flake clone [github:owner/repo]```

# SYNOPSIS

**nix** **flake** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> Flake 子命令。

**show**
> 显示 flake 输出。

**update**
> 更新输入。

**lock**
> 锁定输入。

**init**
> 初始化 flake。

**check**
> 校验 flake。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix flake** 用于管理 Nix flakes。Flakes 提供可复现、封闭式（hermetic）的软件包定义。

该工具处理 flake.nix 文件，管理其中的输入与输出。

# CAVEATS

需要启用实验特性。必须有 flake.nix 文件。会生成对应的锁文件。

# HISTORY

Nix flakes 随 **Nix 2.4** 推出，用于提供可复现、可组合的软件包定义。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-build](/man/nix-build)(1), [nix-develop](/man/nix-develop)(1)
