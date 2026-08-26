# TAGLINE

高性能十六进制转储工具

# TLDR

**将文件显示为十六进制转储**

```fasthex [path/to/file]```

**将输出管道到文件**

```fasthex [path/to/file] > [output.txt]```

**跳过若干字节并读取有限长度**

```fasthex -s 1KiB -n 512 [path/to/file]```

**带颜色显示**

```fasthex --color=always [path/to/file]```

**显示二进制表示**

```fasthex -b [path/to/file]```

# SYNOPSIS

**fasthex** [_options_] [_file_...]

# PARAMETERS

**-s**, **--skip** _N_
> 跳过前 N 个字节（负数从末尾计）。支持 KiB、MiB、GiB 后缀。

**-n**, **--length** _N_
> 只读取 N 个字节。

**-W**, **--width** _N_
> 每行字节数。默认：16。

**-g**, **--group** _N_
> 每组字节数：1、2、4 或 8。

**-x**, **--hex**
> 单字节十六进制显示。

**-b**, **--binary**
> 二进制显示（每字节 8 位）。

**-A**, **--no-ascii**
> 隐藏 ASCII 面板。

**-L**, **--color** _WHEN_
> 颜色模式：auto、always 或 never。

**-w**, **--squeeze**
> 用 **\*** 替代连续相同的行。

**-r**, **--reverse**
> 将十六进制转储转换回二进制。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**fasthex** 是一个 Rust 编写的十六进制转储工具，针对大文件的速度进行了优化。它对输入进行内存映射，并使用 SIMD（AVX2、SSE4.1 或标量回退）并行格式化输出，同时采用双缓冲 I/O，并尽可能利用零拷贝内核管道传输。

多个文件会被拼接为一个流处理。不带文件参数时，**fasthex** 从 stdin 读取。输出遵循 **xxd** 和 **hexdump** 中常见的经典偏移量 / 十六进制字节 / ASCII 布局，并提供额外的格式模式（八进制、十进制、纯十六进制字符串、C include 风格），以及可配置的字节序、边框和配色方案。

# CAVEATS

通过 **cargo install --git** 安装；目前尚无已发布的 crate 版本。向 TTY 输出颜色时可能比管道到文件或 **/dev/null** 更慢。

# INSTALL

```aur: yay -S fasthex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xxd](/man/xxd)(1), [hexdump](/man/hexdump)(1), [hexyl](/man/hexyl)(1)

# RESOURCES

```[Source code](https://github.com/CallMeAlphabet/fasthex)```

<!-- verified: 2026-07-11 -->
