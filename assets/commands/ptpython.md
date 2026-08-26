# TAGLINE

增强版交互式 Python REPL

# TLDR

**启动 Python REPL**

```ptpython```

**以 vi 模式启动**

```ptpython --vi```

**执行文件后进入 REPL**

```ptpython -i [script.py]```

**以 IPython 模式启动**

```ptipython```

# SYNOPSIS

**ptpython** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要执行的 Python 文件。

**--vi**
> 使用 Vi 风格按键绑定，代替 Emacs（默认）。

**-i**, **--interactive**
> 运行给定脚本后进入 REPL。

**--light-bg**
> 为浅色背景终端优化配色。

**--dark-bg**
> 为深色背景终端优化配色。

**--config-file** _FILE_
> 使用指定的 Python 配置文件代替默认配置。

**--history-file** _FILE_
> 使用自定义的历史文件位置。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**ptpython** 是基于 **prompt_toolkit** 库构建的增强版 Python REPL。它提供语法高亮、多行编辑、自动补全、鼠标支持和 vi/emacs 按键绑定，交互体验显著优于默认的 Python shell。

功能包括函数签名提示、输入验证、剪贴板支持，以及将 ptpython 嵌入现有应用的能力。**ptipython** 变体则将 ptpython 的界面与 IPython 的魔法命令和特性结合在一起。

# CONFIGURATION

**~/.config/ptpython/config.py**
> 用于自定义按键绑定、配色方案、补全行为和其他 REPL 设置的 Python 配置文件。

# CAVEATS

需要安装。基于 prompt_toolkit。

# HISTORY

ptpython 作为具备现代特性的**增强版 Python REPL** 而创建。

# INSTALL

```brew: brew install ptpython```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [ipython](/man/ipython)(1), [bpython](/man/bpython)(1)
