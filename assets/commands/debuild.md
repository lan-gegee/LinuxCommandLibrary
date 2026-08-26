# TAGLINE

从源码构建 Debian 软件包

# TLDR

**在当前目录构建软件包**

```debuild```

**仅构建二进制软件包**

```debuild -b```

**仅构建源码软件包**

```debuild -S```

**构建时不签名**

```debuild -us -uc```

**并行构建**

```debuild -j[4]```

**构建时不运行 lintian**

```debuild --no-lintian```

# SYNOPSIS

**debuild** [_options_] [_dpkg-buildpackage options_]

# DESCRIPTION

**debuild** 从源码构建 Debian 软件包。它是 dpkg-buildpackage 的包装器，额外提供了自动 lintian 检查和正确的环境设置等功能。

需在包含 debian/control 及其他打包文件的 Debian 源码包目录中运行。

# PARAMETERS

**-b**
> 仅构建二进制软件包

**-S**
> 仅构建源码软件包

**--no-lintian**
> 构建后跳过 lintian 检查

**-us**
> 不对源码软件包签名

**-uc**
> 不对 changes 文件签名

**-j** _n_
> 使用 n 个作业并行构建

# CONFIGURATION

**~/.devscripts**
> debuild 默认选项，包括 lintian 设置和构建行为。

# CAVEATS

必须在配置妥当的 Debian 源码目录中运行。构建依赖必须已安装。属于 devscripts 软件包。

# SEE ALSO

[dpkg-buildpackage](/man/dpkg-buildpackage)(1), [lintian](/man/lintian)(1), [dch](/man/dch)(1)
