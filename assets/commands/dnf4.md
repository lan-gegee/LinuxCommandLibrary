# TAGLINE

旧版 DNF 4 软件包管理器

# TLDR

**升级**所有软件包

```sudo dnf4 upgrade```

**搜索**软件包

```dnf4 search [keyword1] [keyword2]```

显示软件包**信息**

```dnf4 info [package]```

**安装**软件包

```sudo dnf4 install [package1] [package2]```

**移除**软件包

```sudo dnf4 remove [package1] [package2]```

列出**已安装的**软件包

```dnf4 list --installed```

查找**提供**某命令的软件包

```dnf4 provides [command]```

查看**历史**

```dnf4 history```

# SYNOPSIS

**dnf4** _command_ [_options_] [_packages_]

# DESCRIPTION

**dnf4** 是 DNF 第 4 版软件包管理器，用于 RHEL 8/9 和较旧的 Fedora 版本（41 之前）。它是 yum 的后继者，负责管理 RPM 软件包。

在 Fedora 41+ 上，dnf 默认使用第 5 版。需要旧版时请显式使用 dnf4。

# PARAMETERS

**upgrade**
> 升级已安装的软件包

**search** _keywords_
> 搜索软件包名称和摘要

**info** _package_
> 显示软件包详情

**install** _packages_
> 安装软件包

**remove** _packages_
> 移除软件包

**list**
> 列出软件包

**provides** _file_
> 查找拥有某文件的软件包

**history**
> 查看事务历史

# CAVEATS

属于旧版本，较新的系统使用 dnf5。支持命令缩写（in、rm、se 等）。

# INSTALL

```zypper: sudo zypper install dnf4```

```nix: nix profile install nixpkgs#dnf4```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnf](/man/dnf)(8), [dnf5](/man/dnf5)(8), [rpm](/man/rpm)(8)

# RESOURCES

```[Source code](https://github.com/rpm-software-management/dnf)```

```[Documentation](https://dnf.readthedocs.io/)```

<!-- verified: 2026-07-11 -->
