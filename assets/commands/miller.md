# TAGLINE

类似 awk、sed、cut、join 和 sort，但面向 CSV 等以名称索引的数据

# TLDR

**将 CSV 转换为 JSON**

```mlr --csv --ojson cat [file.csv]```

**过滤记录**

```mlr --csv filter '$[field] > [10]' [file.csv]```

**选择列**

```mlr --csv cut -f [name,age] [file.csv]```

**按字段排序**

```mlr --csv sort -f [age] [file.csv]```

**聚合统计**

```mlr --csv stats1 -a sum,mean -f [value] -g [category] [file.csv]```

**转换字段**

```mlr --csv put '$[total] = $[price] * $[quantity]' [file.csv]```

# SYNOPSIS

**mlr** [_options_] _verb_ [_verb-options_] _files_...

# PARAMETERS

**--csv**
> CSV 输入格式。

**--json**
> JSON 输入格式。

**--ojson**
> JSON 输出格式。

**--icsv --ojson**
> CSV 输入，JSON 输出。

**cat**
> 原样传递记录。

**filter**
> 选择匹配的记录。

**cut**
> 选择字段。

**sort**
> 对记录排序。

**put**
> 添加/修改字段。

**stats1**
> 聚合统计。

# DESCRIPTION

**Miller**（mlr）就像面向 CSV、TSV 和 JSON 等以名称索引的数据的 awk、sed、cut、join 和 sort。它专为在命令行处理结构化文本数据而设计。

Miller 用一致的语法处理异构数据格式。

# FORMAT CONVERSION

```bash
mlr --icsv --ojson cat data.csv
mlr --ijson --ocsv cat data.json
mlr --csv --opprint cat data.csv
```

# CAVEATS

DSL 语法与 awk 不同。字段名区分大小写。大文件采用流式处理。

# HISTORY

Miller 由 **John Kerl** 于 **2015 年**开始开发，旨在提供一个统一的结构化文本处理工具。

# INSTALL

```dnf: sudo dnf install miller```

```pacman: sudo pacman -S miller```

```zypper: sudo zypper install miller```

```brew: brew install miller```

```nix: nix profile install nixpkgs#miller```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [awk](/man/awk)(1), [csvkit](/man/csvkit)(1), [xsv](/man/xsv)(1)
