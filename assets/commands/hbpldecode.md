# TAGLINE

解码 HP Business Inkjet Printer Language 文件

# TLDR

**解码 HBP 文件**

```hbpldecode [input.hbp]```

**解码到文件**

```hbpldecode [input.hbp] > [output.pbm]```

**详细输出**

```hbpldecode -v [input.hbp]```

# SYNOPSIS

**hbpldecode** [_options_] _file_

# PARAMETERS

_FILE_
> 要解码的 HBP 文件。

**-v**
> 详细模式。

**-h**
> 显示帮助。

# DESCRIPTION

**hbpldecode** 用于解码 HP Business Inkjet Printer Language 文件。它从打印机假脱机文件中提取图像数据。

该工具是 foo2hbpl 打印机驱动套件的一部分，适合分析打印机数据和提取内嵌图像。

# CAVEATS

仅适用于 HP 打印机。属于 foo2hbpl 软件包的一部分。支持的文件格式有限。

# HISTORY

hbpldecode 作为 **foo2hbpl** 的一部分开发，用于支持 HP Business Inkjet 打印机的 Linux 打印。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2hbpl](/man/foo2hbpl)(1)
