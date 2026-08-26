# TAGLINE

用于查看文本文件的分页程序，作为 more/less 的替代品而设计

# TLDR

**查看文件**

```most [file]```

**查看多个文件**

```most [file1] [file2]```

**以二进制模式打开**

```most -b [file]```

**压缩多个空行**

```most -s [file]```

**折行显示长行**

```most -w [file]```

**用作 man page 的分页器**

```export PAGER=most```

**跳转到指定行**

```most +[100] [file]```

# SYNOPSIS

**most** [_-bstvw_] [_+line_] [_files_]

# PARAMETERS

**-b**
> 二进制模式（显示控制字符）。

**-s**
> 将多个空行压缩为一行。

**-t**
> 禁用制表符展开。

**-v**
> 以可见形式显示控制字符。

**-w**
> 折行显示长行，而不是截断。

**+** _line_
> 从指定行号开始显示。

**-d**
> 禁用彩色 ANSI 转义序列。

**-c**
> 让按键操作为页面着色。

# KEYBOARD SHORTCUTS

**Space / D**
> 向下翻页。

**B / U**
> 向上翻页。

**Enter / Down**
> 向下滚动一行。

**Up**
> 向上滚动一行。

**< / >**
> 跳到文件开头 / 结尾。

**/ pattern**
> 向前搜索。

**? pattern**
> 向后搜索。

**n**
> 下一个搜索匹配项。

**:n**
> 下一个文件。

**:p**
> 上一个文件。

**q / Q**
> 退出。

**h**
> 帮助屏幕。

# DESCRIPTION

**most** 是一个用于查看文本文件的分页程序，设计为 more 和 less 的替代品。它可以显示多个窗口，并支持对宽文件进行左右滚动。

与 less 不同，most 可以在同一屏幕上打开多个窗口，从而并排查看不同文件，或查看同一文件的不同位置。窗口命令可以分割显示并在各窗格之间导航。

对颜色和 ANSI 转义序列的支持使其适合作为 man page 及彩色输出的分页器。长行可以折行或水平滚动显示。

搜索功能支持正则表达式。可以设置并召回标记位置以便导航。其界面总体上比 less 更直观，状态信息显示醒目。

二进制模式可以在不弄乱显示的情况下处理非文本文件。压缩模式会合并多个空行，对于空行过多的文件很有用。

# CAVEATS

在某些高级操作上功能不如 less 丰富。窗口管理有一定学习曲线。不如 less 普遍可用。部分快捷键与 less/more 的惯例不同。处理超大文件的效率可能不高。

# HISTORY

**most** 由 **John E. Davis** 于 **20 世纪 90 年代初**编写，是 S-Lang 库工具集的一部分。它旨在解决既有分页器的局限，特别是增加了多窗口支持和对宽文件更好的处理。该工具作为 S-Lang 项目的一部分仍在积极维护。

# INSTALL

```apt: sudo apt install most```

```dnf: sudo dnf install most```

```pacman: sudo pacman -S most```

```apk: sudo apk add most```

```zypper: sudo zypper install most```

```brew: brew install most```

```nix: nix profile install nixpkgs#most```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [more](/man/more)(1), [bat](/man/bat)(1), [view](/man/view)(1)
