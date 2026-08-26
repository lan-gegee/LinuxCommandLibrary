# TAGLINE

将 locale 定义文件编译为 C 库可用的二进制 locale 数据

# TLDR

列出**已编译的 locale**

```localedef --list-archive```

显示**帮助**

```localedef --help```

**编译**一个 locale

```localedef -i [locale] -f [charmap] [output_path]```

# SYNOPSIS

**localedef** [_options_] _output_path_

# DESCRIPTION

**localedef** 将 locale 定义文件编译为 C 库可用的二进制 locale 数据。它读取字符映射表和 locale 定义文件来创建 locale 归档。

# PARAMETERS

**--list-archive**
> 列出归档中的 locale

**-i, --inputfile FILE**
> locale 定义的输入文件

**-f, --charmap FILE**
> 字符映射表文件

**-c, --force**
> 即使出现警告也创建输出

**--delete-from-archive**
> 从归档中删除 locale

**--add-to-archive**
> 将编译好的 locale 添加到归档

**-?, --help**
> 显示帮助信息

# CAVEATS

底层工具；大多数用户应改用 locale-gen。错误的 locale 定义可能导致应用程序出错。

# INSTALL

```apt: sudo apt install libc-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[locale](/man/locale)(1), [locale-gen](/man/locale-gen)(8)
