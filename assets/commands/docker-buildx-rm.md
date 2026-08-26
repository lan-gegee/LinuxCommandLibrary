# TAGLINE

移除 Docker Buildx 构建器实例

# TLDR

**移除指定的**构建器实例

```docker buildx rm [builder_name]```

**移除构建器**且不弹出确认提示

```docker buildx rm -f [builder_name]```

**移除所有非活动**构建器

```docker buildx rm --all-inactive```

**移除构建器**但保持 BuildKit 守护进程运行

```docker buildx rm --keep-daemon [builder_name]```

**移除构建器**但保留其状态以便复用

```docker buildx rm --keep-state [builder_name]```

# SYNOPSIS

**docker buildx rm** [_options_] [_name..._]

# PARAMETERS

**--all-inactive**
> 移除所有非活动的构建器实例。

**-f**, **--force**
> 不弹出确认提示。

**--keep-daemon**
> 移除构建器后仍保持 BuildKit 守护进程运行。仅 docker-container 和 kubernetes 驱动支持。

**--keep-state**
> 保留 BuildKit 状态，使之后同名的新构建器可以复用。仅 docker-container 驱动支持。

**--timeout** _duration_
> 覆盖加载构建器状态的默认超时时间（默认：20s）。

# DESCRIPTION

**docker buildx rm** 移除指定的构建器实例；若未给出名称，则移除当前选定的构建器。移除 **default** 构建器是空操作，因为它使用 Docker 守护进程的内置构建能力。

默认情况下，该命令会停止关联的 BuildKit 守护进程并清理其状态。使用 **--keep-daemon** 可让守护进程继续独立运行；使用 **--keep-state** 可保留构建缓存和状态，供未来同名的构建器使用。

# CAVEATS

默认构建器无法移除。**--keep-daemon** 标志只对 docker-container 和 kubernetes 驱动有效。**--keep-state** 标志只对 docker-container 驱动有效。

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

[docker-buildx-ls](/man/docker-buildx-ls)(1), [docker-buildx-prune](/man/docker-buildx-prune)(1), [docker-build](/man/docker-build)(1), [docker](/man/docker)(1)
