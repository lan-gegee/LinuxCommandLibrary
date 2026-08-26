# TAGLINE

从语法描述生成解析器

# TLDR

**生成**解析器

```bison [grammar.y]```

以**详细输出**生成

```bison -v [grammar.y]```

**指定**输出文件

```bison -o [parser.c] [grammar.y]```

生成**头文件**

```bison -d [grammar.y]```

# SYNOPSIS

**bison** [_options_] _file_

# DESCRIPTION

**bison** 是一个通用解析器生成器，可将语法描述（.y 文件）转换为 C、C++ 或 Java 解析器。它与 yacc 兼容，用于构建编译器、解释器和其他语言处理器。

该工具是 yacc 的 GNU 替代品，具有更多特性和更好的错误处理。

# PARAMETERS

**-o**, **--output=**_file_
> 输出文件名

**-d**, **--defines**
> 生成包含 token 定义的头部文件（也写作 **--header**）

**-H**, **--header**[**=**_file_]
> 生成 token 定义头文件，可指定路径

**-v**, **--verbose**
> 创建包含解析器状态的 .output 文件

**-t**, **--debug**
> 在解析器中启用调试输出

**-g**, **--graph**
> 生成解析器的 VCG 图形

**-r**, **--report=**_things_
> 生成报告（state、itemset、lookahead）

**-W**, **--warnings**
> 启用警告

**-l**, **--no-lines**
> 不生成 #line 指令

**-L**, **--language=**_lang_
> 目标输出语言：c、c++ 或 java

**-y**, **--yacc**
> 模拟 POSIX yacc（默认输出名 y.tab.c、y.tab.h）

# GRAMMAR FILE FORMAT

```yacc
%{
#include <stdio.h>
%}

%token NUMBER
%%

expr: NUMBER '+' NUMBER { $$ = $1 + $3; }
    ;

%%
```

# FEATURES

- LALR(1) 解析器生成
- GLR 解析支持
- C++、Java 输出
- 位置追踪
- 错误恢复
- 优先级声明
- 语义动作

# WORKFLOW

```bash
# Generate parser
bison -d calculator.y

# Compile with flex lexer
flex lexer.l
gcc lex.yy.c calculator.tab.c -o calculator

# View parser details
bison -v grammar.y
cat grammar.output
```

# CAVEATS

语法学习曲线存在。可能出现移进/归约和归约/归约冲突。生成的代码可能很大。错误信息有时晦涩难懂。通常与 flex 配合进行词法分析。

# HISTORY

**Bison** 由 Robert Corbett 于 **1985 年**编写，作为 Unix yacc 的自由替代品。Richard Stallman 使其与 yacc 兼容，它由此成为 GNU 计划的一部分。现由 Akim Demaille 等人维护。

# INSTALL

```apt: sudo apt install bison```

```dnf: sudo dnf install bison```

```pacman: sudo pacman -S bison```

```apk: sudo apk add bison```

```zypper: sudo zypper install bison```

```brew: brew install bison```

```nix: nix profile install nixpkgs#bison```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flex](/man/flex)(1), [yacc](/man/yacc)(1), [antlr](/man/antlr)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/bison/)```

```[Documentation](https://www.gnu.org/software/bison/manual/)```

<!-- verified: 2026-06-19 -->
