# TAGLINE

可嵌入的 Common Lisp 解释器

# TLDR

**启动 ECL REPL**

```ecl```

**加载并执行文件**

```ecl -load [file.lisp]```

**求值表达式**

```ecl -eval "(print \"Hello\")"```

**将文件编译为共享库**

```ecl -compile [file.lisp]```

**运行脚本后退出**

```ecl -shell [script.lisp]```

**不加载初始化文件启动**

```ecl -norc```

# SYNOPSIS

**ecl** [_options_] [_args_]

# PARAMETERS

**-load** _file_
> 加载 Lisp 文件。

**-eval** _expr_
> 求值表达式。

**-compile** _file_
> 将文件翻译为 C 并编译成共享库（.fas）。

**-o** _ofile_
> 为编译后的共享库输出文件命名。

**-c** _cfile_
> 为中间 C 文件命名并在编译后保留。

**-h** _hfile_
> 为中间 C 头文件命名并在编译后保留。

**-data** [_datafile_]
> 将编译器数据转储到数据文件中。

**-s**
> 生成可链接的目标文件而非共享库。

**-shell** _script_
> 以脚本方式运行，然后退出。

**-norc**
> 不加载初始化文件（~/.eclrc）。

**-dir** _directory_
> 将指定目录用作系统目录。

**-q**
> 降低编译器输出的详细程度。

# CONFIGURATION

**~/.eclrc**
> 启动时加载的初始化文件，包含用于自定义的 Lisp 表达式。

# DESCRIPTION

**ECL**（Embeddable Common Lisp）是一个设计为可嵌入其他应用的 Common Lisp 实现。它将 Lisp 编译为 C，从而能与 C 库集成并生成原生代码。

ECL 支持完整的 ANSI Common Lisp 标准，并带有线程、FFI（外部函数接口）和嵌入等扩展。它可以生成独立的可执行文件和共享库。

# REPL COMMANDS

```
(quit)           ; Exit ECL
(load "file")    ; Load Lisp file
(compile-file "f"); Compile to object
(require :asdf)  ; Load ASDF
```

# CAVEATS

编译为 C 会增加复杂度。某些库可能需要适配才能在 ECL 上运行。调试编译后的代码比解释执行更困难。线程行为可能与其他实现不同。

# HISTORY

ECL 最初于 **20 世纪 80 年代**在巴黎的 **IRCAM** 开发，当时名为 **KCL**（Kyoto Common Lisp）。它被 fork 后由 **Giuseppe Attardi** 继续开发为 **ECL**，后来交由社区维护。对可嵌入性的专注使其有别于其他 Common Lisp 实现。

# INSTALL

```apt: sudo apt install ecl```

```pacman: sudo pacman -S ecl```

```apk: sudo apk add ecl```

```zypper: sudo zypper install ecl```

```brew: brew install ecl```

```nix: nix profile install nixpkgs#ecl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbcl](/man/sbcl)(1), [clisp](/man/clisp)(1)
