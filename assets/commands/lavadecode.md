# TAGLINE

将 LAVAFLOW 流解码为人类可读的形式

# TLDR

**解码 LAVAFLOW 流文件**

```lavadecode < [path/to/file.lava]```

**解码并打印文件偏移量**

```lavadecode -o < [path/to/file.lava]```

**解码并以十六进制打印文件偏移量**

```lavadecode -h < [path/to/file.lava]```

**解码并将解压后的平面保存为 .pbm 文件**

```lavadecode -d [basename] < [path/to/file.lava]```

**带调试输出进行解码**

```lavadecode -D [level] < [path/to/file.lava]```

# SYNOPSIS

**lavadecode** [_options_] <_lavaflow-file_

# PARAMETERS

**-d** _basename_
> 保存解压平面的 .pbm 文件基础名。

**-h**
> 以十六进制打印文件偏移量。

**-o**
> 打印文件偏移量。

**-D** _level_
> 设置调试级别（默认 0）。

# DESCRIPTION

**lavadecode** 将 LAVAFLOW 流解码为人类可读的形式。LAVAFLOW 是某些 Konica Minolta 打印机（例如 magicolor 2530 DL）所使用的打印语言。

它是 **foo2zjs** 打印机驱动套件的一员，用于检查由 **foo2lava** 生成的流。

# CAVEATS

只能处理 LAVAFLOW 打印机流。输入需通过重定向从 stdin 读取。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2lava](/man/foo2lava)(1), [foo2lava-wrapper](/man/foo2lava-wrapper)(1)
