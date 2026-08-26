# TAGLINE

在容器与宿主机之间复制文件

# TLDR

**将文件从容器复制到宿主机**

```docker cp [container]:[/path/to/file] [/local/path]```

**将文件从宿主机复制到容器**

```docker cp [/local/file] [container]:[/path/in/container]```

**递归复制目录**

```docker cp [container]:[/path/to/dir] [/local/dir]```

**复制时保留所有者信息**

```docker cp -a [container]:[/path] [/local/path]```

# SYNOPSIS

**docker** **cp** [_options_] _container:src_path_ _dest_path_

**docker** **cp** [_options_] _src_path_ _container:dest_path_

# PARAMETERS

**-a**, **--archive**
> 归档模式（复制全部 uid/gid 信息）。

**-L**, **--follow-link**
> 跟随源路径中的符号链接。

**-q**, **--quiet**
> 抑制进度输出。

# DESCRIPTION

**docker cp** 在容器的文件系统和本地宿主机的文件系统之间复制文件或目录，支持容器到宿主机和宿主机到容器的双向传输。此命令对运行中和已停止的容器都有效，可用于提取日志、注入配置文件或备份数据。

该命令内部使用 tar 进行高效传输，在容器与宿主机之间流式传送数据。归档模式（**-a**）会保留文件的所有者和权限，在复制系统文件或需要保持一致文件属性时很重要。

与在容器创建时就固定下来的卷挂载不同，**docker cp** 允许在容器生命周期的任意时刻进行临时文件传输。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-container-cp](/man/docker-container-cp)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
