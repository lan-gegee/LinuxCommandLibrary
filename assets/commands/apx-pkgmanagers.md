# TAGLINE

管理 apx 子系统的软件包管理器配置

# TLDR

交互式**创建**新的软件包管理器配置

```apx pkgmanagers new```

用指定的命令**创建**软件包管理器配置

```apx pkgmanagers new --name [name] --install '[install_cmd]' --remove '[remove_cmd]' --update '[update_cmd]'```

**列出**所有可用的软件包管理器配置

```apx pkgmanagers list```

**删除**软件包管理器配置

```apx pkgmanagers rm --name [name]```

显示特定软件包管理器的**信息**

```apx pkgmanagers show [name]```

# SYNOPSIS

**apx pkgmanagers** _command_ [_options_]

# DESCRIPTION

**apx pkgmanagers** 管理 apx 中的软件包管理器配置。这些配置定义了在子系统内如何安装、更新和删除软件包。

用户创建的软件包管理器配置存储在 **~/.local/share/apx/pkgmanagers**。默认提供 apt、dnf 和 pacman 等常见软件包管理器的内置配置。

# SUBCOMMANDS

**new**
> 创建新的软件包管理器配置（交互式或通过标志指定）。

**list**
> 显示所有可用的软件包管理器配置。

**rm**
> 删除软件包管理器配置。

**show**
> 显示特定软件包管理器的详细信息。

# PARAMETERS

**--name** _string_
> 指定软件包管理器名称。

**--install** _string_
> 该软件包管理器的安装命令。

**--remove** _string_
> 该软件包管理器的删除命令。

**--update** _string_
> 该软件包管理器的更新命令。

# INSTALL

```dnf: sudo dnf install apx```

```aur: yay -S apx```

```nix: nix profile install nixpkgs#apx```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apx](/man/apx)(1), [apx-stacks](/man/apx-stacks)(1), [apx-subsystems](/man/apx-subsystems)(1)
