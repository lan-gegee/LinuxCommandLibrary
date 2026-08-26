# TAGLINE

将光栅对象（OPL）流解码为人类可读形式

# TLDR

**从文件解码 OPL 流**

```opldecode < [file.opl]```

**解码时显示十六进制文件偏移**

```opldecode -h < [file.opl]```

**解码并将解压后的色平面保存为 PBM 文件**

```opldecode -d [basename] < [file.opl]```

**带调试输出进行解码**

```opldecode -D [2] < [file.opl]```

# SYNOPSIS

**opldecode** [_options_] < _opl-file_

# PARAMETERS

**-d** _basename_
> 用于保存解压后色平面的 .pbm 文件基名。

**-h**
> 打印十六进制文件偏移。

**-o**
> 打印文件偏移。

**-D** _level_
> 设置调试级别（默认：0）。

# DESCRIPTION

**opldecode** 将光栅对象（OPL）流解码为人类可读形式。OPL 流是某些柯尼卡美能达（Konica Minolta）打印机（如 magicolor 2480 MF）使用的打印机语言。解码输出会显示分辨率、介质设置和光栅对象压缩等配置细节。

它是 **foo2zjs** 打印机驱动套件的组成部分。

# CAVEATS

输入从标准输入读取，而非文件名参数。仅对调试特定柯尼卡美能达硬件的打印机数据流有用。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2zjs](/man/foo2zjs)(1), [zjsdecode](/man/zjsdecode)(1), [foo2lava](/man/foo2lava)(1), [gs](/man/gs)(1)
