# TAGLINE

快速词法分析器生成器

# TLDR

从 Lex 文件**生成**分析器（输出：lex.yy.c）

```flex [analyzer.l]```

**指定输出文件**

```flex -o [analyzer.c] [analyzer.l]```

将分析器写入**标准输出**

```flex -t [analyzer.l]```

生成**批处理扫描器**而非交互式扫描器

```flex -B [analyzer.l]```

生成**大小写不敏感**的扫描器

```flex -i [analyzer.l]```

生成启用**调试**的扫描器

```flex -d [analyzer.l]```

**编译**生成的 C 文件

```cc lex.yy.c -o [executable] -lfl```

# SYNOPSIS

**flex** [_options_] [_file..._]

# PARAMETERS

**-o, --outfile** _file_
> 将生成的扫描器写入指定文件

**-t, --stdout**
> 将扫描器写入标准输出而不是文件

**-B, --batch**
> 生成批处理扫描器（为吞吐量优化）

**-I, --interactive**
> 生成交互式扫描器（默认）

**-i, --case-insensitive**
> 生成大小写不敏感的扫描器

**-d, --debug**
> 在生成的扫描器中启用调试模式

**-b, --backup**
> 生成回退信息文件（lex.backup）

**-p, --perf-report**
> 向标准错误输出生成性能报告

**-v, --verbose**
> 向标准错误输出打印扫描器统计信息

**-f, --full**
> 使用完整表生成快速但较大的扫描器（-Cfr）。

**-F, --fast**
> 使用替代表表示生成快速扫描器（-CFr）。

**--header-file** _file_
> 生成 C 头文件

**-+, --c++**
> 生成 C++ 扫描器类

**--yylineno**
> 在生成的扫描器中跟踪行号

# DESCRIPTION

**Flex**（fast lexical analyzer generator，快速词法分析器生成器）生成对文本执行模式匹配的程序。给定一个描述模式和动作的规格文件（通常以 **.l** 为扩展名），flex 会生成实现词法分析器的 C 源代码。

生成的扫描器读取输入，将其与规格中定义的模式进行匹配，并执行相应的动作。这通常用于为编译器和解释器构建分词器，与 **bison** 或 **yacc** 等解析器生成器配合使用。

默认情况下，flex 将输出写到 **lex.yy.c**。生成的代码需要链接 **-lfl**（flex 库），或定义 **yywrap()** 使其返回 1。

# CAVEATS

除非指定了 **%option noyywrap**，否则生成的扫描器依赖于 flex 运行时库（**-lfl**）。庞大的模式集合可能生成体积可观的表驱动扫描器；可以使用压缩选项（**-Ce**、**-Cm**）来减小体积，但要付出一些性能代价。默认的交互式模式会增加缓冲开销；批处理时请使用 **-B**。

# HISTORY

Flex 由 Vern Paxson 于 **1987 年**前后编写，是对 AT&T Unix 原始 **lex** 工具（由 Mike Lesk 和 Eric Schmidt 于 1970 年代中期创建）的自由开源替代品。其名字意为 "fast lexical analyzer generator"。Flex 已成为大多数类 Unix 系统上的标准 lex 实现，目前仍在 GitHub 上持续维护。

# INSTALL

```apt: sudo apt install flex```

```dnf: sudo dnf install flex```

```pacman: sudo pacman -S flex```

```apk: sudo apk add flex```

```zypper: sudo zypper install flex```

```brew: brew install flex```

```nix: nix profile install nixpkgs#flex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lex](/man/lex)(1), [bison](/man/bison)(1), [yacc](/man/yacc)(1), [gcc](/man/gcc)(1), [cc](/man/cc)(1)
