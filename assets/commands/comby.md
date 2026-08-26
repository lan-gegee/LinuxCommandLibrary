# TAGLINE

结构化代码搜索替换工具

# TLDR

**简单替换**

```comby 'console.log(:[arg])' 'logger.info(:[arg])' [.js]```

**在目录中替换**

```comby 'foo(:[x])' 'bar(:[x])' [src/] -matcher [.py]```

**预览更改**

```comby 'old' 'new' -match-only```

**交互式审查**

```comby 'pattern' 'replacement' -review```

**原地修改**

```comby 'old' 'new' -in-place [file.go]```

**输出 diff**

```comby 'old' 'new' -diff [file.js]```

# SYNOPSIS

**comby** _match_template_ _rewrite_template_ [_path_] [_options_]

# DESCRIPTION

**comby** 是适用于任何语言的结构化代码搜索替换工具。它使用带孔洞（:[name]）的轻量级模板来匹配代码结构，能理解代码块、字符串和注释的语法。

# PARAMETERS

**-matcher** _ext_
> 文件扩展名匹配器（.py、.js 等）

**-match-only**
> 只显示匹配项，不进行重写

**-in-place**
> 原地修改文件

**-diff**
> 显示统一 diff 输出

**-review**
> 交互式审查模式

**-stdin**
> 从标准输入读取

**-stdout**
> 写入标准输出

**-count**
> 仅统计匹配数量

**-d** _dir_
> 目标目录

# HOLE SYNTAX

**:[name]**
> 匹配任意表达式

**:[name:e]**
> 匹配配平的表达式（括号闭合平衡）

**:[[name]]**
> 跨行匹配

**:[_]**
> 匿名孔洞（丢弃）

# CAVEATS

对于嵌套结构比正则表达式更好用。不支持缩进敏感的语言（Python、Haskell）。

# INSTALL

```brew: brew install comby```

```nix: nix profile install nixpkgs#comby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sed](/man/sed)(1), [ast-grep](/man/ast-grep)(1), [semgrep](/man/semgrep)(1)

# RESOURCES

```[Source code](https://github.com/comby-tools/comby)```

```[Homepage](https://comby.dev)```

```[Documentation](https://comby.dev/docs/overview)```

<!-- verified: 2026-06-22 -->
