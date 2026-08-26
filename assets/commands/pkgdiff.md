# TAGLINE

比较 Slackware 软件包的内容差异

# TLDR

**比较**两个软件包

```pkgdiff [package1.txz] [package2.txz]```

以带**颜色**的输出进行比较

```pkgdiff -c [package1.txz] [package2.txz]```

输出 **unified diff** 格式

```pkgdiff -a [package1.txz] [package2.txz]```

# SYNOPSIS

**pkgdiff** [**-a**] [**-c**] _package1_ _package2_

# PARAMETERS

**-a**
> 输出简单的 unified diff 格式

**-c**
> 为输出着色以提高可读性

# DESCRIPTION

**pkgdiff** 比较两个 Slackware 软件包的内容并显示差异。它会展示软件包版本之间新增、删除或修改的文件，适合审查软件包更新。

该工具临时解压两个软件包，比较它们的文件列表和内容，类似 diff 但专为软件包归档而设计。

# CAVEATS

Slackware 专用工具。需要 txz/tgz 软件包格式。解压需要临时磁盘空间。大型软件包的比较可能耗时。

# HISTORY

**pkgdiff** 是 Slackware **pkgtools** 软件包管理套件的一部分。Slackware 使用简单的基于 tar 的软件包格式，pkgdiff 帮助维护者和用户了解软件包版本之间的变化。

# INSTALL

```dnf: sudo dnf install pkgdiff```

```pacman: sudo pacman -S pkgdiff```

```zypper: sudo zypper install pkgdiff```

```brew: brew install pkgdiff```

```nix: nix profile install nixpkgs#pkgdiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[installpkg](/man/installpkg)(8), [removepkg](/man/removepkg)(8), [upgradepkg](/man/upgradepkg)(8)
