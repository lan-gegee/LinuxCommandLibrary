# TAGLINE

GNU Ubiquitous Intelligent Language for Extensions（GNU 扩展语言）

# TLDR

**启动交互式 REPL**

```guile```

**运行脚本文件**

```guile -s [script.scm]```

**求值表达式后退出**

```guile -c "(display \"Hello\")"```

**加载文件后进入交互式 REPL**

```guile -l [library.scm] --```

**以指定入口函数运行脚本**

```guile -e [main] -s [script.scm] [args]```

**向模块加载路径添加目录**

```guile -L [/path/to/modules] -s [script.scm]```

**加载 SRFI 扩展**

```guile --use-srfi=[1,13] -s [script.scm]```

**以启用调试 VM 的方式启动**

```guile --debug [script.scm]```

# SYNOPSIS

**guile** [_-L directory_] [_-l file_] [_-e function_] [_\\_] [_-c expr_] [_-s script_] [_--_] [_script_] [_args_]

# PARAMETERS

**-s** _SCRIPT_
> 从 SCRIPT 加载 Scheme 源码并作为脚本执行。

**-c** _EXPR_
> 将 EXPR 作为 Scheme 表达式求值后退出。

**-l** _FILE_
> 从 FILE 加载 Scheme 源代码。

**-e** _FUNCTION_
> 读取脚本后，将 FUNCTION 应用于命令行参数。

**-L** _DIRECTORY_
> 将 DIRECTORY 添加到 Guile 模块加载路径的最前面。

**-x** _EXTENSION_
> 向 Guile 的加载扩展名列表添加 EXTENSION。

**-ds**
> 在选项序列的当前位置执行 -s SCRIPT（与 -l 配合使用）。

**--**
> 停止参数处理并以交互模式启动 Guile。

**\\**
> 元开关，用于绕过 #! 脚本的限制。

**--debug**
> 以调试 VM 启动（交互模式下为默认）。

**--no-debug**
> 不使用调试 VM 启动。

**--auto-compile**
> 自动编译源文件（默认）。

**--no-auto-compile**
> 禁用自动源文件编译。

**--listen**[=_P_]
> 在端口或套接字 P 上监听远程 REPL 连接。

**--use-srfi=**_N,M,..._
> 加载 SRFI 扩展 N、M 等。

**-q**
> 交互模式下不加载用户的初始化文件。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**Guile** 即 GNU Ubiquitous Intelligent Language for Extensions。它实现了 R5RS 和 R6RS Scheme 标准，用于编写脚本和扩展应用程序。

Guile 提供完整的 Scheme 功能，并附带面向实用编程的扩展，包括模块系统、POSIX 接口、网络功能和 SRFI 支持。它作为 GNU 官方的扩展语言，被设计为可嵌入 C/C++ 应用。源文件会自动编译为字节码以加快执行速度。

# CAVEATS

Scheme 语法与其他 Lisp 方言不同。扩展库和 API 在 Guile 2.x 与 3.x 之间可能存在差异。GUILE_LOAD_PATH 和 GUILE_LOAD_COMPILED_PATH 环境变量控制模块搜索路径。

# HISTORY

Guile 由 **GNU 工程**创建，作为其官方扩展语言，首次发布于 **1993 年**。

# INSTALL

```pacman: sudo pacman -S guile```

```apk: sudo apk add guile```

```zypper: sudo zypper install guile```

```brew: brew install guile```

```nix: nix profile install nixpkgs#guile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scheme](/man/scheme)(1), [racket](/man/racket)(1), [clisp](/man/clisp)(1), [emacs](/man/emacs)(1)
