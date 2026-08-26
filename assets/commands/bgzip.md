# TAGLINE

支持随机访问的基因组数据分块压缩工具

# TLDR

**压缩**文件

```bgzip [file.vcf]```

**解压**文件

```bgzip -d [file.vcf.gz]```

**用指定线程数压缩**

```bgzip -@ [4] [file.vcf]```

**为压缩文件建索引**

```bgzip -r [file.vcf.gz]```

# SYNOPSIS

**bgzip** [_options_] [_file_]

# DESCRIPTION

**bgzip** 是一个分块压缩工具，可创建兼容 gzip 且带内部索引支持的文件。与标准 gzip 不同，bgzip 以块为单位压缩数据，配合 .gzi 索引即可随机访问特定区域。

该工具是 htslib 的一部分，常用于基因组数据文件（VCF、SAM、BED），以启用索引访问。

# PARAMETERS

**-d**, **--decompress**
> 解压文件

**-c**, **--stdout**
> 写入标准输出

**-@**, **--threads** _n_
> 线程数

**-r**, **--reindex**
> 重建 .gzi 索引

**-b**, **--offset** _n_
> 用于随机访问的虚拟文件偏移量

**-s**, **--size** _n_
> 要提取的大小（配合 -b 使用）

**-l**, **--compress-level** _n_
> 压缩级别（0-9）

# FEATURES

- 基于块的压缩
- 随机访问支持
- 兼容 gzip 的格式
- 多线程压缩
- 索引生成（.gzi 文件）
- 流式处理支持

# WORKFLOW

```bash
# Compress VCF
bgzip variants.vcf

# Creates: variants.vcf.gz

# Decompress
bgzip -d variants.vcf.gz

# Compress with 4 threads
bgzip -@ 4 large.vcf

# Random access (requires .gzi index)
bgzip -b 1000 -s 500 file.vcf.gz
```

# USE WITH TABIX

```bash
# Compress and index
bgzip file.vcf
tabix -p vcf file.vcf.gz

# Now tools can query regions
tabix file.vcf.gz chr1:1000-2000
```

# CAVEATS

文件比最大压缩级别的 gzip 略大。随机访问需要 .gzi 索引。并非所有 gzip 工具都能识别块结构。主要用于基因组学应用。

# HISTORY

**bgzip** 约 **2009 年**作为 SAMtools/htslib 的一部分开发，用于高效地随机访问压缩的基因组数据文件。

# INSTALL

```apt: sudo apt install tabix```

```zypper: sudo zypper install tabix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [tabix](/man/tabix)(1)
