# TAGLINE

面向一次写入、多次读取数据的快速解压 LZ 编解码器 CLI

# TLDR

**压缩**文件（写出 `FILE.misa77`）

```misa compress [file]```

**解压** `.misa77` 归档

```misa decompress [file.misa77]```

以**最快解码**级别**压缩**

```misa compress -l 0 [file]```

以默认的**更高压缩率**级别**压缩**

```misa compress -l 1 [file]```

为文件**建议**调优参数（写出 `FILE.misap`）

```misa suggest [file]```

使用之前建议的 **params 文件****压缩**

```misa compress --params [file.misap] [file]```

**强制覆盖**并设置输出路径

```misa compress -f -o [out.misa77] [file]```

# SYNOPSIS

**misa** **compress** | **decompress** | **suggest** [_options_] _FILE_

# DESCRIPTION

**misa** 是 **misa77** 的命令行前端。misa77 是一种基于 LZ 的无损压缩编解码器，面向一次写入、多次读取的工作负载。它优先保证极高的单线程解压吞吐量和适中的压缩比（可与高投入的 LZ4 相当），代价是较慢的压缩速度。内存占用有界：各压缩模式下最多约 5 MB，解压时几乎不占用。

该 CLI 仅处理**单个文件**（不支持目录递归或管道/流式）。归档文件为 `.misa77`；来自 `suggest` 的参数向量使用 `.misap`。压缩级别 **0** 偏重解码速度；级别 **1**（默认）在相近编码吞吐量下偏重压缩率。实验性标志如 **--adaptive**、**--params** 和 **--yolo** 提供解码优化或自动调优模式，不得相互组合，也不得与 **--level** 组合。

misa77 需要小端序 64 位系统和 C++20 工具链来构建。在项目处于 pre-1.0 阶段时流格式可能变化；无效输入被视为未定义行为，本工具属于实验性软件。

# PARAMETERS

**compress** _FILE_
> 将 _FILE_ 压缩为 _FILE_.misa77（或用 **-o** 指定路径）。

**decompress** _FILE.misa77_
> 将 misa77 归档解压回原始名称（或用 **-o** 指定路径）。

**suggest** _FILE_
> 对输入采样并写出调优参数文件（_FILE_.misap），供之后配合 **--params** 使用。

**-l** _N_, **--level** _N_
> **compress** 的压缩级别（0 = 最快解码，1 = 默认更高压缩率）。

**-o** _PATH_
> 输出路径。

**-f**
> 不提示直接覆盖已有输出。

**--adaptive**
> 为解码速度自动调优压缩（对同质数据最佳）；实验性；不可与 **--level** 组合。

**--params** _FILE.misap_
> 使用 **misa suggest** 生成的参数进行压缩；实验性；不可与 **--level** 组合。

**--yolo**
> 高投入、解码优化的实验模式；不可与 **--level** 组合。

**--tune** **loose**|**tight**
> **--adaptive** / **suggest** 的权衡取舍（类似级别 0/1；默认 loose）。

**--sample** _MB_
> 选择参数时采样的输入量（默认 2 MB）。

# CAVEATS

仅支持基于文件：目录或多文件打包请先用 **tar**（或类似工具）。格式在 0.x 版本中可能变化。解码器假定输入是有效的 misa77 数据；对损坏的流未做加固。对于解压速度比编码时间或最大压缩率更重要的冷存储和读密集型归档，优先选择 **misa**。

# SEE ALSO

[lz4](/man/lz4)(1), [zstd](/man/zstd)(1), [gzip](/man/gzip)(1), [tar](/man/tar)(1)

# RESOURCES

```[Source code](https://github.com/welcome-to-the-sunny-side/misa77)```

<!-- verified: 2026-07-15 -->
