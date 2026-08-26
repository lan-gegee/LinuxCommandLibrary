# TAGLINE

将镜像保存为 tar 归档

# TLDR

**将镜像保存为 tar 归档**

```docker image save -o [image.tar] [image]```

**保存到标准输出**

```docker image save [image] > [image.tar]```

**保存多个镜像**

```docker image save -o [images.tar] [image1] [image2]```

**保存时压缩**

```docker image save [image] | gzip > [image.tar.gz]```

# SYNOPSIS

**docker** **image** **save** [_options_] _image_ [_image..._]

# PARAMETERS

**-o**, **--output** _file_
> 写入文件而不是标准输出。

# DESCRIPTION

**docker image save** 将一个或多个 Docker 镜像保存为 tar 归档，把所有镜像层、配置和元数据打包成单个文件。该命令适用于在不使用镜像仓库的情况下在系统之间传输镜像、备份重要镜像，或通过离线介质分发镜像。

生成的 tar 归档包含完整的镜像结构，包括所有文件系统层、镜像清单和配置 JSON。可以将多个镜像保存到同一个归档中，便于把相关镜像打包在一起。

输出可以通过 **-o** 重定向到文件，也可以写到标准输出，从而灵活地与 gzip 等压缩工具集成或通过网络连接传输。使用 **docker image load** 可以从这些归档中恢复镜像。

# CAVEATS

归档中以原始 tar 文件形式包含镜像的文件系统层；它与 **docker export** 的归档**并不**相同（后者会将运行中容器的文件系统平铺导出且不含历史记录）。按镜像 **ID** 而不是名称保存时，归档中不会保留任何软件仓库标签；传入 **name:tag** 才能保留它们。较新 Docker 引擎生成的归档使用 OCI 清单格式，可能无法顺利加载到非常旧的引擎中。

# HISTORY

**docker save** 自 **2013 年**起就是 Docker CLI 的一部分。在 **Docker 1.13**（2017 年 1 月）中，该子命令被重组到 **docker image** 命名空间下，同时保留了旧版简写形式作为别名。

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

[docker-save](/man/docker-save)(1), [docker-image-load](/man/docker-image-load)(1), [docker-load](/man/docker-load)(1)
