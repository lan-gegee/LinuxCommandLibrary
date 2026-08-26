# TAGLINE

校验并格式化 JSON 文件

# TLDR

**校验 JSON 文件**

```jsonlint [file.json]```

**以静默模式校验**

```jsonlint -q [file.json]```

**校验并格式化**

```jsonlint -i [file.json]```

**紧凑输出**

```jsonlint -c [file.json]```

**排序键**

```jsonlint -s [file.json]```

**校验多个文件**

```jsonlint [file1.json] [file2.json]```

# SYNOPSIS

**jsonlint** [_options_] [_files_...]

# PARAMETERS

**-q**, **--quiet**
> 无输出，仅返回退出码。

**-c**, **--compact**
> 紧凑输出。

**-i**, **--in-place**
> 格式化并覆盖原文件。

**-s**, **--sort-keys**
> 排序对象键。

**-t** _chars_
> 用于缩进的制表符字符。

**-e** _env_
> 从环境变量获取输入。

**-p**, **--pretty-print**
> 格式化输出。

**-V**, **--validate**
> 仅校验，无输出。

# DESCRIPTION

**jsonlint** 校验并格式化 JSON 文件。它检查语法错误，并能对 JSON 数据进行格式化打印或紧凑输出。

该工具适用于校验配置文件、API 响应和数据文件。对于格式有误的 JSON，它会给出清晰的错误信息。

# VALIDATION ERRORS

```
$ jsonlint bad.json
Error: Parse error on line 3:
...  "name": "test"  "value": 42
---------------------^
Expecting 'EOF', '}', ',', ']', got 'STRING'
```

# CAVEATS

存在多种实现（Node.js、Python）。不支持按 JSON Schema 校验。不支持注释（JSON 规范如此）。

# HISTORY

jsonlint 有多种实现。这一概念源于 JavaScript 的 linting 工具。流行的实现包括 Zach Carter 开发的 npm jsonlint 软件包。

# INSTALL

```brew: brew install jsonlint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1)
