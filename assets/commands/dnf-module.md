# TAGLINE

管理软件包的模块化流

# TLDR

查看**模块化概览**

```dnf module list```

查看**特定软件包**的模块化信息

```dnf module list [package_name]```

**启用**模块流

```sudo dnf module enable [package_name]:[stream]```

**安装**指定的模块版本

```dnf module install [package_name]:[stream]```

# SYNOPSIS

**dnf module** _command_ [_module:stream_]

# DESCRIPTION

**dnf module** 管理软件包模块化，允许多个版本的软件在同一仓库中共存。模块将具有特定用途的软件包组织在一起，流则代表不同的版本。

模块化用于 RHEL 8+ 和 Fedora 中需要在多版本间选择的软件，如 Python、Node.js 和 PHP。

# PARAMETERS

**list**
> 列出可用模块

**enable** _module:stream_
> 启用模块流

**disable** _module_
> 禁用模块

**install** _module:stream_
> 安装模块软件包

**remove** _module_
> 移除模块软件包

**reset** _module_
> 重置模块状态

# CAVEATS

同一模块一次只能激活一个流。启用流并不会安装软件包；安装需使用 install 命令。适用于 RHEL 8+ 和较新的 Fedora。

# INSTALL

```pacman: sudo pacman -S dnf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnf](/man/dnf)(8), [dnf-install](/man/dnf-install)(8)

# RESOURCES

```[Source code](https://github.com/rpm-software-management/dnf)```

```[Documentation](https://dnf.readthedocs.io/en/latest/command_ref.html)```

<!-- verified: 2026-07-11 -->
