# TAGLINE

在容器与宿主机之间复制文件

# TLDR

**将文件从容器复制到宿主机**

```docker container cp [container]:[/path/in/container] [/local/path]```

**将文件从宿主机复制到容器**

```docker container cp [/local/file] [container]:[/path/in/container]```

**复制目录**

```docker container cp [container]:[/src/dir] [/dest/dir]```

# SYNOPSIS

**docker** **container** **cp** [_options_] _src_ _dest_

# PARAMETERS

**-a**, **--archive**
> 归档模式（保留权限）。

**-L**, **--follow-link**
> 跟随符号链接。

# DESCRIPTION

**docker container cp** 在容器和本地文件系统之间复制文件。适用于运行中或已停止的容器。

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

[docker-cp](/man/docker-cp)(1), [docker-container](/man/docker-container)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
