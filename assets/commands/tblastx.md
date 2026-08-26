# TAGLINE

翻译后的核苷酸对核苷酸的搜索

# TLDR

**用查询序列搜索数据库**

```tblastx -query [sequence.fasta] -db [database] -out [results.txt]```

**以指定的输出格式搜索**

```tblastx -query [sequence.fasta] -db [database] -outfmt [6]```

**对本地 FASTA 文件进行搜索**

```tblastx -query [query.fasta] -subject [subject.fasta]```

**设置 E 值阈值**

```tblastx -query [sequence.fasta] -db [database] -evalue [1e-5]```

**使用多线程**

```tblastx -query [sequence.fasta] -db [database] -num_threads [4]```

**限制比对数量**

```tblastx -query [sequence.fasta] -db [database] -max_target_seqs [10]```

**显示帮助**

```tblastx -help```

# SYNOPSIS

**tblastx** [_options_]

# PARAMETERS

**-query** _file_
> 包含核苷酸查询序列的输入 FASTA 文件。

**-db** _database_
> 要搜索的 BLAST 数据库名称。

**-subject** _file_
> 用于配对比较的目标序列文件。

**-out** _file_
> 输出文件（默认为 stdout）。

**-outfmt** _format_
> 输出格式（0=配对、6=表格、7=带注释的表格等）。

**-evalue** _value_
> 期望值阈值（默认为 10）。

**-max_target_seqs** _n_
> 保留的比对序列最大数量。

**-num_threads** _n_
> 使用的 CPU 线程数。

**-query_gencode** _code_
> 翻译查询序列使用的遗传密码。

**-db_gencode** _code_
> 翻译数据库序列使用的遗传密码。

**-strand** _strand_
> 要搜索的查询链：both、plus、minus。

**-soft_masking** _bool_
> 对查询序列应用软掩蔽。

**-seg** _value_
> 使用 SEG 过滤查询序列（yes、no 或参数）。

**-matrix** _name_
> 打分矩阵（默认为 BLOSUM62）。

**-word_size** _n_
> 初始匹配的字长。

**-h**, **-help**
> 显示帮助信息。

# DESCRIPTION

**tblastx** 将翻译后的核苷酸查询序列与翻译后的核苷酸数据库进行比较。查询和数据库序列都会按全部六个阅读框（三个正向、三个反向）翻译，然后在蛋白质层面进行比较。

该程序适用于寻找核苷酸序列之间较远的蛋白编码亲缘关系，尤其在处理未经注释的基因组或 EST 数据时非常有用。由于需要进行多次翻译，其计算量很大。

与其他 BLAST 程序不同，tblastx 只支持无缺口比对。对于存在插入或缺失的序列，建议改用 blastx 或 tblastn。

作为 NCBI BLAST+ 套件的一部分，tblastx 需要使用 makeblastdb 创建的格式正确的 BLAST 数据库。

# CAVEATS

仅支持无缺口比对。由于对查询和数据库都要做六框翻译，计算量非常大。需要安装 BLAST+ 并准备好格式化的数据库。内存占用随数据库和查询规模而增长。

# HISTORY

**tblastx** 是 BLAST（Basic Local Alignment Search Tool，基础局部比对搜索工具）的一部分，最初由 Stephen Altschul 及其同事于 1990 年在 NCBI 开发。用 C++ 重写的 BLAST+ 套件取代了最初的 C 实现。它至今仍是生物信息学中序列相似性搜索的基础工具。

# INSTALL

```apt: sudo apt install ncbi-blast+```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blastn](/man/blastn)(1), [blastp](/man/blastp)(1), [blastx](/man/blastx)(1), [makeblastdb](/man/makeblastdb)(1)
