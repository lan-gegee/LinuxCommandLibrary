# TAGLINE

从归档加载容器镜像

# TLDR

**从归档加载镜像**

```podman load -i [image.tar]```

**从 stdin 加载**

```cat [image.tar] | podman load```

**以新名称加载**

```podman load -i [archive.tar]```

# SYNOPSIS

**podman load** [_options_]

# PARAMETERS

**-i**, **--input** _FILE_
> 输入的归档文件。

**-q**, **--quiet**
> 抑制输出。

# DESCRIPTION

**podman load** 从之前由 podman save 或 docker save 创建的 tar 归档中恢复容器镜像。与 podman import 不同，它会保留所有镜像层、元数据、标签和构建历史。

归档可通过 **-i** 从文件读取，或从 stdin 管道传入。这是在不使用 registry 的情况下在系统之间传输完整镜像的标准方式。

# CAVEATS

用于 podman save 创建的归档。兼容 OCI 格式。

# HISTORY

podman load 提供**镜像归档**加载功能。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [podman-save](/man/podman-save)(1), [podman-import](/man/podman-import)(1)
