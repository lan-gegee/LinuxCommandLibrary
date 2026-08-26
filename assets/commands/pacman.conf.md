# TAGLINE

Arch Linux 软件包管理器 pacman 的配置文件

# TLDR

**启用 multilib 仓库**

```[multilib]\nInclude = /etc/pacman.d/mirrorlist```

**设置并行下载**

```ParallelDownloads = 5```

**启用彩色输出**

```Color```

**添加自定义仓库**

```[custom]\nServer = https://example.com/$repo/$arch```

# SYNOPSIS

**/etc/pacman.conf**

# PARAMETERS

**[options]**
> 常规选项节。

**Color**
> 启用彩色输出。

**ParallelDownloads**
> 并发下载数。

**CheckSpace**
> 检查磁盘空间。

**SigLevel**
> 软件包签名级别。

**[repository]**
> 仓库定义。

**Include**
> 引入镜像列表。

**Server**
> 直接指定服务器 URL。

# DESCRIPTION

**pacman.conf** 是 Arch Linux 软件包管理器 pacman 的配置文件。它定义仓库、签名检查以及各种选项。

该文件采用 INI 风格的节结构，[options] 用于常规设置，[reponame] 用于仓库。

# EXAMPLE CONFIG

```ini
[options]
HoldPkg = pacman glibc
Architecture = auto
Color
CheckSpace
ParallelDownloads = 5
SigLevel = Required DatabaseOptional

[core]
Include = /etc/pacman.d/mirrorlist

[extra]
Include = /etc/pacman.d/mirrorlist

[multilib]
Include = /etc/pacman.d/mirrorlist
```

# CAVEATS

仓库顺序很重要。更改后需要运行 pacman -Sy。编辑前请先备份。

# SEE ALSO

[pacman](/man/pacman)(8), [makepkg](/man/makepkg)(8), [libalpm](/man/libalpm)(3)
