# TAGLINE

变异检测与 VCF/BCF 文件处理

# TLDR

**查看 VCF/BCF 文件**

```bcftools view [input.vcf.gz]```

**按区域过滤变异**

```bcftools view -r [chr1:1000000-2000000] [input.vcf.gz]```

**将 VCF 转换为 BCF**

```bcftools view -Ob -o [output.bcf] [input.vcf.gz]```

从比对后的读段**检测变异**

```bcftools mpileup -f [reference.fa] [aligned.bam] | bcftools call -mv -Oz -o [calls.vcf.gz]```

**合并多个 VCF 文件**

```bcftools merge [file1.vcf.gz] [file2.vcf.gz] -Oz -o [merged.vcf.gz]```

**按质量过滤变异**

```bcftools filter -i 'QUAL>30 && DP>10' [input.vcf.gz] -Oz -o [filtered.vcf.gz]```

**提取样本基因型**

```bcftools query -f '%CHROM\t%POS\t%REF\t%ALT[\t%GT]\n' [input.vcf.gz]```

**为 VCF/BCF 文件建立索引**

```bcftools index [input.vcf.gz]```

# SYNOPSIS

**bcftools** _subcommand_ [_options_] [_file_]

# DESCRIPTION

**bcftools** 是一套用于变异检测和处理 Variant Call Format（VCF）及其二进制格式 BCF 文件的实用工具集。它属于 SAMtools/HTSlib 项目，在生物信息学的基因组变异分析中应用广泛。

所有命令都能透明地处理 VCF 和 BCF 文件，无论是否压缩。这些工具专为管道化工作流设计，从 stdin 读取并向 stdout 写出。

# SUBCOMMANDS

**变异检测**
> mpileup, call

**文件操作**
> view, merge, concat, sort, index, convert

**过滤与查询**
> filter, query, norm

**统计**
> stats, roh, gtcheck

**注释**
> annotate, csq, fill-tags

**数据处理**
> reheader, isec, head, cnv, polysomy

**共识序列**
> consensus

**插件**
> plugin (e.g. +split, +scatter, +fill-tags, +setGT)

# PARAMETERS

**-Ob**
> 输出压缩的 BCF

**-Oz**
> 输出压缩的 VCF（bgzip 压缩）

**-Ov**
> 输出未压缩的 VCF

**-Ou**
> 输出未压缩的 BCF（管道传输时最快）

**-r** _region_
> 限定到逗号分隔的区域（chr:from-to 格式），需要索引文件

**-R** _file_
> 限定到文件中列出的区域（VCF、BED 或制表符分隔）

**-t** _region_
> 限定到目标区域，流式处理无需索引

**-T** _file_
> 限定到文件中列出的目标区域

**-s** _samples_
> 要包含的样本列表，逗号分隔（加 ^ 前缀表示排除）

**-S** _file_
> 从文件读取样本列表

**--threads** _int_
> 输出压缩所用的额外工作线程数

**-W, --write-index** _[fmt]_
> 自动为输出建立索引（tbi 或 csi）

**-i** _expression_
> 保留匹配过滤表达式的位点

**-e** _expression_
> 排除匹配过滤表达式的位点

**-o** _file_
> 输出文件名

# CAVEATS

在 bcftools 子命令之间用管道连接时，请使用 **-Ou** 以避免不必要的压缩开销。随机访问和某些操作需要已建索引的文件。大多数操作要求 VCF/BCF 文件按染色体和位置排好序。

# HISTORY

bcftools 作为 **SAMtools** 项目的一部分开发，最初由 Wellcome Sanger 研究所的 **Heng Li** 创建。约 **2014** 年，随着 HTSlib 库的重写，它成为独立项目，并在变异分析方面获得了大量新功能。

# INSTALL

```apt: sudo apt install bcftools```

```dnf: sudo dnf install bcftools```

```aur: yay -S bcftools```

```zypper: sudo zypper install bcftools```

```brew: brew install bcftools```

```nix: nix profile install nixpkgs#bcftools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[samtools](/man/samtools)(1), [tabix](/man/tabix)(1), [bgzip](/man/bgzip)(1), [vcftools](/man/vcftools)(1)

# RESOURCES

```[Homepage](https://samtools.github.io/bcftools/)```

```[Source code](https://github.com/samtools/bcftools)```

```[Documentation](https://samtools.github.io/bcftools/bcftools.html)```

<!-- verified: 2026-06-19 -->
