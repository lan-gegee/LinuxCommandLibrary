# TAGLINE

高性能多序列比对程序

# TLDR

**比对序列（自动选择策略）**

```mafft --auto [input.fasta] > [aligned.fasta]```

**快速比对**

```mafft --retree 1 [input.fasta] > [aligned.fasta]```

**精确比对**

```mafft --maxiterate 1000 --localpair [input.fasta] > [aligned.fasta]```

**使用多线程**

```mafft --thread [8] --auto [input.fasta] > [aligned.fasta]```

**将序列加入现有比对**

```mafft --add [new.fasta] [existing.fasta] > [combined.fasta]```

# SYNOPSIS

**mafft** [_options_] _input_ > _output_

# PARAMETERS

**--auto**
> 自动选择策略。

**--maxiterate** _n_
> 迭代次数。

**--localpair**
> 使用 L-INS-i（精确）。

**--globalpair**
> 使用 G-INS-i。

**--thread** _n_
> 线程数。

**--add** _file_
> 加入现有比对。

**--retree** _n_
> 渐进式比对中构建进化树的迭代次数。1 较快，2 为默认值。

**--reorder**
> 按相似度重排输出序列。

**--adjustdirection**
> 必要时自动检测输入序列并进行反向互补处理。

**--quiet**
> 抑制进度消息和警告。

# DESCRIPTION

**MAFFT**（Multiple Alignment using Fast Fourier Transform，利用快速傅里叶变换的多重比对）是一款高性能的多序列比对程序。它提供多种在速度与准确性之间权衡的算法。

MAFFT 在生物信息学领域被广泛用于比对 DNA、RNA 和蛋白质序列。

# STRATEGIES

```
FFT-NS-1  - Fast, suitable for large datasets (--retree 1)
FFT-NS-2  - Default progressive method (--retree 2)
FFT-NS-i  - Iterative refinement (--maxiterate >0)
L-INS-i   - Most accurate, local alignment, <200 sequences (--localpair)
G-INS-i   - Global alignment (--globalpair)
E-INS-i   - For sequences with long unalignable regions (--genafpair)
```

# CAVEATS

内存占用随序列数量增长。超长序列可能需要调整参数。auto 模式会根据输入规模选择策略。

# HISTORY

MAFFT 由 **Kazutaka Katoh** 及其同事开发，于 **2002 年**首次发表。它是生物信息学中被引用最多的比对工具之一。

# INSTALL

```apt: sudo apt install mafft```

```brew: brew install mafft```

```nix: nix profile install nixpkgs#mafft```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[samtools](/man/samtools)(1), [bedtools](/man/bedtools)(1)
