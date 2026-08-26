# TAGLINE

将 Lua 提前编译为原生可执行文件

# TLDR

将 Lua 脚本**编译**为原生可执行文件

```clx [file.lua]```

以**自定义输出**名称编译

```clx [file.lua] --output [name]```

针对**速度**或**体积**优化

```clx [file.lua] --fast
clx [file.lua] --size```

仅生成 **C++ 源码**（不编译）

```clx --cpp [file.lua]```

生成**目标文件**或**静态模块**

```clx --object [file.lua]
clx --static [file.lua]```

**最小化**运行时（仅包含 base 和 package 模块）

```clx [file.lua] --minimal```

# SYNOPSIS

**clx** [_options_] _file.lua_

# DESCRIPTION

**clx** 是一个跨平台的提前编译（AOT）Lua 编译器与运行时，通过现代 C++ 工具链（Clang、GCC 或 MSVC）生成独立的原生可执行文件。它以 Lua 5.5 兼容为目标，追求快速启动、易于部署的二进制文件以及无需字节码解释器的可预测性能。

未知的标志会被转发给后端 C++ 编译器（例如 **-O2**）。面向体积的构建可以生成紧凑的可执行文件；**--minimal** 仅链接 base 和 package 模块。

# PARAMETERS

**--output** _name_
> 输出可执行文件的名称

**--object** / **--static** / **--cpp**
> 生成目标文件、静态库或 C++ 源码，而非完整可执行文件

**--fast** / **--size** / **--debug**
> 分别针对速度、体积（默认取向）或调试进行优化

**--minimal**
> 仅链接 base 和 package 模块

**--version** / **--help**
> 版本或用法

# CAVEATS

在纯 AOT 模型中，动态加载（**load**、**dofile**、**loadfile**、**string.dump**）和完整的 **debug** 支持均受限。不支持传统的 Lua C API；原生模块使用 clx 的 C++ API。构建 clx 所用的编译器在构建时即已固定，以保证与生成代码的 ABI 兼容性。

# SEE ALSO

[lua](/man/lua)(1), [luajit](/man/luajit)(1)

# RESOURCES

```[Source code](https://github.com/samyeyo/clx)```

```[Homepage](https://samyeyo.github.io/clx)```

```[Documentation](https://github.com/samyeyo/clx/blob/main/doc/index.md)```

<!-- verified: 2026-07-14 -->
