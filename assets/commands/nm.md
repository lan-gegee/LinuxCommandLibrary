# TAGLINE

列出目标文件中的符号

# TLDR

**列出符号**

```nm [binary]```

**只显示外部符号**

```nm -g [binary]```

**显示未定义符号**

```nm -u [binary]```

**显示已定义符号**

```nm -U [binary]```

**反修饰（demangle）C++ 符号**

```nm -C [binary]```

**按地址排序**

```nm -n [binary]```

**显示符号大小**

```nm -S [binary]```

# SYNOPSIS

**nm** [_options_] _files_

# PARAMETERS

_FILES_
> 目标文件或库。

**-g**
> 仅限外部符号。

**-u**
> 仅限未定义符号。

**-U**
> 仅限已定义符号。

**-C**
> 反修饰 C++ 名称。

**-n**
> 按地址排序。

**-S**
> 打印符号大小。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nm** 列出目标文件中的符号。显示函数和变量名称。

该工具用于检查二进制文件。是调试和逆向工程的必备工具。

# CAVEATS

要有调试符号才能获得最佳效果。属于 binutils。不同平台存在差异。

# HISTORY

nm 是早期 Unix 系统中经典的 **Unix** 工具，用于检查目标文件的符号。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[objdump](/man/objdump)(1), [readelf](/man/readelf)(1), [strings](/man/strings)(1)
