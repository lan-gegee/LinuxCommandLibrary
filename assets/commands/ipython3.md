# TAGLINE

增强的交互式 Python shell

# TLDR

**启动 IPython shell**

```ipython3```

**在 IPython 中运行脚本**

```ipython3 [script.py]```

**以指定配置档启动**

```ipython3 --profile=[myprofile]```

**以无横幅模式运行**

```ipython3 --no-banner```

**启动 Qt 控制台**

```ipython3 qtconsole```

**启动 notebook 服务器**

```jupyter notebook```

# SYNOPSIS

**ipython3** [_options_] [_file_] [_args_]

# PARAMETERS

**--profile** _name_
> 使用指定的配置档。

**--no-banner**
> 不显示启动横幅。

**-i**
> 脚本执行后进入交互模式。

**-c** _command_
> 执行命令。

**--pdb**
> 发生异常时自动启用调试器。

**--matplotlib** _backend_
> 配置 matplotlib 后端。

**qtconsole**
> 启动 Qt 图形界面控制台。

**notebook**
> 启动 Jupyter notebook（已弃用，请使用 jupyter）。

# DESCRIPTION

**IPython** 是一个增强的交互式 Python shell。它提供语法高亮、制表符补全、魔法命令、Shell 集成和富媒体显示。

IPython 通过跨会话历史、对象内省和系统 shell 访问等特性扩展了 Python 的 REPL。它是 Jupyter notebook 背后的内核。

# MAGIC COMMANDS

```
%run script.py     Run Python file
%timeit expr       Time execution
%debug             Enter debugger
%history           Show history
%paste             Paste from clipboard
%cd                Change directory
!command           Run shell command
?object            Get help
??object           Get source code
```

# CAVEATS

与标准 Python 是分开的。某些魔法命令为 IPython 专有。notebook 界面推荐使用 Jupyter notebooks。

# HISTORY

IPython 由 **Fernando Pérez** 于 **2001 年**创建，旨在提升 Python 的交互能力。它成为 Jupyter 的基础，后者将 notebook 概念推广到多种语言。

# INSTALL

```pacman: sudo pacman -S ipython```

```apk: sudo apk add ipython```

```brew: brew install ipython```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python3](/man/python3)(1), [jupyter](/man/jupyter)(1), [bpython](/man/bpython)(1)
