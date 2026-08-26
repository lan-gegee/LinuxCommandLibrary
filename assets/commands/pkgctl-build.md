# TAGLINE

在干净的 chroot 中构建 Arch 软件包

# TLDR

自动选择合适的构建脚本，在干净的 chroot 中**构建软件包**

```pkgctl build```

使用**指定选项**手动构建软件包

```pkgctl build --arch [architecture] --repo [repository] --clean```

# SYNOPSIS

**pkgctl build** [_options_]

# PARAMETERS

**--arch _arch_**
> 要构建的目标架构

**--repo _name_**
> 目标仓库

**--clean**
> 构建前清理 chroot

**--staging**
> 针对 staging 仓库构建

**--testing**
> 针对 testing 仓库构建

**--worker _n_**
> 并行工作进程数量

**--inspect _when_**
> 检查 chroot：always、never 或 failure

# DESCRIPTION

**pkgctl build** 在干净的 chroot 环境中构建 Arch Linux 软件包，确保构建可重现且相互隔离。它是 Arch Linux 打包者为仓库构建软件包的官方工具。

该命令会从 PKGBUILD 和仓库设置中自动检测合适的构建配置。它使用 **devtools** 基础设施创建隔离的构建环境。

在干净的 chroot 中构建可以避免污染宿主系统，并确保软件包只依赖声明的依赖项。

# CAVEATS

需要 devtools 软件包和正确的 chroot 设置。首次构建会下载基础系统软件包。需要足够的磁盘空间存放 chroot。属于面向 Arch Linux 维护者的 pkgctl 工具集。

# SEE ALSO

[pkgctl](/man/pkgctl)(1), [pkgctl-repo](/man/pkgctl-repo)(1), [makepkg](/man/makepkg)(8), [makechrootpkg](/man/makechrootpkg)(1)
