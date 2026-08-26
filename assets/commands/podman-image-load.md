# TAGLINE

从 tar 归档加载容器镜像

# TLDR

**从归档加载镜像**

```podman image load -i [image.tar]```

**从 stdin 加载**

```cat [image.tar] | podman image load```

**安静模式加载**

```podman image load -q -i [image.tar]```

# SYNOPSIS

**podman** **image** **load** [_options_]

# PARAMETERS

**-i**, **--input** _file_
> 从归档文件读取。

**-q**, **--quiet**
> 抑制输出。

# DESCRIPTION

**podman image load** 从由 podman save 或 docker save 创建的 tar 归档中加载镜像。恢复镜像时包括所有层和元数据。适用于在系统之间传输镜像。

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

[podman](/man/podman)(1), [podman-save](/man/podman-save)(1)
