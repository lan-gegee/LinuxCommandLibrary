# TAGLINE

列出所有 Distrobox 容器

# TLDR

**列出**所有 Distrobox 容器

```distrobox-list```

以**详细信息**列出

```distrobox-list -v```

# SYNOPSIS

**distrobox-list** [_options_]

# DESCRIPTION

**distrobox-list** 列出所有 Distrobox 容器。Distrobox 容器会与普通的 Podman 或 Docker 容器分开显示。

输出内容包括容器名称、状态以及使用的镜像。

# PARAMETERS

**-v, --verbose**
> 显示详细信息

# CAVEATS

只显示由 Distrobox 创建的容器，不包括普通 Docker/Podman 容器。

# INSTALL

```dnf: sudo dnf install distrobox```

```pacman: sudo pacman -S distrobox```

```apk: sudo apk add distrobox```

```zypper: sudo zypper install distrobox```

```brew: brew install distrobox```

```nix: nix profile install nixpkgs#distrobox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distrobox](/man/distrobox)(1), [distrobox-create](/man/distrobox-create)(1), [podman](/man/podman)(1)

# RESOURCES

```[Source code](https://github.com/89luca89/distrobox)```

```[Homepage](https://distrobox.it/)```

<!-- verified: 2026-07-11 -->
