# TAGLINE

祖先序列重建与分子钟分析

# TLDR

推断祖先序列

```treetime ancestral```

分析同塑性

```treetime homoplasy```

估计分子钟

```treetime clock```

将离散特征映射到树

```treetime mugration```

# SYNOPSIS

**treetime** _COMMAND_ [_OPTIONS_]

# COMMANDS

**ancestral**
> 以最大似然法推断祖先序列

**homoplasy**
> 分析反复突变模式

**clock**
> 估计分子钟参数并重设树的根

**mugration**
> 将离散特征（宿主、国家）映射到树上

# DESCRIPTION

**treetime** 提供祖先序列重建和分子钟系统发育推断的例程。它用于系统发育分析，以理解进化关系和分化事件的时间。

该工具可以重建祖先序列、检测同塑性（趋同进化）、估计突变率，以及将地理或宿主信息映射到系统发育树上。

# CAVEATS

需要提供系统发育树和序列比对输入。对大型数据集计算量大。结果依赖于模型假设。

# HISTORY

**treetime** 为分子流行病学和进化生物学中的系统发育分析而开发，提供了理解病原体进化和传播的工具。

# SEE ALSO

[iqtree](/man/iqtree)(1), [raxml](/man/raxml)(1)
