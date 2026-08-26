# TAGLINE

在干净的 chroot 环境中构建 Debian 软件包

# TLDR

**构建软件包**

```sbuild [package.dsc]```

**针对特定发行版构建**

```sbuild -d [unstable] [package.dsc]```

**针对特定架构构建**

```sbuild --arch=[arm64] [package.dsc]```

**使用并行任务构建**

```sbuild -j[4] [package.dsc]```

**构建完成后运行 lintian**

```sbuild --run-lintian [package.dsc]```

**创建 chroot 环境**

```sbuild-createchroot [unstable] [/srv/chroot/unstable] [http://deb.debian.org/debian]```

# SYNOPSIS

**sbuild** [_-d dist_] [_--arch arch_] [_options_] _dsc-file_

# PARAMETERS

**-d**, **--dist=**_DIST_
> 目标发行版（例如 unstable、bookworm）。

**--arch=**_ARCH_
> 构建架构（例如 amd64、arm64）。

**-c**, **--chroot=**_CHROOT_
> 使用指定的 chroot 环境。

**-j**, **--jobs=**_N_
> 并行构建任务数。

**-s**, **--source**
> 除二进制包外同时构建源码包。

**-A**, **--arch-all**
> 同时构建架构无关的软件包。

**--build-dep-resolver=**_RESOLVER_
> 选择依赖解析器：apt（默认）、aptitude、aspcud。

**--extra-repository=**_SPEC_
> 为构建添加额外的 apt 仓库。

**--run-lintian**
> 构建成功后运行 lintian。

**--no-clean-source**
> 构建前跳过 debian/rules clean。

**--profiles=**_PROFILE[,...]_
> 指定构建 profile。

**-p**, **--purge=**_MODE_
> 清理构建目录：always、never 或 successful。

**-v**, **--verbose**
> 详细输出。

**-n**, **--nolog**
> 仅将输出打印到标准输出，不写日志文件。

# DESCRIPTION

**sbuild** 在由 schroot 管理的干净 chroot 环境中构建 Debian 软件包，每次构建都从一个原始的基础系统开始，从而确保结果可重现。构建依赖每次都会全新安装，避免了之前构建或宿主系统的污染。

该工具支持跨架构构建，可以在 x86 宿主机上为 arm64、armhf 等不同平台编译软件包。它与 Debian buildd 基础设施兼容，这意味着用 sbuild 构建的软件包与官方 Debian 归档构建器使用的构建流程完全一致。

# CAVEATS

需要先通过 sbuild-createchroot 配置 chroot。需要 root 权限或相应的组成员身份（sbuild 组）。主要用于 Debian/Ubuntu 打包。

# HISTORY

**sbuild** 最初为 **Debian** 的 buildd 网络而开发。它提供干净且可重现的软件包构建。

# INSTALL

```brew: brew install sbuild```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dpkg-buildpackage](/man/dpkg-buildpackage)(1), [pbuilder](/man/pbuilder)(1), [schroot](/man/schroot)(1), [debootstrap](/man/debootstrap)(1), [lintian](/man/lintian)(1)
