# TAGLINE

为任意命令添加 readline 编辑功能

# TLDR

**为命令添加 readline 支持**

```rlwrap [command]```

**使用历史文件**

```rlwrap -H [~/.command_history] [command]```

**使用补全文件**

```rlwrap -f [completions.txt] [command]```

**始终启用 readline**（即使连接到终端）

```rlwrap -a [command]```

**记住多行输入**

```rlwrap -m [command]```

**引用特殊字符**

```rlwrap -q '"' [command]```

**不区分大小写的补全**

```rlwrap -i [command]```

# SYNOPSIS

**rlwrap** [_-a_] [_-H file_] [_-f file_] [_-i_] [_options_] _command_ [_args_]

# PARAMETERS

**-a**, **--always-readline**
> 始终使用 readline。

**-H** _FILE_
> 历史文件。

**-f** _FILE_
> 补全文件。

**-i**, **--case-insensitive**
> 不区分大小写的补全。

**-m** [_CHAR_]
> 多行模式。

**-q** _CHAR_
> 引用字符。

**-c**, **--complete-filenames**
> 补全文件名。

**-r**, **--remember**
> 记住输入内容用于补全。

**-p** _PROMPT_
> 提示符颜色。

**-b** _CHARS_
> 单词分隔字符。

**-s** _N_
> 历史记录大小。

**--no-warnings**
> 抑制警告信息。

# DESCRIPTION

**rlwrap** 为任意命令添加 readline 能力。它为缺少行编辑、历史和补全功能的程序提供这些特性。

使用 -H 时历史会在多个会话之间保留。可以用 Ctrl-R 搜索以前的输入，用方向键浏览历史。

补全文件包含用于 Tab 补全的单词。-r 选项会从输出中学习单词，构建动态补全。

多行模式可处理跨越多行的命令。这对于接受多行输入的 SQL 客户端和 REPL 很有用。

该工具拦截输入，通过 readline 处理后再传给被包装的命令。输出则原样传递。

提示符会被检测并着色，从而提高交互会话中的可见性。

# CAVEATS

可能会干扰对终端做特殊处理的程序。提示符检测是启发式的。某些控制序列可能无法正常工作。

# HISTORY

**rlwrap** 由 **Hans Lub** 编写，旨在为任意程序添加 readline 支持。它填补了没有内置行编辑功能的程序的空白。

# INSTALL

```apt: sudo apt install rlwrap```

```dnf: sudo dnf install rlwrap```

```pacman: sudo pacman -S rlwrap```

```apk: sudo apk add rlwrap```

```zypper: sudo zypper install rlwrap```

```brew: brew install rlwrap```

```nix: nix profile install nixpkgs#rlwrap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[readline](/man/readline)(3), [bash](/man/bash)(1), [ledit](/man/ledit)(1)
