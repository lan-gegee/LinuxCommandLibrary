# TAGLINE

支持 A/B 切换的不可变根分区管理器

# TLDR

向本地镜像**添加**软件包

```sudo abroot pkg add [package]```

从本地镜像**移除**软件包

```sudo abroot pkg remove [package]```

**列出**本地镜像中的软件包

```sudo abroot pkg list```

在本地镜像中**应用**更改

```sudo abroot pkg apply```

将系统**回滚**到之前的状态

```sudo abroot rollback```

编辑或查看**内核参数**

```sudo abroot kargs [edit|show]```

显示**状态**

```sudo abroot status```

# SYNOPSIS

**abroot** [_pkg_] [_rollback_] [_kargs_] [_status_] [_command_]

# DESCRIPTION

**abroot** 是一个通过在两个根分区状态（A⟺B）之间进行事务切换来提供完全不可变性与原子性的实用工具。更新通过 OCI 镜像执行，以确保系统始终处于一致状态。

这种方式允许安全的系统更新：如果出现问题，更改可以回滚。系统从一个根分区启动，而更改则应用于另一个分区。

# PARAMETERS

**pkg add PACKAGE**
> 向本地镜像添加软件包；需要执行 apply 才能生效

**pkg remove PACKAGE**
> 从本地镜像移除软件包；需要执行 apply 才能生效

**pkg list**
> 列出本地镜像中的软件包

**pkg apply**
> 应用待处理的软件包更改；需要重启系统

**upgrade**
> 将启动分区更新为最新的 OCI 镜像

**rollback**
> 回滚到之前的系统状态

**kargs edit**
> 编辑内核参数

**kargs show**
> 显示当前的内核参数

**status**
> 显示当前系统状态

**-h, --help**
> 显示帮助信息

# CAVEATS

软件包更改需要先运行 **pkg apply**，再重启系统后才能生效。

# HISTORY

为 **Vanilla OS** 开发，这是一个专注于通过 A/B 分区方案提供不可变、原子化桌面体验的 Linux 发行版。

# INSTALL

```aur: yay -S abroot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(8), [dnf](/man/dnf)(8), [ostree](/man/ostree)(1)

# RESOURCES

```[Source code](https://github.com/Vanilla-OS/ABRoot)```

```[Homepage](https://vanillaos.org)```

<!-- verified: 2026-06-10 -->
