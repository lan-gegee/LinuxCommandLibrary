# TAGLINE

多线程 zstd 压缩

# TLDR

**多线程压缩**

```zstdmt [file]```

**指定线程数压缩**

```zstdmt -T[4] [file]```

**多线程解压**

```zstdmt -d [file.zst]```

**最大压缩**

```zstdmt -19 [file]```

# SYNOPSIS

**zstdmt** [_options_] [_files_...]

# PARAMETERS

**-T** _n_
> 线程数（0 = 自动）。

**-d**
> 解压。

**-1** to **-19**
> 压缩级别。

**--ultra**
> 启用极限模式（级别 20-22）。

**-k**, **--keep**
> 保留源文件（压缩后不删除）。

**-c**, **--stdout**
> 写入标准输出。

**-o** _FILE_
> 将输出写入 FILE。

**-f**, **--force**
> 不提示直接覆盖输出。

**--rm**
> 操作成功后删除源文件。

**-r**
> 递归处理目录。

**--long**[=_WINDOWLOG_]
> 启用长距离匹配模式以提升压缩比。

**-B** _SIZE_
> 设置任务块大小（每个线程处理该大小的数据块）。

**--rsyncable**
> 生成对 rsync 友好的压缩输出。

# DESCRIPTION

**zstdmt** 是 zstd 压缩工具的多线程变体。它会自动调用所有可用的 CPU 核心进行压缩，等同于运行 **zstd -T0**，在多核系统上吞吐量显著更高。

其压缩输出与标准 zstd 文件完全兼容，任何支持 zstd 的工具都能解压。压缩级别、解压和文件处理等所有标准 zstd 选项均受支持。

线程数可通过 **ZSTD_NBTHREADS** 环境变量设置。使用 **-T0** 时采用检测到的物理 CPU 核心数，在 64 位系统上以 256 为上限。

# INSTALL

```apt: sudo apt install zstd```

```dnf: sudo dnf install zstd```

```pacman: sudo pacman -S zstd```

```apk: sudo apk add zstd```

```zypper: sudo zypper install zstd```

```brew: brew install zstd```

```nix: nix profile install nixpkgs#zstd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zstd](/man/zstd)(1), [zstdcat](/man/zstdcat)(1), [unzstd](/man/unzstd)(1)
