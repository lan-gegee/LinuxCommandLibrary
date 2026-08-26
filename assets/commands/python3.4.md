# TAGLINE

带 asyncio 和 pathlib 的 Python 3.4 解释器

# TLDR

**运行 Python 3.4 脚本**

```python3.4 [script.py]```

**交互模式**

```python3.4```

**执行命令**

```python3.4 -c "[print('hello')]"```

**运行模块**

```python3.4 -m [module]```

# SYNOPSIS

**python3.4** [_options_] [_script_] [_args_]

# PARAMETERS

**-c** _command_
> 执行命令。

**-m** _module_
> 以脚本方式运行库模块。

**-i**
> 脚本执行后进入交互模式。

**-u**
> I/O 不使用缓冲。

**-O**
> 优化字节码。

**-B**
> 不写入字节码。

**-v**
> 导入过程详细输出。

**-V**
> 打印版本。

# DESCRIPTION

**python3.4** 是 Python 3.4 解释器。Python 3.4 发布于 2014 年，引入了 asyncio、enum、pathlib 等特性。现已被更新的 Python 3 版本取代。

# EXAMPLES

```bash
# Run script
python3.4 myscript.py

# Check version
python3.4 --version

# Create virtual environment
python3.4 -m venv myenv

# Run simple server
python3.4 -m http.server 8000
```

# FEATURES IN 3.4

```python
import asyncio         # Async I/O
import enum            # Enumerations
import pathlib         # Object-oriented paths
import statistics      # Basic statistics
import selectors       # I/O multiplexing
```

# CAVEATS

Python 3.4 已终止支持（2019 年 3 月）。当前开发请使用 Python 3.10+。旧版本缺少安全更新。

# HISTORY

Python 3.4 发布于 2014 年 3 月 16 日。每个 Python 版本约有 5 年的支持周期。

# SEE ALSO

[python3](/man/python3)(1), [pip](/man/pip)(1), [venv](/man/venv)(1)
