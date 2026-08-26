# TAGLINE

IPython 增强的 Python 调试器

# TLDR

**启动 ipdb 调试器**

```python -m ipdb [script.py]```

**在代码中设置断点**

```import ipdb; ipdb.set_trace()```

**事后调试**

```python -m ipdb -c continue [script.py]```

**运行直到发生异常**

```ipdb.pm()```

# SYNOPSIS

**python -m ipdb** [_options_] _script_ [_args_]

# PARAMETERS

**-c** _command_
> 启动时执行命令。

_script_
> 要调试的 Python 脚本。

# DEBUGGER COMMANDS

```
n (next)      Execute next line
s (step)      Step into function
c (continue)  Continue execution
r (return)    Return from function
l (list)      List source code
p expr        Print expression
pp expr       Pretty-print expression
b line        Set breakpoint
cl            Clear breakpoints
q (quit)      Quit debugger
h (help)      Show help
```

# DESCRIPTION

**ipdb** 是 IPython 增强的 Python 调试器。它提供与 pdb 相同的接口，但借助 IPython 具备语法高亮、制表符补全和更强的内省能力。

ipdb 让 Python 调试更具交互性、更友好，尤其适合查看变量和理解程序状态。

# USAGE IN CODE

```python
import ipdb

def problematic_function():
    x = calculate_something()
    ipdb.set_trace()  # Debugger starts here
    return process(x)
```

# CAVEATS

需要 ipython 软件包。断点会暂停程序执行。不要把 set_trace() 留在生产代码中。在 Python 3.7+ 中可使用 breakpoint() 并设置 PYTHONBREAKPOINT=ipdb.set_trace。

# HISTORY

ipdb 作为 pdb 的直接替代品而创建，充分利用了 IPython 的特性。它在保留 pdb 熟悉接口的同时增强了易用性。

# SEE ALSO

[ipython](/man/ipython)(1), [pudb](/man/pudb)(1)
