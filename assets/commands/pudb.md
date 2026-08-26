# TAGLINE

全屏控制台 Python 调试器

# TLDR

**调试 Python 脚本**

```pudb [script.py]```

**带参数调试**

```pudb [script.py] [arg1] [arg2]```

**从断点启动**

```python -m pudb [script.py]```

**事后调试**

```pudb --post-mortem [script.py]```

# SYNOPSIS

**pudb** [_options_] _script_ [_args_]

# PARAMETERS

**--pre-run** _command_
> 在脚本之前运行命令。

**--post-mortem**
> 在异常发生后调试。

**--steal-output**
> 捕获 stdout/stderr。

**-m** _module_
> 运行模块。

# DESCRIPTION

**pudb** 是一款基于控制台的 Python 全屏可视化调试器。它提供一个 TUI，包含代码视图、变量检查器、堆栈跟踪和断点功能。

# EXAMPLES

```bash
# Debug script
pudb myscript.py

# With arguments
pudb myscript.py --config=test

# Run as module
python -m pudb myscript.py

# Post-mortem on crash
pudb --post-mortem crashing_script.py
```

# IN-CODE BREAKPOINT

```python
import pudb; pudb.set_trace()

# Or Python 3.7+
breakpoint()  # with PYTHONBREAKPOINT=pudb.set_trace
```

# KEY BINDINGS

```
n     - Next line
s     - Step into
c     - Continue
b     - Set breakpoint
q     - Quit
?     - Help
Ctrl+p - Preferences
```

# CAVEATS

终端必须支持 curses。可能与某些终端设置冲突。仅限 Python。

# HISTORY

pudb 由 **Andreas Klöckner** 创建，作为 pdb 的可视化替代品，灵感来自 Borland 的 Turbo Debugger。

# SEE ALSO

[ipdb](/man/ipdb)(1), [gdb](/man/gdb)(1), [python](/man/python)(1)
