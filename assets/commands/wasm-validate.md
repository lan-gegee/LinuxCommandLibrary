# TAGLINE

校验 WebAssembly 二进制文件

# TLDR

**校验** WebAssembly 二进制文件

```wasm-validate [file.wasm]```

以**详细输出**进行**校验**

```wasm-validate -v [file.wasm]```

启用**全部特性**进行**校验**

```wasm-validate --enable-all [file.wasm]```

启用**线程**支持进行**校验**

```wasm-validate --enable-threads [file.wasm]```

启用**垃圾回收**支持进行**校验**

```wasm-validate --enable-gc [file.wasm]```

**校验**时忽略**自定义节区**中的错误

```wasm-validate --ignore-custom-section-errors [file.wasm]```

# SYNOPSIS

**wasm-validate** [_options_] _file_

# PARAMETERS

**-v**, **--verbose**
> 使用详细输出。可多次使用以获得更多细节。

**--enable-exceptions**
> 启用实验性的异常处理。

**--enable-threads**
> 启用线程支持。

**--enable-function-references**
> 启用带类型的函数引用。

**--enable-tail-call**
> 启用尾调用支持。

**--enable-annotations**
> 启用自定义注解语法。

**--enable-code-metadata**
> 启用代码元数据。

**--enable-gc**
> 启用垃圾回收。

**--enable-memory64**
> 启用 64 位内存支持。

**--enable-multi-memory**
> 启用多内存支持。

**--enable-extended-const**
> 启用扩展常量表达式。

**--enable-all**
> 启用所有特性。

**--disable-mutable-globals**
> 禁用可变全局变量的导入/导出。

**--disable-saturating-float-to-int**
> 禁用饱和浮点转整数运算符。

**--disable-sign-extension**
> 禁用符号扩展运算符。

**--disable-simd**
> 禁用 SIMD 支持。

**--disable-multi-value**
> 禁用多返回值支持。

**--disable-bulk-memory**
> 禁用批量内存操作。

**--disable-reference-types**
> 禁用引用类型（externref）。

**--no-debug-names**
> 忽略二进制文件中的调试名称。

**--ignore-custom-section-errors**
> 忽略自定义节区中的错误。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**wasm-validate** 读取 WebAssembly 二进制格式的文件，并按照 WebAssembly 规范对其进行校验。它是 WABT（WebAssembly Binary Toolkit）的一部分。

校验器检查模块结构、类型正确性、指令有效性以及其他规范要求。对于格式错误或无效、会在运行时加载失败的模块，它会报告相应错误。

特性标志用于启用或禁用各 WebAssembly 提案的校验。某些特性（如可变全局变量和批量内存）默认启用，而 threads、GC 和 exceptions 等提案必须显式启用。

# EXIT STATUS

模块有效则返回 0，否则返回非零值。

# CAVEATS

有效的模块仍可能出现运行时错误。特性标志必须与目标运行时的能力相匹配。属于 WABT 软件包的一部分。

# HISTORY

**wasm-validate** 是 WABT（WebAssembly Binary Toolkit）的一部分，由 WebAssembly 社区组开发。它可以在尝试运行之前及早发现无效模块，在构建流水线和调试中很有用。

# INSTALL

```apt: sudo apt install wabt```

```dnf: sudo dnf install wabt```

```pacman: sudo pacman -S wabt```

```brew: brew install wabt```

```nix: nix profile install nixpkgs#wabt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasm-objdump](/man/wasm-objdump)(1), [wasm-strip](/man/wasm-strip)(1), [wasm2wat](/man/wasm2wat)(1), [wat2wasm](/man/wat2wasm)(1), [wasm2c](/man/wasm2c)(1)
