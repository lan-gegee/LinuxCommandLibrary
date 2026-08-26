# TAGLINE

面向 C 的 LALR 解析器生成器

# TLDR

从语法文件**生成解析器**

```yacc [grammar.y]```

生成解析器及用于记号定义的**头文件**

```yacc -d [grammar.y]```

**使用自定义文件名前缀**代替 y

```yacc -b [prefix] [grammar.y]```

**使用自定义符号前缀**代替 yy

```yacc -p [prefix] [grammar.y]```

**生成描述解析器的详细输出**

```yacc -v [grammar.y]```

在生成的代码中**启用调试**

```yacc -t [grammar.y]```

将代码与表**生成为独立文件**

```yacc -r [grammar.y]```

# SYNOPSIS

**yacc** [_-dgilrtv_] [_-b prefix_] [_-p prefix_] _filename_

# PARAMETERS

**-b** _prefix_
> 输出文件名使用 prefix 而不是 **y**。

**-d**
> 生成包含记号定义的头文件 **y.tab.h**。

**-g**
> 生成 graphviz 格式的文件 **y.dot** 用于可视化。

**-i**
> 生成补充头文件 **y.tab.i**。

**-l**
> 不在生成的代码中插入 **#line** 指令。

**-p** _prefix_
> yacc 生成的符号使用 prefix 而不是 **yy**。

**-P**
> 创建可重入的（纯）解析器。

**-r**
> 将代码（**y.code.c**）和表（**y.tab.c**）生成为独立文件。

**-t**
> 在编译后的代码中启用调试语句。

**-v**
> 生成详细的描述文件 **y.output**。

**-V**
> 打印版本信息。

# DESCRIPTION

**yacc**（Yet Another Compiler Compiler）是一个 LALR(1) 解析器生成器，读取语法规范并生成 C 语言解析器代码。语法文件定义了记号、语法规则和语义动作。

yacc 生成的 **y.tab.c** 包含解析表和驱动例程。配合 **-d** 使用时，还会生成包含记号定义的 **y.tab.h**，供 lex/flex 词法分析器使用。

在大多数 Linux 系统上，**yacc** 实际上是 **bison**（GNU 解析器生成器）或 **byacc**（Berkeley Yacc），两者都与传统的 AT&T yacc 兼容。

# CAVEATS

yacc 会报告移进/归约冲突和归约/归约冲突，这些冲突可能表明语法存在歧义。永远不会被归约的规则也会被报告。生成的解析器默认使用全局变量；需要可重入解析器时请使用 **-P**。

# HISTORY

yacc 由贝尔实验室的 **Stephen C. Johnson** 编写，于 **1975 年**随 Unix Version 6 首次发布。名字是 "Yet Another Compiler Compiler" 的缩写。**Berkeley Yacc**（byacc）由 Robert Corbett 于 **1989 年**编写，是一个公有领域实现。**GNU Bison** 是一个兼容的替代品并带有扩展，首次发布于 **1985 年**，现在是 GNU/Linux 系统上的标准 yacc。

# INSTALL

```dnf: sudo dnf install bison```

```pacman: sudo pacman -S bison```

```apk: sudo apk add bison```

```zypper: sudo zypper install bison```

```brew: brew install bison```

```nix: nix profile install nixpkgs#bison```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bison](/man/bison)(1), [lex](/man/lex)(1), [flex](/man/flex)(1), [cc](/man/cc)(1)
