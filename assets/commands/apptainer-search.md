# TAGLINE

在容器库中搜索可用的镜像。

# TLDR

**搜索**匹配查询的容器镜像

```apptainer search [query]```

搜索**特定架构**的容器镜像

```apptainer search --arch [amd64|arm64|386|ppc64le|s390x] [query]```

只搜索**已签名**的容器镜像

```apptainer search --signed [query]```

在**特定的 Container Library** 中搜索

```apptainer search --library [library_url] [query]```

# SYNOPSIS

**apptainer search** [_options_] _query_

# DESCRIPTION

**apptainer search** 向 Container Library 查询与指定搜索词匹配的可用容器镜像。结果包括镜像名称、描述和可用的标签。

默认情况下，搜索针对 Sylabs Container Library 进行。可以使用 **--library** 选项指定其他库。

# PARAMETERS

**--arch** _architecture_
> 按 CPU 架构过滤结果（默认：amd64）。

**--signed**
> 只显示带有加密签名的容器。

**--library** _url_
> 指定要搜索的其他 Container Library URI。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-pull](/man/apptainer-pull)(1), [apptainer-push](/man/apptainer-push)(1), [apptainer-delete](/man/apptainer-delete)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
