# TAGLINE

逐屏翻阅文本的过滤器

# TLDR

**打开文件**进行翻阅

```more [path/to/file]```

**从指定行开始**显示

```more +[line_number] [path/to/file]```

显示前先**搜索字符串**

```more +/[pattern] [path/to/file]```

将多个连续空行**压缩**为一行

```more -s [path/to/file]```

设置**每屏行数**

```more -n [20] [path/to/file]```

# SYNOPSIS

**more** [**-d**] [**-l**] [**-s**] [**-p**] [**-c**] [**-n** _lines_] [**+**_linenum_] [**+/**_pattern_] [_file_...]

# PARAMETERS

**-d**, **--silent**
> 出错时显示 "[Press space to continue, 'q' to quit.]" 提示，而不是响铃。

**-l**, **--logical**
> 在包含换页符的行之后不暂停。

**-e**, **--exit-on-eof**
> 到达文件末尾时自动退出。不在终端上运行时默认启用。

**-f**, **--no-pause**
> 按逻辑行而非屏幕行计数（长行不折叠）。

**-p**, **--print-over**
> 显示前清屏，不滚动。

**-c**, **--clean-print**
> 从顶部逐行绘制每一屏，并清除各行剩余部分。

**-s**, **--squeeze**
> 将多个连续空行压缩为一行。

**-u**, **--plain**
> 不显示下划线。

**-n** _number_, **--lines** _number_
> 指定每屏的行数。

**-**_number_
> 等价于 **--lines** _number_。

**+**_number_
> 从指定行号开始显示。

**+/**_pattern_
> 显示前搜索 pattern。

**-h**, **--help**
> 显示帮助文本并退出。

**-V**, **--version**
> 输出版本信息并退出。

# INTERACTIVE COMMANDS

**Space** 或 **z**
> 显示下一屏。

**Enter**
> 显示下一行。

**d** 或 **^D**
> 向前滚动半屏（默认 11 行）。

**s**
> 向前跳过一行。

**f**
> 向前跳过一整屏。

**b** 或 **^B**
> 向后跳过一整屏（仅限文件）。

**/**_pattern_
> 向前搜索 pattern。

**n**
> 重复上次搜索。

**'**
> 返回上次搜索的位置。

**q** 或 **Q**
> 退出。

**h** 或 **?**
> 显示帮助摘要。

**=**
> 显示当前行号。

**v**
> 在当前行打开编辑器。

**:f**
> 显示当前文件名和行号。

**:n**
> 跳到下一个文件。

**:p**
> 跳到上一个文件。

**!**_command_
> 在子 shell 中执行命令。

**.**
> 重复上一条命令。

**^L**
> 重绘屏幕。

# DESCRIPTION

**more** 是一个逐屏翻阅文本的过滤器。它以交互方式显示文件内容，支持向前翻页和在文本中搜索。

操作命令遵循 vi 的惯例，并且可以在前面加上数字参数。该分页器可从文件或标准输入读取内容，因此在管道中很有用。

# CAVEATS

与提供向后滚动等更多功能的 **less** 相比，more 命令被认为较为简陋。多数情况下建议改用 less。**MORE** 环境变量可以设置默认选项。若设置了 **POSIXLY_CORRECT**，则默认不启用 **-e**。

# HISTORY

**more** 命令首次出现于 **3.0BSD**，由 UC Berkeley 的 **Eric Shienbrood** 编写，是最早的面向屏幕的工具之一。它曾成为标准的 Unix 分页器，不过功能更多的 **less**（由 Mark Nudelman 于 1983 年编写）已在很大程度上取代了它。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [most](/man/most)(1), [pg](/man/pg)(1), [cat](/man/cat)(1), [head](/man/head)(1), [tail](/man/tail)(1)
