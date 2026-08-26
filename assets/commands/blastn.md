# TAGLINE

核酸对核酸的序列比对搜索

# TLDR

**比对序列**，使用 megablast 并设置 E 值阈值

```blastn -query [query.fa] -subject [subject.fa] -evalue [1e-9]```

使用**标准 blastn** 比对序列

```blastn -task blastn -query [query.fa] -subject [subject.fa]```

以**自定义表格输出**比对并写入文件

```blastn -query [query.fa] -subject [subject.fa] -outfmt '6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident' -out [output.tsv]```

多线程搜索**核酸数据库**

```blastn -query [query.fa] -db [path/to/blast_db] -num_threads [16] -max_target_seqs [10]```

搜索**远程非冗余**核酸数据库

```blastn -query [query.fa] -db nt -remote```

显示**帮助**

```blastn -h```

# SYNOPSIS

**blastn** [_options_]

# DESCRIPTION

**blastn** 执行核酸对核酸的 BLAST（Basic Local Alignment Search Tool）搜索。它查找核酸序列之间的相似区域，这些区域可能指示功能、结构或进化上的关系。

该工具支持多种搜索算法，包括 megablast（默认，适合高度相似的序列）、不连续 megablast（discontiguous megablast）和标准 blastn。结果可用于鉴定基因、比较基因组或查找同源序列。

# PARAMETERS

**-query** _file_
> 包含 FASTA 格式查询序列的输入文件

**-subject** _file_
> 用于直接比较的目标序列文件

**-db** _name_
> 用于搜索的 BLAST 数据库名称

**-evalue** _threshold_
> 报告匹配的期望值（E）阈值

**-task** _name_
> 算法变体：megablast（默认）、dc-megablast、blastn、blastn-short 或 rmblastn

**-word_size** _n_
> 初始精确匹配种子的长度（越小能找到差异越大的命中）

**-perc_identity** _n_
> 仅报告一致度达到或超过此百分比的比对

**-outfmt** _format_
> 输出格式（0=成对，6=表格，7=带表头的表格，11=BLAST 归档）

**-out** _file_
> 输出文件名

**-num_threads** _n_
> 使用的 CPU 线程数

**-max_target_seqs** _n_
> 保留的最大比对序列数

**-remote**
> 在 NCBI 服务器上执行搜索

# CAVEATS

大型数据库搜索需要大量内存和时间。远程搜索有速率限制。本地数据库搜索需要用 **makeblastdb** 创建的预格式化 BLAST 数据库。

# HISTORY

BLAST 由 NCBI（美国国家生物技术信息中心）开发，原始算法由 Altschul 等人于 **1990 年**发表。它已成为使用最广泛的生物信息学工具之一。

# INSTALL

```apt: sudo apt install ncbi-blast+```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blastp](/man/blastp)(1), [blastx](/man/blastx)(1), [tblastn](/man/tblastn)(1), [makeblastdb](/man/makeblastdb)(1)

# RESOURCES

```[Homepage](https://blast.ncbi.nlm.nih.gov/)```

```[Documentation](https://www.ncbi.nlm.nih.gov/books/NBK279690/)```

<!-- verified: 2026-06-19 -->
