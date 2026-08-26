# TAGLINE

显示容器文件系统的变更

# TLDR

**查看容器内的文件系统变更**

```docker container diff [container]```

# SYNOPSIS

**docker** **container** **diff** _container_

# DESCRIPTION

**docker container diff** 检查容器文件系统上文件或目录的变更。与基础镜像相比，它会标出新增（A）、修改（C）或删除（D）的文件。

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

[docker-diff](/man/docker-diff)(1), [docker-container](/man/docker-container)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
