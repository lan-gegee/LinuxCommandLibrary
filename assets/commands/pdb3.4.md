# TAGLINE

Python 调试器

# TLDR

**调试 Python 脚本**

```python3.4 -m pdb [script.py]```

**在代码中设置断点**

```import pdb; pdb.set_trace()```

**运行事后调试**

```python3.4 -m pdb -c continue [script.py]```

# SYNOPSIS

**python3.4** **-m** **pdb** [_options_] _script_ [_args_]

# PARAMETERS

_SCRIPT_
> 要调试的 Python 脚本。

**-c** _COMMAND_
> 启动时执行命令。

调试器命令：
- **n** - 下一行
- **s** - 步入
- **c** - 继续
- **b** - 断点
- **p** - 打印
- **q** - 退出

# DESCRIPTION

**pdb** 是 Python 调试器，提供交互式调试环境。

该工具提供断点和检查功能。属于 Python 标准库的一部分。

# CAVEATS

特定于版本（3.4）。与其他版本的 pdb 相同。交互式调试器。

# HISTORY

pdb 自早期版本起就是 **Python 标准库**的一部分。

# SEE ALSO

[python](/man/python)(1), [ipdb](/man/ipdb)(1), [pudb](/man/pudb)(1)
