# TAGLINE

为 APT 仓库生成索引文件。

# TLDR

**生成** Packages 文件

```apt-ftparchive packages [pool/] > [Packages]```

生成 **Sources** 文件

```apt-ftparchive sources [pool/] > [Sources]```

生成 **Release** 文件

```apt-ftparchive release [dists/stable] > [Release]```

使用**配置文件**生成

```apt-ftparchive generate [config.conf]```

# SYNOPSIS

**apt-ftparchive** [_options_] _command_ [_arguments_]

# DESCRIPTION

**apt-ftparchive** 为 APT 仓库生成索引文件。它从一个存放 .deb 和 .dsc 文件的目录创建 Packages、Sources、Contents 和 Release 文件。

此工具对于创建和维护本地 APT 仓库或镜像至关重要。

# PARAMETERS

**packages** _dir_
> 从目录生成 Packages 文件

**sources** _dir_
> 生成 Sources 文件

**contents** _dir_
> 生成 Contents 文件

**release** _dir_
> 生成 Release 文件

**generate** _config_
> 按配置生成文件

**clean** _config_
> 清理数据库文件

**-c** _file_
> 配置文件

**-d** _db_
> 数据库目录

**--md5**, **--sha1**, **--sha256**, **--sha512**
> 要生成的哈希算法

# CAVEATS

Release 文件应使用 gpg 签名以构建安全的仓库。大型仓库的索引可能耗时较长。数据库缓存可以提升重新生成的速度。

# HISTORY

**apt-ftparchive** 是 APT 的组成部分，专为仓库维护者设计，用于创建 APT 客户端查找和下载软件包所需的索引文件。

# INSTALL

```apt: sudo apt install apt-utils```

```dnf: sudo dnf install apt-utils```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8)
