# TAGLINE

Alpine Linux 软件包管理器

# TLDR

**更新**仓库索引并升级所有软件包

```apk upgrade -U```

只更新**仓库索引**

```apk update```

**安装**新软件包

```apk add [package]```

**安装**时不缓存索引（Dockerfile 中的常见做法）

```apk add --no-cache [package]```

**删除**软件包

```apk del [package]```

在不改动主依赖的情况下**修复/重装**软件包

```apk fix [package]```

按名称并附带描述**搜索**软件包

```apk search -v [keyword]```

按**描述**搜索软件包

```apk search -d [keyword]```

显示指定软件包的**信息**

```apk info [package]```

# SYNOPSIS

**apk** [_options_] _command_ [_arguments_]

# DESCRIPTION

**apk**（Alpine Package Keeper）是 Alpine Linux 的软件包管理工具。它负责软件包的安装、升级和删除，以及仓库管理和系统维护。

# PARAMETERS

**add**
> 添加或修改约束并提交更改

**del**
> 移除约束并提交更改

**fix**
> 在不修改 world 集合的情况下修复、重装或升级软件包

**update**
> 更新仓库索引

**upgrade**
> 安装仓库中可用的升级

**cache**
> 管理本地软件包缓存

**search**
> 按名称或描述搜索软件包

**info**
> 显示软件包的详细信息

**list**
> 列出匹配某个模式或条件的软件包

**query**
> 查询已安装数据库和索引

**policy**
> 显示软件包的仓库策略

**version**
> 比较软件包版本或检查可用升级

**fetch**
> 将软件包从仓库下载到当前目录

**stats**
> 显示软件包数据库的统计信息

**-U, --update-cache**
> 在操作前更新软件包列表（--cache-max-age 0 的别名）

**-v, --verbose**
> 打印更详细的信息（重复使用可获得更多细节）

**-q, --quiet**
> 打印更少的信息

**-d, --description**
> 在软件包描述中搜索

**--no-cache**
> 不使用也不更新任何本地缓存；直接获取索引

**--allow-untrusted**
> 安装签名不可信或缺失的软件包

**-X, --repository** _url_
> 指定补充仓库

**-p, --root** _dir_
> 管理以给定目录为根的文件系统

# CONFIGURATION

**/etc/apk/repositories**
> 软件包仓库 URL 列表，每行一个。

**/etc/apk/world**
> 显式安装的软件包及版本约束列表。

**/etc/apk/keys/**
> 存放受信任仓库签名密钥的目录。

# CAVEATS

仅适用于 Alpine Linux；其他发行版上不可用。使用为体积和简洁性设计的极简软件包格式。

# HISTORY

为 **Alpine Linux** 开发，这是一个面向安全、轻量级的 Linux 发行版。Alpine 因其占用空间小而被广泛用于容器环境。

# INSTALL

```dnf: sudo dnf install apk-tools```

```pacman: sudo pacman -S apk-tools```

```apk: sudo apk add apk-tools```

```zypper: sudo zypper install apk-tools```

```nix: nix profile install nixpkgs#apk-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [dnf](/man/dnf)(8), [pacman](/man/pacman)(8)

# RESOURCES

```[Source code](https://github.com/alpinelinux/apk-tools)```

```[Documentation](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper)```

<!-- verified: 2026-06-11 -->
