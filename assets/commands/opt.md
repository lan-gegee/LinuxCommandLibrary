# TAGLINE

LLVM 优化器

# TLDR

**优化 LLVM 位码**

```opt [input.bc] -o [output.bc]```

**运行特定的 pass**

```opt -mem2reg [input.bc] -o [output.bc]```

**启用所有优化**

```opt -O3 [input.bc] -o [output.bc]```

**打印 pass 统计信息**

```opt -stats [input.bc] -o [output.bc]```

**列出可用的 pass**

```opt --print-passes```

# SYNOPSIS

**opt** [_options_] [_input_]

# PARAMETERS

_INPUT_
> LLVM 位码文件。

**-o** _OUTPUT_
> 输出文件。

**-O**_LEVEL_
> 优化级别（0-3）。

**--print-passes**
> 列出可用的 pass。

**-stats**
> 打印统计信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**opt** 是 LLVM 优化器，对位码运行各种优化 pass。

该工具用于变换 LLVM 中间表示。属于 LLVM 工具链。

# CAVEATS

属于 LLVM。仅支持位码。pass 名称因版本而异。

# HISTORY

opt 作为 **LLVM 编译器基础设施**项目的组成部分而开发。

# INSTALL

```apt: sudo apt install llvm```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llvm-as](/man/llvm-as)(1), [llc](/man/llc)(1), [clang](/man/clang)(1)
