# TAGLINE

增强型的 OCaml 交互式顶层 REPL

# TLDR

**启动 utop REPL**

```utop```

**把文件加载进 utop**

```utop -init [file.ml]```

**加载特定库后启动**

```utop -require [lwt]```

**求值表达式后退出**

```utop -e "[print_endline \"Hello\"]"```

**不加载初始化文件启动**

```utop -no-init```

# SYNOPSIS

**utop** [_options_] [_file_]

# PARAMETERS

**-init** _file_
> 启动时加载指定的文件。

**-require** _package_
> 引入指定的 findlib 软件包。

**-e** _expression_
> 对表达式求值后退出。

**-no-init**
> 跳过初始化文件的加载。

**-emacs**
> 以 Emacs 模式运行。

**-stdin**
> 从标准输入读取内容。

**-help**
> 显示帮助。

# COMMANDS

**#help**: 显示可用命令。

**#quit** 或 Ctrl-D：退出 utop。

**#use** _file_: 把文件加载进当前会话。

**#require** _package_: 加载 findlib 软件包。

**#list**: 列出已加载的模块。

**#utop_bindings**: 显示按键绑定。

# DESCRIPTION

**utop** 是一款面向 OCaml 的增强型顶层环境（REPL），特性包括实时的上下文敏感补全、语法高亮、历史记录以及对多种编辑模式的支持。

补全栏会在你输入时展示候选补全项并动态更新。使用 Alt-Left/Right 在候选间导航，按 Alt-Down 选中。界面支持多行输入，不需要显式的续行符。

utop 可与 Emacs 集成，配合 Tuareg、caml 和 ReasonML 等模式工作。在 Emacs 中执行 M-x utop 即可启动会话，并获得额外的按键绑定，用于对缓冲区中的代码求值。

# CONFIGURATION

**~/.config/utop/init.ml**: 初始化脚本。

**~/.utoprc**: 颜色与相关设置的配置文件。

**~/.ocamlinit**: 另一种初始化文件（标准 ocaml 也使用它）。

# CAVEATS

需要安装 OCaml。部分功能依赖 findlib。Emacs 集成需要事先配置好相应的模式。体量较大的软件包可能拖慢启动速度。

# HISTORY

**utop** 作为标准 OCaml 顶层的现代化替代品而诞生，凭借补全、历史记录和编辑器集成显著改善了用户体验。它由 OCaml 社区维护，如今已成为 OCaml 开发中受推荐的 REPL。

# INSTALL

```apt: sudo apt install utop```

```dnf: sudo dnf install utop```

```apk: sudo apk add utop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ocaml](/man/ocaml)(1), [ocamlfind](/man/ocamlfind)(1), [opam](/man/opam)(1)
