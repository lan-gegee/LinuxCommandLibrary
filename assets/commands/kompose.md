# TAGLINE

将 Docker Compose 文件转换为 Kubernetes 资源

# TLDR

**转换为 Kubernetes**

```kompose convert```

**转换指定文件**

```kompose convert -f [docker-compose.yml]```

**转换为 Helm chart**

```kompose convert -c```

以指定的控制器类型**转换**

```kompose convert --controller [daemonSet]```

**以 JSON 输出**到 stdout

```kompose convert --json --stdout```

带副本数**转换**

```kompose convert --replicas [3]```

**直接部署到集群**

```kompose up```

# SYNOPSIS

**kompose** _command_ [_options_]

# PARAMETERS

**convert**
> 将 compose 文件转换为 Kubernetes。

**up**
> 部署到 Kubernetes。

**down**
> 从 Kubernetes 中移除。

**-f** _FILE_
> 要转换的 compose 文件。

**-c**, **--chart**
> 输出 Helm chart。

**-o** _DIR_
> 输出目录。

**--replicas** _N_
> 设置副本数（默认 1）。

**--controller** _TYPE_
> 设置输出的控制器类型（deployment、daemonSet、replicationController）。

**--volumes** _TYPE_
> 卷的生成类型（persistentVolumeClaim、emptyDir、hostPath、configMap）。默认 persistentVolumeClaim。

**--json**
> 以 JSON 格式生成资源文件。

**--stdout**
> 将转换后的对象输出到 stdout。

**--provider** _PROVIDER_
> 目标平台（kubernetes、openshift）。默认 kubernetes。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kompose** 是一款转换工具，可将 Docker Compose 文件翻译成 Kubernetes 资源清单。它解析 `docker-compose.yml` 定义并生成相应的 Deployment、Service、PersistentVolumeClaim 等 Kubernetes 对象，为最初基于 Docker Compose 设计的应用提供迁移路径。

该工具支持多种输出格式，包括标准 Kubernetes YAML、JSON 和 Helm chart。它还可以通过 `kompose up` 将转换后的资源直接部署到集群，或用 `kompose down` 拆除它们。作为 CNCF sandbox 项目，kompose 能够处理端口映射、卷、环境变量和副本数等常见 Compose 指令，但某些 Compose 特有功能可能需要在转换后手动调整。

# CAVEATS

并非所有 Compose 特性都能被转换。可能需要手动调整。CNCF 项目。

# HISTORY

kompose 的创建目的是帮助用户从 Docker Compose 迁移到 Kubernetes，后来成为 CNCF sandbox 项目。

# INSTALL

```pacman: sudo pacman -S kompose```

```zypper: sudo zypper install kompose```

```brew: brew install kompose```

```nix: nix profile install nixpkgs#kompose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [docker-compose](/man/docker-compose)(1), [helm](/man/helm)(1)
