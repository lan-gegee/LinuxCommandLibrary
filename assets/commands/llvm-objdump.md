# TAGLINE

显示目标文件的相关信息

# TLDR

**反汇编目标文件**

```llvm-objdump -d [file.o]```

**显示所有头部信息**

```llvm-objdump -x [file]```

**显示节头部**

```llvm-objdump -h [file]```

**带源码反汇编**

```llvm-objdump -dS [file]```

**显示重定位信息**

```llvm-objdump -r [file.o]```

**显示符号表**

```llvm-objdump -t [file]```

# SYNOPSIS

**llvm-objdump** [_options_] [_file_...]

# PARAMETERS

**-d**, **--disassemble**
> 反汇编 text 节。

**-D**, **--disassemble-all**
> 反汇编所有节。

**-S**, **--source**
> 在反汇编输出中显示源码。

**-h**, **--headers**
> 显示节头部。

**-x**, **--all-headers**
> 显示所有头部信息。

**-t**, **--syms**
> 显示符号表。

**-r**, **--reloc**
> 显示重定位信息。

**--demangle**
> 对符号名进行反修饰。

# DESCRIPTION

**llvm-objdump** 显示目标文件的相关信息。它是 GNU objdump 的直接替代品，支持对多种二进制格式进行反汇编、显示头部信息、查看符号表和重定位信息。

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

[objdump](/man/objdump)(1), [llvm-nm](/man/llvm-nm)(1)
