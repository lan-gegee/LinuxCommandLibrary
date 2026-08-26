# TAGLINE

专为逆向工程师和程序员设计的功能丰富的十六进制编辑器

# TLDR

在 ImHex 中**打开**文件

```imhex [path/to/file]```

**创建**新的空文件

```imhex --new```

打开文件并使用十六进制偏移量**选中**字节范围

```imhex --open [path/to/file] --select [0x100] [0x200]```

显示**文件信息**（类型、熵等）

```imhex --file-info [path/to/file]```

计算文件的 **SHA-256 哈希**

```imhex --hash sha256 [path/to/file]```

生成文件的**十六进制转储**

```imhex --hexdump [path/to/file]```

显示**版本**信息

```imhex --version```

# SYNOPSIS

**imhex** [_options_] [_file_]

# PARAMETERS

**--new**
> 创建新的空文件

**--open** _FILE_
> 打开指定文件

**--select** _START_ _END_
> 选中字节范围（十六进制偏移量）

**--file-info** _FILE_
> 显示文件信息

**--hash** _ALGORITHM_ _FILE_
> 计算文件哈希（md5、sha1、sha224、sha256、sha384、sha512）

**--hexdump** _FILE_
> 生成十六进制转储

**--version**
> 显示版本信息

# DESCRIPTION

**ImHex** 是一款专为逆向工程师和程序员设计的功能丰富的十六进制编辑器。它提供高级分析工具，包括用于解析二进制格式的自定义模式语言、数据检查、哈希计算和可视化功能。

该编辑器支持多种数据视图、书签管理以及通过插件进行扩展。它能够高效处理大型文件，并内置了常见文件格式的解析器。

# CAVEATS

GUI 应用程序，但部分功能可通过命令行使用。处理超大文件需要较多内存。模式语言有一定学习曲线。

# HISTORY

ImHex 由 WerWolv 创建，于 **2020 年**首次发布。它被设计为老式十六进制编辑器的现代替代品，融入了专门面向逆向工程和二进制分析的功能。

# INSTALL

```dnf: sudo dnf install imhex```

```apk: sudo apk add imhex```

```nix: nix profile install nixpkgs#imhex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xxd](/man/xxd)(1), [hexdump](/man/hexdump)(1), [hexedit](/man/hexedit)(1), [od](/man/od)(1), [radare2](/man/radare2)(1)
