# TAGLINE

蛋白质查询序列对核苷酸数据库的搜索

# TLDR

**用蛋白质查询序列搜索**核苷酸数据库

```tblastn -query [protein.fasta] -db [nt_database]```

**以指定的输出格式搜索**

```tblastn -query [protein.fasta] -db [database] -outfmt [6]```

**将结果保存到文件**

```tblastn -query [protein.fasta] -db [database] -out [results.txt]```

**使用多线程**加快搜索

```tblastn -query [protein.fasta] -db [database] -num_threads [4]```

**设置 E 值阈值**

```tblastn -query [protein.fasta] -db [database] -evalue [1e-10]```

**使用快速任务**进行更快的搜索

```tblastn -query [protein.fasta] -db [database] -task tblastn-fast```

**搜索远程 NCBI 数据库**

```tblastn -query [protein.fasta] -db [nr] -remote```

# SYNOPSIS

**tblastn** [**-query** _file_] [**-db** _database_] [**-out** _file_] [_options_]

# PARAMETERS

**-query** _file_
> 包含 FASTA 格式蛋白质查询序列的输入文件。

**-db** _database_
> 要搜索的核苷酸数据库名称或路径。

**-out** _file_
> 结果输出文件（默认为 stdout）。

**-outfmt** _format_
> 输出格式：0（配对）、6（表格）、7（带注释的表格）、10（CSV）等。

**-evalue** _value_
> 报告匹配的 E 值阈值（默认为 10）。

**-num_threads** _n_
> 并行执行所用的线程数。

**-task** _task_
> 要执行的任务：**tblastn**（标准）或 **tblastn-fast**（更快，字长更大）。

**-remote**
> 针对 NCBI 服务器而非本地数据库执行搜索。

**-max_target_seqs** _n_
> 保留的比对序列最大数量。

**-word_size** _n_
> 初始匹配的字长（tblastn 默认为 3，tblastn-fast 默认为 6）。

**-matrix** _name_
> 打分矩阵（默认为 BLOSUM62）。其他选项包括 PAM30、PAM70、BLOSUM45、BLOSUM80。

**-gapopen** _n_
> 打开缺口的代价。

**-gapextend** _n_
> 延伸缺口的代价。

**-db_gencode** _n_
> 翻译数据库序列使用的遗传密码（默认为 1）。

**-comp_based_stats** _mode_
> 基于组成的统计模式（0-3）。

**-seg** _options_
> 使用 SEG 算法过滤查询序列。

**-threshold** _n_
> 将单词加入 BLAST 查找表的最低分值（tblastn 默认为 13，tblastn-fast 默认为 21）。

**-h**
> 打印简略帮助。

**-help**
> 打印含全部选项的详细帮助。

**-version**
> 打印版本信息。

# DESCRIPTION

**tblastn** 是 NCBI BLAST+ 序列比对工具套件的一部分。它以蛋白质查询序列搜索核苷酸序列数据库，在搜索时将数据库序列按全部六个阅读框翻译。这适用于在核苷酸序列中寻找蛋白编码区域。

该算法将每个蛋白质查询与翻译后的核苷酸目标序列进行比较，并报告具有统计学显著性的比对。结果可以多种方式格式化以便下游分析，其中包括适合解析的表格格式。

# CAVEATS

针对翻译后数据库的搜索计算量很大，因为每条目标序列都要按六个阅读框翻译。对于大型数据库，应使用 **-num_threads** 启用并行执行。**tblastn-fast** 任务搜索更快但灵敏度较低。本地数据库搜索需要使用 **makeblastdb** 预先构建 BLAST 数据库。

# HISTORY

BLAST（Basic Local Alignment Search Tool，基础局部比对搜索工具）由 **NCBI** 的 **Stephen Altschul** 及其同事开发，原始算法于 **1990 年**发表。tblastn 是最初 BLAST 套件中用于蛋白质对翻译后核苷酸搜索的工具。BLAST+ 命令行程序是用 C++ 完全重写的版本，于 **2009 年**发布，至今仍由 NCBI 积极维护。

# INSTALL

```apt: sudo apt install ncbi-blast+```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blastn](/man/blastn)(1), [blastp](/man/blastp)(1), [blastx](/man/blastx)(1), [makeblastdb](/man/makeblastdb)(1), [tblastx](/man/tblastx)(1)
