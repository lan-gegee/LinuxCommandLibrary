# TAGLINE

Arch Linux 软件包维护者工具集

# TLDR

向 Arch Linux GitLab 实例进行**身份验证**

```pkgctl auth login```

在干净的 chroot 中**构建**软件包

```pkgctl build```

发布后**更新**二进制仓库数据库

```pkgctl db update```

**比较**当前软件包与仓库版本

```pkgctl diff```

将软件包**发布**到二进制仓库

```pkgctl release```

从 GitLab **克隆**打包仓库

```pkgctl repo clone [pkgbase]```

显示**版本**信息

```pkgctl version```

# SYNOPSIS

**pkgctl** [_command_] [_options_]

# COMMANDS

**auth**
> 向 GitLab 和其他服务进行身份验证

**build**
> 在干净的 chroot 中构建软件包

**db update**
> 更新二进制仓库数据库

**diff**
> 比较软件包文件

**release**
> 发布构建产物

**repo**
> 管理 Git 打包仓库

**version**
> 显示版本信息

# DESCRIPTION

**pkgctl** 是 Arch Linux 软件包维护者工具的统一命令行界面。它将各种 devtools 命令整合到一个入口，简化了构建和发布 Arch 软件包的工作流程。

该工具与 Arch 基础设施集成，包括 GitLab、二进制仓库和 Arch 构建系统（ABS）。

# CAVEATS

面向 Arch 软件包维护者。需要 devtools 软件包。某些操作需要身份验证。需要了解 PKGBUILD 文件。

# HISTORY

**pkgctl** 作为 Arch Linux devtools 现代化的一部分推出。它提供统一接口，取代了 archbuild、archrelease 等分散的工具，改善了软件包维护者的体验。

# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8), [devtools](/man/devtools)(7), [asp](/man/asp)(1), [pkgctl-build](/man/pkgctl-build)(1)
