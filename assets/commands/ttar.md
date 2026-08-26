# TAGLINE

用 C 编写的微型独立 tar 归档工具

# TLDR

从文件**创建归档**

```ttar c [archive.tar] [file1] [file2]```

**解压**归档

```ttar x [archive.tar]```

# SYNOPSIS

**ttar** **c** _archive.tar_ _files..._

**ttar** **x** _archive.tar_

# DESCRIPTION

**ttar**（tiny tar）是一个用独立（freestanding）C 编写的极简 tar 归档工具。它只使用原始系统调用，不依赖 libc、外部库或其他任何依赖，生成非常小的静态二进制文件（arm64 上约 2.4 KB）。它面向多种架构，包括 arm64、arm-v7、mips、riscv、x86 和 i386。

该工具只支持两种操作：从文件列表创建未压缩的 tar 归档，以及解压现有的 tar 归档。它适用于完整 **tar** 实现不可用或过于庞大的极简、嵌入式或引导（bootstrap）环境。

# PARAMETERS

**c** _archive.tar_ _files..._
> 创建包含所列文件的 _archive.tar_。

**x** _archive.tar_
> 将 _archive.tar_ 的内容解压到当前目录。

# CAVEATS

模式必须是第一个参数且只能为 **c** 或 **x**；其他任何值都会报错退出。ttar 不压缩归档，也不提供完整 tar 实现中的列出、追加或过滤选项。如需压缩，请对生成的归档使用 **gzip** 等专用压缩工具。

# HISTORY

**ttar** 的发布是为了展示一个纯 C 编写、无 libc、仅用系统调用的归档工具，强调极其精小的二进制体积。它以 GPL-3.0 许可证发布。

# SEE ALSO

[tar](/man/tar)(1), [cpio](/man/cpio)(1), [pax](/man/pax)(1), [ar](/man/ar)(1), [gzip](/man/gzip)(1)

# RESOURCES

```[Source code](https://github.com/Ferki-git-creator/ttar-tiny-tar-archivist)```

<!-- verified: 2026-06-14 -->
