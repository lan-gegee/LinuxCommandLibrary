# TAGLINE

Arch Linux 软件包构建脚本

# TLDR

**在干净的 chroot 中构建软件包**

```extra-x86_64-build```

**构建 testing 软件包**

```testing-x86_64-build```

**构建 staging 软件包**

```staging-x86_64-build```

**创建一个干净的 chroot**

```mkarchroot [/path/to/chroot/root] base-devel```

**更新 chroot 中的软件包**

```arch-nspawn [/path/to/chroot/root] pacman -Syu```

**在 chroot 中运行命令**

```arch-nspawn [/path/to/chroot/root] [command]```

**为软件包签名**

```signpkg [package.pkg.tar.zst]```

# SYNOPSIS

**extra-x86_64-build** [_options_]

**mkarchroot** _chroot_ _packages_...

**arch-nspawn** _chroot_ _command_

# BUILD COMMANDS

**extra-x86_64-build**
> 为 extra 仓库构建。

**testing-x86_64-build**
> 为 testing 仓库构建。

**staging-x86_64-build**
> 为 staging 仓库构建。

**multilib-build**
> 构建 32 位 multilib 软件包。

# CHROOT COMMANDS

**mkarchroot** _path_ _pkgs_
> 用指定软件包创建新的 chroot。

**arch-nspawn** _chroot_ _cmd_
> 使用 nspawn 在现有 chroot 中运行命令。

**makechrootpkg** [_options_]
> 在 chroot 中构建软件包。

**makerepropkg** [_options_]
> 重新构建一个软件包以检验可复现性。

# PACKAGE TOOLS

**signpkg** _pkg_
> 用 GPG 为软件包签名。

**checkpkg**
> 将软件包与仓库版本进行比较。

**diffpkg** _pkg_
> 以不同模式比较软件包文件。

**find-libdeps** _pkg_
> 查找共享库依赖。

**find-libprovides** _pkg_
> 查找软件包提供的 soname。

**lddd**
> 查找系统中失效的库链接。

**sogrep** _repo_ _lib_
> 搜索使用某个库的软件包。

# DESCRIPTION

**devtools** 是 Arch Linux 开发者和受信用户（Trusted User）用于在干净 chroot 环境中构建软件包的工具集合。它附带统一的命令行前端 **pkgctl**，方便地与该集合中的所有工具交互。

构建脚本（extra-x86_64-build 等）会创建与官方仓库状态一致的隔离 chroot，在其中构建软件包并验证结果。这保证了软件包在全新安装的 Arch 上也能正常工作。

其他工具辅助软件包维护：查找依赖、比较版本、为软件包签名以及管理 chroot。

# CONFIGURATION

**/etc/makepkg.conf**
> 影响构建行为的系统级 makepkg 配置。

**~/.makepkg.conf**
> 针对软件包构建的用户级 makepkg 覆盖配置。

# CAVEATS

需要 sudo 和 systemd-nspawn。首次创建 chroot 会下载基础系统。chroot 需要数 GB 磁盘空间。构建耗时取决于软件包复杂度。构建前应更新 chroot。

# HISTORY

devtools 由 **Arch Linux 开发者**开发，目的是标准化软件包构建。这些脚本从手工流程逐步演化为自动化工具。为保证可复现性，官方 Arch 软件包强制要求使用干净 chroot 构建。经过 Arch 打包社区多年使用，这些工具不断完善。

# INSTALL

```pacman: sudo pacman -S devtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8), [pkgctl](/man/pkgctl)(1), [systemd-nspawn](/man/systemd-nspawn)(1)
