# TAGLINE

获取镜像的内容摘要

# TLDR

**获取镜像的摘要**

```crane digest [image:tag]```

**获取特定平台的摘要**

```crane digest --platform [linux/amd64] [image:tag]```

# SYNOPSIS

**crane** **digest** [_options_] _image_

# PARAMETERS

**--platform** _platform_
> 获取特定平台的摘要。

**--full-ref**
> 打印带摘要的完整镜像引用。

**--tarball** _path_
> 包含该镜像的 tar 包路径。

# DESCRIPTION

**crane digest** 获取容器镜像的内容寻址摘要（SHA256）。无论标签如何变化，摘要都能唯一标识镜像内容。

# SEE ALSO

[crane](/man/crane)(1), [crane-manifest](/man/crane-manifest)(1)
