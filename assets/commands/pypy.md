# TAGLINE

采用 JIT 编译的高速 Python 解释器

# TLDR

**运行 Python 脚本**

```pypy [script.py]```

**启动交互模式**

```pypy```

**带参数运行**

```pypy [script.py] [arg1] [arg2]```

**内联执行代码**

```pypy -c "[print('Hello')]"```

**将模块**作为脚本运行

```pypy -m [module_name]```

通过 PyPy 使用 **pip** 安装软件包

```pypy -m pip install [package]```

以启用**优化**的方式运行脚本（移除 assert 语句）

```pypy -O [script.py]```

在运行脚本**之后**进入交互模式（用于调试）

```pypy -i [script.py]```

# SYNOPSIS

**pypy** [_options_] [_script_] [_args_]

# PARAMETERS

_SCRIPT_
> 要运行的 Python 脚本。

_ARGS_
> 脚本参数。

**-c** _CODE_
> 执行代码。

**-m** _MODULE_
> 运行模块。

**-i**
> 脚本执行后进入交互模式。

**-O**
> 优化模式：移除 assert 语句并将 __debug__ 设为 False。

**-V**, **--version**
> 输出 PyPy 版本并退出。

**-u**
> stdout 和 stderr 不使用缓冲。

**-W** _arg_
> 警告控制（例如 **-Wall** 显示所有警告）。

# DESCRIPTION

**PyPy** 是一个替代的 Python 解释器，使用即时（JIT）编译器，在许多工作负载下执行速度显著快于 CPython。它兼容 Python 2.7 和 Python 3.x 语法，无需修改即可运行大多数纯 Python 代码，长时间运行的程序可获得 2-10 倍甚至更高的加速。

JIT 编译器在运行时分析代码，把频繁执行的路径编译为机器码，因此大量循环或重复计算的程序受益最大。PyPy 还通过更紧凑的对象表示对内存占用做了优化。部分 C 扩展模块可能不兼容，但基于 cffi 的扩展工作良好。

# CAVEATS

并非所有 C 扩展包都兼容；基于 cffi 的扩展工作良好，但部分 CPython C API 扩展可能不行。JIT 编译存在预热期，短命脚本可能感受不到速度提升。请使用 **pypy -m pip** 而非系统 pip 向 PyPy 环境安装软件包。

# HISTORY

PyPy 作为带有 JIT 的**高性能** Python 解释器而创建。

# INSTALL

```dnf: sudo dnf install pypy```

```pacman: sudo pacman -S pypy```

```brew: brew install pypy```

```nix: nix profile install nixpkgs#pypy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [python3](/man/python3)(1), [pip](/man/pip)(1)
