# TAGLINE

病毒基因组序列比对工具

# TLDR

**将序列比对到参考基因组**

```nextalign run --input-ref [reference.fasta] -i [sequences.fasta] -o [aligned.fasta]```

**使用基因组注释**

```nextalign run --input-ref [ref.fasta] --input-annotation [genemap.gff3] -i [seqs.fasta] -o [out.fasta]```

**将所有结果输出到一个目录**

```nextalign run --input-ref [ref.fasta] -i [seqs.fasta] --output-all [output_dir/]```

**使用 Nextclade 数据集代替单独的文件**

```nextalign run --input-dataset [nextstrain/sars-cov-2/wuhan-hu-1/orfs] -i [seqs.fasta] -o [out.fasta]```

**设置线程数**

```nextalign run -j [8] --input-ref [ref.fasta] -i [seqs.fasta] -o [out.fasta]```

# SYNOPSIS

**nextalign** run [_options_]

# PARAMETERS

**--input-ref** _file_
> 参考序列（FASTA）。不使用 --input-dataset 时必填。

**-i**, **--input** _file_
> 输入序列（FASTA）。

**-o**, **--output-fasta** _file_
> 输出比对后的序列。

**--input-annotation** _file_
> 基因组注释（GFF3）。

**--input-dataset** _name_
> 使用 Nextclade 数据集（替代单独的 --input-ref、--input-annotation）。

**--output-all** _dir_
> 将所有输出文件写入一个目录。

**--output-translations** _template_
> 输出翻译后的蛋白质序列。

**-j**, **--jobs** _n_
> 线程数量。

**--include-reference**
> 在输出比对中包含参考序列。

**--in-order**
> 按输入顺序输出序列。

# DESCRIPTION

**Nextalign** 是一款病毒基因组序列比对工具。它将病毒序列与参考序列进行成对比对，并识别突变、插入和缺失。

Nextalign 是 Nextclade 工具套件的组成部分，常用于 SARS-CoV-2 分析。从 Nextclade v3 起，独立的 Nextalign CLI 已被 **nextclade run** 取代，后者提供相同的比对功能及额外的分析。建议用户迁移到 **nextclade**。

# OUTPUT FILES

```
aligned.fasta        - Aligned sequences
insertions.csv       - Insertion positions
translations/        - Translated proteins
```

# CAVEATS

针对低分歧度的病毒基因组优化（与参考序列差异小于 10%）。对于多样性更高的数据集，mafft 或 minimap2 等工具更为稳健。从 v3 起，独立的 nextalign CLI 已被移除，由 **nextclade run** 取代。

# HISTORY

Nextalign 由 **Nextstrain** 项目开发，该项目由 **Trevor Bedford** 和 **Richard Neher** 领导，在 COVID-19 疫情期间声名鹊起。

# SEE ALSO

[nextclade](/man/nextclade)(1), [mafft](/man/mafft)(1), [minimap2](/man/minimap2)(1)
