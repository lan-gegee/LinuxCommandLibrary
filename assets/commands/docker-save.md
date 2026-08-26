# TAGLINE

将 Docker 镜像保存为 tar 归档

# TLDR

**将镜像保存为 tar 文件**

```docker save -o [image.tar] [image]```

**保存到标准输出**

```docker save [image] > [image.tar]```

**保存时压缩**

```docker save [image] | gzip > [image.tar.gz]```

**保存多个镜像**

```docker save -o [images.tar] [image1] [image2]```

**保存指定标签**

```docker save -o [image.tar] [image]:[tag]```

**保存特定平台变体**

```docker save --platform [linux/amd64] -o [image.tar] [image]```

# SYNOPSIS

**docker** **save** [_options_] _image_ [_image..._]

# PARAMETERS

**-o**, **--output** _file_
> 写入文件而不是标准输出。

**--platform** _os[/arch[/variant]]_
> 保存特定平台变体。默认保存镜像存储中存在的所有平台变体。

# DESCRIPTION

**docker save** 将一个或多个镜像保存为 tar 归档，包括所有父层、标签和版本。使用 docker load 可将其恢复。该命令适用于离线分发、备份镜像，或在无需镜像仓库的情况下在系统之间传输镜像。生成的归档保留完整的镜像及其所有元数据和历史记录。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-image-save](/man/docker-image-save)(1), [docker-load](/man/docker-load)(1), [docker-image](/man/docker-image)(1)
