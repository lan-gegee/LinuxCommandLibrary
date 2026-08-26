# TAGLINE

管理 Docker Swarm 中的敏感数据

# TLDR

**从文件创建 secret**

```docker secret create [name] [file]```

**从标准输入创建 secret**

```echo "[secret_value]" | docker secret create [name] -```

**列出 secrets**

```docker secret ls```

**查看一个 secret**

```docker secret inspect [name]```

**删除一个 secret**

```docker secret rm [name]```

# SYNOPSIS

**docker** **secret** _command_ [_options_]

# SUBCOMMANDS

**create**
> 从文件或 STDIN 创建 secret。

**ls**
> 列出 secrets。

**inspect**
> 显示详细信息。

**rm**
> 删除 secrets。

# DESCRIPTION

**docker secret** 管理 Swarm secrets，即密码、证书或 API 密钥等敏感数据。Secret 经过加密，只有需要它的服务才能访问。inspect 输出中永远不会暴露 secret 的内容本身，只显示元数据。Secret 以文件形式挂载到服务容器的 /run/secrets 目录中。

# CAVEATS

仅在 Swarm 模式下可用。Secret 无法更新；需要创建新版本并轮换服务。

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

[docker-swarm](/man/docker-swarm)(1), [docker-service](/man/docker-service)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
