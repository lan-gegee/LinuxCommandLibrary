# TAGLINE

在镜像仓库之间复制容器镜像

# TLDR

**在镜像仓库之间复制镜像**

```crane copy [source_image] [destination_image]```

**连同所有标签一起复制**

```crane copy --all-tags [source_repo] [destination_repo]```

**复制特定平台**

```crane copy --platform [linux/amd64] [source] [destination]```

# SYNOPSIS

**crane** **copy** [_options_] _source_ _destination_

# PARAMETERS

**-a**, **--all-tags**
> 复制源仓库中的所有标签。

**--platform** _platform_
> 只复制特定平台（例如 linux/amd64）。

**-n**, **--no-clobber**
> 不覆盖已存在的标签。

# DESCRIPTION

**crane copy** 在镜像仓库之间复制容器镜像，无需先拉取到本地存储。它比 docker pull/push 更高效，因为数据直接在镜像仓库之间传输。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-cp](/man/crane-cp)(1), [skopeo](/man/skopeo)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md)```

<!-- verified: 2026-06-26 -->
