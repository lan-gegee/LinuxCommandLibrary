# TAGLINE

为已有镜像添加标签别名

# TLDR

**为镜像添加标签**

```crane tag [image:existing] [new_tag]```

**按摘要打标签**

```crane tag [image]@[sha256:abc...] [tag_name]```

# SYNOPSIS

**crane** **tag** [_options_] _image_ _tag_

# DESCRIPTION

**crane tag** 为已有镜像添加新标签。这会创建一个别名，而无需复制镜像数据。

# SEE ALSO

[crane](/man/crane)(1), [crane-copy](/man/crane-copy)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md)```

<!-- verified: 2026-06-26 -->
