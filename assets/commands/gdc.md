# TAGLINE

D 编程语言的 GNU D 编译器

# TLDR

**编译 D 文件**

```gdc [source.d] -o [output]```

**开启优化编译**

```gdc -O2 [source.d] -o [output]```

**启用调试信息**

```gdc -g [source.d] -o [output]```

**仅编译**

```gdc -c [source.d]```

**链接库**

```gdc [source.d] -l[library] -o [output]```

# SYNOPSIS

**gdc** [_options_] _files_...

# PARAMETERS

_FILES_
> 要编译的 D 源文件。

**-o** _FILE_
> 输出文件名。

**-c**
> 仅编译，不链接。

**-g**
> 生成调试信息。

**-O** _LEVEL_
> 优化级别（0-3）。

**-I** _PATH_
> 导入路径。

**-L** _FLAG_
> 链接器标志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gdc** 是 GNU D 编译器，为 GCC（GNU 编译器套件）后端提供 D 编程语言前端。它借助 GCC 成熟的优化基础设施和代码生成能力，将 D 源代码编译为原生机器码。

该编译器支持 D2 语言规范，包括编译期函数执行（CTFE）、mixin、模板和垃圾回收等现代特性。作为 GCC 前端，gdc 与 GNU 工具链无缝集成，接受熟悉的 GCC 标志来控制优化级别、调试、链接和交叉编译。

gdc 受益于 GCC 广泛的平台支持，使 D 代码可以移植到 GCC 支持的各种架构上。它利用 GCC 成熟的优化过程，通常能生成高效的原生代码。该编译器还可以通过 D 的外部函数接口能力与 C 和 C++ 代码互操作。

虽然参考实现 DMD 编译器通常率先实现新的语言特性，但 gdc 提供了更广泛的平台支持，并受益于 GCC 的优化技术。当优先考虑最大可移植性、GCC 生态集成或特定的优化特性时，它是 D 开发的可靠选择。

# CAVEATS

可能落后于参考的 DMD 编译器。某些 D 特性可能存在差异。存在 GCC 版本依赖。

# HISTORY

gdc 的开发目的是将 D 编程语言引入 GCC，作为参考 DMD 编译器之外提供更广泛平台支持的选择。

# INSTALL

```apt: sudo apt install gdc```

```dnf: sudo dnf install gcc-gdc```

```apk: sudo apk add gcc-gdc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [dmd](/man/dmd)(1), [ldc](/man/ldc)(1), [dub](/man/dub)(1)
