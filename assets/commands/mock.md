# TAGLINE

在干净的 chroot 环境中构建 RPM

# TLDR

**在 chroot 中构建软件包**

```mock -r [fedora-39-x86_64] [package.src.rpm]```

**初始化 chroot**

```mock -r [fedora-39-x86_64] --init```

**清理 chroot**

```mock -r [fedora-39-x86_64] --clean```

**进入 chroot shell**

```mock -r [fedora-39-x86_64] --shell```

**从 spec 构建**

```mock -r [fedora-39-x86_64] --spec [package.spec] --sources [sources/]```

**重新构建 SRPM**

```mock -r [fedora-39-x86_64] --rebuild [package.src.rpm]```

# SYNOPSIS

**mock** [_options_] _srpm_

# PARAMETERS

_SRPM_
> 要构建的源码 RPM。

**-r** _CONFIG_
> chroot 配置。

**--init**
> 初始化 chroot。

**--clean**
> 清理 chroot。

**--shell**
> 进入 chroot shell。

**--rebuild**
> 重新构建 SRPM。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mock** 在干净的 chroot 环境中构建 RPM。它将构建过程与宿主系统隔离开来。

该工具可创建可复现的构建，用于 Fedora/RHEL 的软件包构建。

# CAVEATS

面向 Fedora/RHEL。需要加入 mock 组。需要 chroot 配置文件。

# HISTORY

Mock 由 **Fedora** 项目创建，用于在隔离环境中构建 RPM 软件包。

# INSTALL

```dnf: sudo dnf install mock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpmbuild](/man/rpmbuild)(8), [dnf](/man/dnf)(8), [koji](/man/koji)(1)
