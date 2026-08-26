# TAGLINE

垃圾回收无标签的镜像

# TLDR

**垃圾回收无标签的镜像**

```gcrane gc [gcr.io/project/repo]```

**试运行**

```gcrane gc --dry-run [gcr.io/project/repo]```

**带宽限期进行垃圾回收**

```gcrane gc --grace [24h] [gcr.io/project/repo]```

# SYNOPSIS

**gcrane** **gc** [_options_] _repository_

# PARAMETERS

**--dry-run**
> 显示将被删除的内容。

**--grace** _duration_
> 保留比指定时长更新的镜像。

# DESCRIPTION

**gcrane gc** 在 Google Container Registry 或 Artifact Registry 中找出可作为垃圾回收候选的无标签容器镜像。这些孤立镜像通常由重新打标签或删除标签产生，留下占用存储空间的未被引用的清单（manifest）。

该命令列出没有关联标签的镜像摘要（digest）。它不会直接删除镜像；输出应通过管道传给 gcrane delete 来实际执行删除。宽限期选项可保护最近创建的镜像不被误删。试运行模式在不做任何更改的情况下显示将被删除的内容，便于在清理前安全预览。

# INSTALL

```zypper: sudo zypper install gcrane```

```nix: nix profile install nixpkgs#gcrane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcrane](/man/gcrane)(1), [gcrane-ls](/man/gcrane-ls)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

<!-- verified: 2026-07-15 -->
