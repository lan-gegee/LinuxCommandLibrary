# TAGLINE

一次一屏查看文本文件内容的终端分页程序

# TLDR

**查看文件**

```less [file]```

**带行号查看文件**

```less -N [file]```

打开后**搜索模式**

```/[pattern]```

查看**命令的输出**

```[command] | less```

**跟踪文件的**增长（类似 tail -f）

```less +F [file]```

在指定行**打开文件**

```less +[line_number] [file]```

# SYNOPSIS

**less** [_-options_] [_file ..._]

# PARAMETERS

**-N**, **--LINE-NUMBERS**
> 在每行开头显示行号

**-S**, **--chop-long-lines**
> 截断长行而不是折行显示

**-i**, **--ignore-case**
> 搜索时忽略大小写（模式中含大写字母时除外）

**-I**, **--IGNORE-CASE**
> 搜索时无条件忽略大小写

**-F**, **--quit-if-one-screen**
> 若整个文件能在一屏内显示则立即退出

**-R**, **--RAW-CONTROL-CHARS**
> 输出原始控制字符（保留颜色）

**-X**, **--no-init**
> 退出时不清除屏幕

**-g**, **--hilite-search**
> 只高亮当前匹配项，而不是所有匹配项

**-n**, **--line-numbers**
> 不显示行号（出于性能考虑）

**+F**
> 跟随模式，向前滚动并等待更多数据

**+** _command_
> 启动时执行指定的命令（例如 +/pattern 进行搜索）

**-p** _pattern_
> 从模式第一次出现的位置开始显示

**-o** _file_
> 将输入复制到文件（从管道读取时）

# NAVIGATION

**Space**, **f**, **PgDn**
> 向前翻一屏

**b**, **PgUp**
> 向后翻一屏

**d**, **u**
> 向前/向后翻半屏

**j**, **k** 或 **方向键**
> 向前/向后移动一行

**g**, **G**
> 跳转到文件开头/结尾

**/** _pattern_
> 向前搜索模式

**?** _pattern_
> 向后搜索模式

**n**, **N**
> 向前/向后重复上一次搜索

**q**
> 退出

**h**
> 显示帮助

# DESCRIPTION

**less** 是一个终端分页程序，用于一次一屏地查看文本文件内容。与 **more** 不同，它允许在文件中向后翻阅，并且不必读完整个文件就能开始显示，因此处理大文件非常高效。

该程序提供强大的搜索能力，支持正则表达式，可以显示行号，还能在单个会话中处理多个文件。它常被用作手册页的默认分页器，在查看日志文件和命令输出时不可或缺。

Less 可以从标准输入读取内容，因此非常适合接收管道传来的命令输出。跟随模式（+F）能够实时监视不断增长的文件，类似于 **tail -f**，但同时拥有 less 完整的导航能力。

# CAVEATS

二进制文件可能显示不正确或引发终端问题。在不使用 **-S** 选项的情况下，超长行的渲染可能很慢。LESSOPEN 和 LESSCLOSE 环境变量可用于预处理文件，但如果配置不当可能带来安全风险。

# HISTORY

**less** 由 **Mark Nudelman** 编写，于 **1984 年**首次发布，用来取代 Unix 的 **more** 命令。这个名字取自 "less is more"（少即是多）的双关。如今它已成为类 Unix 系统上的标准实用工具，也是大多数 Linux 发行版的默认分页器。该程序仍在积极维护，定期更新添加新特性和改进。

# INSTALL

```apt: sudo apt install less```

```dnf: sudo dnf install less```

```pacman: sudo pacman -S less```

```apk: sudo apk add less```

```zypper: sudo zypper install less```

```brew: brew install less```

```nix: nix profile install nixpkgs#less```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[more](/man/more)(1), [cat](/man/cat)(1), [tail](/man/tail)(1), [head](/man/head)(1), [most](/man/most)(1)
