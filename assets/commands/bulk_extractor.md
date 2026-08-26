# TAGLINE

高性能数字取证数据提取工具

# TLDR

**从磁盘镜像中提取数据**

```bulk_extractor -o [output_dir] [image.dd]```

**使用多线程扫描**

```bulk_extractor -o [output_dir] -j [8] [image.dd]```

**启用指定扫描器**

```bulk_extractor -o [output_dir] -e [exif] [image.dd]```

**禁用指定扫描器**

```bulk_extractor -o [output_dir] -x [email] [image.dd]```

**扫描指定字节范围**

```bulk_extractor -o [output_dir] -Y [0-1000000000] [image.dd]```

**递归扫描目录**

```bulk_extractor -o [output_dir] -R [directory]```

**搜索特定模式**

```bulk_extractor -o [output_dir] -f "[pattern]" [image.dd]```

**列出可用的扫描器**

```bulk_extractor -H```

# SYNOPSIS

**bulk_extractor** [_options_] _image_

# DESCRIPTION

**bulk_extractor** 是一款高性能数字取证工具，可扫描磁盘镜像、文件或目录，在不解析文件系统结构的情况下提取结构化信息。它直接从原始数据流中提取电子邮件地址、信用卡号、URL、EXIF 元数据等痕迹。

该工具可在多个 CPU 核心上并行处理数据，速度显著快于传统取证工具。它处理的是原始字节而非文件系统元数据，因此能够在未分配空间、slack space 以及压缩或编码内容中发现数据。每个扫描器插件会在输出目录生成单独的特征文件，便于对结果进行过滤和分析。

# PARAMETERS

**-o** _directory_
> 输出目录（必需）

**-e** _scanner_
> 启用指定扫描器

**-x** _scanner_
> 禁用指定扫描器

**-j** _threads_
> 使用的线程数

**-G** _bytes_
> 页大小（默认：16777216）

**-M** _depth_
> 最大递归深度（默认：7）

**-R**
> 递归扫描目录

**-f** _pattern_
> 搜索特定模式

**-F** _file_
> 从文件读取模式

**-Y** _start-end_
> 扫描指定字节范围

**-z** _pagestart_
> 从指定的页码开始处理

**-Z**
> 开始前清空输出目录

**-q**
> 静默模式（不输出状态信息）

**-H**
> 列出可用扫描器及其说明

# OUTPUT

生成包含本次运行的数字取证 XML 元数据的 **report.xml**。各个特征文件包含提取出的不同类型数据（emails.txt、ccn.txt、urls.txt 等）。

# CAVEATS

输出目录必须不存在，或者用 -Z 清空。处理大型镜像时，输出需要大量磁盘空间。某些扫描器可能产生误报，需要人工复核。

# HISTORY

**bulk_extractor** 由海军研究生院的 **Simson Garfinkel** 创建，于 **2011 年**前后首次发布。它被广泛用于执法和事件响应中的取证数据提取。

# INSTALL

```zypper: sudo zypper install bulk_extractor```

```brew: brew install bulk_extractor```

```nix: nix profile install nixpkgs#bulk_extractor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foremost](/man/foremost)(1), [scalpel](/man/scalpel)(1), [strings](/man/strings)(1), [photorec](/man/photorec)(1)
