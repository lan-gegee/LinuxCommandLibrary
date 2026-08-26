# TAGLINE

在分区内创建压缩 ROM 文件系统

# TLDR

从目录创建 **cramfs**

```sudo mkfs.cramfs [path/to/directory] /dev/sdXY```

创建带**卷名**的 cramfs

```sudo mkfs.cramfs -n [volume_name] [path/to/directory] /dev/sdXY```

# SYNOPSIS

**mkfs.cramfs** [_options_] _directory_ _device_

# DESCRIPTION

**mkfs.cramfs** 在分区内创建压缩 ROM 文件系统（cramfs）。Cramfs 是一种简单的只读文件系统，专为小型嵌入式系统和启动 ROM 设计。

# PARAMETERS

**-n NAME**
> 设置卷名（最长 16 个字符）

**-E**
> 将警告视为错误

**-e EDITION**
> 设置版本号

**-b BLOCKSIZE**
> 块大小（默认：PAGE_SIZE）

**-s, --sortbyname**
> 按名称对目录项排序

# CAVEATS

只读文件系统。单文件最大 16MB，文件系统最大 256MB。专为嵌入式用途设计。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [mount](/man/mount)(8)
