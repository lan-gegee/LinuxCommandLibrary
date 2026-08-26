# TAGLINE

解压 Slackware 软件包内容而不安装

# TLDR

将软件包**解压**到当前目录

```explodepkg [path/to/package.tgz]```

解压**多个**软件包

```explodepkg [path/to/package1.tgz] [path/to/package2.tgz]```

# SYNOPSIS

**explodepkg** _packages_

# DESCRIPTION

**explodepkg** 将 Slackware 软件包的内容解压到当前目录。与 installpkg 不同，它不会把软件包安装到系统中，也不会运行安装脚本。

Slackware 软件包是具有特定结构的压缩 tar 包（.tgz 或 .txz）。该工具将其解开以便检查，可以提取文件来查看软件包内容、文档，或者用于制作修改后的软件包。

适合在安装前检查软件包内容、调试软件包问题，或在不完整安装的情况下提取特定文件。属于 Slackware pkgtools 套件的一部分。

# PARAMETERS

_packages_
> 一个或多个要解压的 Slackware 软件包

# CAVEATS

仅适用于 Slackware Linux。解压到当前目录而非系统路径。不运行 doinst.sh 脚本。属于 pkgtools 套件。

# SEE ALSO

[installpkg](/man/installpkg)(8), [removepkg](/man/removepkg)(8), [upgradepkg](/man/upgradepkg)(8), [makepkg](/man/makepkg)(8)

# RESOURCES

```[Homepage](http://www.slackware.com/)```

<!-- verified: 2026-07-15 -->
