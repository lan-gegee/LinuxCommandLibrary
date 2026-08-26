# TAGLINE

将文本显示为 ASCII 纸带艺术

# TLDR

**转换为纸带格式**

```ppt [text]```

**转换文件**

```cat [file.txt] | ppt```

**显示纸带**

```echo "Hello" | ppt```

# SYNOPSIS

**ppt** [_text_]

# PARAMETERS

_TEXT_
> 要转换的文本。

# DESCRIPTION

**ppt** 将文本输入转换为穿孔纸带的 ASCII 艺术表示。穿孔纸带是早期计算机和电传打字机使用的存储介质。每个字符显示为一行与其二进制编码对应的孔（点）。

这个趣味工具是 BSD games 合集的一部分，既是娱乐，也是了解历史数据编码格式的教育工具。

# CAVEATS

娱乐性工具。属于 bsdgames。

# HISTORY

ppt 是作为 **BSD games** 工具创建的，用于纸带模拟。

# SEE ALSO

[banner](/man/banner)(1), [morse](/man/morse)(1)
