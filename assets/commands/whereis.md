# TAGLINE

定位二进制文件、源码文件和 man page 文件

# TLDR

定位 SSH 的**二进制文件、源码文件和 man page**

```whereis ssh```

只定位 ls 的**二进制文件和 man page**

```whereis -bm ls```

定位 gcc 的**源码**和 Git 的 **man page**

```whereis -s gcc -m git```

只在 /usr/bin/ 中定位 gcc 的**二进制文件**

```whereis -b -B /usr/bin/ -f gcc```

定位**异常的**二进制文件（多于或少于一个二进制文件）

```whereis -u *```

定位带有**异常手册条目**的二进制文件

```whereis -u -m *```

# SYNOPSIS

**whereis** [**-bmsuf**] [**-BMS** _directory_... **-f**] _name_...

# PARAMETERS

**-b**
> 只搜索二进制文件

**-m**
> 只搜索手册章节

**-s**
> 只搜索源码

**-u**
> 搜索异常条目（拥有多于一个二进制文件、或没有手册的命令）

**-B** _list_
> 将二进制搜索限制在指定目录

**-M** _list_
> 将手册搜索限制在指定目录

**-S** _list_
> 将源码搜索限制在指定目录

**-f**
> 终止目录列表（使用 -B、-M 或 -S 时必需）

**-l**
> 输出生效的搜索路径列表

# DESCRIPTION

**whereis** 通过搜索一组标准位置来定位命令的二进制文件、源码文件和手册页文件。与 **which** 不同，它搜索的是预定义目录而非 PATH 变量，并且能找到源码和文档文件。

该命令使用硬编码的目录列表，可能包括 /bin、/sbin、/usr/bin、/usr/share/man、/usr/src 及类似的系统目录。使用 **-l** 可以查看你系统上的实际搜索路径。

# CAVEATS

可能找不到位于非标准位置的二进制文件（基于 PATH 的查找请使用 **which**）。二进制发行版中源码目录通常是空的。结果取决于编译时内置的搜索路径，不同发行版之间有所差异。

# HISTORY

起源于 UC Berkeley 的 **3BSD Unix**（1979 年），是伯克利早期添加到 Unix 中用于定位程序组件的工具之一。在现代 Linux 系统上是 **util-linux** 的一部分。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[which](/man/which)(1), [whatis](/man/whatis)(1), [type](/man/type)(1), [locate](/man/locate)(1)
