# TAGLINE

在受管理的 chroot 环境中运行命令

# TLDR

**列出**可用的 chroot

```schroot --list```

在指定 chroot 中运行**命令**

```schroot --chroot chroot_name command```

在 chroot 中带**选项**运行命令

```schroot --chroot chroot_name -- command command_options```

在**所有** chroot 中运行命令

```schroot --all command```

以指定用户启动**交互式 shell**

```schroot --chroot chroot_name --user user```

**开始**新会话

```schroot --begin-session --chroot chroot_name```

**连接**到现有会话

```schroot --run-session --chroot session_id```

**结束**会话

```schroot --end-session --chroot session_id```

# SYNOPSIS

**schroot** [_options_] [_command_]

# PARAMETERS

**-l**, **--list**
> 列出可用的 chroot。

**-c** _NAME_, **--chroot** _NAME_
> 指定 chroot 环境。

**-u** _USER_, **--user** _USER_
> 以指定用户身份运行。

**-a**, **--all**
> 在所有可用的 chroot 中运行。

**--begin-session**
> 开始新会话。

**--run-session**
> 连接到现有会话。

**--end-session**
> 终止会话。

**-i**, **--info**
> 显示指定 chroot 的详细信息。

**-d** _DIR_, **--directory** _DIR_
> 在运行命令前先切换到 chroot 内的目录。

**-p**, **--preserve-environment**
> 在 chroot 内保留用户的环境变量。

**-q**, **--quiet**
> 减少输出。

**-v**, **--verbose**
> 增加输出。

# DESCRIPTION

**schroot** 在不同的根目录环境中运行命令或启动交互式 shell。相比基础的 chroot，它提供更多特性和自定义能力，包括会话管理和用户映射。

它通过 /etc/schroot/schroot.conf 进行配置，支持多种 chroot 类型和配置。

# CONFIGURATION

**/etc/schroot/schroot.conf**
> 主配置文件，定义可用的 chroot 环境及其类型、位置和访问权限。

**/etc/schroot/chroot.d/**
> 存放各个 chroot 定义文件的目录，支持模块化配置。

**/etc/schroot/setup.d/**
> 存放在会话开始和结束时执行的设置脚本的目录，负责处理挂载点、网络和环境准备。

# CAVEATS

需要正确的 chroot 配置。必须结束会话才能释放资源。

# HISTORY

为 **Debian** 开发，是一款安全性和易用性更佳的改进版 chroot 方案。

# INSTALL

```apt: sudo apt install schroot```

```pacman: sudo pacman -S schroot```

```nix: nix profile install nixpkgs#schroot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chroot](/man/chroot)(8), [debootstrap](/man/debootstrap)(8)
