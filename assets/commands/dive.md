# TAGLINE

探索 Docker 镜像内容与层效率

# TLDR

**分析 Docker 镜像**

```dive [image:tag]```

**以 CI 模式分析**

```dive [image:tag] --ci```

**一步完成构建与分析**

```dive build -t [image:tag] [.]```

**从 tar 归档分析**

```dive --source [docker-archive] [image.tar]```

**为 CI 设置效率阈值**

```dive [image:tag] --ci --highestUserWastedPercent [0.1]```

# SYNOPSIS

**dive** [_options_] _image_

# PARAMETERS

_IMAGE_
> 带可选标签的 Docker 镜像名。

**--ci**
> CI 模式（无 TUI 界面，返回退出码）。

**--source** _SOURCE_
> 镜像来源：docker、podman、docker-archive。

**build** [_args_]
> 构建镜像后进行分析。

**--highestUserWastedPercent** _N_
> CI 通过所允许的最大空间浪费百分比。

**--lowestEfficiency** _N_
> CI 通过所需的最低效率值。

**--json**
> 以 JSON 格式输出结果。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dive** 是一款用于探索 Docker 镜像内容和层效率的工具。它提供交互式 TUI 界面，展示每一层中的变更内容，帮助发现缩小镜像体积的机会。

该工具逐层展示镜像文件系统的构成，高亮新增、删除和修改的文件。效率分数反映镜像的优化程度，并明确显示浪费的空间。

dive 可集成到 CI 流水线中以强制执行镜像效率要求。它可以分析来自 Docker、Podman 或归档文件的镜像，还能在分析前先构建镜像。

# CAVEATS

大型镜像的分析可能耗时较久。部分层信息依赖于镜像的构建历史。压缩合并后的镜像层信息有限。分析实时镜像需要访问容器运行时。

# HISTORY

dive 由 **Alex Goodman** 开发并于 **2018 年**发布。它旨在解决 Docker 镜像臃肿这一常见问题，让层内容可视化并量化效率。

# INSTALL

```pacman: sudo pacman -S dive```

```apk: sudo apk add dive```

```zypper: sudo zypper install dive```

```brew: brew install dive```

```nix: nix profile install nixpkgs#dive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [podman](/man/podman)(1), [skopeo](/man/skopeo)(1)

# RESOURCES

```[Source code](https://github.com/wagoodman/dive)```

<!-- verified: 2026-07-11 -->
