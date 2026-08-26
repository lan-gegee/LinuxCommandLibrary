# TAGLINE

解析 JSON5 格式并输出标准 JSON

# TLDR

**将 JSON5 解析为 JSON**

```json5 [file.json5]```

**从 stdin 转换**

```echo '{name: "test"}' | json5```

**格式化输出**

```json5 --space [2] [file.json5]```

**仅校验**

```json5 --validate [file.json5]```

**用制表符缩进**

```json5 --space t [file.json5]```

**转换并写入文件**

```json5 --out-file [output.json] [file.json5]```

# SYNOPSIS

**json5** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要解析的 JSON5 文件。省略时从 stdin 读取。

**-s**, **--space** _N_
> 缩进空格数，"t" 表示制表符。

**-v**, **--validate**
> 仅校验 JSON5 语法，不输出 JSON。

**-o**, **--out-file** _FILE_
> 将结果写入文件而非 stdout。

**-V**, **--version**
> 显示版本号。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**json5** 解析 JSON5 格式并输出标准 JSON。JSON5 是 JSON 的扩展，支持注释、尾随逗号和不带引号的键。

该工具将可读性更好的 JSON5 配置转换为严格的 JSON。它可以校验并格式化 JSON5 输入。

# CAVEATS

Node.js 工具。JSON5 是 JSON 的超集。输出为标准 JSON。

# HISTORY

json5 实现了 **JSON5** 规范，该规范旨在让 JSON 对配置文件场景更加友好。

# INSTALL

```brew: brew install json5```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [json_pp](/man/json_pp)(1), [jsonlint](/man/jsonlint)(1)
