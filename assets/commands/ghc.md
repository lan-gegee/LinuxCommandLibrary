# TAGLINE

Haskell 函数式编程语言的编译器

# TLDR

**编译 Haskell 文件**

```ghc [file.hs]```

**开启优化编译**

```ghc -O2 [file.hs]```

**只编译为目标文件**

```ghc -c [file.hs]```

**指定输出名称**

```ghc -o [program] [file.hs]```

**启用所有警告**

```ghc -Wall [file.hs]```

**并行编译模块**

```ghc -j [file.hs]```

**启用语言扩展**

```ghc -XOverloadedStrings [file.hs]```

# SYNOPSIS

**ghc** [_options_] _files_

# PARAMETERS

_FILES_
> Haskell 源文件（.hs、.lhs）。

**-o** _FILE_
> 输出文件名。

**-c**
> 只编译为目标文件。

**-O**, **-O1**
> 启用标准优化。

**-O2**
> 启用激进优化，包含额外的优化 pass。

**-O0**
> 关闭优化（默认）。

**-Wall**
> 启用大多数警告。

**-w**
> 抑制所有警告。

**-Werror**
> 将警告视为错误。

**-i**_DIR_
> 将目录加入导入搜索路径。

**-package** _PKG_
> 公开指定的软件包。

**--make**
> 构建程序并自动解析模块依赖。

**-e** _EXPR_
> 求值单个表达式后退出。

**-j**[_N_]
> 并行编译 N 个模块。

**-threaded**
> 使用多线程运行时系统。

**-prof**
> 启用性能分析（profiling）。

**-fllvm**
> 通过 LLVM 后端编译。

**-X**_EXTENSION_
> 启用某个语言扩展（例如 -XOverloadedStrings）。

**-cpp**
> 对源文件运行 C 预处理器。

**-v**[_N_]
> 设置输出详细程度（0-3）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ghc**（Glasgow Haskell Compiler）是 Haskell 编程语言的主流编译器。它将 Haskell 源代码编译为原生机器码，生成高效的的可执行文件。

GHC 支持完整的 Haskell 语言标准，还提供大量扩展，覆盖高级类型系统特性、并行性和性能等方面。--make 模式（默认）会自动处理模块依赖。GHC 还提供原生代码生成以及可选的 LLVM 后端。

# CAVEATS

编译可能占用大量内存。大型项目宜采用增量构建。扩展标志随 GHC 版本不同而变化。相比 **-O**，**-O2** 级别会显著增加编译时间。

# HISTORY

GHC 于 **1989 年**在**格拉斯哥大学**启动开发。它已成为事实上的标准 Haskell 编译器，由 Haskell 社区和工业界用户持续活跃开发。

# INSTALL

```apt: sudo apt install ghc```

```dnf: sudo dnf install ghc```

```pacman: sudo pacman -S ghc```

```apk: sudo apk add ghc```

```zypper: sudo zypper install ghc```

```brew: brew install ghc```

```nix: nix profile install nixpkgs#ghc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghci](/man/ghci)(1), [runghc](/man/runghc)(1), [cabal](/man/cabal)(1), [stack](/man/stack)(1)
