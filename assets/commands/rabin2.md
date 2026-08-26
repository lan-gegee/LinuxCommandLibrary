# TAGLINE

从二进制文件中提取信息

# TLDR

**显示二进制文件信息**

```rabin2 -I [binary]```

**列出符号**

```rabin2 -s [binary]```

**列出导入**

```rabin2 -i [binary]```

**列出导出**

```rabin2 -E [binary]```

**列出字符串**

```rabin2 -z [binary]```

**列出节区**

```rabin2 -S [binary]```

**显示入口点**

```rabin2 -e [binary]```

**列出库**

```rabin2 -l [binary]```

# SYNOPSIS

**rabin2** [_-I_] [_-s_] [_-i_] [_-z_] [_-S_] [_options_] _binary_

# PARAMETERS

**-I**
> 二进制文件信息。

**-s**
> 符号。

**-i**
> 导入。

**-E**
> 导出。

**-z**
> 字符串。

**-S**
> 节区。

**-e**
> 入口点。

**-l**
> 库。

**-H**
> 头部字段。

**-c**
> 类（ObjC/Java）。

**-j**
> JSON 输出。

# DESCRIPTION

**rabin2** 从二进制文件中提取信息。它是 radare2 逆向工程框架的组成部分。

二进制信息包括格式、架构和保护机制。可以检测 PIE、栈保护（canary）和 NX。

符号表揭示函数名和变量名。调试符号和动态符号都会列出。

字符串提取可以发现嵌入的文本，有助于找到硬编码的数据。

节区列表展示内存布局，并显示权限和大小。

# CAVEATS

属于 radare2。大型二进制文件可能较慢。已剥离符号的二进制文件信息有限。

# HISTORY

**rabin2** 是 **radare2** 的组成部分，由 **pancake**（Sergi Alvarez）于 **2006 年**前后创建。它无需完整反汇编即可完成二进制分析。

# INSTALL

```dnf: sudo dnf install radare2```

```pacman: sudo pacman -S radare2```

```apk: sudo apk add radare2```

```zypper: sudo zypper install radare2```

```brew: brew install radare2```

```nix: nix profile install nixpkgs#radare2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[r2](/man/r2)(1), [objdump](/man/objdump)(1), [readelf](/man/readelf)(1), [nm](/man/nm)(1)
