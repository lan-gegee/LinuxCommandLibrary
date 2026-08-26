# TAGLINE

以十六进制格式显示文件内容

# TLDR

**以十六进制显示文件**

```hd [file]```

**只显示前 100 字节**

```hd -n 100 [file]```

**跳过前 50 字节**

```hd -s 50 [file]```

**单字节八进制显示**

```hd -b [file]```

**标准的十六进制+ASCII 显示**

```hd -C [file]```

# SYNOPSIS

**hd** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要显示的文件。

**-n** _LENGTH_
> 要显示的字节数。

**-s** _OFFSET_
> 跳过 offset 字节。

**-b**
> 单字节八进制显示。

**-C**
> 标准的十六进制+ASCII 显示。

**-v**
> 显示全部数据（不做重复行抑制）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hd** 以十六进制格式显示文件内容。以 **hd** 名称调用 **hexdump** 等价于加 **-C** 运行：偏移量、十六进制字节和 ASCII 表示会并排显示。

该工具适用于检查二进制文件、分析数据格式和调试。它会将输出格式化为易读的列。

# CAVEATS

不可打印的字节在 ASCII 列中以点号显示。大文件会产生大量输出；建议通过分页器管道查看，或用 **-n**/**-s** 限制范围。

# HISTORY

**hd** 最初是 BSD 中 **hexdump** 的一个便捷别名。在当前的 Linux 系统上，它由 **util-linux** 软件包提供（util-linux 在 2017 年前后吸收了旧 bsdmainutils 软件包中的 hexdump），因此 **hexdump** 与 **hd** 调用的是同一个二进制程序。

# INSTALL

```apt: sudo apt install bsdextrautils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hexdump](/man/hexdump)(1), [xxd](/man/xxd)(1), [od](/man/od)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux/blob/master/text-utils/hexdump.c)```
```[Documentation](https://man7.org/linux/man-pages/man1/hexdump.1.html)```

<!-- verified: 2026-07-17 -->
