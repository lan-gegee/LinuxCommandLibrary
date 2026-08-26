# TAGLINE

基于 LLVM 的 D 编译器

# TLDR

**编译 D 程序**

```ldc2 [source.d]```

**指定输出可执行文件名**

```ldc2 -of=[output] [source.d]```

**开启优化编译**

```ldc2 -O2 [source.d]```

**发布构建**

```ldc2 -release [source.d]```

**调试构建**

```ldc2 -g [source.d]```

**仅编译**

```ldc2 -c [source.d]```

# SYNOPSIS

**ldc2** [_options_] _files_

# PARAMETERS

_FILES_
> D 源文件。

**-of** _FILE_
> 输出文件名。

**-O** _LEVEL_
> 优化级别。

**-release**
> 禁用运行时检查。

**-g**
> 包含调试信息。

**-c**
> 仅编译，不链接。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ldc** 是基于 LLVM 的 D 编译器。它将 D 语言源代码编译为本地可执行文件。

该编译器利用 LLVM 优化生成高速代码。它是与 DMD 并列的 D 语言主要编译器之一。

# CAVEATS

需要 LLVM。D 语言专用。功能上可能落后于 DMD。

# HISTORY

LDC 的创建目的是为 **D 编程语言**提供基于 LLVM 的编译，从而带来更好的优化效果。

# INSTALL

```dnf: sudo dnf install ldc```

```pacman: sudo pacman -S ldc```

```zypper: sudo zypper install ldc```

```brew: brew install ldc```

```nix: nix profile install nixpkgs#ldc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmd](/man/dmd)(1), [gdc](/man/gdc)(1), [dub](/man/dub)(1)
