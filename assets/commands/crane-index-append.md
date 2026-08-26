# TAGLINE

向清单索引添加镜像

# TLDR

**向索引添加镜像**

```crane index append -t [index:tag] -m [image:tag]```

**用多个镜像创建新索引**

```crane index append -t [index:tag] -m [linux/amd64:tag] -m [linux/arm64:tag]```

# SYNOPSIS

**crane** **index** **append** [_options_]

# PARAMETERS

**-t**, **--tag** _tag_
> 结果索引的标签。

**-m**, **--manifest** _image_
> 要添加到索引的镜像（可重复指定）。

# DESCRIPTION

**crane index append** 将镜像添加到多平台清单索引。这会创建或更新一个索引，使拉取时能够自动选择对应平台的镜像。

# SEE ALSO

[crane](/man/crane)(1), [crane-index](/man/crane-index)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md)```

<!-- verified: 2026-06-26 -->
