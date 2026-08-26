# 压缩与归档

## 快速上手
在 Linux 上，归档和压缩是两个独立的步骤：**tar** 把许多文件打包成一个归档，而 **gzip**、**xz**、**zstd** 这类压缩器则缩小单一数据流。这就是为什么典型的格式是经过压缩的 tar 归档，例如 **.tar.gz** 或 **.tar.zst**。**zip** 和 **7z** 格式则用一个工具同时完成这两项工作。

## tar 归档
第一个选项告诉 **tar** 要做什么：**c** 创建、**x** 解压、**t** 列出。再加上 **f** 指定归档文件名，加 **v** 则在处理每个文件时把它打印出来。

| 选项 | 说明 |
|-----|-------------|
| **c** | 创建归档 |
| **x** | 解压归档 |
| **t** | 列出归档内容 |
| **f** | 归档文件名（此选项必须紧挨在文件名之前） |
| **v** | 详细输出：显示正在处理的文件 |
| **z** | gzip 压缩（.tar.gz） |
| **j** | bzip2 压缩（.tar.bz2） |
| **J** | xz 压缩（.tar.xz） |
| **--zstd** | zstd 压缩（.tar.zst） |
| **-C dir** | 解压前先切换到指定目录 |
| **--exclude=pattern** | 排除符合模式的文件 |

```[tar](/man/tar) czf archive.tar.gz [files]```
```[tar](/man/tar) cJf archive.tar.xz [files]```
```[tar](/man/tar) --zstd -cf archive.tar.zst [files]```
```[tar](/man/tar) czf backup.tar.gz --exclude="*.log" [directory]```

解压时，现代 GNU tar 会自动检测压缩方式，因此只用 **xf** 就能应对所有格式。
```[tar](/man/tar) xf archive.tar.gz```
```[tar](/man/tar) xf archive.tar.zst -C [directory]```

解压来自不受信任来源的归档前先列出内容；在命令中指明文件名即可只解压单个文件。
```[tar](/man/tar) tf archive.tar.gz```
```[tar](/man/tar) xf archive.tar.gz path/inside/archive.txt```

规范的归档包含一个单一的顶层目录。如果 **tar tf** 列出的是散落的文件，请用 **-C** 解压到一个全新的目录，免得弄乱当前目录。

## 选择压缩器
所有压缩器都在速度与压缩率之间取舍。经验法则是：**zstd** 是现代的默认选择，**gzip** 是普遍兼容的保底方案，**xz** 在不计时间成本时压得最紧。

| 工具 | 说明 |
|-----|-------------|
| **gzip** | 速度快，处处受支持，压缩率适中 |
| **bzip2** | 压缩率高于 gzip 但速度慢，如今多属遗留用途 |
| **xz** | 压缩率最高，压缩慢，常见于软件发布 |
| **zstd** | 非常快且压缩率接近 xz，综合最佳选择 |
| **lz4** | 极快，压缩率较低，适合实时管道 |

## 压缩单个文件
经典压缩器共用同一套接口：它们就地压缩文件并用压缩结果替换原文件，同时追加各自的扩展名。**-k** 保留原文件，**-d** 用于解压，**-1** 到 **-9** 在速度与压缩率之间取舍。
```[gzip](/man/gzip) [file]```
```[gzip](/man/gzip) -k -9 [file]```
```[bzip2](/man/bzip2) [file]```
```[xz](/man/xz) [file]```
```[zstd](/man/zstd) [file]```
```[zstd](/man/zstd) -19 [file]```

每种格式都有配套的解压工具。
```[gunzip](/man/gunzip) [file].gz```
```[bunzip2](/man/bunzip2) [file].bz2```
```[unxz](/man/unxz) [file].xz```
```[unzstd](/man/unzstd) [file].zst```

这些工具只能压缩单个文件。要压缩目录，先用 **tar** 打包，或者改用 **zip**。

在多核机器上，**xz -T0** 和 **zstd -T0** 会调用全部核心；**pigz** 是可直接替换 gzip 的并行实现。
```[xz](/man/xz) -T0 [file]```
```[pigz](/man/pigz) [file]```

## 操作压缩文件
无需解包即可读取、搜索和比较压缩的文本文件。
```[zcat](/man/zcat) [file].gz```
```[zless](/man/zless) [file].gz```
```[zgrep](/man/zgrep) "pattern" [file].gz```
```[zdiff](/man/zdiff) [file1].gz [file2].gz```

其他格式也有各自的 cat 类工具。
```[bzcat](/man/bzcat) [file].bz2```
```[xzcat](/man/xzcat) [file].xz```
```[zstdcat](/man/zstdcat) [file].zst```

## zip 归档
**zip** 是与 Windows 和 macOS 互通的标准交换格式。用 **-r** 递归纳入目录，用 **-e** 进行密码加密。
```[zip](/man/zip) -r archive.zip [directory]```
```[zip](/man/zip) -e -r secret.zip [directory]```

用 **unzip** 解压，加 **-d** 可解压到指定目录，也可以先查看内容。
```[unzip](/man/unzip) archive.zip```
```[unzip](/man/unzip) archive.zip -d [directory]```
```[unzip](/man/unzip) -l archive.zip```
```[zipinfo](/man/zipinfo) archive.zip```

zip 无法完整保留 Unix 的所有者和权限信息。做系统备份时请坚持使用 **tar**。

## 7-Zip 归档
**7z** 提供极高的压缩率和强健的 AES-256 加密。**a** 添加到归档，**x** 按完整路径解压，**l** 列出内容。
```[7z](/man/7z) a archive.7z [files]```
```[7z](/man/7z) a -p archive.7z [files]```
```[7z](/man/7z) x archive.7z```
```[7z](/man/7z) l archive.7z```

解压请用 **x** 而不是 **e**：**e** 命令会把所有文件摊平到当前目录，丢弃原有的路径结构。

## Rar 归档
Rar 是专有格式；用 **unrar** 解压。
```[unrar](/man/unrar) x archive.rar```
```[unrar](/man/unrar) l archive.rar```

## 通用解压工具
这类工具会自动识别格式，在你不想记住各格式专属参数时非常好用。
```[atool](/man/atool) -x archive.tar.gz```
```[unp](/man/unp) archive.rar```
```[dtrx](/man/dtrx) archive.zip```
```[ouch](/man/ouch) decompress archive.tar.zst```

## cpio 与 ar
**cpio** 从标准输入读取文件列表；initramfs 镜像和 RPM 软件包底层用的就是这种格式。
```[find](/man/find) . | [cpio](/man/cpio) -o > archive.cpio```
```[cpio](/man/cpio) -id < archive.cpio```

静态库（.a）和 Debian 软件包（.deb）背后的归档由 **ar** 创建。
```[ar](/man/ar) rcs libfoo.a [object-files]```
```[ar](/man/ar) t package.deb```
