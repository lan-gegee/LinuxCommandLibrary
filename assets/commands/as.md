# TAGLINE

将汇编语言源代码翻译成目标文件。

# TLDR

**汇编**一个文件，输出写入 a.out

```as [path/to/file.s]```

汇编到**指定的输出文件**

```as [path/to/file.s] -o [path/to/output.o]```

跳过空白预处理，**更快**地生成输出

```as -f [path/to/file.s]```

将目录添加到 **include 搜索路径**

```as -I [path/to/directory] [path/to/file.s]```

# SYNOPSIS

**as** [_options_] _file_...

# DESCRIPTION

**as** 是 GNU 汇编器，属于 GNU Binutils 工具集。它将汇编语言源文件翻译成目标文件，这些文件可再用 **ld** 链接生成可执行文件。

它主要用于汇编 **gcc** 等编译器的输出，但也可以直接用于底层编程。该汇编器支持多种目标架构和输出格式。

# PARAMETERS

**-o** _file_
> 将输出的目标文件写入 _file_，而非 a.out

**-f**
> 快速模式：跳过空白和注释预处理（只应用于可信的编译器输出）

**-I** _directory_
> 将 _directory_ 添加到 **.include** 指令的搜索路径

**-g**
> 生成调试信息

**--32** / **--64**
> 生成 32 位或 64 位代码（x86）

**-W**, **--no-warn**
> 不显示警告消息。

**--warn**
> 不抑制警告（默认）。

**--fatal-warnings**
> 将警告视为错误。

**-a**[_letters_]
> 开启清单输出；子选项包括 _h_（高级语言）、_l_（汇编）、_s_（符号）、_n_（省略 forms 处理）。

**--statistics**
> 打印处理统计信息（最大空间、总耗时）。

**-march=**_CPU_
> 为特定 CPU 架构进行汇编。

# CAVEATS

不同架构的汇编语法各不相同。GNU as 在 x86 上默认使用 AT&T 语法，与 Intel 语法不同。要使用 Intel 语法，请使用 **.intel_syntax noprefix** 指令。**-f** 选项只应配合编译器生成的输出使用，因为它会跳过手写源码可能依赖的空白和注释预处理。

# HISTORY

GNU 汇编器作为 GNU 计划的一部分始于 1980 年代。后来它成为 GNU Binutils 的一部分，支持几乎所有 GCC 面向的架构。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[gcc](/man/gcc)(1), [ld](/man/ld)(1), [objdump](/man/objdump)(1), [readelf](/man/readelf)(1)
