# TAGLINE

管理软件包组

# TLDR

**列出** DNF 组

```dnf group list```

显示**组信息**

```dnf group info [group_name]```

**安装**一个组

```dnf group install [group_name]```

**移除**一个组

```dnf group remove [group_name]```

**升级**一个组

```dnf group upgrade [group_name]```

# SYNOPSIS

**dnf group** _command_ [_group_name_]

# DESCRIPTION

**dnf group** 管理虚拟的软件包集合。组将相关的软件打包在一起，例如"Development Tools"或"Server"。

安装一个组会安装其中所有必选和默认的软件包。

# PARAMETERS

**list**
> 列出可用的组

**info** _group_
> 显示组的详细信息，包括所含软件包

**install** _group_
> 安装组内软件包

**remove** _group_
> 移除组内软件包

**upgrade** _group_
> 升级组内软件包

# CAVEATS

可以通过名称或 ID 引用组。组内的可选软件包默认不安装。移除组后部分软件包可能仍保留在系统中。

# INSTALL

```pacman: sudo pacman -S dnf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnf](/man/dnf)(8), [dnf-install](/man/dnf-install)(8)

# RESOURCES

```[Source code](https://github.com/rpm-software-management/dnf)```

```[Documentation](https://dnf.readthedocs.io/en/latest/command_ref.html)```

<!-- verified: 2026-07-11 -->
