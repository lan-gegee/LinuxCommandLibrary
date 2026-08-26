# TAGLINE

校验并美化输出 JSON 数据

# TLDR

**美化输出 JSON**

```python -m json.tool [file.json]```

**从 stdin 格式化**

```echo '{"key":"value"}' | python -m json.tool```

**紧凑输出**

```python -m json.tool --compact [file.json]```

**排序键**

```python -m json.tool --sort-keys [file.json]```

# SYNOPSIS

**python -m json.tool** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要格式化的 JSON 文件。

**--sort-keys**
> 对对象的键排序。

**--compact**
> 紧凑输出。

**--indent** _N_
> 缩进层级。

**--no-ensure-ascii**
> 允许非 ASCII 字符。

# DESCRIPTION

**python -m json.tool** 是 Python 内置模块，用于校验和美化 JSON 数据。它从文件参数或标准输入读取 JSON，检查语法错误，并输出带有适当缩进的格式化版本以便阅读。

该工具适合快速检查 API 响应、配置文件或从其他命令管道传入的任何 JSON 输出。选项可控制键排序、缩进深度和紧凑输出模式。由于它随 Python 标准库一起提供，无需额外安装。

# CAVEATS

属于 Python 标准库。功能较为基础。

# HISTORY

json.tool 是 **Python 标准库**中用于 JSON 格式化的模块。

# SEE ALSO

[jq](/man/jq)(1), [python](/man/python)(1)
