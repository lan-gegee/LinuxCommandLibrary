# TAGLINE

从 FASTA 序列创建 BLAST 数据库

# TLDR

**创建核苷酸数据库**

```makeblastdb -in [sequences.fasta] -dbtype nucl -out [mydb]```

**创建蛋白质数据库**

```makeblastdb -in [proteins.fasta] -dbtype prot -out [mydb]```

**为数据库添加标题**

```makeblastdb -in [sequences.fasta] -dbtype nucl -title "[My Database]" -out [mydb]```

**解析序列 ID**

```makeblastdb -in [sequences.fasta] -dbtype nucl -parse_seqids -out [mydb]```

**创建带分类信息的数据库**

```makeblastdb -in [sequences.fasta] -dbtype nucl -taxid_map [taxid.map] -out [mydb]```

# SYNOPSIS

**makeblastdb** -in _fasta_ -dbtype _type_ [_options_]

# PARAMETERS

**-in** _file_
> 输入的 FASTA 文件。

**-dbtype** _type_
> nucl（核苷酸）或 prot（蛋白质）。

**-out** _name_
> 数据库文件名前缀。

**-title** _title_
> 数据库标题。

**-parse_seqids**
> 解析序列标识符。

**-taxid_map** _file_
> 分类映射文件。

**-hash_index**
> 创建哈希索引。

# DESCRIPTION

**makeblastdb** 从 FASTA 序列创建 BLAST 数据库。运行本地 BLAST 搜索（如 blastn、blastp、blastx 及相关程序）时必须使用这些数据库。

生成的数据库由多个文件组成：核苷酸数据库使用 .nhr、.nin、.nsq 等扩展名，蛋白质数据库使用 .phr、.pin、.psq 等扩展名。

# OUTPUT FILES

```
mydb.nhr  # Header
mydb.nin  # Index
mydb.nsq  # Sequences
```

# CAVEATS

处理大型序列需要较多内存。数据库文件必须保存在一起。源数据变更后需要重新构建。

# HISTORY

makeblastdb 是 **BLAST+** 的一部分，BLAST+ 是传统 BLAST 的后继版本，由 **NCBI**（美国国家生物技术信息中心）开发。

# INSTALL

```apt: sudo apt install ncbi-blast+```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blastn](/man/blastn)(1), [blastp](/man/blastp)(1), [blastx](/man/blastx)(1), [tblastn](/man/tblastn)(1)
