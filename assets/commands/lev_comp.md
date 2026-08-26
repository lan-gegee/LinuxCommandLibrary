# TAGLINE

计算字符串之间的 Levenshtein 距离

# TLDR

**比较两个字符串并显示距离**

```lev_comp "[string1]" "[string2]"```

**比较字符串并输出详细的距离信息**

```lev_comp -d "[string1]" "[string2]"```

**不区分大小写地比较字符串**

```lev_comp -i "[String1]" "[string2]"```

# SYNOPSIS

**lev_comp** [_options_] _string1_ _string2_

# PARAMETERS

_STRING1_ _STRING2_
> 要比较的字符串。

**-d**
> 显示 Levenshtein 距离。

**-i**
> 不区分大小写进行比较。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lev_comp** 计算两个字符串之间的 Levenshtein 距离。该距离表示将一个字符串变换为另一个字符串所需的最少单字符编辑操作次数（插入、删除或替换）。

距离越小，说明两个字符串越相似。距离为零表示两者完全相同。

# CAVEATS

这是一个小众工具，标准软件仓库中未必提供。只支持简单的编辑距离，不支持加权操作或换位（transposition）。

# HISTORY

lev_comp 实现了 **Levenshtein 距离**算法。该度量由 Vladimir Levenshtein 于 1965 年定义，并以其名字命名。

# SEE ALSO

[diff](/man/diff)(1), [cmp](/man/cmp)(1)
