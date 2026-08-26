# TAGLINE

校验容器镜像的结构

# TLDR

**校验远程镜像**

```crane validate --remote [image:tag]```

**校验本地 tar 包**

```crane validate --tarball [image.tar]```

# SYNOPSIS

**crane** **validate** [_options_]

# PARAMETERS

**--remote** _image_
> 校验远程镜像。

**--tarball** _file_
> 校验本地 tar 包。

# DESCRIPTION

**crane validate** 检查容器镜像是否格式良好。它会验证清单结构、层摘要以及配置的有效性。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-manifest](/man/crane-manifest)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md)```

<!-- verified: 2026-06-26 -->
