# TAGLINE

CPIO 固件镜像创建工具

# TLDR

从当前目录创建 **CPIO 归档**

```create-image -o [path/to/output.cpio]```

显示**帮助**

```create-image -h```

# SYNOPSIS

**create-image** [_options_]

# DESCRIPTION

**create-image** 从当前目录创建 CPIO 镜像。它是 BlueZ 蓝牙协议栈工具的一部分，用于制作固件镜像。

该工具将目录内容打包为 CPIO 归档格式，这种格式常用于 initramfs 和固件镜像。

# PARAMETERS

**-o, --output** _file_
> 输出文件路径

**-h, --help**
> 显示帮助信息

# CAVEATS

属于 BlueZ 工具集。作用于当前目录的内容。CPIO 格式不做压缩；如有需要请单独使用 gzip。

# SEE ALSO

[cpio](/man/cpio)(1), [find](/man/find)(1)

# RESOURCES

```[Source code](https://github.com/bluez/bluez)```

<!-- verified: 2026-06-26 -->
