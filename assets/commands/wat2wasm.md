# TAGLINE

将 WebAssembly 文本汇编为二进制

# TLDR

**将 WAT 编译为 WASM**

```wat2wasm [input.wat]```

**输出到文件**

```wat2wasm [input.wat] -o [output.wasm]```

**仅校验**

```wat2wasm --validate [input.wat]```

输出详细信息

```wat2wasm -v [input.wat]```

**调试名称**

```wat2wasm --debug-names [input.wat]```

# SYNOPSIS

**wat2wasm** [_-o output_] [_-v_] [_options_] _input_

# PARAMETERS

**-o** _FILE_
> 输出文件。

**-v**
> 详细模式。

**--validate**
> 仅校验。

**--debug-names**
> 包含调试名称。

**--help**
> 显示帮助。

# DESCRIPTION

**wat2wasm** 是 WABT（WebAssembly Binary Toolkit）中的一款汇编器，可将 WebAssembly 文本格式（WAT）文件编译为二进制 WebAssembly（.wasm）模块。它是 wasm2wat 的对应工具，后者执行反向转换。

该工具在编译期间会按照 WebAssembly 规范校验输入的 WAT 源码，在生成输出之前报告语法和类型错误。仅校验模式可以在不生成二进制输出的情况下检查文件，这在构建流水线中很有用。

--debug-names 选项将 WAT 源码中的函数和变量名作为自定义节区嵌入二进制文件，使输出在浏览器和其他显示命名符号的工具中更易于调试。

# CAVEATS

必须使用 WAT 语法。属于 WABT 的一部分。校验严格。

# HISTORY

**wat2wasm** 是 **WABT**（WebAssembly Binary Toolkit）的一部分，用于将 WAT 文本格式编译为二进制 WASM。

# INSTALL

```apt: sudo apt install wabt```

```dnf: sudo dnf install wabt```

```pacman: sudo pacman -S wabt```

```brew: brew install wabt```

```nix: nix profile install nixpkgs#wabt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasm2wat](/man/wasm2wat)(1), [wasm-opt](/man/wasm-opt)(1), [wasm-validate](/man/wasm-validate)(1)
