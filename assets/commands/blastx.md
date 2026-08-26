# TAGLINE

翻译后的核酸对蛋白质序列搜索

# TLDR

**将翻译后的核酸**与蛋白质数据库比对

```blastx -query [sequences.fasta] -db [nr] -out [results.txt]```

**以表格格式输出**

```blastx -query [sequences.fasta] -db [swissprot] -outfmt 6 -out [results.tsv]```

**以 XML 格式输出**

```blastx -query [sequences.fasta] -db [nr] -outfmt 5 -out [results.xml]```

**设置 E 值阈值**

```blastx -query [sequences.fasta] -db [nr] -evalue [0.001] -out [results.txt]```

**限制比对数量**

```blastx -query [sequences.fasta] -db [nr] -max_target_seqs [10] -out [results.txt]```

**使用多线程**

```blastx -query [sequences.fasta] -db [nr] -num_threads [8] -out [results.txt]```

**显示帮助**

```blastx -help```

# SYNOPSIS

**blastx** [_-query file_] [_-db database_] [_-out file_] [_options_]

# DESCRIPTION

**blastx** 将核酸查询序列按全部六种阅读框翻译，然后与蛋白质数据库进行搜索。它是 NCBI BLAST+ 序列相似性搜索套件的一部分。

该工具可用于鉴定核酸序列的蛋白质同源物、注释基因以及在 DNA 序列中查找编码区。

# PARAMETERS

**-query** _file_
> 输入的核酸序列文件（FASTA 格式）

**-db** _name_
> 用于比对的蛋白质数据库（如 nr、swissprot）

**-out** _file_
> 结果输出文件

**-outfmt** _format_
> 输出格式：0=成对，5=XML，6=表格，7=带注释行的表格

**-evalue** _value_
> 报告命中的 E 值阈值（默认：10）

**-max_target_seqs** _n_
> 保留的最大比对序列数

**-num_threads** _n_
> 使用的线程/CPU 数

**-word_size** _n_
> 初始匹配的字长

**-matrix** _name_
> 打分矩阵（如 BLOSUM62、PAM250）

**-query_gencode** _n_
> 查询序列翻译所用的遗传密码（默认：1）。

**-seg** _method_
> 过滤查询序列中的低复杂度区域（默认：12 2.2 2.5）。

**-task** _name_
> 要执行的任务：blastx（默认）或 blastx-fast。

**-remote**
> 在 NCBI 服务器上远程执行搜索。

# CAVEATS

需要有预格式化的 BLAST 数据库；请使用 **makeblastdb** 创建。像 nr 这样的大型数据库需要大量磁盘空间和内存。六框翻译使得计算时间比 blastn 更长。

# HISTORY

BLAST（Basic Local Alignment Search Tool）最初由 **Stephen Altschul** 及其同事于 **1990 年**在 NCBI 开发。包含 blastx 的 BLAST+ 套件于 **2009 年**发布，性能更佳并引入了新功能。

# INSTALL

```apt: sudo apt install ncbi-blast+```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blastn](/man/blastn)(1), [blastp](/man/blastp)(1), [tblastn](/man/tblastn)(1), [tblastx](/man/tblastx)(1), [makeblastdb](/man/makeblastdb)(1), [blastdbcmd](/man/blastdbcmd)(1)
