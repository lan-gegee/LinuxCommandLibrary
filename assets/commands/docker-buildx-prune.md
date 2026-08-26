# TAGLINE

清除 Docker Buildx 构建缓存

# TLDR

**清理所有构建缓存**，带确认提示

```docker buildx prune```

**强制清理**，无需确认

```docker buildx prune -f```

**清理全部缓存**，包括内部镜像和 frontend 镜像

```docker buildx prune --all```

**清理超过 24 小时**的缓存

```docker buildx prune --filter until=[24h]```

**清理缓存**并最多保留 2 GB

```docker buildx prune --max-used-space [2gb]```

**清理缓存**并确保至少有 10 GB 可用磁盘空间

```docker buildx prune --min-free-space [10gb]```

# SYNOPSIS

**docker buildx prune** [_options_]

# PARAMETERS

**-a**, **--all**
> 清除全部缓存，包括内部镜像和 frontend 镜像。

**-f**, **--force**
> 跳过确认提示。

**--filter** _key=value_
> 过滤要清理的缓存记录（例如 until=24h、type、inuse、shared）。

**--max-used-space** _size_
> 缓存可占用的最大磁盘空间总量（例如 2gb、512mb）。

**--min-free-space** _size_
> 清理后目标保留的可用磁盘空间量。

**--reserved-space** _size_
> 永久为缓存预留的最小磁盘空间。

**--timeout** _duration_
> 覆盖加载构建器状态的默认超时时间（默认：20s）。

**--verbose**
> 显示详细输出。

# DESCRIPTION

**docker buildx prune** 清除当前选定构建器实例的构建缓存。默认只移除可回收的缓存条目，并提示确认。配合 **--all** 时还会移除内部镜像和 frontend 镜像。

空间管理标志（**--max-used-space**、**--min-free-space**、**--reserved-space**）允许对磁盘占用进行精细控制。**--filter** 标志支持 **until**、**id**、**type**、**inuse**、**mutable**、**shared** 和 **private** 等选择器，多个条件按 AND 逻辑组合。

# CAVEATS

不带 **--all** 时，内部镜像和 frontend 缓存会被保留。空间标志接受人类可读的值（如 128mb、2gb）。同时指定多个空间标志时，所有约束会一并生效。

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

[docker-buildx-du](/man/docker-buildx-du)(1), [docker-buildx-rm](/man/docker-buildx-rm)(1), [docker-build](/man/docker-build)(1), [docker](/man/docker)(1)
