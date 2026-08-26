# TAGLINE

ANSI Common Lisp 实现

# TLDR

**启动交互式 REPL**

```clisp```

**运行 Lisp 文件**

```clisp [script.lisp]```

**求值表达式**

```clisp -x "(print \"Hello World\")"```

**加载文件并进入 REPL**

```clisp -i [script.lisp]```

**将文件编译为字节码**

```clisp -c [source.lisp]```

不显示启动消息地**运行**

```clisp -q```

**设置内存限制**

```clisp -m [100MB]```

# SYNOPSIS

**clisp** [_options_] [_files_]

# PARAMETERS

**-c** _file_
> 将文件编译为字节码（.fas）。

**-x** _expression_
> 执行表达式后退出。

**-i** _file_
> 在进入 REPL 前加载文件。

**-o** _file_
> 编译输出文件。

**-q**, **--quiet**
> 不显示横幅和启动消息。

**-m** _size_
> 设置内存大小限制。

**-M** _file_
> 使用内存映像文件。

**-modern**
> 使用现代（小写）符号大小写。

**-ansi**
> 遵循 ANSI Common Lisp 标准。

**-traditional**
> 使用传统（ANSI 之前）行为。

**-norc**
> 不加载用户 RC 文件（~/.clisprc.lisp）。

**-repl**
> 无论其他选项如何都启动 REPL。

**-on-error** _action_
> 出错时的处理方式：debug、exit、abort、appease。

**-disable-readline**
> 输入时不使用 GNU readline。

**--help**
> 显示帮助。

**--version**
> 显示版本信息。

# DESCRIPTION

**CLISP** 是 ANSI Common Lisp 的一个实现，提供交互式开发环境和编译器。它具有字节码编译器、解释器、调试器以及 CLOS（Common Lisp Object System）支持。

REPL（Read-Eval-Print Loop）提供带 readline 支持、历史记录和补全的交互式 Lisp 开发。文件可以被加载、编译为字节码以加快执行，或组合成独立的可执行文件。

CLISP 包含广泛的标准库支持、用于调用 C 代码的外部函数接口（FFI）、套接字与网络功能，以及包括 Unicode 在内的国际化支持。

# CAVEATS

字节码不能跨不同 CLISP 版本或平台移植。某些 Common Lisp 库可能存在兼容性问题。性能通常慢于 SBCL 等编译型实现。其 FFI 语法与其他 Lisp 实现不同。

# HISTORY

CLISP 最初由 **Bruno Haible** 和 **Michael Stoll** 于 **1987 年**在德国卡尔斯鲁厄大学开始开发。它被设计为可移植且节省内存的实现。数十年来该项目由众多贡献者维护，至今仍是最具可移植性的 Common Lisp 实现之一，可在 Unix、Windows 和嵌入式系统等众多平台上运行。

# INSTALL

```apt: sudo apt install clisp```

```dnf: sudo dnf install clisp```

```pacman: sudo pacman -S clisp```

```apk: sudo apk add clisp```

```zypper: sudo zypper install clisp```

```brew: brew install clisp```

```nix: nix profile install nixpkgs#clisp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sbcl](/man/sbcl)(1), [ecl](/man/ecl)(1), [quicklisp](/man/quicklisp)(1)
