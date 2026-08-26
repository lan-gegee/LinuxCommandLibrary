# TAGLINE

GCC 封装器，改用 musl libc 而非 glibc 编译程序

# TLDR

**使用 musl libc 编译程序**

```musl-gcc -o [program] [source.c]```

**编译静态二进制文件**

```musl-gcc -static -o [program] [source.c]```

**带优化编译**

```musl-gcc -O2 -o [program] [source.c]```

# SYNOPSIS

**musl-gcc** [_options_] _source_files_...

# PARAMETERS

**-o** _file_
> 输出文件名。

**-static**
> 创建静态链接的二进制文件。

**-O** _level_
> 优化级别。

**-specs** _file_
> 使用自定义 specs 文件。

# DESCRIPTION

**musl-gcc** 是一个 GCC 封装器，它让程序链接 musl libc 而不是 glibc。musl 是一款为静态链接和嵌入式系统设计的轻量级 C 标准库。它能生成更小的可移植二进制文件，适合容器和极简环境使用。

# INSTALL

```apt: sudo apt install musl-tools```

```dnf: sudo dnf install musl-gcc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang](/man/clang)(1)
