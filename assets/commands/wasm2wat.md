# TAGLINE

将 WebAssembly 二进制反汇编为文本

# TLDR

**转换为 WAT**

```wasm2wat [input.wasm]```

**输出到文件**

```wasm2wat [input.wasm] -o [output.wat]```

**折叠表达式**

```wasm2wat --fold-exprs [input.wasm]```

**生成名称**

```wasm2wat --generate-names [input.wasm]```

# SYNOPSIS

**wasm2wat** [_-o output_] [_--fold-exprs_] [_options_] _input_

# PARAMETERS

**-o** _FILE_
> 输出文件。

**--fold-exprs**
> 折叠表达式。

**--generate-names**
> 生成名称。

**--inline-exports**
> 内联导出。

**--help**
> 显示帮助。

# DESCRIPTION

**wasm2wat** 是 WABT（WebAssembly Binary Toolkit）中的一款反汇编器，可将 WebAssembly 二进制（.wasm）文件转换为人类可读的 WebAssembly 文本格式（WAT）。WAT 输出采用 S 表达式语法，以可读的形式表示模块结构、函数、类型、导入和导出。

该工具对调试和检查编译后的 WebAssembly 模块至关重要，让开发者能够查看编译器实际生成的指令。--fold-exprs 等选项通过嵌套表达式产生更紧凑的输出，--generate-names 则为未命名的函数和变量分配可读的名称。

输出可以写入文件或打印到 stdout 以便管道传给其他工具。反向操作（文本转二进制）由配套工具 wat2wasm 完成。

# CAVEATS

大多是单向转换。属于 WABT 的一部分。大模块会产生大量输出。

# HISTORY

**wasm2wat** 是 **WABT**（WebAssembly Binary Toolkit）的一部分，用于将二进制 WASM 转换为可读的 WAT 文本格式。

# INSTALL

```apt: sudo apt install wabt```

```dnf: sudo dnf install wabt```

```pacman: sudo pacman -S wabt```

```brew: brew install wabt```

```nix: nix profile install nixpkgs#wabt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wat2wasm](/man/wat2wasm)(1), [wasm2c](/man/wasm2c)(1), [wasm-objdump](/man/wasm-objdump)(1)
