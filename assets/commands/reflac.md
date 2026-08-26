# TAGLINE

重新编码 FLAC 音频文件

# TLDR

**重新编码 FLAC 文件**

```reflac [path/to/music]```

**最大压缩**

```reflac -8 [path/to/music]```

**编码后校验**

```reflac --verify [path/to/music]```

**保留文件时间**

```reflac --preserve-modtime [path/to/music]```

**试运行**

```reflac --dry-run [path/to/music]```

**递归处理**

```reflac -r [path/to/directory]```

# SYNOPSIS

**reflac** [_-0..-8_] [_--verify_] [_options_] _path_

# PARAMETERS

**-0** to **-8**
> 压缩级别。

**--verify**
> 编码后校验。

**--preserve-modtime**
> 保留文件时间。

**--dry-run**
> 显示将要执行的操作。

**-r**, **--recursive**
> 处理子目录。

**-j** _N_
> 并行任务数。

# DESCRIPTION

**reflac** 是一款批处理工具，用于以更新后的压缩设置重新编码 FLAC 音频文件。它递归处理 FLAC 文件目录，应用指定的压缩级别，同时保留所有元数据标签，确保处理过程中不丢失任何音频数据。

该工具通过 **-j** 选项支持并行处理，可显著加快大型音乐库的处理速度。压缩级别从 **-0**（最快）到 **-8**（文件最小），与标准 FLAC 编码器选项一致。**--verify** 标志会解码每个重新编码的文件并与原始音频数据比较，从而启用完整性检查。

当你想将使用旧版或欠佳压缩设置编码的 FLAC 集合升级，以利用新版 FLAC 改进的编码时，该工具尤为有用——可在毫无音质损失的情况下降低存储需求。

# CAVEATS

需要 FLAC 编码器。高级别下 CPU 占用高。不可能提升音质。

# HISTORY

**reflac** 的创建目的是在保留所有元数据的前提下，用现代压缩设置批量重新编码 FLAC 文件。

# INSTALL

```aur: yay -S reflac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flac](/man/flac)(1), [metaflac](/man/metaflac)(1), [sox](/man/sox)(1)
