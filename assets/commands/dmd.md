# TAGLINE

D 编程语言参考编译器

# TLDR

**编译 D 源文件**

```dmd [file.d]```

**指定输出名称**编译

```dmd -of=[output] [file.d]```

**启用优化**编译

```dmd -O [file.d]```

**只编译为目标**文件

```dmd -c [file.d]```

**添加导入路径**

```dmd -I[/path/to/imports] [file.d]```

**启用所有警告**

```dmd -w [file.d]```

**生成调试信息**

```dmd -g [file.d]```

# SYNOPSIS

**dmd** [_options_] _file_...

# PARAMETERS

_FILE_
> 要编译的 D 源文件。

**-of**=_FILE_
> 输出文件名。

**-O**
> 启用优化。

**-c**
> 仅编译（不链接）。

**-I**_PATH_
> 添加导入路径。

**-w**
> 启用所有警告。

**-g**
> 生成调试信息。

**-release**
> 以发布模式编译（禁用断言）。

**-unittest**
> 编译并运行单元测试。

**--help**
> 显示帮助信息。

# CONFIGURATION

**/etc/dmd.conf** 或 **~/.dmd/dmd.conf**
> 导入路径、库路径和默认编译器标志。

# DESCRIPTION

**dmd** 是 D 编程语言的参考编译器。它将 D 源代码编译为原生机器码，支持完整的 D 语言规范，包括模板、mixin 和编译期函数执行。

D 语言兼具底层编程的能力和垃圾回收、闭包、内置单元测试等现代语言特性。dmd 编译速度快，适合快速开发迭代。

该编译器附带标准库（Phobos），为常见编程任务提供丰富功能，并支持与 C 和 C++ 代码交互。

# CAVEATS

参考实现与其他编译器（LDC、GDC）可能存在性能差异。某些优化的激进程度不及基于 LLVM 的编译器。各平台支持情况不一。

# HISTORY

dmd 由 **Walter Bright** 创建。他于 **1999 年**开始开发 D 语言，作为 C 和 C++ 的后继者。首个公开版本于 **2001 年**发布。D 汲取了多年编译器开发经验，致力于解决 C++ 中被认为存在的问题。

# INSTALL

```pacman: sudo pacman -S dmd```

```apk: sudo apk add dmd```

```zypper: sudo zypper install dmd```

```brew: brew install dmd```

```nix: nix profile install nixpkgs#dmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldc](/man/ldc)(1), [gdc](/man/gdc)(1)
