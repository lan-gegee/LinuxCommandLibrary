# TAGLINE

使用 MinHash sketch 快速从基因组序列创建距离树

# TLDR

**最快方法**：使用多线程从 fastq 和/或 fasta 文件创建树

```mashtree --numcpus [12] [*.fastq.gz] [*.fasta] > [mashtree.dnd]```

**最精确方法**：以 mindepth 0 创建树

```mashtree --mindepth 0 --numcpus [12] [*.fastq.gz] [*.fasta] > [mashtree.dnd]```

最精确方法并带**置信值**（bootstrap）

```mashtree_bootstrap.pl --reps [100] --numcpus [12] [*.fastq.gz] -- --min-depth 0 > [mashtree.bootstrap.dnd]```

# SYNOPSIS

**mashtree** [_options_] _genome_files_...

# PARAMETERS

**--numcpus _n_**
> 用于并行处理的 CPU 线程数

**--mindepth _n_**
> k-mer 计数的最小深度（0 表示最高精度）

**--genomesize _size_**
> 用于 sketch 计算的估计基因组大小

**--truncLength _n_**
> 将序列名截断到该长度

**--outtree _file_**
> 树的输出文件（默认：stdout）

# DESCRIPTION

**mashtree** 使用 MinHash sketch 快速从基因组序列创建距离树。它基于 k-mer 相似度计算基因组之间的两两距离，并构建邻接法（neighbor-joining）树。

该工具接受 FASTA、FASTQ 及两种格式的压缩版本（.gz）。它内部使用 Mash 算法进行高效的基于 sketch 的距离计算，因此适用于数千个基因组。

输出为 Newick 格式（.dnd），与各种树可视化工具兼容。注意 mashtree 创建的是距离树而非系统发生树——它展示的是相似性关系，而不是演化历史。

# CAVEATS

不适用于正式的系统发生分析；演化研究请使用正规的系统发生学方法。精度取决于基因组的完整性和质量。差异极大的序列可能产生不可靠的树。内存占用随被比较基因组数量增长。

# HISTORY

Mashtree 由 CDC（美国疾病控制与预防中心）的 Lee Katz 开发，用于公共卫生微生物学中的快速疫情分析和基因组聚类。

# SEE ALSO
