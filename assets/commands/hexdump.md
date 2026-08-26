# TAGLINE

以十六进制、十进制、八进制或 ASCII 格式显示文件内容

# TLDR

输出文件的**十六进制表示**

```hexdump [path/to/file]```

以规范格式显示偏移量和 **ASCII 表示**

```hexdump -C [path/to/file]```

以十六进制显示，但只解释 **n 个字节**

```hexdump -C -n [number_of_bytes] [path/to/file]```

**不将**重复行替换为 '*'

```hexdump -v [path/to/file]```

# SYNOPSIS

**hexdump** [_options_] _file_...

# PARAMETERS

**-C**, **--canonical**
> 规范的十六进制+ASCII 显示（最常用的格式）

**-n**, **--length** _LENGTH_
> 只解释输入的前 _LENGTH_ 个字节

**-s**, **--skip** _OFFSET_
> 跳过开头的 _OFFSET_ 个字节

**-v**, **--no-squeezing**
> 显示所有行（不压缩相同的行）

**-e** _FORMAT_
> 指定自定义格式字符串

**-b**
> 单字节八进制显示

**-c**
> 单字节字符显示

**-d**
> 双字节十进制显示

**-o**
> 双字节八进制显示

**-x**
> 双字节十六进制显示

# DESCRIPTION

**hexdump** 以十六进制、十进制、八进制或 ASCII 格式显示文件内容。它是检查二进制文件、调试数据格式和分析文件结构的必备工具。

**-C**（规范）格式最为常用，它并排显示偏移量、十六进制字节和 ASCII 表示。默认情况下，重复的相同行会被替换为 '*' 以节省空间。

自定义格式字符串（**-e**）允许精确控制输出格式，便于脚本编写和自动化。

# CAVEATS

大文件会产生海量输出；请使用 **-n** 加以限制。默认格式的可读性不佳；实际检查时应使用 **-C**。若需编辑十六进制内容，请考虑 xxd 或 hexedit 等工具。

# HISTORY

hexdump 起源于 BSD Unix，在 Linux 系统上是 util-linux 软件包的一部分。它提供与较早的 od（octal dump）命令类似的功能，但格式选项更灵活。

# INSTALL

```apt: sudo apt install bsdextrautils```

```apk: sudo apk add hexdump```

```nix: nix profile install nixpkgs#hexdump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xxd](/man/xxd)(1), [od](/man/od)(1), [hexyl](/man/hexyl)(1), [strings](/man/strings)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/hexdump.1.html)```

<!-- verified: 2026-07-19 -->
