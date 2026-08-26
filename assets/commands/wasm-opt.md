# TAGLINE

优化 WebAssembly 二进制模块

# TLDR

**优化 WASM**

```wasm-opt -O [input.wasm] -o [output.wasm]```

**最大程度优化**

```wasm-opt -O4 [input.wasm] -o [output.wasm]```

**体积优化**

```wasm-opt -Os [input.wasm] -o [output.wasm]```

**打印统计信息**

```wasm-opt --print [input.wasm]```

**仅校验**

```wasm-opt --validate [input.wasm]```

# SYNOPSIS

**wasm-opt** [_-O_] [_-Os_] [_-o output_] [_options_] _input_

# PARAMETERS

**-O**
> 执行默认的优化 pass。

**-O0**
> 不执行任何优化 pass。

**-O1**
> 快速而实用的优化，适合迭代构建。

**-O2**
> 启用大多数优化，通常能获得大部分性能收益。

**-O3**
> 更激进的优化，可能耗时较长。

**-O4**
> 还会扁平化 IR；可能消耗多得多的时间和内存。

**-Os**
> 针对代码体积进行优化。

**-Oz**
> 激进地针对代码体积进行优化。

**-o** _FILE_
> 输出文件。

**--print**
> 以文本格式打印模块。

**--validate**
> 只校验模块，不做优化。

**--converge**
> 反复迭代优化 pass，直到不再有改进为止。

**-g**, **--debuginfo**
> 在输出中保留调试信息。

**-ism** _FILE_
> 读取输入 source map。

**-osm** _FILE_
> 写出输出 source map。

# DESCRIPTION

**wasm-opt** 是 Binaryen 工具集中的 WebAssembly 优化器，通过应用各种优化 pass 来缩减模块体积并提升执行速度。它处理 .wasm 二进制文件，输出适合生产部署的优化版本。

优化级别从 -O0（无）到 -O4（最高），每个级别逐步启用更激进的变换。-O1 为迭代构建提供快速收益，-O2 覆盖大多数优化，-O3 更为激进，-O4 额外扁平化 IR。-Os 和 -Oz 标志针对代码体积优化，这对 Web 交付很重要。可用的 pass 包括死代码消除、内联、常量折叠以及许多 WebAssembly 特有的优化。

该工具还可以按规范校验模块，并以文本格式打印模块内容供检查。它通常作为从源语言编译之后的后处理步骤，用于 WebAssembly 构建流水线。

# CAVEATS

属于 Binaryen 的一部分。仅针对 WASM。极少数情况下可能改变语义。

# HISTORY

**wasm-opt** 是 **Binaryen** 的一部分，后者是面向 WebAssembly 的编译器基础设施库。

# INSTALL

```apt: sudo apt install binaryen```

```dnf: sudo dnf install binaryen```

```pacman: sudo pacman -S binaryen```

```apk: sudo apk add binaryen```

```zypper: sudo zypper install binaryen```

```brew: brew install binaryen```

```nix: nix profile install nixpkgs#binaryen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasm2wat](/man/wasm2wat)(1), [wat2wasm](/man/wat2wasm)(1), [wasm-strip](/man/wasm-strip)(1)
