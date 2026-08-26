# TAGLINE

重命名现有容器

# TLDR

**重命名容器**

```docker container rename [old_name] [new_name]```

# SYNOPSIS

**docker** **container** **rename** _container_ _new_name_

# DESCRIPTION

**docker container rename** 将容器重命名为新名称，不影响其配置、状态或数据。此操作对运行中和已停止的容器都有效，可以用来纠正命名错误或重新组织容器的命名方案。

容器名称在 Docker 主机上必须唯一。重命名不会修改容器的 ID 或除名称以外的任何属性。简写别名 **docker rename** 与之等价。

# CAVEATS

其他通过 Docker DNS 或旧式 `--link` 标志引用旧名称的容器，在重新连接或重启之前仍会使用旧名称。由 Compose 管理的容器应通过 Compose 配置来重命名，以保持状态一致。

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

[docker-rename](/man/docker-rename)(1), [docker-container](/man/docker-container)(1)
