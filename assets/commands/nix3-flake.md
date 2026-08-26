# TAGLINE

管理 Nix flakes

# TLDR

**显示 flake 输出**

```nix3 flake show```

**更新输入**

```nix3 flake update```

**初始化 flake**

```nix3 flake init```

**检查 flake**

```nix3 flake check```

# SYNOPSIS

**nix3** **flake** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> flake 子命令。

**show**
> 显示输出。

**update**
> 更新输入。

**init**
> 创建新 flake。

**check**
> 校验 flake。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix3 flake** 管理 Nix flakes。是 nix flake 各命令的别名。

该工具处理 flake.nix 文件。管理可复现的软件包定义。

# CAVEATS

nix flake 的别名。实验特性。锁文件管理。

# HISTORY

nix3 flake 是 **Nix 3.x** 封闭构建（hermetic builds）flake 系统的一部分。

# SEE ALSO

[nix](/man/nix)(1), [nix-flake](/man/nix-flake)(1), [nix3-build](/man/nix3-build)(1)
