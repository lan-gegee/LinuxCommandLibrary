# TAGLINE

按列值过滤 TSV 文件

# TLDR

**按列值过滤**

```tsv-filter --eq [1]:[value] [file.tsv]```

**大于**

```tsv-filter --gt [2]:[100] [file.tsv]```

**字符串包含**

```tsv-filter --str-in-fld [1]:[pattern] [file.tsv]```

**多个条件**

```tsv-filter --ge [2]:[10] --le [2]:[100] [file.tsv]```

**反转过滤结果**

```tsv-filter --invert --eq [1]:[value] [file.tsv]```

# SYNOPSIS

**tsv-filter** [_--eq col:val_] [_--gt col:val_] [_options_] [_file_]

# PARAMETERS

**--eq** _COL:VAL_
> 等于指定值。

**--gt** _COL:VAL_
> 大于。

**--lt** _COL:VAL_
> 小于。

**--str-in-fld** _COL:PAT_
> 字符串包含。

**--invert**
> 反转匹配结果。

**-H**
> 含有表头。

# DESCRIPTION

**tsv-filter** 根据列条件从制表符分隔值文件中筛选行。它既支持数值比较（等于、大于、小于），也支持字符串操作（包含、精确匹配），可以对结构化数据进行精确过滤。

多个条件可以组合使用，默认以 AND 逻辑连接——所有条件都匹配时该行才会被选中。**--invert** 选项会反转筛选结果，改为输出不匹配的行。

tsv-filter 属于 **tsv-utils** 工具集，用 D 语言编写，在大数据集上具有高性能。列号从 1 开始计数，**-H** 选项启用对表头的感知处理。

# CAVEATS

仅支持 TSV 格式。列号从 1 开始。属于 tsv-utils 工具集。

# HISTORY

**tsv-filter** 是 **tsv-utils** 的一部分，后者是一组面向 TSV 文件的高性能命令行工具。

# SEE ALSO

[awk](/man/awk)(1), [cut](/man/cut)(1), [miller](/man/miller)(1)
