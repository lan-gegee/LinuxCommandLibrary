# TAGLINE

**pacman --sync** 的简写形式，用于同步软件包

# TLDR

此命令是 **pacman --sync** 的别名

查看原始命令的文档

```tldr pacman sync```

# SYNOPSIS

**pacman -S** [_options_] [_package(s)_]

# PARAMETERS

**-y**, **--refresh**
> 从服务器下载主软件包数据库的最新副本。

**-u**, **--sysupgrade**
> 升级所有过期的软件包。

**-s**, **--search** _regexp_
> 在同步数据库中搜索软件包名称和描述。

**-i**, **--info**
> 显示同步数据库中软件包的详细信息。

**-c**, **--clean**
> 从缓存目录移除旧软件包。

**-l**, **--list**
> 列出指定仓库中的所有软件包。

**-g**, **--groups**
> 显示软件包组的成员。

**-q**, **--quiet**
> 查询和搜索结果显示更少的信息。

**--needed**
> 不重装已是最新版本的软件包。

**--asdeps**
> 以非显式安装（作为依赖）的方式安装软件包。

**--overwrite** _glob_
> 覆盖匹配给定 glob 模式的冲突文件。

**--downloadonly**, **-w**
> 只下载软件包而不安装。

**--ignore** _package_
> 跳过指定软件包的升级。

# DESCRIPTION

**pacman -S** 是 **pacman --sync** 的简写形式，用于同步软件包。它负责从仓库安装软件包、更新软件包数据库以及执行系统升级。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-sync](/man/pacman-sync)(8)
