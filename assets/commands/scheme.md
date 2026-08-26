# TAGLINE

Scheme 编程语言解释器

# TLDR

**启动 REPL**

```scheme```

**运行文件**

```scheme [file.scm]```

**求值表达式**

```scheme -e "[(+ 1 2)]"```

**加载文件后进入 REPL**

```scheme -l [file.scm]```

**安静模式**

```scheme -q```

# SYNOPSIS

**scheme** [_-e expr_] [_-l file_] [_options_] [_file_]

# PARAMETERS

**-e** _EXPR_
> 求值表达式。

**-l** _FILE_
> 加载文件。

**-q**
> 安静启动。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**scheme** 是 Scheme 编程语言的解释器。Scheme 是 Lisp 的一个极简方言，强调函数式编程、词法作用域和一等过程。它既提供用于实验的交互式 REPL，也能直接运行 Scheme 源文件。

Scheme 的设计遵循 R5RS 和 R7RS 语言标准，提供了一个小巧而强大的核心，具备适当的尾递归、continuation 和卫生宏等特性。交互式 REPL 可以立即对表达式求值，非常适合学习、原型设计和算法探索。

**scheme** 命令在不同系统上可能指向不同的实现，包括 MIT/GNU Scheme、Chez Scheme 或 GNU Guile。每种实现都在标准之上提供了自己的扩展，因此行为和可用库可能有所不同。

# CAVEATS

具体实现因系统而异。命令名可能不同（guile、mit-scheme）。存在可移植性问题。

# HISTORY

**Scheme** 由 **Guy Steele** 和 **Gerald Sussman** 于 1975 年设计。各种实现都提供了 scheme 命令。

# SEE ALSO

[guile](/man/guile)(1), [racket](/man/racket)(1), [clisp](/man/clisp)(1)
