# TAGLINE

将 GNU recutils 记录导出为 CSV 格式

# TLDR

**将 recfile 转换为 CSV**

```rec2csv [file.rec] > [output.csv]```

**选择特定字段**

```rec2csv -f [field1,field2] [file.rec]```

**选择记录类型**

```rec2csv -t [Type] [file.rec]```

**包含表头**

```rec2csv -H [file.rec]```

# SYNOPSIS

**rec2csv** [_options_] [_file_]

# PARAMETERS

**-t**, **--type** _type_
> 选择记录类型。

**-f**, **--fields** _fields_
> 要输出的字段（逗号分隔）。

**-H**, **--headers**
> 包含列标题。

**-s**, **--sort** _field_
> 按字段排序。

**-n**, **--num** _n_
> 限制记录数量。

# DESCRIPTION

**rec2csv** 将 GNU recutils 纯文本数据库文件转换为 CSV 格式，便于导入电子表格、数据库或其他处理表格数据的工具。它读取 recfile 记录（以空行分隔的键值对结构），并将其输出为逗号分隔的行，可通过 **-H** 标志可选地包含列标题。

当 recfile 包含多种记录类型时，**-t** 标志可选择特定类型；**-f** 将输出限制为指定字段。它可与 **recsel** 在管道中组合，先过滤记录再转换为 CSV。属于 GNU recutils 工具集。

# EXAMPLES

```bash
# Basic conversion
rec2csv contacts.rec > contacts.csv

# With headers
rec2csv -H books.rec > books.csv

# Select fields
rec2csv -f Name,Email,Phone contacts.rec

# Specific type
rec2csv -t Book -f Title,Author library.rec

# With selection
recsel -e "Price > 10" items.rec | rec2csv -H
```

# RECFILE FORMAT

```
Name: John Doe
Email: john@example.com
Phone: 555-1234

Name: Jane Smith
Email: jane@example.com
Phone: 555-5678
```

# CAVEATS

多行字段值可能需要特殊处理。属于 GNU recutils 软件包。

# HISTORY

rec2csv 是 **Jose E. Marchesi** 开发的 **GNU recutils** 的组成部分，用于管理纯文本数据库。

# INSTALL

```dnf: sudo dnf install recutils```

```apk: sudo apk add recutils```

```brew: brew install recutils```

```nix: nix profile install nixpkgs#recutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[recsel](/man/recsel)(1), [recins](/man/recins)(1), [recdel](/man/recdel)(1)
