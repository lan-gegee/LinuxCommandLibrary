# TAGLINE

备份和恢复已安装软件包的状态

# TLDR

将当前系统的软件包状态**克隆**到目录中

```sudo apt-clone clone [path/to/directory]```

克隆时包含**仓库**中已不可用的软件包

```sudo apt-clone clone --with-dpkg-repack [path/to/directory]```

从克隆文件**恢复**软件包状态

```sudo apt-clone restore [path/to/apt-clone-state-hostname.tar.gz]```

恢复到**特定目录**（debootstrap）

```sudo apt-clone restore [path/to/clone.tar.gz] --destination [path/to/directory]```

显示克隆文件的**信息**

```apt-clone info [path/to/apt-clone-state-hostname.tar.gz]```

恢复并**升级**到新的发行版版本

```sudo apt-clone restore-new-distro [path/to/clone.tar.gz] [new_distro_codename]```

# SYNOPSIS

**apt-clone** _command_ [_options_]

# DESCRIPTION

**apt-clone** 创建并恢复基于 Debian 的系统上已安装软件包状态的备份。它记录已安装软件包及其版本和仓库来源的信息，用于系统迁移或恢复。

克隆文件是压缩的 tar 归档，包含软件包列表和 APT 源配置。这使你能够在另一台机器上或在全新安装之后复刻一个系统的软件配置。

# SUBCOMMANDS

**clone** _destination_
> 在指定的目标目录中创建当前软件包状态的克隆文件。

**restore** _source_ [**--destination** _path_]
> 从克隆文件恢复软件包。可选择 debootstrap 到特定目录。

**restore-new-distro** _source_ _new_distro_codename_
> 恢复克隆文件，并尝试将软件包升级到新的发行版版本。

**info** _source_
> 显示克隆文件的信息。

# PARAMETERS

**--source** _path_
> 指定用于克隆的其他来源目录（默认为 /）。

**--destination** _path_
> 指定恢复的目标目录（将克隆 debootstrap 到该目录）。

**--with-dpkg-repack**
> 包含仓库中已不再可用的软件包的软件包文件。

**--with-dpkg-status**
> 包含完整的 dpkg status 文件。

**-h**, **--help**
> 显示帮助信息并退出。

**--debug**
> 启用调试输出。

# CAVEATS

在不同发行版版本上恢复克隆可能因软件包不兼容而失败；跨版本恢复请使用 **restore-new-distro**。克隆和恢复操作需要 root 权限。恢复期间需要有效的网络连接来下载软件包。已配置仓库中不存在的软件包会被跳过，除非克隆时使用了 **--with-dpkg-repack**。

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1), [apt-get](/man/apt-get)(8), [apt-mark](/man/apt-mark)(8)
