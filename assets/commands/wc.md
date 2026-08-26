# TAGLINE

统计文件中的行数、单词数和字节数

# TLDR

**统计行数、单词数和字节数**

```wc [file]```

**只统计行数**

```wc -l [file]```

**只统计单词数**

```wc -w [file]```

**只统计字符数**

```wc -m [file]```

**只统计字节数**

```wc -c [file]```

**统计命令输出的行数**

```[command] | wc -l```

**统计目录中的文件数**

```ls | wc -l```

**统计最长行的长度**

```wc -L [file]```

# SYNOPSIS

**wc** [_options_] [_file_...]

# PARAMETERS

**-l**, **--lines**
> 输出行数

**-w**, **--words**
> 输出单词数

**-c**, **--bytes**
> 输出字节数

**-m**, **--chars**
> 输出字符数

**-L**, **--max-line-length**
> 输出最长行的长度

**--files0-from**=_F_
> 从文件 F 读取文件名（以 NUL 结尾）

**--total**=_when_
> 何时输出总计（auto、always、only、never）

# DESCRIPTION

**wc**（word count）为每个文件输出换行符、单词和字节计数。给定多个文件时，还会输出总计。未指定文件或输入来自 stdin 时，则读取标准输入。

单词被定义为以空白字符分隔、由非空白字符组成的序列，边界由空白或行界决定。这与大多数人对"单词"的直观定义一致。

默认输出依次显示行数、单词数和字节数。选项用于选择要显示的计数；若未指定任何选项，则三项全部显示。

**wc -l** 在管道中统计条目数量极为常用，例如统计文件数、匹配数或日志条目数。

# CAVEATS

对于 UTF-8 等多字节编码，字节数（**-c**）与字符数（**-m**）不同。要统计实际字符数请使用 **-m**。

统计文件数时，如果文件名包含换行符，**ls | wc -l** 会出错。为了稳健性，请使用 **find -print0 | wc -l --files0-from=-**。

空文件的行数为 0、单词数为 0、字节数为 0。只包含 "hello"（无换行符）的文件行数为 0，但单词数为 1。

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

[sort](/man/sort)(1), [uniq](/man/uniq)(1), [cut](/man/cut)(1), [awk](/man/awk)(1)
