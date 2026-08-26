# TAGLINE

解析并校验 JSON 输入

# TLDR

**解析通用 JSON**

```cat [file.json] | jc --json```

**校验 JSON**

```jc --json < [file.json]```

**以美化格式解析**

```jc --json -p < [file.json]```

**解析 JSON Lines**

```jc --jsonl < [file.jsonl]```

# SYNOPSIS

**jc** **--json** [_options_]

# PARAMETERS

**--json**
> 解析 JSON 输入。

**--jsonl**
> 解析 JSON Lines 格式。

**-p**, **--pretty**
> 美化输出。

**-r**, **--raw**
> 原始输出模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jc --json** 用于解析和校验 JSON 输入。它是 jc 中的 JSON 直通解析器，用于格式校验和规范化。

该解析器从 stdin 接受 JSON 并输出格式化的 JSON。适用于校验或重新格式化 JSON 数据。

# CAVEATS

是 jc 工具集的一部分。JSON 直通解析器。主要用于校验/格式化。

# HISTORY

这个 JSON 解析器被添加到 **jc** 中，使解析器的集合更加完整，包括对 JSON 输入的处理。

# SEE ALSO

[jc](/man/jc)(1), [jq](/man/jq)(1), [jsonlint](/man/jsonlint)(1)
