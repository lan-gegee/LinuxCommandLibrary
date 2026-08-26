# TAGLINE

C 源代码美化器

# TLDR

**美化文件中的 C 代码**

```cb < [path/to/source.c] > [path/to/output.c]```

**按 Kernighan & Ritchie 风格格式化**

```cb -s < [path/to/source.c]```

**设置最大行宽**

```cb -l [80] < [path/to/source.c]```

**将 case 标签合并到单行**

```cb -j < [path/to/source.c]```

**显示版本信息**

```cb -V```

# SYNOPSIS

**cb** [**-s**] [**-j**] [**-l** _length_] [**-V**] [_file_ ...]

# DESCRIPTION

**cb**（C Beautifier）是一个经典的 Unix 工具，用于重新排版 C 源代码以提升可读性。它从参数或标准输入读取，将美化后的代码写到标准输出，因此适合在管道中使用。

该工具只进行词法层面的排版而不做完整的语法分析，通过调整缩进、空格和换行来呈现代码结构。

# PARAMETERS

**-s**
> 按《The C Programming Language》中 Kernighan & Ritchie 的风格输出代码

**-j**
> 把被拆开的行重新拼合

**-l** _length_
> 拆分超过 _length_ 的行

**-V**
> 将版本信息打印到标准错误

# CAVEATS

**cb** 命令只做词法分析，对于会改变代码结构的复杂预处理器宏可能产生错误的格式。它只支持 C 代码，不支持 C++ 或其他语言。

在现代 Linux 发行版中，**cb** 通常不再默认安装，基本上已被视为过时。

# HISTORY

**cb** 命令起源于贝尔实验室的早期 Unix 系统，是用于统一 C 代码格式的简单工具。如今它已被 **indent**、**astyle** 和 **clang-format** 等更完善的格式化工具取代，后者具备更完整的语法理解能力和更高的可配置性。

# INSTALL

```apk: sudo apk add clipboard```

```brew: brew install clipboard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[indent](/man/indent)(1), [clang-format](/man/clang-format)(1), [astyle](/man/astyle)(1)
