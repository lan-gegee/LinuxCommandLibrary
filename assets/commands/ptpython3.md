# TAGLINE

增强版交互式 Python 3 REPL

# TLDR

**启动 Python 3 REPL**

```ptpython3```

**以 vi 模式启动**

```ptpython3 --vi```

**执行文件后进入 REPL**

```ptpython3 -i [script.py]```

# SYNOPSIS

**ptpython3** [_options_] [_file_]

# PARAMETERS

_FILE_
> 在进入 REPL 前要执行的 Python 文件。

**--vi**
> 使用 Vi 按键绑定，代替默认的 Emacs 绑定。

**-i**, **--interactive**
> 执行 _FILE_ 后进入交互式 REPL。

**--asyncio**
> 运行 asyncio 事件循环，使顶层 _await_ 表达式可用。

**--light-bg**
> 使用针对浅色背景终端调校的配色方案。

**--dark-bg**
> 使用针对深色背景终端调校的配色方案。

**--config-file** _PATH_
> 从非默认文件加载配置。

**--history-file** _PATH_
> 将输入历史保存到指定文件。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**ptpython3** 是 ptpython 的 Python 3 变体——一款基于 **prompt_toolkit** 库构建的增强型交互式 REPL，具备语法高亮、自动补全、多行编辑和 vi/emacs 按键绑定。

在 Python 3 为默认版本的现代系统上，**ptpython** 与 **ptpython3** 通常完全相同。单独的二进制文件是为同时安装了 Python 2 和 Python 3 的系统准备的。

# CONFIGURATION

**$PTPYTHON_CONFIG_HOME**
> 覆盖 ptpython 搜索配置文件的目录。默认为平台相关的用户配置目录（如 Linux 上的 **~/.config/ptpython/**）。

**$PYTHONSTARTUP**
> 标准 Python 环境变量；所引用的文件会在交互式提示符出现前运行。

# CAVEATS

ptpython 的 Python 3 变体；在 Python 3 为默认版本的现代系统上两者等价。仅当直接启动 ptpython 时才会读取配置文件——嵌入其他应用时无效。

# HISTORY

ptpython3 是 ptpython 的 **Python 3 变体**。

# INSTALL

```dnf: sudo dnf install ptpython3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ptpython](/man/ptpython)(1), [python3](/man/python3)(1), [ipython3](/man/ipython3)(1)
