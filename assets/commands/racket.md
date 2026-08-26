# TAGLINE

通用多范式编程语言

# TLDR

**启动 REPL**

```racket```

**运行脚本**

```racket [script.rkt]```

**求值表达式**

```racket -e "(+ 1 2 3)"```

**以指定语言运行**

```racket -l [typed/racket] [script.rkt]```

**加载文件并进入交互**

```racket -it [script.rkt]```

**编译为字节码**

```raco make [script.rkt]```

**创建可执行文件**

```raco exe [script.rkt]```

# SYNOPSIS

**racket** [_-e expr_] [_-l lang_] [_-it_] [_options_] [_file_] [_args_]

# PARAMETERS

**-e** _EXPR_
> 求值表达式。

**-l** _LANG_
> 使用指定语言。

**-f** _FILE_
> 加载文件。

**-t** _FILE_
> require 文件。

**-i**
> 交互模式。

**-it** _FILE_
> 加载并交互。

**-I** _LANG_
> 设置语言并交互。

**-m**, **--main**
> 运行 main 子模块。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

**--**
> 选项结束标记。

# DESCRIPTION

**racket** 是 Racket 语言的主实现。Racket 是 Lisp/Scheme 家族中的一门通用编程语言。

该语言强调面向语言的编程。文件开头的 #lang 指令用于选择语言：racket、typed/racket、scribble 等等。

REPL 提供交互式开发体验。制表符补全、历史记录和内联文档支持探索式编程。

raco 是 Racket 的命令行工具，用于软件包管理、编译、文档生成等任务，扩展了 Racket 的能力。

Typed Racket 添加了可选的静态类型。类型注解能在编译期捕获错误，同时保持 Racket 的表达力。

DrRacket IDE 提供图形化环境，带有调试、性能分析和教学功能。

# CAVEATS

某些方面与标准 Scheme 不同。包系统需要网络访问。标准发行版体积较大。

# HISTORY

**Racket** 由 **1995 年**始于**莱斯大学**的 **PLT Scheme** 演化而来。**2010 年**更名为 Racket，以体现其超越 Scheme 的发展。它被广泛用于程序语言研究与教学。

# INSTALL

```apt: sudo apt install racket```

```dnf: sudo dnf install racket```

```pacman: sudo pacman -S racket```

```apk: sudo apk add racket```

```zypper: sudo zypper install racket```

```brew: brew install racket```

```nix: nix profile install nixpkgs#racket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[raco](/man/raco)(1), [drracket](/man/drracket)(1), [scheme](/man/scheme)(1), [guile](/man/guile)(1)
