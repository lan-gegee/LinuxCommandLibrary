# TAGLINE

从文本输入中删除指定的列

# TLDR

从标准输入中删除**第一列**

```colrm 1 1```

删除每行**第 3 列到行尾**的内容

```colrm 3```

删除**第 3 到第 5 列**

```colrm 3 5```

# SYNOPSIS

**colrm** [_first_] [_last_]

# DESCRIPTION

**colrm** 从标准输入读取的文本中删除选定的列。列号从 1 开始计数。如果只给出一个参数，则删除从该列到行尾的所有内容。

该工具适用于需要在文本处理管道中剥离特定列范围的场景。

# PARAMETERS

_first_
> 要删除的第一列（从 1 开始计数）

_last_
> 要删除的最后一列（可选，默认到行尾）

**-h**, **--help**
> 显示帮助文本并退出

**-V**, **--version**
> 打印版本信息并退出

# CAVEATS

列号从 1 开始计数，而不是 0。制表符被视为前进到下一个 8 列的倍数位置。退格字符会使列计数减一。属于 util-linux 软件包的一部分。

# INSTALL

```apt: sudo apt install bsdextrautils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cut](/man/cut)(1), [column](/man/column)(1), [awk](/man/awk)(1), [expand](/man/expand)(1), [paste](/man/paste)(1)
