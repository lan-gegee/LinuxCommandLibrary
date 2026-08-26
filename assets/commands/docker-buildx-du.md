# TAGLINE

显示 Docker 构建缓存的磁盘占用

# TLDR

**查看构建缓存**的磁盘占用

```docker buildx du```

**显示包含全部元数据的详细**磁盘占用

```docker buildx du --verbose```

**查看指定构建器的**磁盘占用

```docker buildx du --builder [builder_name]```

按缓存记录年龄**过滤**

```docker buildx du --filter until=[24h]```

按类型**过滤**缓存记录

```docker buildx du --filter type=[regular]```

# SYNOPSIS

**docker buildx du** [_options_]

# PARAMETERS

**--filter** _key=value_
> 使用键值选择器过滤输出（例如 `until=24h`、`type=...`）。

**--verbose**
> 显示带有附加元数据的详细输出。

**--builder** _name_
> 针对指定的构建器实例（覆盖默认设置）。

# DESCRIPTION

**docker buildx du** 显示当前选定（或指定）构建器实例构建缓存的磁盘占用信息。输出会列出各条缓存记录及其 ID、是否可回收、大小以及最近访问时间。

此命令有助于在决定用 **docker buildx prune** 清理之前了解构建缓存占用了多少磁盘空间。

# CAVEATS

输出中的星号表示可变记录（大小可能变化）或与其他资源重叠的共享存储。当记录被多个构建共享时，报告的大小可能并不反映实际可回收的空间。

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

[docker-buildx-prune](/man/docker-buildx-prune)(1), [docker-buildx-ls](/man/docker-buildx-ls)(1), [docker-build](/man/docker-build)(1), [docker](/man/docker)(1)
