# TAGLINE

十六进制转储与还原工具

# TLDR

**创建文件的十六进制转储**

```xxd [file]```

**创建纯十六进制转储**（无行号和 ASCII）

```xxd -p [file]```

创建二进制转储而非十六进制

```xxd -b [file]```

**只转储前 N 个字节**

```xxd -l [16] [file]```

**从指定偏移量开始**

```xxd -s [0x100] [file]```

输出为 **C include 数组**

```xxd -i [file]```

**将十六进制转储转换回二进制**

```xxd -r [hexdump.txt] [output.bin]```

**将纯十六进制**转换为二进制

```echo "[48656c6c6f]" | xxd -r -p```

# SYNOPSIS

**xxd** [_options_] [_infile_ [_outfile_]]

# PARAMETERS

**-b**
> 输出二进制位转储而不是十六进制

**-c** _cols_
> 每行按指定列数格式化输出（默认：16）

**-g** _bytes_
> 每组的字节数（默认：2）

**-i**
> 以 C include 文件形式输出（数组定义）

**-l** _len_
> 输出 len 字节后停止

**-p**, **-ps**, **-plain**
> 纯十六进制转储风格（连续十六进制，不带地址）

**-r**, **-revert**
> 反向操作：将十六进制转储转换为二进制

**-s** _seek_
> 从文件中的指定偏移量开始

**-u**
> 使用大写十六进制字母

**-e**
> 小端序转储（组内字节顺序颠倒）

# DESCRIPTION

**xxd** 创建文件或标准输入的十六进制转储。输出显示数据的偏移量、十六进制值和 ASCII 表示。它还可以将十六进制转储还原为原始的二进制数据。

默认输出格式每行显示 16 个字节，包含文件偏移量、以 2 字节分组的十六进制值以及可打印的 ASCII 字符。**-p** 选项产生不带格式的连续十六进制字符串。

**-i** 选项生成 C 源代码，将数据表示为 unsigned char 数组，适合在程序中嵌入二进制数据。

**-r** 选项执行相反的过程，把十六进制转储转回二进制。与 **-p** 组合使用时，可以将纯十六进制字符串转换为二进制数据。

# VIM INTEGRATION

xxd 与 vim 集成可进行十六进制编辑。在 vim 中，用 **:%!xxd** 将缓冲区转换为十六进制转储，编辑十六进制值，再用 **:%!xxd -r** 转换回二进制。

# CAVEATS

使用 **-r** 时，如果输出可寻址（seekable），xxd 对缺失或乱序的行是宽容的。还原时会忽略十六进制列中的非十六进制字符。**-r** 选项要求输入符合 xxd 的输出格式（或配合 **-p** 使用纯十六进制）。

# HISTORY

**xxd** 由 **Juergen Weigert** 编写，随 **vim** 一同分发。它是作为传统十六进制转储工具（如 **od**）的更灵活替代品而创建的。该工具自 20 世纪 90 年代中期起就是 vim 发行版的一部分，在类 Unix 系统上普遍可用。

# INSTALL

```apt: sudo apt install xxd```

```dnf: sudo dnf install xxd```

```apk: sudo apk add xxd```

```zypper: sudo zypper install xxd```

```nix: nix profile install nixpkgs#xxd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[od](/man/od)(1), [hexdump](/man/hexdump)(1), [hd](/man/hd)(1), [vim](/man/vim)(1)
