# TAGLINE

分析基因组变异调用格式（VCF）文件

# TLDR

**按染色体过滤 VCF 文件**并输出新的 VCF

```vcftools --vcf [input.vcf] --chr [chr1] --recode --out [output]```

**计算等位基因频率**

```vcftools --vcf [input.vcf] --freq --out [output]```

**提取特定个体**

```vcftools --vcf [input.vcf] --keep [individuals.txt] --recode --out [output]```

**按最低质量分数过滤**

```vcftools --vcf [input.vcf] --minQ [30] --recode --out [output]```

**计算每个个体的深度统计信息**

```vcftools --vcf [input.vcf] --depth --out [output]```

**按最小等位基因频率过滤**

```vcftools --vcf [input.vcf] --maf [0.05] --recode --out [output]```

**读取压缩的 VCF 文件**

```vcftools --gzvcf [input.vcf.gz] --freq --out [output]```

# SYNOPSIS

**vcftools** [**--vcf** _file_ | **--gzvcf** _file_ | **--bcf** _file_] [**--out** _prefix_] [_options_]

# PARAMETERS

**--vcf** _file_
> 输入 VCF 文件（v4.0、v4.1 或 v4.2）。

**--gzvcf** _file_
> 输入压缩（gzip）VCF 文件。

**--bcf** _file_
> 输入 BCF2 格式文件。

**--out** _prefix_
> 输出文件前缀。结果写入 prefix.extension。

**--recode**
> 应用过滤器后输出新的 VCF 文件。

**--recode-INFO-all**
> 在重新编码的输出中保留所有 INFO 字段。

**--chr** _name_
> 只处理指定染色体上的变异。

**--keep** _file_
> 只保留文件中列出的个体（每行一个 ID）。

**--remove** _file_
> 移除文件中列出的个体。

**--maf** _float_
> 按最小等位基因频率过滤。

**--minQ** _int_
> 变异的最低质量分数。

**--freq**
> 计算等位基因频率。

**--depth**
> 计算每个个体的平均测序深度。

**--relatedness**
> 计算两两个体间的亲缘关系统计量。

**--hap-r2**
> 使用相位已知的单倍型计算连锁不平衡统计量。

# DESCRIPTION

**VCFtools** 是一套用于分析变异调用格式（VCF）和二进制调用格式（BCF）文件的实用工具，这两种是存储基因组序列变异的标准格式。它提供全面的工具来过滤、操作变异数据并计算相关统计量。

该工具支持按质量分数、等位基因频率、缺失数据、基因组区域和个体样本过滤变异。它可以计算群体遗传学统计量，包括等位基因频率、核苷酸多样性、Fst、连锁不平衡以及亲缘关系度量。

VCFtools 可以在不同格式之间转换、比较 VCF 文件，以及提取数据子集供下游分析使用。输出文件使用 **--out** 指定的前缀，并根据分析类型加上相应的扩展名。

# CAVEATS

大型 VCF 文件可能占用大量内存。某些操作要求输入按染色体和位置排序。压缩文件应使用 bgzip 压缩（而非 gzip），以配合索引获得最佳性能。重复分析时二进制 BCF 格式速度更快。

# HISTORY

**VCFtools** 由康奈尔大学的 **Adam Auton** 和 **Anthony Marcketta** 开发，首个版本约于 **2011 年**发布。随着下一代测序技术的普及，高效操作 VCF 的需求催生了这一工具。如今它已成为生物信息学中变异分析和质量控制流程的标准工具。

# INSTALL

```apt: sudo apt install vcftools```

```dnf: sudo dnf install vcftools```

```brew: brew install vcftools```

```nix: nix profile install nixpkgs#vcftools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bcftools](/man/bcftools)(1), [tabix](/man/tabix)(1), [bgzip](/man/bgzip)(1), [samtools](/man/samtools)(1)
