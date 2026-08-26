# TAGLINE

将容器镜像下载为 tar 包

# TLDR

**拉取镜像**为 tar 包

```crane pull [image:tag] [output.tar]```

**拉取特定平台**

```crane pull --platform [linux/amd64] [image:tag] [output.tar]```

# SYNOPSIS

**crane** **pull** [_options_] _image_ _output_

# PARAMETERS

**--platform** _platform_
> 拉取特定平台。

**--format** _format_
> 输出格式（tarball 或 legacy）。

# DESCRIPTION

**crane pull** 下载容器镜像并将其保存为 tar 包。该 tar 包可通过 **docker load** 导入 Docker。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-push](/man/crane-push)(1), [crane-export](/man/crane-export)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md)```

<!-- verified: 2026-06-26 -->
