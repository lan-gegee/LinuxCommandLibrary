# TAGLINE

Haskell 的解析器生成器，类似于 C 语言中的 yacc

# TLDR

**从文法文件生成解析器**

```happy [grammar.y] -o [Parser.hs]```

**生成信息文件以便调试**

```happy -i [grammar.y]```

**使用 GHC 扩展生成更快的代码**

```happy -g [grammar.y]```

**生成基于数组并以 GHC 字符串编码的解析器**

```happy -ag [grammar.y]```

**生成运行时可打印调试信息的解析器**

```happy -d [grammar.y]```

**生成 GLR 解析器**

```happy -l [grammar.y]```

# SYNOPSIS

**happy** [_options_] _file_

# PARAMETERS

_FILE_
> 文法文件（.y）。

**-o** _FILE_
> 输出文件名。默认为 FILE.hs。

**-i** [_FILE_]
> 生成包含文法细节、解析器状态和冲突信息的信息文件。

**-g**, **--ghc**
> 使用 GHC 特有的扩展，以生成更快的解析器。

**-a**, **--array**
> 生成基于数组的解析器（更小但更慢）。与 -g 组合时，数组会编码为字符串以提升性能。

**-c**, **--coerce**
> 使用 GHC 的 unsafeCoerce# 生成更小更快的解析器。如果文法存在类型错误，可能在运行时崩溃。

**-d**, **--debug**
> 生成会向 stderr 打印移进/归约调试信息的解析器。

**-l**, **--glr**
> 生成 GLR 解析器而不是 LALR(1)。

**-t** _DIR_, **--template=**_DIR_
> 模板文件所在目录。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 打印版本信息。

# DESCRIPTION

**Happy** 是 Haskell 的解析器生成器，类似于 C 语言中的 yacc。它接受一份文法规范并生成一个 Haskell 解析器模块。

该工具从类 BNF 文法生成 LALR 解析器，也可以生成 GLR 解析器。它与 Alex 词法分析器生成器集成，构成完整的解析方案。

# CAVEATS

仅适用于 Haskell。文法语法有一定的学习曲线。需要调试移进/归约冲突。

# HISTORY

Happy 是为 **Haskell** 打造的 yacc/bison 等价物，广泛用于 Haskell 编译器以及 GHC 等工具中。

# INSTALL

```apt: sudo apt install happy```

```dnf: sudo dnf install happy```

```pacman: sudo pacman -S happy```

```apk: sudo apk add happy```

```zypper: sudo zypper install happy```

```nix: nix profile install nixpkgs#happy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alex](/man/alex)(1), [ghc](/man/ghc)(1), [yacc](/man/yacc)(1), [bison](/man/bison)(1)
