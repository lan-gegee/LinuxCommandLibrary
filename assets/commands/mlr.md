# TAGLINE

处理结构化文本数据

# TLDR

**将 CSV 转换为 JSON**

```mlr --csv --ojson cat [data.csv]```

**过滤记录**

```mlr --csv filter '$status == "active"' [data.csv]```

**选择字段**

```mlr --csv cut -f [name,email] [data.csv]```

**排序记录**

```mlr --csv sort -f [age] [data.csv]```

**计算统计值**

```mlr --csv stats1 -a mean -f [price] [data.csv]```

**变换字段**

```mlr --csv put '$total = $price * $quantity' [data.csv]```

# SYNOPSIS

**mlr** [_options_] _verbs_ _file_

# PARAMETERS

_VERBS_
> 要执行的操作。

**--csv**
> CSV 格式。

**--json**
> JSON 格式。

**--ojson**
> 以 JSON 输出。

**filter**
> 过滤记录。

**cut**
> 选择字段。

**sort**
> 排序记录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mlr**（Miller）处理结构化文本数据，支持 CSV、JSON 等格式。

该工具为结构化数据提供类似 awk 的处理能力，非常适合数据变换。

# CAVEATS

动词（verb）众多，需要学习。能感知格式。已用 Go 重写。

# HISTORY

Miller 由 **John Kerl** 创建，定位是"面向按名称索引的数据的 awk/sed/cut"。

# INSTALL

```apt: sudo apt install miller```

```dnf: sudo dnf install miller```

```pacman: sudo pacman -S miller```

```apk: sudo apk add miller```

```zypper: sudo zypper install miller```

```brew: brew install miller```

```nix: nix profile install nixpkgs#miller```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [awk](/man/awk)(1), [csvtool](/man/csvtool)(1)
