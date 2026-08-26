# TAGLINE

面向 DNA 和 RNA 序列的多功能序列比对工具

# TLDR

**将长读长比对到参考序列**

```minimap2 -a [reference.fa] [reads.fq] > [aligned.sam]```

**使用 ONT 读长预设进行比对**

```minimap2 -ax map-ont [reference.fa] [ont_reads.fq] > [aligned.sam]```

**比对 PacBio HiFi 读长**

```minimap2 -ax map-hifi [reference.fa] [hifi.fq] > [aligned.sam]```

**比对短读长**

```minimap2 -ax sr [reference.fa] [reads_1.fq] [reads_2.fq] > [aligned.sam]```

**创建索引**

```minimap2 -d [reference.mmi] [reference.fa]```

**使用多线程**

```minimap2 -t [8] -ax map-ont [reference.fa] [reads.fq] > [aligned.sam]```

# SYNOPSIS

**minimap2** [_options_] _target_ [_query_...]

# PARAMETERS

**-a**
> 输出 SAM 格式。

**-x** _preset_
> 预设（map-ont、map-pb、map-hifi、sr、asm5）。

**-t** _threads_
> 线程数。

**-d** _file_
> 将索引保存到文件。

**-o** _file_
> 输出文件。

**-k** _k_
> K-mer 大小。

**-w** _w_
> Minimizer 窗口大小。

# DESCRIPTION

**minimap2** 是一款面向 DNA 和 RNA 序列的多功能序列比对工具。它可以比对来自 PacBio 或 Oxford Nanopore 的长读长、短读长，甚至整个组装结果。

minimap2 极其快速且节省内存，已成为长读长比对的标准工具。

# PRESETS

```
map-ont   - ONT reads to reference
map-hifi  - PacBio HiFi reads
map-pb    - PacBio CLR reads
sr        - Short reads
asm5      - Divergent assembly
splice    - Long-read RNA-seq
```

# CAVEATS

默认输出 PAF；使用 -a 输出 SAM。索引大小取决于参考序列。预设应与数据类型匹配。

# HISTORY

minimap2 由 **Heng Li**（BWA 作者）开发，于 **2018 年**发表，作为快速精确的长读长比对工具。

# INSTALL

```apt: sudo apt install minimap2```

```brew: brew install minimap2```

```nix: nix profile install nixpkgs#minimap2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bwa](/man/bwa)(1), [samtools](/man/samtools)(1)
