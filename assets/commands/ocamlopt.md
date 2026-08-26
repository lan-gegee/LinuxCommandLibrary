# TAGLINE

OCaml 原生代码编译器

# TLDR

**编译为原生代码**

```ocamlopt -o [program] [source.ml]```

**编译多个文件**

```ocamlopt -o [program] [file1.ml] [file2.ml]```

**带优化编译**

```ocamlopt -O3 -o [program] [source.ml]```

**编译为目标文件**

```ocamlopt -c [source.ml]```

**创建原生库**

```ocamlopt -a -o [library.cmxa] [file1.ml] [file2.ml]```

# SYNOPSIS

**ocamlopt** [_options_] _files_...

# PARAMETERS

**-o** _file_
> 指定输出文件名。

**-c**
> 仅编译；跳过链接阶段。生成 `.cmx` 和 `.o` 文件。

**-a**
> 从给定的目标文件构建库（`.cmxa` 和 `.a` 文件）。

**-shared**
> 构建可动态加载的插件（`.cmxs` 文件）。

**-pack**
> 将多个 `.cmx` 文件合并为单个编译单元。

**-O** _level_
> 优化级别：`0` 禁用所有优化，`3` 启用包括去装箱在内的激进优化。默认为 `1`。

**-I** _dir_
> 将 _dir_ 加入 `.cmi` 和 `.cmx` 文件的搜索路径。

**-g**
> 添加调试信息，以支持运行时的栈回溯。

**-S**
> 将编译过程中产生的汇编代码保留在 `.s` 文件中。

**-inline** _n_
> 设置内联的激进程度（默认 10；数值越高内联越多）。

**-compact**
> 优化生成的代码以节省空间而非追求速度。

**-unsafe**
> 禁用数组/字符串访问的边界检查和除零检查；更快但不安全。

**-for-pack** _module-path_
> 生成一个对象文件，之后可作为子模块包含在 `-pack` 编译中。

**-linkall**
> 强制链接库中包含的所有模块。

**-pp** _command_
> 将源文件通过指定的预处理命令管道处理。

**-ppx** _command_
> 将抽象语法树通过指定的预处理器处理。

**-w** _warning-list_
> 启用、禁用或标记特定编译器警告为致命错误。

**-warn-error** _warning-list_
> 将指定警告转为错误。

**-open** _Module_
> 在处理每个源文件前打开指定模块。

**-nostdlib**
> 不将标准库目录加入搜索路径。

**-cc** _ccomp_
> 构建可执行文件时使用 _ccomp_ 作为 C 链接器。

**-cclib** _-llib_
> 与给定的 C 库链接。

**-ccopt** _option_
> 将 _option_ 传递给 C 编译器和链接器。

**-verbose**
> 打印所有正在执行的外部命令。

**-v**
> 打印编译器的版本号和标准库位置。

**-i**
> 将推断出的接口打印到 stdout；不生成目标文件。

**-bin-annot**
> 在 `.cmt` 和 `.cmti` 文件中生成详细的类型与位置信息。

# DESCRIPTION

**ocamlopt** 是 OCaml 的原生代码编译器。它将 OCaml 源文件直接编译为原生机器码，生成的可执行文件比字节码编译器 **ocamlc** 快得多。其输出与架构相关，不能跨平台移植。

编译分三个阶段进行：类型检查并编译为 `.cmx` / `.o` 文件（`-c`）、可选的库归档（`-a`），以及链接。接口文件（`.mli`）会编译为 `.cmi` 文件，可与字节码编译器共享。

# CAVEATS

原生代码编译比字节码编译慢。生成的可执行文件是平台特定的。调试原生代码比调试字节码困难；**ocamldebug** 不支持原生可执行文件（请使用 `-g` 以及 `gdb` 等系统调试器）。

# HISTORY

OCaml 原生代码编译器由 **INRIA** 与字节码编译器一同开发，是 Caml/OCaml 项目的一部分，旨在保持语言类型安全保证的同时提供高性能编译。

# INSTALL

```apt: sudo apt install ocaml```

```dnf: sudo dnf install ocaml```

```pacman: sudo pacman -S ocaml```

```apk: sudo apk add ocaml5```

```zypper: sudo zypper install ocaml```

```brew: brew install ocaml```

```nix: nix profile install nixpkgs#ocaml```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ocamlc](/man/ocamlc)(1), [ocamlfind](/man/ocamlfind)(1), [opam](/man/opam)(1), [dune](/man/dune)(1)
