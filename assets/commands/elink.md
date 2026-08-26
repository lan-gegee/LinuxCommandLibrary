# TAGLINE

查找 NCBI 数据库间的关联记录

# TLDR

搜索 pubmed 然后查找**相关序列**

```esearch -db pubmed -query "[query]" | elink -target nuccore```

搜索核苷酸然后查找**相关生物样本**

```esearch -db nuccore -query "[query]" | elink -target biosample```

# SYNOPSIS

**elink** [_options_]

# DESCRIPTION

**elink** 在 NCBI 数据库内查询预计算的邻居记录，或在其他数据库中查找关联记录。它接收 esearch 的搜索结果并找出相关条目。

属于 NCBI EDirect 工具集，用于以编程方式访问生物学数据库。

# PARAMETERS

**-target** _database_
> 关联记录的目标数据库

**-name** _linkname_
> 要跟随的特定链接名称

**-db** _database_
> 源数据库

**-cmd** _command_
> Entrez 链接命令模式

# CAVEATS

属于 NCBI 的 edirect 软件包。配合 esearch 的管道输入工作。需要互联网连接。

# INSTALL

```apt: sudo apt install ncbi-entrez-direct```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[esearch](/man/esearch)(1), [einfo](/man/einfo)(1)
