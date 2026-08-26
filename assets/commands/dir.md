# TAGLINE

以多列形式列出目录内容

# TLDR

**列出**当前目录的文件（分列显示）

```dir```

**列出所有文件**，包括隐藏文件

```dir -a```

**以长格式列出**详细信息

```dir -l```

**以人类可读的方式列出**文件大小

```dir -lh```

**按修改时间排序列出**（最新在前）

```dir -t```

**按文件大小排序列出**（最大在前）

```dir -S```

**递归列出**包括子目录在内的内容

```dir -R```

# SYNOPSIS

**dir** [_options_] [_files..._]

# DESCRIPTION

**dir** 列出目录内容，等价于 **ls -C -b**。默认情况下，文件按纵向排序的多列形式列出，非图形字符以 C 风格的反斜杠转义序列显示。

与 **ls** 会根据输出目标是终端还是管道而改变输出格式不同，**dir** 始终产生带转义特殊字符的分列输出。这使其在脚本编写中行为更可预测。

该命令属于 GNU coreutils，接受与 **ls** 相同的选项。

# PARAMETERS

**-a, --all**
> 包含隐藏文件（以 . 开头）

**-A, --almost-all**
> 类似 -a，但排除 . 和 ..

**-l**
> 带详细信息的长列表格式

**-h, --human-readable**
> 人类可读的文件大小（1K、234M、2G）

**-t**
> 按修改时间排序（最新在前）

**-S**
> 按文件大小排序（最大在前）

**-r, --reverse**
> 反转排序顺序

**-R, --recursive**
> 递归列出子目录

**-d, --directory**
> 列出目录本身，而非其内容

**-F, --classify**
> 为条目附加指示符（*/=>@|）

**-i, --inode**
> 打印每个文件的 inode 号

**-s, --size**
> 以块为单位打印每个文件的已分配大小

**--color**[=_WHEN_]
> 彩色输出（always、auto、never）

# CAVEATS

等价于 **ls -C -b**。GNU coreutils 特有；并非在所有 Unix 系统上都可用。追求最大可移植性请使用 **ls**。

# HISTORY

**dir** 是 **GNU coreutils** 的一部分，由 Richard M. Stallman 和 David MacKenzie 编写。无论输出目的地是什么，它都提供一致的分列输出并转义特殊字符。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [vdir](/man/vdir)(1), [tree](/man/tree)(1), [find](/man/find)(1)
