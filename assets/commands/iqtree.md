# TAGLINE

用于最大似然树推断的系统发育分析工具

# TLDR

**运行系统发育分析**

```iqtree -s [alignment.fasta]```

**指定模型**

```iqtree -s [alignment.fasta] -m [GTR+G]```

**自动模型选择**

```iqtree -s [alignment.fasta] -m MFP```

**标准自展分析**

```iqtree -s [alignment.fasta] -b [1000]```

**超快自展**（IQ-TREE2 使用 -B）

```iqtree -s [alignment.fasta] -B [1000]```

**使用多线程**（IQ-TREE2 使用 -T）

```iqtree -s [alignment.fasta] -T [4]```

# SYNOPSIS

**iqtree** [_options_] **-s** _alignment_

# PARAMETERS

**-s** _file_
> 输入的比对文件。

**-m** _model_
> 替换模型（或用 MFP 进行模型选择）。

**-b** _n_
> 标准自展重复次数。

**-B**, **--ufboot** _n_
> 超快自展重复次数（最少 1000）。IQ-TREE v1 使用 -bb。

**-T**, **--threads** _n_|AUTO
> CPU 线程数，或用 AUTO 自动检测。IQ-TREE v1 使用 -nt。

**-pre** _prefix_
> 输出文件前缀。

**-o** _taxa_
> 外群分类单元。

**-t** _tree_
> 起始树文件。

**-wbt**
> 输出自展树。

**--bnni**
> 在自展比对上通过 NNI 优化 UFBoot 树（减少高估）。

**-alrt** _n_
> SH 类近似似然比检验。

# DESCRIPTION

**IQ-TREE** 是一款用于最大似然树推断的系统发育分析工具。它支持多种替换模型、模型选择以及多种自展方法。

IQ-TREE 以其速度和准确性著称，实现了面向大规模系统发育分析的高效算法。它可处理 DNA、蛋白质、密码子和形态学数据。

# OUTPUT FILES

```
.treefile    Best tree in Newick format
.iqtree      Analysis report
.log         Screen log
.mldist      ML distances
.bionj       BIONJ starting tree
```

# CAVEATS

大型比对需要大量内存。模型选择可能耗时较长。自展次数因研究需求而异。

# HISTORY

IQ-TREE 由维也纳大学的 **Bui Quang Minh**、**Lam-Tung Nguyen** 和 **Arndt von Haeseler** 开发。首次发布于 **2014 年**，现已成为分子系统发育学的标准工具。

# INSTALL

```nix: nix profile install nixpkgs#iqtree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mafft](/man/mafft)(1), [raxml](/man/raxml)(1)
