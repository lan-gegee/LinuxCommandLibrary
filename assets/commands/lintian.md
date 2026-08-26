# TAGLINE

检查 Debian 软件包是否符合策略规范

# TLDR

**检查 Debian 软件包**

```lintian [package.deb]```

**检查 changes 文件**

```lintian [package.changes]```

**详细输出**

```lintian -v [package.deb]```

**显示 info 级标签**

```lintian -I [package.deb]```

**显示所有标签**

```lintian -iI [package.deb]```

**检查特定标签**

```lintian --tags [tag-name] [package.deb]```

# SYNOPSIS

**lintian** [_options_] _packages_

# PARAMETERS

_PACKAGES_
> Debian 软件包、changes 文件或 dsc 文件。

**-v**
> 详细输出。

**-I**
> 显示 info 级标签。

**-i**
> 显示标签描述。

**--tags** _TAG_
> 只检查特定标签。

**--suppress-tags** _TAG_
> 抑制特定标签。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lintian** 检查 Debian 软件包是否符合策略规范。它能识别缺陷、违反策略之处和其他问题。

该工具对 Debian 维护者至关重要。它可以检查二进制软件包和源码软件包。

# CAVEATS

专注于 Debian/Ubuntu。标签数据库庞大。某些检查需要已安装的软件包。

# HISTORY

Lintian 由 **Christian Schwarz** 于 1998 年创建，旨在帮助 Debian 维护者产出高质量的软件包。

# INSTALL

```aur: yay -S lintian```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lintian-info](/man/lintian-info)(1), [dpkg](/man/dpkg)(1), [debuild](/man/debuild)(1)
