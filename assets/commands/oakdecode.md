# TAGLINE

将 OAKT 打印机数据流解码为人类可读的形式

# TLDR

**从文件解码 OAKT 打印机数据流**

```oakdecode < [file.prn]```

**解码并将解压后的色面保存为 PBM 文件**

```oakdecode -d [basename] < [file.prn]```

**解码并将原始色面保存为 JBIG 文件**

```oakdecode -r [basename] < [file.prn]```

**解码并在输出中显示文件偏移量**

```oakdecode -o < [file.prn]```

**解码但不显示图像记录**

```oakdecode -i < [file.prn]```

# SYNOPSIS

**oakdecode** [_options_] <_OAKT-file_

# PARAMETERS

**-d** _BASENAME_
> 以指定基名将解压后的色面保存为 .pbm 文件。

**-r** _BASENAME_
> 以指定基名将原始色面保存为 .jbg 文件。

**-i**
> 不在输出中显示图像记录。

**-o**
> 在输出中包含文件偏移量。

**-D** _LEVEL_
> 设置调试详细级别（默认：0）。

# DESCRIPTION

**oakdecode** 将 OAKT 打印机数据流解码为人类可读的形式。它面向使用 OAKT 打印语言的打印机，例如 HP Color LaserJet 1500。该工具从标准输入读取打印机数据流，并以可读格式输出解码后的记录，显示页面设置、压缩信息和图像数据。

该工具是 foo2oak 打印机驱动套件的一部分，主要用于调试和分析 OAKT 格式的打印任务。

# CAVEATS

只能从标准输入读取。仅适用于某些 HP Color LaserJet 型号所用的 OAKT 打印语言。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2oak](/man/foo2oak)(1), [foo2oak-wrapper](/man/foo2oak-wrapper)(1)
