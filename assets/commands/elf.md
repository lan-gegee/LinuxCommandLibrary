# TAGLINE

Unix 二进制文件的可执行与可链接格式（ELF）

# TLDR

**查看 ELF 头**

```readelf -h [binary]```

**列出节区**

```readelf -S [binary]```

**列出程序头**

```readelf -l [binary]```

**显示符号**

```readelf -s [binary]```

**显示动态节区**

```readelf -d [binary]```

**显示全部信息**

```readelf -a [binary]```

# SYNOPSIS

**readelf** [_options_] _elf-file_

# DESCRIPTION

**ELF**（Executable and Linkable Format，可执行与可链接格式）是类 Unix 系统上可执行文件、目标文件、共享库和核心转储的标准二进制格式。**readelf** 和 **objdump** 等工具可以检查 ELF 文件。

ELF 文件包含描述二进制结构的头部、包含代码和数据的节区，以及供运行时加载器使用的段信息。理解 ELF 对调试、逆向工程和系统编程至关重要。

# ELF STRUCTURE

```
ELF Header        - Magic number, architecture, entry point
Program Headers   - Segments for runtime loading
Section Headers   - Sections for linking (.text, .data, etc.)
.text             - Executable code
.data             - Initialized data
.bss              - Uninitialized data
.rodata           - Read-only data
.symtab           - Symbol table
.strtab           - String table
.dynamic          - Dynamic linking info
```

# RELATED TOOLS

```
readelf     - Display ELF information
objdump     - Disassemble and display
nm          - List symbols
ldd         - Show shared library dependencies
file        - Identify file type
```

# SEE ALSO

[readelf](/man/readelf)(1), [objdump](/man/objdump)(1), [nm](/man/nm)(1), [ldd](/man/ldd)(1), [file](/man/file)(1), [strip](/man/strip)(1)

# RESOURCES

```[Documentation](https://man7.org/linux/man-pages/man5/elf.5.html)```

<!-- verified: 2026-07-14 -->
