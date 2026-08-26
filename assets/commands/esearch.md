# TAGLINE

NCBI Entrez 数据库搜索工具

# TLDR

在 **pubmed** 中搜索查询词

```esearch -db pubmed -query "[selective serotonin reuptake inhibitor]"```

使用正则表达式搜索 **protein** 数据库

```esearch -db [protein] -query '[Escherichia*]'```

带字段限定符搜索 **nucleotide** 数据库

```esearch -db nuccore -query "[insulin [PROT] AND rodents [ORGN]]"```

显示**帮助**

```esearch [-h|-help]```

# SYNOPSIS

**esearch** [_options_]

# DESCRIPTION

**esearch** 是一个命令行工具，用于通过索引字段查询在 NCBI 的 Entrez 数据库中执行搜索。它提供对主要生物学数据库的编程访问能力，包括 PubMed（生物医学文献）、GenBank（核苷酸序列）、Protein（蛋白质序列）等众多数据库。

该工具属于 NCBI EDirect（Entrez Direct）实用程序套件，专为自动化检索和处理生物学数据而设计。esearch 通常作为管道的第一步，找出符合搜索条件的记录。其输出通常通过管道传给其他 EDirect 命令，如 efetch（获取完整记录）或 elink（查找跨数据库的关联数据）。这使得研究工作流中的生物数据库查询可以高效地自动化。

# PARAMETERS

**-db** _database_
> 要搜索的数据库

**-query** _string_
> 搜索查询，可附带字段限定符

**-h, -help**
> 显示帮助

# CAVEATS

属于 NCBI 的 edirect 软件包。需要联网。其输出通常通过管道传给 elink 或 efetch 作进一步处理。

# INSTALL

```apt: sudo apt install ncbi-entrez-direct```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elink](/man/elink)(1), [einfo](/man/einfo)(1)
