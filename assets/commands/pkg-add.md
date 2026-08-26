# TAGLINE

在 OpenBSD 和 NetBSD 上安装软件包

# TLDR

**从软件仓库安装软件包**

```pkg_add [package]```

**安装指定的软件包文件**

```pkg_add [/path/to/package.tgz]```

**从 URL 安装**

```pkg_add [https://example.com/package.tgz]```

**以详细输出安装**

```pkg_add -v [package]```

# SYNOPSIS

**pkg_add** [_options_] _pkg_...

# PARAMETERS

**-v**
> 详细模式。

**-D**
> 强制安装。

**-I**
> 非交互模式。

**-u**
> 更新模式。

**-n**
> 试运行。

**-r**
> 替换已存在的软件包。

# DESCRIPTION

**pkg_add** 在 OpenBSD 和 NetBSD 系统上安装软件包。它会处理依赖关系、从镜像站下载软件包，并对已安装的软件进行配置。

这是 BSD 的传统软件包管理器。

# EXAMPLES

```bash
# Install package
pkg_add vim

# Update package
pkg_add -u vim

# Install from mirror
export PKG_PATH=https://cdn.openbsd.org/pub/OpenBSD/$(uname -r)/packages/$(uname -m)/
pkg_add firefox

# Verbose install
pkg_add -v nginx
```

# ENVIRONMENT

```bash
PKG_PATH  # Package repository URL
PKG_CACHE # Local cache directory
```

# CAVEATS

仅适用于 OpenBSD/NetBSD。远程安装需设置 PKG_PATH。使用 pkg_info 列出软件包。

# HISTORY

pkg_add 是 **OpenBSD** 和 **NetBSD** 软件包工具的一部分，自 20 世纪 90 年代起提供简单的软件包管理功能。

# INSTALL

```nix: nix profile install nixpkgs#pkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkg](/man/pkg)(1)
