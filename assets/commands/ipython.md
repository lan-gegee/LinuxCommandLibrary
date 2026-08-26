# TAGLINE

增强的交互式 Python shell

# TLDR

**启动 IPython**

```ipython```

**运行脚本**

```ipython [script.py]```

**以指定配置档启动**

```ipython --profile=[name]```

**执行代码并进入交互式 shell**

```ipython -i -c "[import numpy as np; arr = np.array([1,2,3])]"```

**启动时不显示启动横幅**

```ipython --no-banner```

**创建命名配置档**

```ipython profile create [name]```

**发生异常时启动调试器**

```ipython --pdb```

# SYNOPSIS

**ipython** [_options_] [_files_...]

# DESCRIPTION

**ipython**（Interactive Python）是一个增强的 Python shell，通过一系列面向高效探索式编程的特性扩展了标准解释器。它提供自动语法高亮、针对对象、模块和文件路径的全面制表符补全、用 `?` 和 `??` 后缀访问内联文档字符串，以及跨会话保留的可搜索输入历史。

一个显著特性是 IPython 的魔法命令系统——以 `%`（行魔法）或 `%%`（单元魔法）为前缀的特殊指令——它们提供超出常规 Python 语法的功能，例如用于基准测试的 `%timeit`、执行脚本的 `%run`、事后调试的 `%debug`，以及能正确处理剪贴板中缩进代码的 `%paste`。IPython 还与科学计算 Python 生态系统深度集成，可通过 `--pylab` 可选地自动导入 NumPy 和 Matplotlib，并充当 Jupyter notebook 的默认内核。

# PARAMETERS

**-i**
> 脚本执行后进入交互式检查。

**-c** _code_
> 执行代码。

**--profile** _name_
> 使用指定配置档。

**--colors** _scheme_
> 配色方案。

**--no-banner**
> 不显示启动横幅。

**--automagic**
> 启用不带 % 前缀调用魔法命令。

**--pdb**
> 发生异常时启动调试器。

**--pylab** [_backend_]
> 加载 numpy 和 matplotlib。

**--matplotlib** [_backend_]
> 加载 matplotlib。

# MAGIC COMMANDS

**%run**: 执行脚本
**%timeit**: 计时
**%debug**: 事后调试
**%history**: 显示历史
**%load**: 从文件加载代码
**%edit**: 在外部编辑器中编辑

# CONFIGURATION

**~/.ipython/profile_default/ipython_config.py**
> 默认配置档，可用于自定义启动行为、魔法命令、扩展和按键绑定。

# CAVEATS

比标准 Python 更重。魔法命令不是合法的 Python 语法。配置档配置在大版本升级之间可能需要迁移。**ipython notebook** 子命令已被移除，请改用 **jupyter notebook**。

# HISTORY

**IPython** 由 **Fernando Perez** 于 **2001 年**创建，旨在改善 Python 的交互体验。它后来演化为 Jupyter 项目，IPython 则继续作为其中的 Python 内核。它已成为科学计算 Python 生态的重要基础设施。

# INSTALL

```pacman: sudo pacman -S ipython```

```apk: sudo apk add ipython```

```brew: brew install ipython```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [jupyter](/man/jupyter)(1), [bpython](/man/bpython)(1), [ptpython](/man/ptpython)(1)
