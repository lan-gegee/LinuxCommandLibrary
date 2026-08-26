# TAGLINE

GNU/Linux 的交互式软件包管理器和资源监视器

# TLDR

**启动软件包仪表盘**

```pkgtop```

**按字母顺序列出软件包**

```pkgtop -a```

# SYNOPSIS

**pkgtop** [_options_]

# PARAMETERS

**-a**
> 按字母顺序而非大小排列软件包。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**pkgtop** 是一个面向 GNU/Linux 的交互式终端仪表盘，用于管理软件包和监控系统资源。它按大小列出已安装的软件包、显示软件包信息，并支持安装、升级、移除和搜索软件包。仪表盘还会显示磁盘使用情况和一般系统信息。

# CAVEATS

仅支持 Linux。支持 Arch、Debian、Ubuntu、Fedora、CentOS、openSUSE、Void、Gentoo、NixOS、Guix 及其衍生发行版。

# HISTORY

**pkgtop** 由 **Orhun Parmaksiz**（orhun）开发，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#pkgtop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(8), [pacman](/man/pacman)(8), [dnf](/man/dnf)(8), [htop](/man/htop)(1)
