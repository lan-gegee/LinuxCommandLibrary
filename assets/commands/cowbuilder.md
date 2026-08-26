# TAGLINE

写时复制的 Debian 软件包构建器

# TLDR

**创建新的 cowbuilder 环境**

```sudo cowbuilder --create --distribution [bookworm]```

**更新 cowbuilder 环境**

```sudo cowbuilder --update```

**构建软件包**

```sudo cowbuilder --build [package.dsc]```

**登录 cowbuilder 环境**

```sudo cowbuilder --login```

**为特定架构构建**

```sudo cowbuilder --build --architecture [i386] [package.dsc]```

**使用指定的 base.cow 位置**

```sudo cowbuilder --basepath [/var/cache/pbuilder/base-bookworm.cow] --build [package.dsc]```

# SYNOPSIS

**cowbuilder** **--create** | **--update** | **--build** | **--login** [_options_]

# PARAMETERS

**--create**
> 创建新的 base.cow 环境。

**--update**
> 更新 cowbuilder 环境中的软件包。

**--build** _dsc_
> 从 .dsc 文件构建软件包。

**--login**
> 在 chroot 环境中启动一个 shell。

**--distribution** _dist_
> Debian/Ubuntu 发行版（bookworm、jammy 等）。

**--architecture** _arch_
> 目标架构（amd64、i386、arm64）。

**--basepath** _path_
> base.cow 目录的路径。

**--buildresult** _path_
> 存放构建结果的目录。

**--mirror** _url_
> 软件包镜像 URL。

**--save-after-login**
> 保存在登录会话期间所做的更改。

# DESCRIPTION

**cowbuilder** 是 pbuilder 的封装，利用写时复制（COW）机制加快 Debian 软件包的构建。它不为每次构建都创建新的 chroot tarball，而是用硬链接创建工作副本，显著缩短准备时间。

该工具为 Debian 软件包创建干净、可重现的构建环境。每次构建都从原始的基础系统开始，确保软件包能够正确构建，不会隐藏对开发者系统环境的依赖。

cowbuilder 常用于在上传到 Debian 归档前验证软件包构建、在不同发行版间测试软件包，以及用于 Debian 打包的 CI/CD 流水线。

# CAVEATS

chroot 操作需要 root 权限。base.cow 目录必须位于支持硬链接的文件系统上（不能跨文件系统）。更新后的首次构建可能较慢，因为需要预热缓存。如果 base.cow 与构建目录不在同一文件系统上，COW 的优势将不复存在。

# HISTORY

cowbuilder 作为 **pbuilder**（Personal Builder）的增强版而诞生，采用了 COW 文件系统技术。Pbuilder 本身由 **Junichi Uekawa** 在 **2000 年代**初创建，用于在干净环境中构建 Debian 软件包。Cowbuilder 解决了 pbuilder 的主要性能瓶颈：每次构建都要解压基础 tarball。

# INSTALL

```apt: sudo apt install cowbuilder```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pbuilder](/man/pbuilder)(8), [sbuild](/man/sbuild)(1), [debuild](/man/debuild)(1), [dpkg-buildpackage](/man/dpkg-buildpackage)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/cowdancer)```

<!-- verified: 2026-06-23 -->
