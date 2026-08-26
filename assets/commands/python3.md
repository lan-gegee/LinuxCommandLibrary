# TAGLINE

Python 3 编程语言解释器

# TLDR

**启动交互式** Python Shell

```python3```

**执行 Python 脚本**

```python3 [script.py]```

**执行 Python 命令**

```python3 -c "[print('Hello')]"```

**将模块**作为脚本运行

```python3 -m [module_name]```

**在当前目录启动简易 HTTP 服务器**

```python3 -m http.server [8000]```

**使用 pip 安装软件包**

```python3 -m pip install [package]```

**查看 Python 版本**

```python3 --version```

# SYNOPSIS

**python3** [_-BdEhiIOqsSuvVWx?_] [_-c command_] [_-m module_] [_-X option_] [_script_] [_args_]

# PARAMETERS

**-c** _command_
> 执行以字符串传入的 Python 代码

**-m** _module_
> 以脚本方式运行库模块

**-i**
> 脚本运行后进入交互式检查

**-B**
> 不写入 .pyc 字节码文件

**-O**
> 优化生成的字节码

**-OO**
> 在 -O 优化的基础上再移除 docstring

**-q**
> 启动时不打印版本和版权信息

**-s**
> 不把用户 site-packages 加入 sys.path

**-S**
> 不导入 site 模块

**-u**
> stdout 和 stderr 不使用缓冲

**-v**
> 详细模式（跟踪 import 语句）

**-V**, **--version**
> 打印 Python 版本并退出

**-W** _arg_
> 警告控制（error、ignore、always、default、module、once）

**-X** _option_
> 设置实现相关的选项

**-h**, **--help**
> 打印帮助信息并退出

**-E**
> 忽略 PYTHON* 环境变量

# DESCRIPTION

**python3** 是 Python 编程语言 3.x 版本的解释器。它以交互方式或从脚本文件执行 Python 代码，同时支持面向过程和面向对象编程范式。

不带参数调用时，它会启动一个交互式 REPL（Read-Eval-Print Loop），便于实验 Python 代码。以脚本文件为参数时，它执行该脚本。**-m** 选项允许把已安装的模块作为脚本运行，从而实现启动 HTTP 服务器、运行测试或用 pip 管理软件包等功能。

Python 3 是 Python 当前的主版本，相比 Python 2（已于 2020 年停止支持）改进了 Unicode 支持、print 成为函数、整数除法行为变更等众多增强。

# CAVEATS

在某些系统上 **python** 可能仍指向 Python 2；请显式使用 **python3** 以确保是第 3 版。建议使用虚拟环境（**venv**）做项目隔离。全局解释器锁（GIL）限制了真正的多线程并行。带 Windows 换行符的脚本可能出问题；必要时使用 **dos2unix**。

# HISTORY

Python 由 **Guido van Rossum** 创建，首次发布于 **1991 年**。Python 3.0 发布于 **2008 年 12 月 3 日**，引入了破坏 Python 2 向后兼容性的重大变更。过渡期持续多年，Python 2.7 于 **2020 年 1 月 1 日**正式终止支持。Python 已成长为全球最流行的编程语言之一，广泛用于 Web 开发、数据科学、人工智能、脚本编写和教育领域。

# INSTALL

```apt: sudo apt install python3-minimal```

```dnf: sudo dnf install python3```

```apk: sudo apk add python3```

```brew: brew install python3```

```nix: nix profile install nixpkgs#python3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [ipython](/man/ipython)(1), [virtualenv](/man/virtualenv)(1), [perl](/man/perl)(1), [ruby](/man/ruby)(1)
