# TAGLINE

列出目标文件、归档和可执行文件中的符号

# TLDR

**列出目标文件中的符号**

```llvm-nm [file.o]```

**仅显示外部符号**

```llvm-nm --extern-only [file.o]```

**仅显示未定义符号**

```llvm-nm --undefined-only [file.o]```

**显示符号大小**

```llvm-nm --print-size [file.o]```

**对 C++ 符号进行反修饰**

```llvm-nm --demangle [file.o]```

# SYNOPSIS

**llvm-nm** [_options_] [_file_...]

# PARAMETERS

**--extern-only**
> 仅显示外部符号。

**--undefined-only**
> 仅显示未定义符号。

**--defined-only**
> 仅显示已定义符号。

**--demangle**
> 对 C++ 符号名进行反修饰。

**--print-size**
> 显示符号大小。

**--no-sort**
> 不排序输出。

**--numeric-sort**
> 按地址排序。

# DESCRIPTION

**llvm-nm** 列出目标文件、归档和可执行文件中的符号。它是 GNU nm 的直接替代品，显示符号名称、类型和地址。可用于调试链接问题以及了解二进制文件的内容。

# INSTALL

```apt: sudo apt install llvm```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nm](/man/nm)(1), [llvm-objdump](/man/llvm-objdump)(1)
