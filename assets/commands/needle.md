# TAGLINE

Needleman-Wunsch 全局双序列比对（EMBOSS）

# TLDR

对来自 FASTA 文件的两条序列进行**全局比对**

```needle -asequence [seq1.fasta] -bsequence [seq2.fasta] -gapopen [10] -gapextend [0.5] -outfile [out.needle]```

**按数据库登录号比对**（如 UniProt）

```needle -asequence sp:[hba_human] -bsequence sp:[hbb_human] -gapopen [10] -gapextend [0.5] -outfile [result.needle]```

**使用指定的打分矩阵**

```needle -asequence [a.fa] -bsequence [b.fa] -datafile [EBLOSUM62] -gapopen [10] -gapextend [0.5] -outfile [out.needle]```

**选择其他输出格式**

```needle -asequence [a.fa] -bsequence [b.fa] -gapopen [10] -gapextend [0.5] -aformat3 [markx10] -outfile [out.txt]```

**非交互运行**（无提示）

```needle -auto -asequence [a.fa] -bsequence [b.fa] -gapopen [10] -gapextend [0.5] -outfile [a_vs_b.needle]```

# SYNOPSIS

**needle** **-asequence** _seqfile_ **-bsequence** _seqfile_ **-gapopen** _f_ **-gapextend** _f_ **-outfile** _file_ [_options_]

# PARAMETERS

**-asequence** _file_
> 第一条输入序列（单条序列，支持任何 EMBOSS 认可的格式）。

**-bsequence** _file_
> 第二条输入序列（一条或多条，将与第一条比对）。

**-gapopen** _float_
> 开启空位的罚分（典型值：蛋白质 10.0，DNA 10.0）。

**-gapextend** _float_
> 延伸已有空位的罚分（典型值：0.5）。

**-datafile** _matrix_
> 打分矩阵名称（如 _EBLOSUM62_、_EDNAFULL_）。

**-endweight**
> 对末端空位施加罚分（默认 false；末端空位不罚分）。

**-outfile** _file_
> 比对报告的输出路径。

**-aformat3** _format_
> 输出比对格式（_pair_、_markx0_..._markx10_、_msf_、_fasta_ 等）。

**-brief**
> 打印简要的比对摘要而非完整的成对比对视图。

**-auto**
> 跳过所有交互提示（适合脚本）。

# DESCRIPTION

**needle** 使用 **Needleman-Wunsch** 动态规划算法计算两条序列的最优**全局**双序列比对。它随 **EMBOSS**（European Molecular Biology Open Software Suite）一起发布，适用于长度相近、需要端到端完整比对的核苷酸或蛋白质序列。

空位开启罚分（gap-open）和空位延伸罚分（gap-extend）是决定比对结果的必填参数，打分矩阵（BLOSUM、PAM、EDNAFULL 等）则决定匹配与错配的权重。输出为格式化的比对报告，包含得分、长度、一致性百分比、相似性和空位统计；通过 **-aformat3** 可选择多种其他格式。

若要比较子序列请用局部比对工具 **water**；对于内存吃紧的超长序列请用 **stretcher**，它实现了该算法的线性空间变体。

# CAVEATS

时间与内存复杂度是两条序列长度的 O(m·n)，因此 **needle** 不适合超长序列——请改用 **stretcher**。选项语法为 EMBOSS 专有格式（单破折号引导的长名称），不能与 GNU 风格的标志互换。末端空位默认不计罚分；如需惩罚末端空位请启用 **-endweight**。

# HISTORY

**needle** 由 **Alan Bleasby** 编写，是 **EMBOSS** 项目的一部分。EMBOSS 于 **1996 年**在 **Sanger Centre / MRC** 启动，旨在提供一套开放、集成的生物信息学工具。Needleman-Wunsch 算法本身由 **Saul B. Needleman** 和 **Christian D. Wunsch** 于 **1970 年**发表。

# INSTALL

```apt: sudo apt install emboss```

```brew: brew install needle```

```nix: nix profile install nixpkgs#emboss```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blastp](/man/blastp)(1)
