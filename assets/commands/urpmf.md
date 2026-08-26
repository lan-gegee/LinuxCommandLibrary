# TAGLINE

搜索 Mageia 软件包文件和元数据

# TLDR

搜索包含某**文件**的软件包

```urpmf [filename]```

以 AND 方式搜索**摘要**

```urpmf --summary [keyword1] -a [keyword2]```

以 OR 方式搜索**描述**

```urpmf --description [keyword1] -o [keyword2]```

使用**排除**条件搜索

```urpmf --description ! [keyword] -F'|'```

# SYNOPSIS

**urpmf** [_OPTIONS_] _PATTERN_

# PARAMETERS

**--summary**
> 在软件包摘要中搜索

**--description**
> 在软件包描述中搜索

**-a**
> 模式之间的 AND 运算符

**-o**
> 模式之间的 OR 运算符

**!**
> 取反（排除匹配结果）

**-F** _SEP_
> 字段分隔符（默认为冒号）

# DESCRIPTION

**urpmf** 用于在 Mageia Linux 中查找软件包内的文件并查询其相关信息。它可以按文件名、摘要或描述进行搜索，并支持布尔运算符。

属于 Mageia 的 urpmi 软件包管理套件。

# CAVEATS

Mageia 专用。会搜索所有已配置的介质。大规模查询可能需要一些时间处理。

# SEE ALSO

[urpmi](/man/urpmi)(8), [urpmq](/man/urpmq)(8)
