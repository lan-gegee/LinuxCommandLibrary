# TAGLINE

将远程软件仓库同步到本地

# TLDR

将仓库**同步**到本地目录

```dnf reposync --repoid [repo_name]```

同步到**自定义位置**

```dnf reposync --repoid [repo_name] -p [path/to/directory]```

同步软件包**及元数据**

```dnf reposync --repoid [repo_name] --download-metadata```

仅下载**最新的软件包**

```dnf reposync --repoid [repo_name] -n```

仅**打印 URL**

```dnf reposync --repoid [repo_name] -u```

保留**远程时间戳**

```dnf reposync --repoid [repo_name] --remote-time```

# SYNOPSIS

**dnf reposync** [_options_]

# DESCRIPTION

**dnf reposync** 将远程 DNF 软件仓库的软件包和元数据同步到本地目录。属于 dnf-plugins-core。

适用于创建本地镜像或离线仓库。

# PARAMETERS

**--repoid** _repo_
> 要同步的仓库

**-p, --download-path** _path_
> 下载目标位置

**--download-metadata**
> 同时下载仓库元数据

**-n, --newest-only**
> 仅下载最新版本的软件包

**-u, --urls**
> 打印 URL 而不下载

**--remote-time**
> 保留远程时间戳

# CAVEATS

需要 dnf-plugins-core。大型仓库需要大量磁盘空间和带宽。可用 --newest-only 减小体积。

# SEE ALSO

[dnf](/man/dnf)(8), [createrepo](/man/createrepo)(8)
