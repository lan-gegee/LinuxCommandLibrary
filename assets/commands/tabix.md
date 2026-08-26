# TAGLINE

基因组位置文件索引器

# TLDR

为 VCF 文件建立**索引**

```tabix -p vcf [file.vcf.gz]```

为 BED 文件建立**索引**

```tabix -p bed [file.bed.gz]```

为 GFF 文件建立**索引**

```tabix -p gff [file.gff.gz]```

**查询某个区域**

```tabix [file.vcf.gz] [chr1:1000000-2000000]```

输出时包含头部的**查询**

```tabix -h [file.vcf.gz] [chr1:1000000-2000000]```

**列出**索引中的染色体

```tabix -l [file.vcf.gz]```

从文件读取区域进行**查询**

```tabix -R [regions.bed] [file.vcf.gz]```

为大染色体**创建 CSI 索引**

```tabix -C -p vcf [file.vcf.gz]```

# SYNOPSIS

**tabix** [_options_] _file_ [_region_...]

# PARAMETERS

**-p**, **--preset** _format_
> 输入格式预设：gff、bed、sam、vcf。

**-s**, **--sequence** _col_
> 序列名称所在列（默认：1）。

**-b**, **--begin** _col_
> 起始位置所在列（默认：4）。

**-e**, **--end** _col_
> 结束位置所在列（默认：5）。

**-S**, **--skip-lines** _n_
> 跳过前 n 行。

**-c**, **--comment** _char_
> 跳过以此字符开头的行（默认：#）。

**-0**, **--zero-based**
> 位置采用 0 起始的半开区间。

**-C**, **--csi**
> 创建 CSI 索引而非 TBI。

**-f**, **--force**
> 覆盖已有索引。

**-h**, **--print-header**
> 输出时打印头部行。

**-H**, **--only-header**
> 只打印头部/元信息行。

**-l**, **--list-chroms**
> 列出索引文件中存储的序列名称。

**-r**, **--reheader** _file_
> 用 file 的内容替换头部。

**-R**, **--regions** _file_
> 从 BED 或 TAB 分隔的文件中读取查询区域。

**-T**, **--targets** _file_
> 与 -R 类似，但按顺序读取输入。

**-m**, **--min-shift** _INT_
> 将 CSI 索引的最小区间大小设为 2^INT（默认：14）。

**-D**
> 打开前不下载索引文件（仅限远程文件）。

**--separate-regions**
> 在输出的每个分组前插入区域名称。

**--cache** _INT_
> 设置 BGZF 块缓存大小，单位 MB（默认：10）。

# DESCRIPTION

**tabix** 是一个针对 TAB 分隔的基因组位置文件的通用索引器。它创建的索引可以快速检索与指定基因组区域重叠的数据行。

输入文件必须按位置排序并用 **bgzip** 压缩。索引文件（.tbi 或 .csi）支持对压缩数据的随机访问，无需解压整个文件。

常见用途包括为 VCF 变异文件、BED 注释文件和 GFF/GTF 基因注释文件建立索引。在生物信息学流程中处理大型基因组数据集时，该工具必不可少。

区域查询使用 1 起始的闭区间坐标，格式为 chr:start-end。

# CAVEATS

输入必须用 bgzip 压缩，而不是 gzip。TBI 索引格式支持的染色体最长 512 Mbp；更大的请使用 CSI（-C）。预设选项不能与手动指定的列参数组合使用。索引中保存了列设置，因此检索时无需再指定格式。

# HISTORY

**tabix** 由李恒（Heng Li）开发，2011 年发表于 Bioinformatics 期刊。现属于由 samtools/htslib 团队维护的 HTSlib 项目。该工具已成为基因组学工作流中高效数据访问的标准组件。

# INSTALL

```apt: sudo apt install tabix```

```zypper: sudo zypper install tabix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bgzip](/man/bgzip)(1), [bcftools](/man/bcftools)(1), [samtools](/man/samtools)(1), [vcftools](/man/vcftools)(1)
