# TAGLINE

将 DNA 序列比对到参考基因组

# TLDR

为参考基因组建立**索引**

```bwa index [path/to/reference.fa]```

将**单端读段**比对到已建立索引的基因组

```bwa mem -t 32 [path/to/reference.fa] [path/to/read.fq.gz] | gzip > [path/to/alignment.sam.gz]```

将**双端读段**比对到已建立索引的基因组

```bwa mem -t 32 [path/to/reference.fa] [path/to/read_1.fq.gz] [path/to/read_2.fq.gz] | gzip > [path/to/alignment.sam.gz]```

以 **Picard 兼容模式**比对（将较短的分裂比对标记为 secondary）

```bwa mem -M -t 32 [path/to/reference.fa] [path/to/read_1.fq.gz] [path/to/read_2.fq.gz] | gzip > [path/to/alignment.sam.gz]```

比对时**附加 FASTA/Q 注释**

```bwa mem -C -t 32 [path/to/reference.fa] [path/to/read_1.fq.gz] [path/to/read_2.fq.gz] | gzip > [path/to/alignment.sam.gz]```

# SYNOPSIS

**bwa** _command_ [_options_] [_arguments_]

# DESCRIPTION

**bwa**（Burrows-Wheeler Aligner）是一个软件包，用于将低差异的 DNA 序列比对到大型参考基因组（例如人类基因组）。它使用 Burrows-Wheeler 变换来构建参考索引。

**mem** 算法被推荐用于大多数应用，支持 70bp 到数兆碱基的读段，并提供准确的比对结果。

# SUBCOMMANDS

**index**
> 从参考基因组构建索引

**mem**
> 使用 BWA-MEM 算法比对读段

**aln**
> 比对读段（较旧的算法）

**samse/sampe**
> 从 aln 输出生成 SAM

# PARAMETERS

**-t** _threads_
> CPU 线程数

**-M**
> 将较短的分裂比对标记为 secondary（与 Picard 兼容）

**-C**
> 将 FASTA/Q 注释附加到输出

**-R** _string_
> 读组（read group）头行

**-o** _file_
> 输出文件名

# CAVEATS

为大型基因组建立索引需要大量内存和时间。默认输出未压缩的 SAM；存储时建议通过 gzip 管道处理。结果质量取决于读段质量和参考基因组的完整性。

# HISTORY

**BWA** 由 Heng Li 开发，于 **2009 年**首次发表。MEM 算法在 **2013 年**推出，此后成为大多数比对任务的首选方法。

# INSTALL

```apt: sudo apt install bwa```

```dnf: sudo dnf install bwa```

```brew: brew install bwa```

```nix: nix profile install nixpkgs#bwa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[samtools](/man/samtools)(1), [bowtie2](/man/bowtie2)(1), [minimap2](/man/minimap2)(1)

# RESOURCES

```[Source code](https://github.com/lh3/bwa)```

```[Homepage](https://bio-bwa.sourceforge.net/)```

<!-- verified: 2026-06-22 -->
