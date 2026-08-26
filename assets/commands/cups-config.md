# TAGLINE

CUPS 构建配置辅助工具

# TLDR

**获取 CUPS 头文件目录**

```cups-config --cflags```

**获取 CUPS 库链接选项**

```cups-config --libs```

**获取 CUPS 版本**

```cups-config --version```

**获取全部配置**

```cups-config --all```

# SYNOPSIS

**cups-config** [_options_]

# PARAMETERS

**--cflags**
> 打印 CUPS 头文件所需的编译器选项。

**--libs**
> 打印链接 CUPS 库所需的链接器选项。

**--version**
> 打印 CUPS 版本。

**--ldflags**
> 打印链接器的目录选项。

**--serverbin**
> 打印服务器可执行文件目录。

**--serverroot**
> 打印服务器根目录。

**--datadir**
> 打印数据目录。

# DESCRIPTION

**cups-config** 提供 CUPS（Common Unix Printing System）的配置信息。它主要供构建系统在编译使用 CUPS 库的软件时确定编译器和链接器选项。

# INSTALL

```apt: sudo apt install libcups2-dev```

```apk: sudo apk add cups-dev```

```zypper: sudo zypper install cups-config```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsd](/man/cupsd)(8), [lp](/man/lp)(1), [lpr](/man/lpr)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/cups)```

```[Homepage](https://www.cups.org)```

```[Documentation](https://openprinting.github.io/cups/)```

<!-- verified: 2026-06-26 -->
