# TAGLINE

显示 WebAssembly 二进制文件信息

# TLDR

**显示所有信息**

```wasm-objdump [file.wasm]```

**只显示文件头**

```wasm-objdump -h [file.wasm]```

**反汇编函数体**

```wasm-objdump -d [file.wasm]```

**显示节区详情**

```wasm-objdump -x [file.wasm]```

**显示节区原始内容**

```wasm-objdump -s [file.wasm]```

**检查特定节区**

```wasm-objdump -j [Code] [file.wasm]```

**在反汇编中显示重定位信息**

```wasm-objdump -d -r [file.wasm]```

# SYNOPSIS

**wasm-objdump** [_options_] _file_

# PARAMETERS

**-h**, **--headers**
> 打印节区头。

**-d**, **--disassemble**
> 反汇编函数体。

**-x**, **--details**
> 显示节区详情。

**-s**, **--full-contents**
> 打印节区原始内容。

**-j**, **--section** _name_
> 选择特定节区。

**-r**, **--reloc**
> 在反汇编中显示重定位信息。

**--debug**
> 打印调试信息。

**--section-offsets**
> 在反汇编中显示节区偏移量。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**wasm-objdump** 显示 WebAssembly 二进制（.wasm）文件的相关信息。它是 WABT（WebAssembly Binary Toolkit）的一部分，作用类似于原生二进制领域的 objdump。

该工具检查模块结构，包括导入、导出、函数、全局变量、内存布局以及 WebAssembly 字节码指令。它对调试、逆向工程和理解编译后的 WebAssembly 输出至关重要。

用例包括性能分析、安全审计和验证编译器输出。反汇编模式会按函数边界展示 WebAssembly 指令。

# CAVEATS

只能处理 WebAssembly 二进制文件，不适用于原生可执行文件。大型模块可能产生冗长的输出。属于 WABT 软件包的一部分。

# HISTORY

**wasm-objdump** 是 WABT（WebAssembly Binary Toolkit）的一部分，由 WebAssembly 社区组开发。WABT 提供处理 WebAssembly 格式的基础工具，让开发者能够检查和操作 .wasm 文件。

# INSTALL

```apt: sudo apt install wabt```

```dnf: sudo dnf install wabt```

```pacman: sudo pacman -S wabt```

```brew: brew install wabt```

```nix: nix profile install nixpkgs#wabt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasm-validate](/man/wasm-validate)(1), [wasm-strip](/man/wasm-strip)(1), [wasm2wat](/man/wasm2wat)(1), [wat2wasm](/man/wat2wasm)(1)
