# TAGLINE

列出 Docker Buildx 构建器实例

# TLDR

**列出所有构建器**实例

```docker buildx ls```

**列出构建器**且不截断输出

```docker buildx ls --no-trunc```

以自定义格式**列出构建器**

```docker buildx ls --format "{{.Name}}: {{.Status}}"```

以 JSON 格式**列出构建器**

```docker buildx ls --format json```

# SYNOPSIS

**docker buildx ls** [_options_]

# PARAMETERS

**--format** _format_
> 使用 Go 模板或预定义格式输出。默认：table。

**--no-trunc**
> 不截断输出。

**--timeout** _duration_
> 覆盖加载构建器状态的默认超时时间（默认：20s）。

# DESCRIPTION

**docker buildx ls** 列出所有构建器实例及其关联节点。输出包括构建器名称、驱动、端点、状态、BuildKit 版本和支持的平台。当前选定的构建器会标上星号（**\***）。

每个构建器可以有多个节点，代表不同的构建环境或平台。默认构建器使用 Docker 守护进程的内置构建能力，而其他构建器可以使用 **docker-container**、**kubernetes** 或 **remote** 驱动。

# CAVEATS

加载构建器状态时的默认超时为 20 秒。若远程或 Kubernetes 构建器的端点在超时窗口内不可达，它们可能显示为非活动状态。

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

[docker-buildx-rm](/man/docker-buildx-rm)(1), [docker-buildx-du](/man/docker-buildx-du)(1), [docker-build](/man/docker-build)(1), [docker](/man/docker)(1)
