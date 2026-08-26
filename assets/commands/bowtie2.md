# TAGLINE

将测序读段比对到参考基因组。

# TLDR

**将读段比对**到参考基因组

```bowtie2 -x [genome_index] -1 [reads_1.fq] -2 [reads_2.fq] -S [output.sam]```

**比对单端读段**

```bowtie2 -x [genome_index] -U [reads.fq] -S [output.sam]```

**使用多线程**加快比对速度

```bowtie2 -p [8] -x [genome_index] -1 [reads_1.fq] -2 [reads_2.fq] -S [output.sam]```

从参考基因组**构建索引**

```bowtie2-build [reference.fa] [index_base]```

以**局部**（软截断）模式比对

```bowtie2 --local -x [genome_index] -U [reads.fq] -S [output.sam]```

**高灵敏度比对**

```bowtie2 --very-sensitive -x [genome_index] -1 [r1.fq] -2 [r2.fq] -S [out.sam]```

**将未比对的读段输出**到文件

```bowtie2 -x [genome_index] -U [reads.fq] -S [output.sam] --un [unaligned.fq]```

# SYNOPSIS

**bowtie2** [_options_] **-x** _index_ {**-1** _m1_ **-2** _m2_ | **-U** _reads_} **-S** _sam_

**bowtie2-build** [_options_] _reference_ _index_base_

# DESCRIPTION

**bowtie2** 是一款快速且节省内存的工具，用于将测序读段比对到较长的参考序列。它特别擅长将约 50 到 1000 个碱基对的读段比对到人类基因组这类较大的基因组上。

Bowtie2 对参考基因组使用 FM 索引（基于 Burrows-Wheeler 变换），在保持低内存占用的同时实现快速比对。它支持有缺口（gapped）、局部（local）和双端（paired-end）比对模式。

比对结果为 SAM 格式，可由 samtools 和其他下游工具进一步处理，用于变异检测、表达分析等基因组学工作流程。

# PARAMETERS

**-x** _index_
> 索引文件名前缀（用 bowtie2-build 构建）。

**-1** _reads_
> 包含 #1 配对读段的文件，逗号分隔。

**-2** _reads_
> 包含 #2 配对读段的文件，逗号分隔。

**-U** _reads_
> 包含非配对读段的文件，逗号分隔。

**-S** _sam_
> 输出的 SAM 文件。

**-p** _threads_
> 并行线程数。

**--local**
> 局部比对模式（软截断）。

**--end-to-end**
> 端到端比对（默认）。

**--very-fast**
> 极快比对预设。

**--sensitive**
> 高灵敏度比对预设（默认）。

**--very-sensitive**
> 极高灵敏度比对预设。

**--un** _file_
> 将未比对的读段写入文件。

**--al** _file_
> 将已比对的读段写入文件。

**-q**
> 输入文件为 FASTQ（默认）。

**-f**
> 输入文件为 FASTA。

# CAVEATS

比对之前必须先用 bowtie2-build 构建索引。内存占用随基因组大小增长。very-sensitive 模式明显更慢。双端比对要求配对文件相互对应。许多下游应用需要先对输出进行排序。

# HISTORY

**Bowtie2** 由约翰斯·霍普金斯大学的 **Ben Langmead** 和 **Steven Salzberg** 开发，于 **2012 年**发表在 Nature Methods 上。它取代了初代 Bowtie 比对器，改进了对更长读段和有缺口比对的处理。Bowtie2 已成为基因组学研究中最广泛使用的比对工具之一，尤其常用于 DNA-seq 和 ChIP-seq 分析。

# INSTALL

```apt: sudo apt install bowtie2```

```dnf: sudo dnf install bowtie2```

```zypper: sudo zypper install bowtie2```

```brew: brew install bowtie2```

```nix: nix profile install nixpkgs#bowtie2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bwa](/man/bwa)(1), [samtools](/man/samtools)(1)
