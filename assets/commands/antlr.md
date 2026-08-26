# TAGLINE

从文法文件生成解析器

# TLDR

从文法文件**生成解析器**（默认语言：Java）

```antlr4 [Grammar.g4]```

为指定语言**生成解析器**

```antlr4 -Dlanguage=[Python3] [Grammar.g4]```

**生成带 visitor 类的解析器**

```antlr4 -visitor [Grammar.g4]```

**指定生成文件的输出目录**

```antlr4 -o [output/dir] [Grammar.g4]```

以指定包名**生成解析器**

```antlr4 -package [com.example.parser] [Grammar.g4]```

**同时生成 listener 和 visitor**

```antlr4 -listener -visitor [Grammar.g4]```

携带导入文法搜索路径**生成解析器**

```antlr4 -lib [path/to/imports] [Grammar.g4]```

# SYNOPSIS

**antlr4** [_options_] _grammar-file_...

# PARAMETERS

**-o** _directory_
> 生成文件的输出目录（默认：当前目录）

**-lib** _directory_
> 搜索导入文法和 token 文件的位置

**-Dlanguage=**_lang_
> 目标语言：Java（默认）、Python3、CSharp、JavaScript、TypeScript、Go、Cpp、Swift、Dart、PHP。可用 **-D**_option_**=**_value_ 覆盖任何文法级选项。

**-package** _name_
> 生成代码所属的包或命名空间

**-listener**
> 生成语法树 listener 类（默认）

**-no-listener**
> 不生成语法树 listener

**-visitor**
> 生成语法树 visitor 类

**-no-visitor**
> 不生成语法树 visitor（默认）

**-encoding** _name_
> 文法文件编码（默认：UTF-8）

**-atn**
> 生成用于 ATN 可视化的 DOT 图形文件

**-depend**
> 生成文件依赖信息

**-message-format** _format_
> 输出消息格式：antlr、gnu、vs2005

**-long-messages**
> 出错时显示详细的异常信息

**-Werror**
> 将警告视为错误

**-Xlog**
> 创建详细日志文件（antlr-timestamp.log）

**-Xexact-output-dir**
> 将所有输出直接放入 **-o** 目录，不考虑路径或包结构

**-XdbgST**
> 对生成的代码启动 StringTemplate 可视化工具

# DESCRIPTION

**ANTLR**（ANother Tool for Language Recognition）是一款解析器生成器，可以从文法文件创建词法分析器、语法分析器和树遍历器。它生成的代码能够读取、处理和转换结构化的文本或二进制数据。

ANTLR 文法使用带有语义动作的扩展 BNF 表示法。该工具处理 **.g4** 文法文件并生成目标语言的源代码。生成的解析器会构建语法树，可通过 listener 或 visitor 模式进行遍历。

文法同时定义词法规则（token）和解析规则。ANTLR 自动处理左递归规则，并支持语义谓词、动作和文法导入等特性。生成的解析器采用名为 ALL(*) 的自适应 LL(*) 解析算法。

常见工作流：编写文法文件，运行 antlr4 生成代码，将生成的代码与应用一起编译，然后用解析器处理输入文本。

# CAVEATS

执行时需要 Java 运行环境。**antlr4** 命令通常是一个别名或包装脚本；实际工具以 Java JAR 文件形式运行。生成的代码需要目标语言的 ANTLR 运行时库。大型或有歧义的文法可能导致解析器速度缓慢。

# HISTORY

ANTLR 由 **Terence Parr** 自 **1989 年**起在旧金山大学创建。发布于 **2013 年**的 ANTLR4 引入了 ALL(*) 解析算法，能处理比以往 LL(k) 版本更多的文法结构。该工具被广泛用于构建编程语言、数据格式和领域特定语言，在学术界和商业领域均有应用。

# INSTALL

```apt: sudo apt install pccts```

```aur: yay -S pccts```

```zypper: sudo zypper install antlr```

```brew: brew install antlr```

```nix: nix profile install nixpkgs#antlr```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bison](/man/bison)(1), [flex](/man/flex)(1), [yacc](/man/yacc)(1), [lex](/man/lex)(1)
