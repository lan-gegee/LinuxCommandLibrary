# TAGLINE

以合并的时间线查看多个日志文件

# TLDR

交互式地**合并并查看日志文件**

```logmerger [file1.log] [file2.log]```

将日志**内联合并**输出到 stdout

```logmerger --inline [file1.log] [file2.log]```

在时间窗口内**合并日志**

```logmerger --start "[timestamp]" --end "[timestamp]" [file1.log] [file2.log]```

将合并后的输出**写入文件**

```logmerger -o [output.log] [file1.log] [file2.log]```

在交互式浏览器中**添加行号**

```logmerger --line_numbers [file1.log] [file2.log]```

# SYNOPSIS

**logmerger** [_options_] _files_...

# PARAMETERS

_FILES_
> 要合并的一个或多个日志文件。以 **.gz**、**.csv**、**.jsonl** 或 **.pcap**（实验性）结尾的文件会按相应格式读取。

**-i**, **--interactive**
> 在交互式 TUI 浏览器中显示合并结果。这是默认行为。

**--inline**
> 将合并后的日志数据以内联方式输出到 stdout，而不是打开 TUI。

**-o**, **--output** _FILE_
> 将合并后的输出保存到文件。用 **-** 表示 stdout；以 **.md** 结尾的文件会写成 Markdown 表格。

**-s**, **--start** _TIME_
> 用于合并选择的时间窗口起点。

**-e**, **--end** _TIME_
> 用于合并选择的时间窗口终点。

**-ac**, **--autoclip**
> 将合并裁剪到第一个日志文件中日志的时间范围。

**--ignore_non_timestamped**
> 忽略没有时间戳的日志行，而不是把它们附加到前一条目。

**-w**, **--width** _WIDTH_
> 交互模式使用的总屏幕宽度。

**-ln**, **--line_numbers**
> 在输出中添加行号列。

**-enc**, **--encoding** _ENCODING_
> 读取日志文件时使用的编码。

**--timestamp_format** _FORMAT_
> 一个或多个要识别的自定义 strptime 风格时间戳格式。

# DESCRIPTION

**logmerger** 是一款 TUI 工具，用于按时间戳关联并以合并视图查看多个日志文件。它支持纯文本日志、gzip 压缩日志（**.gz**）、CSV（**.csv**）和 JSONL（**.jsonl**）文件，并对数据包捕获（**.pcap**）文件提供实验性支持。

来自不同文件的日志条目按时间戳排序，呈现在统一的彩色编码视图中，每个文件各占一列以便区分。许多常见的时间戳格式可自动识别；其他格式可通过 **--timestamp_format** 提供。

# CAVEATS

准确合并依赖每个日志文件中可识别的时间戳。没有时间戳的行会被附加到前一条目，除非指定 **--ignore_non_timestamped**。pcap 支持需要可选依赖项，通过 `pip install logmerger[pcap]` 安装。

# HISTORY

**logmerger** 是 **Paul McGuire**（ptmcg）用 **Python** 编写的开源工具，以 **logmerger** 包的形式发布在 PyPI 上（`pip install logmerger`）。

# SEE ALSO

[lnav](/man/lnav)(1), [tail](/man/tail)(1), [sort](/man/sort)(1)
