# TAGLINE

分析病毒基因组序列，进行分支分型并检出突变

# TLDR

**分析序列**

```nextclade run -i [sequences.fasta] -d [sars-cov-2]```

**分析并将结果写入输出文件**

```nextclade run -i [sequences.fasta] -d [sars-cov-2] -o [output.tsv]```

**列出可用数据集**

```nextclade dataset list```

**下载数据集**

```nextclade dataset get -n [sars-cov-2] -o [dataset/]```

**使用本地数据集运行**

```nextclade run -i [sequences.fasta] -D [dataset/]```

**生成系统发育树输出**

```nextclade run -i [sequences.fasta] -d [sars-cov-2] --output-tree [tree.json]```

**输出比对后的序列**

```nextclade run -i [sequences.fasta] -d [sars-cov-2] --output-fasta [aligned.fasta]```

# SYNOPSIS

**nextclade** [_run_] [_dataset_] [_-i input_] [_-d dataset_] [_-o output_] [_options_]

# PARAMETERS

**run**
> 分析序列。

**dataset list**
> 列出可用数据集。

**dataset get**
> 下载数据集。

**-i** _FILE_
> 输入的 FASTA 文件。

**-d** _NAME_
> 数据集名称。

**-D** _DIR_
> 数据集目录。

**-o** _FILE_
> 输出的 TSV 文件。

**--output-tree** _FILE_
> 输出树形 JSON。

**--output-fasta** _FILE_
> 输出比对后的 FASTA。

**--output-json** _FILE_
> 输出 JSON 结果。

**-j** _N_
> 线程数量。

**--min-length** _N_
> 最小序列长度。

**--include-reference**
> 在输出中包含参考序列。

# DESCRIPTION

**nextclade** 用于分析病毒基因组序列，进行分支（clade）分型、突变检出和序列质量评估。它被广泛用于 SARS-CoV-2 的基因组监测。

该工具将序列与参考基因组比对，识别突变（替换、插入、缺失），并将序列归入系统发育树中的相应分支。

质量控制指标可标记潜在问题：数据缺失、混合碱基、移码突变、终止密码子和异常突变。这些有助于发现测序错误或污染。

数据集包含参考序列、基因注释和分支定义。主要病原体都有预构建的数据集，也可以创建自定义数据集。

输出包括详细的突变列表、分支归属和质量评分。结果可用于可视化处理或流行病学分析。

树的定位功能可以显示序列在全球系统发育中的位置，有助于追踪疫情源头。

# CAVEATS

结果取决于数据集的质量。新型分支可能无法正确归属。大数据集需要大量内存。某些功能仅针对特定病原体。

# HISTORY

**Nextclade** 由 **Cornelius Roemer** 等人在 **Nextstrain** 项目中开发，始于 **2020 年**前后的 COVID-19 疫情期间。它为全球的基因组监测项目提供快速的分支归属和质量控制。

# SEE ALSO

[nextalign](/man/nextalign)(1), [pangolin](/man/pangolin)(1), [mafft](/man/mafft)(1), [minimap2](/man/minimap2)(1)
