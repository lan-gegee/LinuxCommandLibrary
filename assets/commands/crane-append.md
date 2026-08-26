# TAGLINE

向容器镜像添加层

# TLDR

**向已有镜像追加一个层**

```crane append -b [base_image] -f [layer.tar.gz] -t [new_image:tag]```

**从文件追加**

```crane append --base [gcr.io/project/image] --new_layer [layer.tar] --new_tag [gcr.io/project/image:v2]```

# SYNOPSIS

**crane** **append** [_options_]

# PARAMETERS

**-b**, **--base** _image_
> 要追加到的基础镜像。

**-f**, **--new_layer** _file_
> 要追加的层的 tar 包。

**-t**, **--new_tag** _image_
> 结果镜像的标签。

# DESCRIPTION

**crane append** 无需拉取整个镜像即可向现有容器镜像添加新层。这对于高效地向现有镜像添加文件或配置非常有用。

属于用于容器镜像仓库操作的 crane CLI 工具的一部分。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-mutate](/man/crane-mutate)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md)```

<!-- verified: 2026-06-23 -->
