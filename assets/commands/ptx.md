# TAGLINE

生成置换式上下文关键字索引

# TLDR

生成带**行引用**的索引

```ptx -r [file]```

生成**自动引用**

```ptx -A [file]```

设置输出**宽度**

```ptx -w [80] [file]```

使用**单词过滤表**

```ptx -o [filter_file] [file]```

使用 **SYSV** 传统模式

```ptx -G [file]```

# SYNOPSIS

**ptx** [**-A**] [**-r**] [**-w** _width_] [**-o** _file_] [**-G**] [_input_file_]

# PARAMETERS

**-A, --auto-reference**
> 生成自动索引引用

**-r, --references**
> 将第一个字段用作索引引用

**-w, --width _cols_**
> 输出行宽（以列数计）

**-o, --only-file _file_**
> 读取要索引的单词列表

**-i, --ignore-file _file_**
> 读取要忽略的单词列表

**-G, --traditional**
> 兼容 SYSV 的行为

# DESCRIPTION

**ptx** 从文本文件生成置换索引（也称 KWIC，Key Word In Context）。每个重要的单词都会成为一条带有上下文的索引项，读者可以通过任意单词定位主题。

输出将每个单词居中显示并附带周围上下文，适用于为文档创建词语索引或关键词索引。

# CAVEATS

输出格式面向老式终端设计。现代使用可能需要后处理。单词过滤需要单独的文件。大文件会产生大量输出。

# HISTORY

**ptx** 是传统的 Unix 文本处理工具，属于 GNU coreutils。在全文搜索普及之前，置换索引对印刷文档十分重要。

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

[sort](/man/sort)(1), [grep](/man/grep)(1), [awk](/man/awk)(1)
