# TAGLINE

处理 SAM/BAM/CRAM 序列比对文件

# TLDR

**查看 BAM 文件**

```samtools view [alignment.bam]```

**将 SAM 转换为 BAM**

```samtools view -b [alignment.sam] -o [alignment.bam]```

**对 BAM 文件排序**

```samtools sort [input.bam] -o [sorted.bam]```

**为 BAM 文件建立索引**

```samtools index [sorted.bam]```

**查看特定区域**

```samtools view [sorted.bam] [chr1:1000-2000]```

**统计比对数量**

```samtools view -c [alignment.bam]```

**生成统计信息**

```samtools flagstat [alignment.bam]```

**合并 BAM 文件**

```samtools merge [output.bam] [input1.bam] [input2.bam]```

# SYNOPSIS

**samtools** _command_ [_-b_] [_-o output_] [_-@ threads_] [_options_] [_file_] [_region_]

# PARAMETERS

**view**
> 查看/转换 SAM/BAM/CRAM。

**sort**
> 对比对结果排序。

**index**
> 创建 BAM 索引。

**merge**
> 合并已排序的文件。

**flagstat**
> 基于 FLAG 字段的统计。

**stats**
> 综合统计。

**idxstats**
> 按参考序列的统计。

**faidx**
> 为 FASTA 文件建立索引。

**depth**
> 计算每个位置的深度。

**mpileup**
> 生成用于变异检测的 pileup。

**coverage**
> 计算覆盖度统计。

**fastq**
> 从 BAM 提取 FASTQ。

**collate**
> 按名称打乱并分组比对记录。

**calmd**
> 重新计算 MD/NM 标签。

**-b**
> 输出 BAM 格式。

**-S**
> 输入为 SAM（已忽略，格式会自动检测）。

**-o** _FILE_
> 输出文件。

**-@** _NUM_, **--threads** _NUM_
> 线程数。

**-f** _FLAGS_
> 只保留具有 FLAGS 的读段。

**-F** _FLAGS_
> 排除具有 FLAGS 的读段。

**-q** _MAPQ_
> 最小比对质量。

**-h**
> 包含头部。

# DESCRIPTION

**samtools** 处理 SAM（Sequence Alignment/Map）格式及其二进制等价格式 BAM 中的比对数据。它是新一代测序数据分析的必备工具。

SAM/BAM 文件包含比对到参考基因组的序列读段。每条记录包括读段名称、位置、比对质量、CIGAR 字符串（比对操作）以及可选标签。

view 命令可在不同格式之间转换并过滤比对。排序并建立索引后的 BAM 文件支持对基因组区域的随机访问。大多数下游工具要求 BAM 已排序且已建索引。

统计命令（flagstat、stats、idxstats）汇总比对特征：比对率、插入片段大小、覆盖度分布。这些质量指标可指导分析决策。

pileup 输出（mpileup）聚合每个位置上的比对，用于变异检测。覆盖度命令计算各区域的读段深度。

CRAM 格式采用基于参考序列的编码，压缩率优于 BAM。Samtools 可透明地处理 CRAM。

# CAVEATS

某些操作处理大型 BAM 文件需要大量内存。多线程有帮助，但部分命令是单线程的。未排序的 BAM 会限制可用操作。随机访问需要索引。CRAM 文件需要参考序列。

# HISTORY

**samtools** 由 Wellcome Sanger 研究所的 **Heng Li** 开发，约于 **2009 年**发布。它定义了成为序列比对标准的 SAM/BAM 格式。该项目由 samtools/htslib 团队维护，是基于这些格式的更广泛生物信息学生态系统的一部分。

# INSTALL

```apt: sudo apt install samtools```

```dnf: sudo dnf install samtools```

```zypper: sudo zypper install samtools```

```brew: brew install samtools```

```nix: nix profile install nixpkgs#samtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bcftools](/man/bcftools)(1), [bwa](/man/bwa)(1), [bedtools](/man/bedtools)(1), [tabix](/man/tabix)(1)
