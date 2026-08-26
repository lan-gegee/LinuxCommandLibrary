# TAGLINE

根据容器状态创建镜像

# TLDR

**从容器创建镜像**

```docker container commit [container] [image:tag]```

**附带说明提交**

```docker container commit -m "[message]" [container] [image:tag]```

# SYNOPSIS

**docker** **container** **commit** [_options_] _container_ [_repository[:tag]_]

# DESCRIPTION

**docker container commit** 根据容器的更改创建新镜像。它是 **docker commit** 的别名。

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

[docker-commit](/man/docker-commit)(1), [docker-container](/man/docker-container)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
