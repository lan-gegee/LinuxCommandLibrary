# TAGLINE

查询和过滤 GNU recutils 数据库记录

# TLDR

**选择 recfile 中的全部记录**

```recsel [file.rec]```

**选择满足条件的记录**

```recsel -e "[field] = '[value]'" [file.rec]```

**用多个条件选择记录**

```recsel -e "[field1] = '[value]' && [field2] > [number]" [file.rec]```

**只选择特定字段**

```recsel -p [field1],[field2] [file.rec]```

**选择特定类型的记录**

```recsel -t [record_type] [file.rec]```

**统计匹配的记录数**

```recsel -c -e "[condition]" [file.rec]```

**按字段排序记录**

```recsel -S [field] [file.rec]```

# SYNOPSIS

**recsel** [_options_] [**-e** _expression_] [**-t** _type_] [_file_...]

# PARAMETERS

**-e** _expression_
> 选择与表达式匹配的记录

**-t** _type_
> 只选择指定类型的记录

**-p** _fields_
> 只输出指定字段（逗号分隔）

**-P** _fields_
> 输出指定字段但不带记录分隔符

**-c**, **--count**
> 输出匹配记录的数量

**-C**, **--collapse**
> 将多个字段值合并为一个

**-S** _field_
> 按指定字段排序记录

**-G** _field_
> 按指定字段分组记录

**-n** _max_
> 最多返回 max 条记录

**-R** _random_
> 返回随机记录

**-d**, **--print-descriptors**
> 打印记录描述符

# DESCRIPTION

**recsel** 是 GNU Recutils 的组成部分。GNU Recutils 是一套使用 rec 格式管理纯文本数据库的工具。它基于表达式和条件从 recfile 中选择并打印记录。

Recfile 是人类可读的文本文件，每条记录是一组命名字段，以空行分隔。该格式简单、可用 git 进行版本控制，并且可以用任何文本编辑器编辑。

选择表达式支持比较运算符（=、!=、<、>、<=、>=）、逻辑运算符（&&、||、!）、模式匹配（~）以及字段存在性检查。表达式作用于每条记录内的字段值。

输出可用 **-p** 限制为特定字段，用 **-S** 排序，用 **-n** 限制数量。使用 **-t** 可以处理单个文件中的多种记录类型。

# EXPRESSION SYNTAX

**field = "value"**: 字符串精确匹配
**field ~ "pattern"**: 正则表达式匹配
**field < number**: 数值比较
**field && field2**: 逻辑与
**#field**: 字段存在
**!#field**: 字段不存在

# CAVEATS

表达式中的字段名和字符串值必须遵循 recutils 的引号规则。包含空格的字符串需要加引号。

数值比较要求字段包含有效数字。非数值会导致比较失败。

与真正的数据库相比，处理大型 recfile 可能较慢，但对于中等规模的数据，其简单性和可移植性通常比性能问题更重要。

# INSTALL

```dnf: sudo dnf install recutils```

```apk: sudo apk add recutils```

```brew: brew install recutils```

```nix: nix profile install nixpkgs#recutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[recins](/man/recins)(1), [recdel](/man/recdel)(1), [recset](/man/recset)(1), [recfmt](/man/recfmt)(1), [rec2csv](/man/rec2csv)(1)
