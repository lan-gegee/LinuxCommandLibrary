# TAGLINE

OCaml 的交互式顶层环境，OCaml 是一种静态类型函数式编程语言

# TLDR

**启动交互式顶层环境**

```ocaml```

**运行 OCaml 脚本**

```ocaml [script.ml]```

**带库运行**

```ocaml -I +[str] str.cma [script.ml]```

**运行表达式**

```ocaml -e "print_endline \"Hello\""```

**以自定义初始化文件启动**

```ocaml -init [.ocamlinit]```

**添加库路径**

```ocaml -I [/path/to/lib]```

**带性能分析运行**

```ocaml -p [script.ml]```

# SYNOPSIS

**ocaml** [_-I dir_] [_-init file_] [_-e expr_] [_options_] [_script.ml_] [_arguments_]

# PARAMETERS

**-I** _DIR_
> 将目录加入库搜索路径。

**-init** _FILE_
> 加载初始化文件。

**-noinit**
> 不加载 .ocamlinit。

**-e** _EXPR_
> 求值表达式后退出。

**-stdin**
> 从 stdin 读取脚本。

**-noprompt**
> 在交互模式下隐藏提示符。

**-w** _FLAGS_
> 警告设置。

**-warn-error** _FLAGS_
> 将警告视为错误。

**-version**
> 打印版本。

**-vnum**
> 仅打印版本号。

**-help**
> 显示帮助。

# TOPLEVEL COMMANDS

**#use "file.ml";;**
> 加载源文件。

**#load "module.cma";;**
> 加载字节码库。

**#directory "path";;**
> 添加到搜索路径。

**#show identifier;;**
> 显示类型/模块信息。

**#trace function;;**
> 跟踪函数调用。

**#quit;;**
> 退出顶层环境。

**#help;;**
> 显示指令帮助。

# DESCRIPTION

**ocaml** 是 OCaml 的交互式顶层环境（REPL），OCaml 是一种带有类型推断的静态类型函数式编程语言。

顶层环境读取表达式，编译、执行并打印结果及其类型。表达式以 `;;` 结尾。类型推断系统即使在交互模式下也能在编译时捕获错误。

用 #use 加载的文件会在当前会话中执行其定义。库（.cma 字节码）用 #load 加载。-I 标志将目录加入模块搜索路径。

主目录或当前目录下的 .ocamlinit 文件会在启动时执行。它可以加载常用库、定义工具函数并配置环境。

与 utop 集成可获得增强的顶层环境，提供语法高亮、补全和历史记录。许多用户在交互式开发时更偏好 utop。

对于较大的项目，Dune 构建系统负责编译，但 ocaml 在探索、原型开发和学习方面仍然很有用。

# CAVEATS

表达式必须以 ;; 结尾。某些库需要显式加载。错误信息对初学者可能晦涩难懂。可以使用可变状态但不推荐。真实项目建议使用构建系统。

# HISTORY

**OCaml** 由法国 **INRIA** 自 **1980 年代**起开发的 Caml Light 演化而来。OCaml（Objective Caml）于 **1996 年**加入了对象和原生编译支持。该语言影响了 Rust、F# 等。ocaml 顶层环境在其整个历史中一直是标准的 REPL。

# INSTALL

```apt: sudo apt install ocaml-interp```

```dnf: sudo dnf install ocaml```

```pacman: sudo pacman -S ocaml```

```apk: sudo apk add ocaml5```

```zypper: sudo zypper install ocaml```

```brew: brew install ocaml```

```nix: nix profile install nixpkgs#ocaml```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ocamlopt](/man/ocamlopt)(1), [ocamlc](/man/ocamlc)(1), [dune](/man/dune)(1), [opam](/man/opam)(1), [utop](/man/utop)(1)
