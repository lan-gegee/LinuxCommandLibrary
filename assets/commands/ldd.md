# TAGLINE

显示每个程序或共享对象所需的共享对象

# TLDR

显示**共享库依赖**

```ldd /path/to/binary```

显示依赖的**全部信息**

```ldd -v /path/to/binary```

显示**未使用的**直接依赖

```ldd -u /path/to/binary```

报告缺失对象并执行**数据重定位**

```ldd -d /path/to/binary```

报告缺失对象并执行**函数重定位**

```ldd -r /path/to/binary```

# SYNOPSIS

**ldd** [_option_]... _file_...

# DESCRIPTION

**ldd** 显示命令行上每个程序或共享对象所要求的共享对象（共享库）。它识别依赖项，并显示它们的位置及加载地址。

# PARAMETERS

**-v, --verbose**
> 输出全部信息，包括符号版本控制

**-u, --unused**
> 输出未使用的直接依赖

**-d, --data-relocs**
> 执行数据重定位并报告缺失对象（仅限 ELF）

**-r, --function-relocs**
> 执行数据和函数重定位并报告缺失对象（仅限 ELF）

**--version**
> 显示版本信息

**--help**
> 显示用法信息

# CAVEATS

绝不要对不受信任的可执行文件运行 ldd，因为它可能执行任意代码。对于不受信任的二进制文件，请改用：**objdump -p /path/to/program | grep NEEDED**

# HISTORY

**ldd** 是 GNU C 库（glibc）的一部分。它通过设置 **LD_TRACE_LOADED_OBJECTS** 环境变量并调用动态链接器来工作。

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add musl-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ld.so](/man/ld.so)(8), [ldconfig](/man/ldconfig)(8), [objdump](/man/objdump)(1)
