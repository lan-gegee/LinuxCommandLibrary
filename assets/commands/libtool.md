# TAGLINE

隐藏共享库使用复杂性的通用库支持脚本

# TLDR

将源代码**编译**为 libtool 对象

```libtool compile gcc -c [source.c] -o [source.lo]```

**链接**以创建库

```libtool link gcc -o [library.lo] [source.lo]```

**执行**带库路径的程序

```libtool execute gdb [path/to/program]```

**安装**共享库

```libtool install cp [library.la] [install_dir]```

**完成**库的安装

```libtool finish [install_dir]```

**卸载**库

```libtool uninstall [library.la]```

**清理**已卸载的文件

```libtool clean rm [source.lo] [library.la]```

# SYNOPSIS

**libtool** [_mode_] [_mode-args_]

# DESCRIPTION

**libtool** 是一个通用的库支持脚本，它通过一致、可移植的接口隐藏了使用共享库的复杂性。它负责处理共享库在特定平台上的编译、链接和安装。

# PARAMETERS

**compile, c**
> 将源文件编译为 libtool 对象（.lo）

**link, l**
> 创建库或可执行文件

**execute, e**
> 以正确的库路径执行程序

**install, i**
> 安装库或可执行文件

**finish, f**
> 完成 libtool 库的安装

**uninstall, u**
> 删除已安装的库

**clean, cl**
> 删除已卸载的库

# CAVEATS

Libtool 对象（.lo）和归档（.la）是包含元数据的包装文件。实际编译后的文件位于 `.libs/` 子目录中。

# HISTORY

由 Gordon Matzigkeit 于 **1996 年**作为 GNU 项目的一部分创建，旨在简化跨类 Unix 系统的可移植库创建。

# INSTALL

```apt: sudo apt install libtool-bin```

```dnf: sudo dnf install libtool```

```pacman: sudo pacman -S libtool```

```apk: sudo apk add libtool```

```zypper: sudo zypper install libtool```

```brew: brew install libtool```

```nix: nix profile install nixpkgs#libtool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[libtoolize](/man/libtoolize)(1), [automake](/man/automake)(1), [autoconf](/man/autoconf)(1)
