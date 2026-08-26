# TAGLINE

GNU 链接器

# TLDR

**链接目标文件**

```ld -o [output] [file1.o] [file2.o]```

**链接库**

```ld -o [output] [file.o] -l[library]```

**指定库路径**

```ld -o [output] [file.o] -L[/path/to/lib] -l[name]```

**链接共享库**

```ld -shared -o [lib.so] [file.o]```

**入口点**

```ld -e [main] -o [output] [file.o]```

**详细链接输出**

```ld -v -o [output] [file.o]```

# SYNOPSIS

**ld** [_options_] _files_

# PARAMETERS

_FILES_
> 要链接的目标文件。

**-o** _FILE_
> 输出文件名。

**-l** _NAME_
> 与指定的库链接。

**-L** _DIR_
> 库搜索路径。

**-shared**
> 创建共享库。

**-e** _SYMBOL_
> 入口点符号。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ld** 是 GNU 链接器。它将目标文件组合成可执行文件或库。

链接器负责解析符号并重定位代码。通常通过 gcc 间接调用，而不是直接使用。

# CAVEATS

通常经由 gcc 调用。选项复杂。与平台相关。

# HISTORY

ld 是 GNU 项目的链接器，是 **binutils** 的一部分，为 GNU 工具链提供链接功能。

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

[gcc](/man/gcc)(1), [ld.gold](/man/ld.gold)(1), [ldd](/man/ldd)(1), [nm](/man/nm)(1)
