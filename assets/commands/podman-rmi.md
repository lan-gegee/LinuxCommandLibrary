# TAGLINE

从本地存储移除容器镜像

# TLDR

**移除一个镜像**

```podman rmi [image]```

**移除多个镜像**

```podman rmi [image1] [image2]```

**强制移除**

```podman rmi -f [image]```

**移除所有未使用的镜像**

```podman rmi -a```

# SYNOPSIS

**podman rmi** [_options_] _image_ [_image..._]

# PARAMETERS

_IMAGE_
> 要移除的镜像。

**-f**, **--force**
> 强制移除。

**-a**, **--all**
> 移除所有镜像。

**--ignore**
> 忽略不存在的镜像。

# DESCRIPTION

**podman rmi** 从本地存储中移除一个或多个容器镜像以释放磁盘空间。默认情况下，当前被容器使用的镜像无法移除。

使用 **-f**（强制）即使有容器引用也可移除镜像。**-a** 标志移除所有镜像。**--ignore** 标志静默跳过不存在的镜像而不是返回错误。

# CAVEATS

无法移除使用中的镜像。请谨慎使用 force。

# HISTORY

podman rmi 提供**移除镜像**的功能。

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

[podman](/man/podman)(1), [podman-images](/man/podman-images)(1), [podman-rm](/man/podman-rm)(1)
