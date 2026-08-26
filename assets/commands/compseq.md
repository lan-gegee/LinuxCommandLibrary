# TAGLINE

计算核苷酸和氨基酸组成

# TLDR

通过**交互式提示**统计单词频率

```compseq [path/to/file.fasta]```

从蛋白质序列统计**氨基酸对**

```compseq [path/to/input_protein.fasta] -word 2 [path/to/output_file.comp]```

统计**六核苷酸**，忽略零计数

```compseq [path/to/input_dna.fasta] -word 6 [path/to/output_file.comp] -nozero```

统计特定阅读框中的**密码子**

```compseq -sequence [path/to/input_rna.fasta] -word 3 [path/to/output_file.comp] -nozero -frame [1]```

与上一次运行的结果进行**比较**

```compseq -sequence [path/to/file.fasta] -word 3 [path/to/output.comp] -nozero -infile [path/to/previous.comp]```

根据输入计算**期望频率**

```compseq -sequence [path/to/file.fasta] -word 3 [path/to/output.comp] -nozero -calcfreq```

# SYNOPSIS

**compseq** [_options_] _sequence_ _outfile_

# DESCRIPTION

**compseq** 是 EMBOSS（European Molecular Biology Open Software Suite，欧洲分子生物学开放软件套件）软件包中的一款生物信息学工具，用于对 DNA、RNA 和蛋白质序列执行 k-mer 频率分析。它读取 FASTA 格式的序列，并生成组成统计数据，展示指定长度的每种可能的单词（k-mer）在序列中出现的频率。

该工具在分子生物学中被广泛用于多种用途：分析基因中的密码子使用偏倚、识别指示功能或结构元件的序列组成模式，以及比较不同生物体或基因组区域之间的序列特征。通过指定不同的单词长度，研究人员可以考察二核苷酸频率（长度 2）、密码子频率（长度 3）或更长的寡核苷酸模式。

compseq 既能计算观测频率，也能基于整体碱基组成计算期望频率，因此可用于识别相对于随机分布在统计上显著的偏差。阅读框参数允许对特定阅读框内的编码序列进行分析，这对研究蛋白质编码基因的密码子使用模式至关重要。

# PARAMETERS

**-word** _size_
> 要统计的单词长度（如 2 表示二核苷酸，3 表示密码子）

**-frame** _number_
> 阅读框（1、2 或 3）

**-nozero**
> 忽略输出中的零计数

**-infile** _file_
> 与之前的 compseq 输出进行比较

**-calcfreq**
> 根据输入计算期望频率

**-help**
> 显示帮助

# CAVEATS

属于 EMBOSS 套件的一部分。输入必须是有效的 FASTA 格式。较大的单词长度可能产生非常庞大的输出表。

# INSTALL

```apt: sudo apt install emboss```

```nix: nix profile install nixpkgs#emboss```

<!-- packages: 2026-07-22 -->

# SEE ALSO
