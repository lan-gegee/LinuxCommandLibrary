# TAGLINE

OCaml 字节码编译器

# TLDR

**编译为字节码**

```ocamlc -o [program] [source.ml]```

**编译多个文件**

```ocamlc -o [program] [file1.ml] [file2.ml]```

**带库编译**

```ocamlc -I +[library] [library].cma [source.ml] -o [program]```

**编译为目标文件**

```ocamlc -c [source.ml]```

**带调试信息编译**

```ocamlc -g -o [program] [source.ml]```

# SYNOPSIS

**ocamlc** [_options_] _files_...

# PARAMETERS

**-o** _file_
> 输出文件名。

**-c**
> 仅编译（不链接）。

**-I** _dir_
> 添加包含目录。

**-g**
> 包含调试信息。

**-i**
> 打印推断出的类型。

**-a**
> 创建库归档。

**-linkall**
> 链接所有模块。

# DESCRIPTION

**ocamlc** 是 OCaml 的字节码编译器。它将 OCaml 源文件编译为可在 OCaml 虚拟机上运行的字节码。

若需性能更好的原生代码编译，请改用 ocamlopt。

# FILE EXTENSIONS

```
.ml   - Implementation
.mli  - Interface
.cmo  - Bytecode object
.cma  - Bytecode library
.cmi  - Compiled interface
```

# EXAMPLE

```bash
# Compile simple program
ocamlc -o hello hello.ml

# With standard library
ocamlc -I +str str.cma program.ml -o program
```

# CAVEATS

字节码比原生代码慢。链接顺序很重要。生产环境请使用 ocamlopt。

# HISTORY

OCaml 由 **INRIA**（法国计算研究机构）开发，由 Caml Light 演化而来。字节码编译器自 OCaml 诞生起就是其组成部分。

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

[ocamlopt](/man/ocamlopt)(1), [dune](/man/dune)(1), [opam](/man/opam)(1)
