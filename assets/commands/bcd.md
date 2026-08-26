# TAGLINE

将输入重新格式化为穿孔卡片

# TLDR

以穿孔卡片形式**打印文本**

```bcd [Hello]```

从标准输入**读取文本**

```echo [hello world] | bcd```

将穿孔卡片**解码**回文本

```bcd -d < [card.txt]```

# SYNOPSIS

**bcd** [_-l_] [_string_...]

**bcd** **-d** [_-l_]

# DESCRIPTION

**bcd** 读取给定输入，并将其重新格式化为 IBM 风格穿孔卡片的 ASCII 字符画。它是 BSD games 合集中经典的趣味过滤器之一，同类工具还有 **ppt**（纸带）和 **morse**（摩尔斯电码）。

输入可以通过命令行参数提供，也可以来自标准输入。不带解码标志时，文本会被编码为穿孔卡片；从标准输入读取时只读取第一行。

# PARAMETERS

**-d**
> 将标准输入上的穿孔卡片解码回 ASCII 文本。

**-l**
> 生成或解码 80 列卡片。默认为 48 列。

# CAVEATS

这是一个趣味程序，不是数据处理工具。只有输入的第一行会被编码，不支持的字符会被忽略。它不做二进制、十进制或十六进制的进制转换：这类需求请使用 **bc** 或 **dc**。

# HISTORY

**bcd** 首次出现于 Version 6 AT&T UNIX，模拟的是贝尔实验室在 20 世纪 60 年代末至 70 年代初 GE 635 和 GE 645 计算机所使用的穿孔卡片。如今它作为 **bsdgames** 软件包的一部分发行。

# INSTALL

```dnf: sudo dnf install bcd```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ppt](/man/ppt)(6), [morse](/man/morse)(6), [number](/man/number)(6), [bsdgames](/man/bsdgames)(6)
