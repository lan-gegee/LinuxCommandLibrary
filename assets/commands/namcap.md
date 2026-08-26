# TAGLINE

检查二进制包和源码 PKGBUILD 中的常见打包问题

# TLDR

检查 **PKGBUILD** 文件中的问题

```namcap [path/to/PKGBUILD]```

检查**软件包文件**中的问题

```namcap [path/to/package.pkg.tar.zst]```

**附带额外信息性消息**进行检查

```namcap -i [path/to/file]```

以**机器可读**格式输出

```namcap -m [path/to/file]```

**列出可用规则**

```namcap --rules```

# SYNOPSIS

**namcap** [**-i**] [**-m**] [**--rules** _list_] _filename_

# PARAMETERS

**-i, --info**
> 显示额外的信息性消息

**-m, --machine-readable**
> 以程序可解析的格式输出

**--rules _list_**
> 列出可用的检查规则

**-h, --help**
> 显示帮助信息

# OUTPUT TYPES

**E: (Error)**
> 需要修复的严重问题；涉及安全、许可或权限

**W: (Warning)**
> 建议进行的更改；经验丰富的打包者可以酌情忽略

**I: (Information)**
> 有用的提示；仅在带 --info 标志时显示

# DESCRIPTION

**namcap** 在 Arch Linux 上检查二进制包和源码 PKGBUILD 中的常见打包错误。它验证必填字段、文件权限、依赖、许可证和安全问题。

该工具帮助软件包维护者在提交到 AUR 或官方仓库之前发现潜在问题。它会运行多项基于规则的检查，并按严重程度分类报告。

# COMMON CHECKS

- PKGBUILD 必填字段（pkgname、pkgver、url 等）
- 软件包文件的权限和所有者
- 许可证文件的包含情况
- 缺失或多余的依赖
- 安全问题
- ELF 文件问题
- 空目录

# CAVEATS

并非所有警告都需要处理；有些只是给经验丰富打包者的提示。该工具依据 Arch Linux 的打包标准进行检查，可能不适用于其他发行版。某些检查需要先构建软件包才能分析。

# HISTORY

**namcap** 由 **Arch Linux** 社区开发，是面向软件包维护者的质量保证工具。它作为 Arch Linux 开发工具的一部分维护，帮助确保一致的打包标准。

# INSTALL

```pacman: sudo pacman -S namcap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8), [PKGBUILD](/man/PKGBUILD)(5)
