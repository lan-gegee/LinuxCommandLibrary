# TAGLINE

以八进制及其他格式转储文件内容

# TLDR

**以八进制转储文件**（默认）

```od [file]```

**以十六进制转储**（两字节单位）

```od -x [file]```

**以 ASCII 字符和反斜杠转义转储**

```od -c [file]```

**以十六进制地址和单字节十六进制输出转储**

```od -A x -t x1 [file]```

**从开头跳过若干字节**

```od -j [bytes] [file]```

**将输出限制为指定字节数**

```od -N [bytes] [file]```

**显示所有数据**，不省略重复行

```od -v [file]```

**以命名字符方式转储**（忽略高位比特）

```od -a [file]```

# SYNOPSIS

**od** [_options_] [_file_...]

# PARAMETERS

_FILE_
> 要转储的文件。未指定 FILE 或 FILE 为 - 时，读取标准输入。

**-A** _RADIX_, **--address-radix**=_RADIX_
> 地址进制：d（十进制）、o（八进制）、x（十六进制）、n（无）

**-t** _TYPE_, **--format**=_TYPE_
> 输出类型（a、c、d、f、o、u、x，可带大小后缀）

**-a**
> 命名字符，等同于 **-t a**（忽略高位比特）。

**-b**
> 八进制字节，等同于 **-t o1**。

**-c**
> 可打印字符或反斜杠转义，等同于 **-t c**。

**-d**
> 无符号十进制，两字节单位，等同于 **-t u2**。

**-f**
> 浮点数，等同于 **-t fF**。

**-i**
> 十进制 int（sizeof(int)），等同于 **-t dI**。

**-l**
> 十进制 long，等同于 **-t dL**。

**-o**
> 八进制，两字节单位，等同于 **-t o2**。

**-s**
> 十进制，两字节单位，等同于 **-t d2**。

**-x**
> 十六进制，两字节单位，等同于 **-t x2**。

**-j** _BYTES_, **--skip-bytes**=_BYTES_
> 先跳过 BYTES 个输入字节

**-N** _BYTES_, **--read-bytes**=_BYTES_
> 转储最多 BYTES 个输入字节

**-v**, **--output-duplicates**
> 不用 * 标记被省略的重复行

**-w**[_BYTES_], **--width**[=_BYTES_]
> 每个输出行输出 BYTES 个字节（默认 32）

**-S** _BYTES_, **--strings**[=_BYTES_]
> 只显示长度至少为 BYTES 个可打印字符的 NUL 结尾字符串

**--endian**={big|little}
> 按指定字节序交换输入字节

# DESCRIPTION

**od**（octal dump）将其输入的无歧义表示写入标准输出。默认以八进制显示数据，每行包含一个偏移量和数据值。该工具可用于检查二进制文件、查看不可打印字符以及调试数据格式。

除非使用 **-v**，否则输出中重复的行会被替换为一个 **\*** 字符。

# CAVEATS

默认输出为八进制，对大多数现代场景而言不如十六进制直观。BYTES 参数可以带大小后缀：b（512）、KB（1000）、K（1024）、MB、M 等。属于 GNU coreutils 的一部分。

# HISTORY

od（octal dump）起源于**早期 Unix**（Version 1，1971 年），用于以八进制形式查看文件内容。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hexdump](/man/hexdump)(1), [xxd](/man/xxd)(1), [hd](/man/hd)(1)
