# TAGLINE

将 WebAssembly 转换为可移植的 C 代码

# TLDR

**转换为 C**

```wasm2c [input.wasm] -o [output.c]```

**生成头文件**

```wasm2c [input.wasm] -o [output.c] --header=[output.h]```

**指定模块名**

```wasm2c [input.wasm] -o [output.c] --module-name=[mymod]```

# SYNOPSIS

**wasm2c** [_-o output_] [_--header file_] [_options_] _input_

# PARAMETERS

**-o** _FILE_
> 输出 C 文件。

**--header** _FILE_
> 生成头文件。

**--module-name** _NAME_
> C 模块名称。

**--help**
> 显示帮助。

# DESCRIPTION

**wasm2c** 是 WABT（WebAssembly Binary Toolkit）中的一款工具，可将 WebAssembly 二进制模块翻译为可移植的 C 源代码。生成的 C 代码可以用任何标准 C 编译器编译，使 WebAssembly 模块无需 WebAssembly 运行时即可原生运行。

该工具会生成包含翻译后模块逻辑的 C 源文件，以及一个可选的头文件（含函数声明和类型定义）。可以指定自定义模块名来控制生成符号的命名，这在将多个翻译后的模块链接在一起时很有用。

这种方式适用于在 C/C++ 项目中嵌入 WebAssembly 功能、在没有运行时的平台上运行 WebAssembly，或通过生成的源码分析模块行为。

# CAVEATS

生成的代码较大。编译较慢。属于 WABT 的一部分。

# HISTORY

**wasm2c** 是 **WABT**（WebAssembly Binary Toolkit）的一部分，用于将 WebAssembly 转换为可移植的 C 代码。

# INSTALL

```apt: sudo apt install wabt```

```dnf: sudo dnf install wabt```

```pacman: sudo pacman -S wabt```

```brew: brew install wabt```

```nix: nix profile install nixpkgs#wabt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasm2wat](/man/wasm2wat)(1), [wat2wasm](/man/wat2wasm)(1), [wasmtime](/man/wasmtime)(1)
