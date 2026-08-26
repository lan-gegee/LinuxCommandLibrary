# TAGLINE

从 BLAST 数据库中提取序列

# TLDR

**获取数据库信息**

```blastdbcmd -db [nr] -info```

**列出某路径下可用的数据库**

```blastdbcmd -list [/path/to/databases] -recursive```

**按登录号提取序列**

```blastdbcmd -db [nr] -entry [NP_001234] -out [sequence.fasta]```

**提取数据库中的全部序列**

```blastdbcmd -db [swissprot] -entry all -out [swissprot.fasta]```

**从列表文件提取序列**

```blastdbcmd -db [nr] -entry_batch [ids.txt] -out [sequences.fasta]```

**以指定格式输出序列**

```blastdbcmd -db [nr] -entry [NP_001234] -outfmt "%a %t %s"```

**显示 BLAST 数据库搜索路径**

```blastdbcmd -show_blastdb_search_path```

**获取分类信息**

```blastdbcmd -db [nr] -entry [NP_001234] -outfmt "%a %S %T"```

# SYNOPSIS

**blastdbcmd** [_-db database_] [_-entry id_] [_options_]

# DESCRIPTION

**blastdbcmd** 是一个用于从 BLAST 数据库中提取序列和元数据的工具。它可以按登录号检索单个序列、提取全部序列、显示数据库统计信息，并生成自定义报告。

该工具是 NCBI BLAST+ 套件的一部分，适用于由 **makeblastdb** 创建或从 NCBI 下载的数据库。

# PARAMETERS

**-db** _name_
> BLAST 数据库名称或路径

**-entry** _id_
> 要检索的序列标识符；使用 "all" 表示整个数据库

**-entry_batch** _file_
> 包含序列标识符列表的文件

**-out** _file_
> 输出文件（默认：stdout）。

**-outfmt** _format_
> 使用 % 标记的自定义输出格式字符串。

**-info**
> 显示数据库信息（类型、序列数量、总长度、日期）。

**-list** _path_
> 列出指定路径中的数据库。

**-recursive**
> 递归搜索目录（配合 -list 使用）。

**-show_blastdb_search_path**
> 显示 BLAST 数据库的搜索路径。

**-dbtype** _type_
> 数据库类型：nucl（核酸）或 prot（蛋白质）。当两种类型同名时需要指定。

**-target_only**
> 仅检索目标序列（不含冗余组成员）。

**-tax_info**
> 显示分类学信息（需要分类数据库）。

**-range** _start-stop_
> 提取子序列范围（1 起始、含端点）。

**-strand** _strand_
> 要检索的链：plus 或 minus（仅限核酸）。

**-line_length** _N_
> FASTA 输出的行长度（默认：80）。设为 0 表示单行序列。

**-long_seqids**
> 使用包含数据库名和 accession.version 的长序列标识符。

# OUTPUT FORMAT TOKENS

**%a** - 登录号
**%g** - GI 号
**%o** - OID（顺序 ID）
**%t** - 标题（定义行）
**%s** - 序列数据
**%l** - 序列长度
**%T** - 分类 ID
**%S** - 学名
**%L** - 常用名
**%m** - 屏蔽数据
**%h** - 哈希值
**%e** - 成员关系整数

# ENVIRONMENT

**BLASTDB**
> 用于搜索 BLAST 数据库的目录列表，以冒号分隔。

# CAVEATS

需要有由 **makeblastdb** 创建或从 NCBI 下载的预格式化 BLAST 数据库。分类信息需要安装 BLAST 分类数据库（taxdb.btd/bti）。大规模提取可能耗费大量时间和磁盘空间。**-range** 选项使用 1 起始且含端点的坐标。

# INSTALL

```apt: sudo apt install ncbi-blast+```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[makeblastdb](/man/makeblastdb)(1), [blastn](/man/blastn)(1), [blastp](/man/blastp)(1), [blastx](/man/blastx)(1), [tblastn](/man/tblastn)(1)
