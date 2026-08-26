# TAGLINE

蛋白质对蛋白质的序列比对搜索

# TLDR

**比对序列**，使用 blastp 并设置 E 值阈值

```blastp -query [query.fa] -subject [subject.fa] -evalue [1e-9]```

使用 **blastp-fast** 比对序列

```blastp -task blastp-fast -query [query.fa] -subject [subject.fa]```

以**自定义表格输出**比对并写入文件

```blastp -query [query.fa] -subject [subject.fa] -outfmt '6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident' -out [output.tsv]```

多线程搜索**蛋白质数据库**

```blastp -query [query.fa] -db [blast_database_name] -num_threads [16] -max_target_seqs [10]```

搜索**远程非冗余**蛋白质数据库

```blastp -query [query.fa] -db nr -remote```

显示**帮助**

```blastp -h```

# SYNOPSIS

**blastp** [_options_]

# DESCRIPTION

**blastp** 执行蛋白质对蛋白质的 BLAST（Basic Local Alignment Search Tool）搜索。它比较氨基酸序列以找出相似区域，这些区域可以揭示功能、结构或进化上的关系。

该工具对于鉴定蛋白质家族、跨物种寻找同源物，以及基于与已知序列的相似性为新测定的蛋白质作注释至关重要。

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
> 算法变体：blastp（默认）、blastp-fast 或 blastp-short

**-matrix** _name_
> 打分矩阵（默认 BLOSUM62；如 BLOSUM45、PAM30）

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

大型数据库搜索需要大量内存和时间。远程搜索受 NCBI 速率限制。结果应结合序列长度和数据库规模来解读。

# HISTORY

BLAST 由 NCBI（美国国家生物技术信息中心）开发，原始算法由 Altschul 等人于 **1990 年**发表。命令行应用的 BLAST+ 重写版于 **2009 年**发布，是当前提供 **blastp** 的实现。

# INSTALL

```apt: sudo apt install ncbi-blast+```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blastn](/man/blastn)(1), [blastx](/man/blastx)(1), [tblastn](/man/tblastn)(1), [makeblastdb](/man/makeblastdb)(1)

# RESOURCES

```[Homepage](https://blast.ncbi.nlm.nih.gov/)```

```[Documentation](https://www.ncbi.nlm.nih.gov/books/NBK279690/)```

<!-- verified: 2026-06-19 -->
