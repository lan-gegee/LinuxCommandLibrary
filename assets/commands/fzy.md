# TAGLINE

简单快速的终端模糊文本选择器

# TLDR

从 stdin **模糊选择一行**

```[command] | fzy```

**选择一个文件**进行编辑

```find . -type f | fzy | xargs -r $EDITOR```

**限制可见匹配数**

```[command] | fzy -l [20]```

**显示帮助**

```fzy --help```

# SYNOPSIS

**fzy** [**-l** *lines*] [**-p** *prompt*] [**-q** *query*] [**-e** *query*] [**-t**] [**-s**] [**-0**] [**-j** *workers*]

# DESCRIPTION

**fzy** 是一个极简的模糊查找器：它从 stdin 读取按换行分隔的候选内容，随输入实时过滤，并把选中的行输出到 stdout。它以精简的代码库强调排序质量和速度，是更重量级选择器的轻量替代品。

# PARAMETERS

**-l**, **--lines** *n*

> 最大显示匹配数（默认通常为 10）。

**-p**, **--prompt** *text*

> 输入提示字符串。

**-q**, **--query** *text*

> 初始查询词。

**-e**, **--show-matches** *query*

> 非交互模式：打印 *query* 的排序匹配结果并退出。

**-t**, **--tty-only**

> 仅使用 /dev/tty（行为因版本而异）。

**-0**, **--read-null**

> 读取以 NUL 分隔的输入。

**-j** *workers*

> 并行评分的工作线程数。

# CAVEATS

交互模式需要 TTY。排序结果与 **fzf** 不同；切换工具时脚本可能需要调整。

# INSTALL

```apt: sudo apt install fzy```

```pacman: sudo pacman -S fzy```

```apk: sudo apk add fzy```

```zypper: sudo zypper install fzy```

```brew: brew install fzy```

```nix: nix profile install nixpkgs#fzy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [pick](/man/pick)(1), [sk](/man/sk)(1)

# RESOURCES

```[Source code](https://github.com/jhawthorn/fzy)```

<!-- verified: 2026-07-19 -->
