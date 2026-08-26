# TAGLINE

基于最大似然法的系统发育树推断

# TLDR

**基础系统发育分析**

```raxml -s [alignment.phy] -n [output_name] -m GTRGAMMA```

**快速自助法分析**

```raxml -f a -s [alignment.phy] -n [run] -m GTRGAMMA -x [12345] -N [100]```

**简约法起始树**

```raxml -y -s [alignment.phy] -n [parsimony] -m GTRGAMMA```

**多线程**

```raxmlHPC-PTHREADS -T [4] -s [alignment.phy] -n [run] -m GTRGAMMA```

# SYNOPSIS

**raxml** [_options_] **-s** _alignment_ **-n** _name_

# PARAMETERS

**-s** _file_
> 比对文件（PHYLIP 格式）。

**-n** _name_
> 输出文件名。

**-m** _model_
> 替换模型。

**-f** _algorithm_
> 要执行的算法。

**-x** _seed_
> 自助法的随机种子。

**-N** _num_
> 运行/自助法次数。

**-T** _threads_
> 线程数（PTHREADS 版本）。

**-p** _seed_
> 简约法随机种子。

# DESCRIPTION

**RAxML**（Randomized Axelerated Maximum Likelihood）使用最大似然法推断系统发育树。它广泛应用于进化生物学的大规模系统发育分析。

# EXAMPLES

```bash
# ML search
raxml -s alignment.phy -n result -m GTRGAMMA -p 12345

# Rapid bootstrap + ML search
raxml -f a -s alignment.phy -n boot -m GTRGAMMA -x 12345 -p 12345 -N 100

# Protein sequences
raxml -s proteins.phy -n protein_tree -m PROTGAMMAAUTO

# Partitioned analysis
raxml -s alignment.phy -q partitions.txt -n partitioned -m GTRGAMMA
```

# MODELS

```
GTRGAMMA      - GTR + Gamma (DNA)
PROTGAMMAAUTO - Auto-select protein model
GTRCAT        - Faster approximation
```

# CAVEATS

计算量大。大型数据集请使用 raxmlHPC-PTHREADS 或 MPI 版本。已被 RAxML-NG 取代。

# HISTORY

RAxML 由 **Alexandros Stamatakis** 开发，用于高性能系统发育推断，于 2004 年首次发布。

# INSTALL

```nix: nix profile install nixpkgs#raxml```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iqtree](/man/iqtree)(1)
