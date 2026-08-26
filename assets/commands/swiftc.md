# TAGLINE

将 Swift 源代码编译为可执行文件

# TLDR

**编译 Swift 源文件**

```swiftc [file.swift]```

**以自定义输出名编译**

```swiftc -o [program] [file.swift]```

**编译多个源文件**

```swiftc [main.swift] [utils.swift] -o [program]```

**带调试符号编译**

```swiftc -g [file.swift] -o [program]```

**带优化编译**

```swiftc -O [file.swift] -o [program]```

**显示详细的编译输出**

```swiftc -v [file.swift]```

**以体积优化编译**

```swiftc -Osize [file.swift] -o [program]```

**仅生成目标文件**

```swiftc -c [file.swift] -o [file.o]```

# SYNOPSIS

**swiftc** [_options_] [_files_]

# PARAMETERS

**-o** _file_
> 指定输出文件名

**-c**
> 只编译不链接（生成目标文件）

**-g**
> 生成调试符号

**-O**
> 带优化编译

**-Osize**
> 带优化编译，优先考虑更小的二进制体积

**-Ounchecked**
> 带优化编译，移除运行时安全检查

**-Onone**
> 不带优化编译（debug 的默认值）

**-whole-module-optimization**
> 一次对整个模块进行优化

**-target** _triple_
> 为给定的目标三元组生成代码（例如 x86_64-apple-macosx10.15）

**-v**, **--verbose**
> 显示详细输出，包括执行的命令

**-emit-executable**
> 生成可执行文件（链接时的默认行为）

**-emit-library**
> 生成动态库

**-emit-module**
> 生成 Swift 模块

**-D** _flag_
> 定义条件编译标志

**-I** _path_
> 添加导入搜索路径

**-L** _path_
> 添加库搜索路径

**-l** _library_
> 链接指定的库

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**swiftc** 是 Swift 编译器，负责将 Swift 源代码翻译为可执行二进制、库、目标文件和模块。它是在 Xcode 之外构建 Swift 程序的命令行界面。

该编译器驱动器协调多个编译阶段：解析、类型检查、优化和代码生成。对于单文件程序，swiftc 直接生成可执行文件。多个源文件会被一起编译并链接。

swiftc 是指向 swift 可执行文件的符号链接，后者根据被调用的方式决定自身行为。复杂项目通常由 Swift Package Manager 负责编译。

# CAVEATS

swiftc 要求安装 Swift 工具链。macOS 上随 Xcode 附带；Linux 上需单独安装。模块兼容性依赖 Swift 版本，混用版本可能出问题。

# HISTORY

Swift 由 **Apple** 在 **2014 年** WWDC 上发布，并于 **2015 年 12 月**开源。该编译器最初用 C++ 编写，目前仍在持续努力用 Swift 本身重写各组件。Swift 6 带来了重大的并发与安全性改进。

# INSTALL

```apt: sudo apt install swiftlang```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swift](/man/swift)(1), [clang](/man/clang)(1), [xcodebuild](/man/xcodebuild)(1), [lldb](/man/lldb)(1)
