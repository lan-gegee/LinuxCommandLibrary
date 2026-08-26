# TAGLINE

更改容器的名称标识

# TLDR

**重命名一个容器**

```docker rename [old_name] [new_name]```

# SYNOPSIS

**docker** **rename** _container_ _new_name_

# DESCRIPTION

**docker rename** 用于重命名现有容器，对运行中和已停止的容器都有效。适合为创建时未使用 --name 的容器起一个有意义的名字。容器名称在 Docker 主机内必须唯一，并遵循命名约定（字母数字字符、下划线、句点和连字符）。

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

[docker-container-rename](/man/docker-container-rename)(1), [docker-run](/man/docker-run)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
