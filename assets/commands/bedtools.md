# TAGLINE

分析和操作基因组区间数据

# TLDR

对基因组区间**求交集**

```bedtools intersect -a [file1.bed] -b [file2.bed]```

**合并**重叠区间

```bedtools merge -i [sorted.bed]```

**排序** BED 文件

```bedtools sort -i [unsorted.bed]```

**计算覆盖度**

```bedtools coverage -a [regions.bed] -b [reads.bam]```

**减去**区间

```bedtools subtract -a [all.bed] -b [exclude.bed]```

**查找最近的**特征

```bedtools closest -a [query.bed] -b [reference.bed]```

为区间**提取 FASTA 序列**

```bedtools getfasta -fi [genome.fa] -bed [regions.bed]```

# SYNOPSIS

**bedtools** _command_ [_options_]

# DESCRIPTION

**bedtools** 是一套用于分析 BED、BAM、VCF 和 GFF 格式基因组区间的实用工具集。它提供针对基因组注释的快速操作，包括交集、合并、计数和统计分析。

该工具是基因组学研究和基因组特征比较分析的必备工具。

# COMMANDS

**intersect**
> 查找重叠区间

**merge**
> 合并重叠区间

**coverage**
> 计算覆盖度统计

**subtract**
> 移除重叠区间

**closest**
> 查找最近的区间

**window**
> 在窗口范围内查找邻近区间

**sort**
> 排序 BED/GFF/VCF 文件

**genomecov**
> 计算全基因组覆盖度

**getfasta**
> 从 FASTA 提取序列

**bamtobed**
> 将 BAM 转换为 BED

**slop**
> 将区间扩展指定的碱基数

**flank**
> 为每个特征创建侧翼区间

**complement**
> 返回未被特征覆盖的区间

# COMMON PARAMETERS

**-a** _file_
> 第一个输入文件

**-b** _file_
> 第二个输入文件

**-wa**
> 输出原始 A 条目

**-wb**
> 输出原始 B 条目

**-f** _fraction_
> 最小重叠比例

**-v**
> 报告与 B 无重叠的 A 条目

**-s**
> 要求位于同一条链上

**-S**
> 要求位于相反的链上

**-sorted**
> 对大文件使用已排序算法（内存占用更低）

**-i** _file_
> 输入文件（merge、sort 等子命令使用）

# WORKFLOW

```bash
# Find genes overlapping SNPs
bedtools intersect -a genes.bed -b snps.bed

# Merge nearby features
bedtools merge -i features.bed -d 100

# Count reads in regions
bedtools coverage -a regions.bed -b reads.bam

# Extract promoter regions
bedtools flank -i genes.bed -g genome.txt -l 2000 -r 0
```

# CAVEATS

某些操作要求输入已排序。大文件会占用大量内存。坐标系差异（0-based 与 1-based）可能导致差一错误。性能取决于文件大小和具体操作。

# HISTORY

**bedtools** 由 Aaron Quinlan 和 Ira Hall 创建，于 **2010** 年首次发布，是一套功能全面的基因组区间分析工具箱。

# INSTALL

```apt: sudo apt install bedtools```

```aur: yay -S bedtools```

```brew: brew install bedtools```

```nix: nix profile install nixpkgs#bedtools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[samtools](/man/samtools)(1), [vcftools](/man/vcftools)(1), [bcftools](/man/bcftools)(1)
