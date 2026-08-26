# TAGLINE

在 chroot 中构建 Debian 软件包

# TLDR

**创建基础 tarball**

```pbuilder create```

**构建软件包**

```pbuilder build [package.dsc]```

**更新基础 tarball**

```pbuilder update```

**登录到 chroot**

```pbuilder login```

**针对指定发行版构建**

```pbuilder build --distribution [sid] [package.dsc]```

# SYNOPSIS

**pbuilder** [_command_] [_options_]

# PARAMETERS

**create**
> 创建基础 tarball。

**build** _DSC_
> 从 .dsc 构建软件包。

**update**
> 更新基础 tarball。

**login**
> 进入 chroot shell。

**--distribution** _DIST_
> 目标发行版。

**--basetgz** _FILE_
> 基础 tarball 路径。

# DESCRIPTION

**pbuilder** 在 chroot 中构建 Debian 软件包，提供干净的构建环境。

该工具确保构建可复现。与宿主系统相互隔离。

# CAVEATS

需要 root 权限。仅适用于 Debian/Ubuntu。网络访问可配置。

# HISTORY

pbuilder 是为了在隔离的 chroot 中**干净地构建 Debian 软件包**而创建的。

# INSTALL

```dnf: sudo dnf install pbuilder```

```zypper: sudo zypper install pbuilder```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dpkg-buildpackage](/man/dpkg-buildpackage)(1), [sbuild](/man/sbuild)(1), [cowbuilder](/man/cowbuilder)(1)
