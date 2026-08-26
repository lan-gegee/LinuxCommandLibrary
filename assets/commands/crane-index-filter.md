# TAGLINE

从容器镜像清单索引中筛选平台

# TLDR

**筛选索引，仅保留 linux/amd64**

```crane index filter [image] --platform linux/amd64```

**筛选出多个平台并为结果打标签**

```crane index filter [image] --platform linux/amd64 --platform linux/arm64 -t [registry/image:tag]```

**筛选并显示详细输出**

```crane index filter [image] --platform [linux/amd64] -v```

**筛选时允许不安全的镜像仓库**

```crane index filter [image] --platform [linux/arm64] --insecure -t [registry/image:filtered]```

# SYNOPSIS

**crane** **index** **filter** [_options_] _image_

# PARAMETERS

**--platform** _platform_
> 要保留的平台，格式为 os/arch[/variant][:osversion]。可多次指定。

**-t**, **--tag** _tag_
> 应用于筛选结果镜像的标签。

**--insecure**
> 允许在不使用 TLS 的情况下获取镜像引用。

**--allow-nondistributable-artifacts**
> 允许推送不可分发（foreign）的层。

**-v**, **--verbose**
> 启用调试日志。

**-h**, **--help**
> 显示 filter 命令的帮助信息。

# DESCRIPTION

**crane index filter** 通过移除与指定 **--platform** 标志不匹配的平台来修改远程的多平台镜像索引。结果是一个仅包含所选架构与操作系统组合的新索引。

这有助于减小多架构镜像索引的体积、创建平台专用的发行版本，或者在推送到镜像仓库之前移除不需要的平台。

**--platform** 标志采用 **os/arch[/variant][:osversion]** 格式，例如 `linux/amd64`、`linux/arm64` 或 `linux/arm/v7`。

# SEE ALSO

[crane](/man/crane)(1), [crane-index](/man/crane-index)(1), [crane-index-append](/man/crane-index-append)(1), [crane-manifest](/man/crane-manifest)(1), [crane-push](/man/crane-push)(1)
