# TAGLINE

管理多平台镜像索引

# TLDR

**显示 index 的子命令**

```crane index --help```

# SYNOPSIS

**crane** **index** _subcommand_ [_options_]

# SUBCOMMANDS

**append**
> 将镜像添加到多平台索引。

**filter**
> 从索引中筛选平台。

# DESCRIPTION

**crane index** 管理多平台镜像索引（manifest list）。它允许创建和修改引用平台专属镜像的索引。

# SEE ALSO

[crane](/man/crane)(1), [crane-index-append](/man/crane-index-append)(1), [crane-index-filter](/man/crane-index-filter)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index.md)```

<!-- verified: 2026-06-26 -->
