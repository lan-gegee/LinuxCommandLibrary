# TAGLINE

从 C 头文件生成 Haskell FFI 绑定

# TLDR

**从 C 头文件生成** Haskell 绑定

```c2hs [header.h] [bindings.chs]```

**指定包含路径**

```c2hs -C -I[/path/to/includes] [bindings.chs]```

**传递预处理器宏定义**

```c2hs -C -D[MACRO=value] [bindings.chs]```

**指定输出目录**

```c2hs -o [output_dir] [bindings.chs]```

**显示帮助**

```c2hs --help```

# SYNOPSIS

**c2hs** [_options_] _header.h_ _binding.chs_

# DESCRIPTION

**c2hs** 是一个 C 到 Haskell 的接口生成器，可简化为 C 库创建 FFI 绑定的过程。它从 C 头文件中提取接口信息，并生成包含外部导入（foreign import）和正确类型编组的 Haskell 代码。

该工具处理 .chs 文件，这类文件包含带有内嵌钩子（hook）的 Haskell 代码，用于引用 C 结构和函数。

# PARAMETERS

**-C** _options_
> 向 C 预处理器传递选项（-I、-D 等）

**-o** _directory_
> 生成文件的输出目录

**-c** _compiler_
> 使用指定的 C 编译器

**--cppopts**=_options_
> C 预处理器选项

**-d** _type_
> 转储内部信息（trace、genbind、ctrav、chs）

**-k**
> 保留中间文件

**--help**
> 显示帮助

**--version**
> 显示版本

# WORKFLOW

1. 编写包含 Haskell 代码和 C 钩子的 .chs 文件
2. 运行 c2hs 生成 .hs 文件
3. 编译生成的 Haskell 模块

# CABAL INTEGRATION

Cabal 会自动处理 .chs 文件，并以适当的标志运行 c2hs。

# CAVEATS

生成的代码采用 BSD 许可证。需要能够访问 C 头文件。复杂的 C 构造可能需要手动编写绑定。

# INSTALL

```apt: sudo apt install c2hs```

```dnf: sudo dnf install c2hs```

```pacman: sudo pacman -S c2hs```

```zypper: sudo zypper install c2hs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghc](/man/ghc)(1), [cabal](/man/cabal)(1)
