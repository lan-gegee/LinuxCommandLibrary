# TAGLINE

解释型通用编程语言

# TLDR

**运行 Python 脚本**

```python [script.py]```

**启动交互式 REPL**

```python```

**执行代码**

```python -c "[print('Hello')]"```

**运行模块**

```python -m [module]```

**启动 HTTP 服务器**

```python -m http.server [8080]```

**检查语法**

```python -m py_compile [script.py]```

# SYNOPSIS

**python** [_options_] [_script_] [_args_]

# PARAMETERS

_SCRIPT_
> 要运行的 Python 脚本。

_ARGS_
> 脚本参数。

**-c** _CODE_
> 执行代码字符串。

**-m** _MODULE_
> 以脚本方式运行库模块。

**-i**
> 脚本执行后进入交互模式。

**-O**
> 优化字节码。

**-V**
> 显示版本。

**-u**
> 输出不使用缓冲。

# DESCRIPTION

**python** 是 Python 编程语言的解释器，可执行脚本或启动交互式 REPL 会话。它支持面向过程、面向对象和函数式编程风格，广泛用于脚本编写、Web 开发、数据分析、自动化和科学计算。

不带参数调用时，它会启动一个用于实验的交互式读-求值-输出循环（REPL）。以脚本文件为参数时，它编译并执行代码。**-m** 标志把已安装的模块作为脚本运行，从而启用内置工具，如 HTTP 服务器、JSON 格式化器和通过 pip 的包管理。在许多系统上 **python** 可能指向 Python 2；请显式使用 **python3** 来使用 Python 3。

# CAVEATS

Python 2 与 3 存在差异。Python 3 请使用 python3。

# HISTORY

Python 由 **Guido van Rossum** 于 1991 年创建。

# INSTALL

```dnf: sudo dnf install python3```

```pacman: sudo pacman -S python```

```apk: sudo apk add python3```

```brew: brew install python3```

```nix: nix profile install nixpkgs#python3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python3](/man/python3)(1), [pip](/man/pip)(1), [pydoc](/man/pydoc)(1)
