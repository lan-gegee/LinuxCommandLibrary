# TAGLINE

从 squashfs 提取文件到 stdout

# TLDR

显示 squashfs 中**文件**的内容

```sqfscat [filesystem.squashfs] [file1] [file2]```

使用**多处理器**

```sqfscat -p [num_processors] [filesystem.squashfs] [file]```

设置缓存的**内存限制**

```sqfscat -mem [512M] [filesystem.squashfs] [file]```

跳过文件系统开头的 **offset** 个字节

```sqfscat -o [bytes] [filesystem.squashfs] [file]```

忽略**写入错误**

```sqfscat -ig [filesystem.squashfs] [file]```

# SYNOPSIS

**sqfscat** [_OPTIONS_] _FILESYSTEM_ [_files_...]

# PARAMETERS

**-v, -version**
> 显示版本和版权信息

**-p, -processors** _number_
> 用于解压的处理器数量

**-mem** _size_
> 缓存内存大小（支持 K/M/G 后缀；默认：512MB）

**-mem-percent** _percent_
> 以物理内存的百分比设置缓存

**-o, -offset** _bytes_
> 跳过文件系统开头的字节数

**-ig, -ignore-errors**
> 将写入错误视为非致命错误

**-st, -strict-errors**
> 将所有错误视为致命错误

**-no-exit, -no-exit-code**
> 非致命错误时不设置非零退出码

**-no-wild, -no-wildcards**
> 禁用文件名通配符匹配

**-r, -regex**
> 将文件名视为 POSIX 正则表达式

**-h, -help**
> 显示帮助摘要

# DESCRIPTION

**sqfscat** 将 squashfs 文件系统中文件的内容输出到 stdout，类似于 **cat** 在普通文件系统上的工作方式。Squashfs 是一种高压缩比的只读文件系统，支持 gzip、xz、lzo、lz4、zstd 和 lzma 压缩。

该工具无需挂载文件系统即可提取文件内容，适用于检查、脚本编写和嵌入式系统。可以指定多个文件，其内容会被依次拼接输出。

# EXIT STATUS

**0**：操作成功
**1**：致命错误（数据损坏、I/O 失败）
**2**：非致命错误（无效的文件类型、路径解析问题）

# CAVEATS

仅适用于 squashfs 文件系统。squashfs 内的文件路径相对于其根目录。大文件解压可能需要大量内存。仅提供只读访问。

# HISTORY

**sqfscat** 是 **squashfs-tools** 的一部分，由 **Phillip Lougher** 自 **2002 年**起创建。Squashfs 于 **2.6.29** 版（2009 年）被合并进 Linux 内核主线。这些工具已发展为支持多种压缩算法，并广泛应用于 Live CD、容器镜像和嵌入式系统。

# INSTALL

```apt: sudo apt install squashfs-tools```

```dnf: sudo dnf install squashfs-tools```

```pacman: sudo pacman -S squashfs-tools```

```apk: sudo apk add squashfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unsquashfs](/man/unsquashfs)(1), [mksquashfs](/man/mksquashfs)(1), [sqfstar](/man/sqfstar)(1)
