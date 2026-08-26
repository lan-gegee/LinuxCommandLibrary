# TAGLINE

面向 elementary OS 的 Debian 软件包安装器

# TLDR

**安装** .deb 软件包文件

```eddy [package.deb]```

**一次安装**多个 .deb 软件包

```eddy [package1.deb] [package2.deb]```

**启动**图形化安装器

```eddy```

# SYNOPSIS

**eddy** [_options_] [_files_]

# PARAMETERS

**--debug**
> 启用调试输出以便排查问题。

# DESCRIPTION

**eddy** 是一个专为 elementary OS 设计的图形化 Debian 软件包安装器。它提供基于 GTK 的简洁界面，用于安装、更新、卸载和查看 .deb 软件包的信息。它使用 PackageKit 作为后端，这也使其对 .rpm 等其他软件包格式提供有限的支持。

该应用旨在作为命令行软件包管理的用户友好替代方案，用于处理在系统软件包管理器之外下载的单个软件包文件。

# CAVEATS

主要面向 elementary OS 设计，但可能适用于其他基于 GTK 的发行版。其后端依赖 PackageKit。并非完整的软件包管理器替代品；仅用于安装单个软件包文件。

# INSTALL

```nix: nix profile install nixpkgs#eddy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dpkg](/man/dpkg)(1), [apt](/man/apt)(1), [gdebi](/man/gdebi)(1)
