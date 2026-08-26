# TAGLINE

解码三星 QPDL 打印数据格式

# TLDR

**解码 QPDL 打印格式**

```qpdldecode [input.qpdl] > [output.pbm]```

**显示文件信息**

```qpdldecode -i [input.qpdl]```

# SYNOPSIS

**qpdldecode** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 QPDL 文件。

**-i**
> 仅显示信息。

# DESCRIPTION

**qpdldecode** 用于解码三星专有的 QPDL（Quick Page Description Language，快速页面描述语言）打印格式数据，将其转换为 PBM 等标准图像格式，以便分析或再处理。它作为 SpliX 驱动包的一部分分发，用于三星激光打印机。

该工具还可以在不转换文件的情况下显示 QPDL 文件的元数据，使用 **-i** 标志即可显示页数、分辨率和其他格式细节。

# CAVEATS

仅适用于三星打印机。属于 splix 驱动的一部分。

# HISTORY

qpdldecode 是 **splix** 三星打印机驱动的一部分。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cups](/man/cups)(1)
