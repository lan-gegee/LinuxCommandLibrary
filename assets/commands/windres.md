# TAGLINE

GNU Windows 资源编译器

# TLDR

**将资源脚本编译**为 COFF 目标文件

```windres [input.rc] -o [output.o]```

**编译为二进制资源格式**

```windres -O res [input.rc] -o [output.res]```

**将 res 文件转换**为 COFF 目标文件

```windres -i [input.res] -o [output.o]```

显式**指定输入格式**

```windres -I rc -i [input.rc] -O coff -o [output.o]```

头文件的**包含目录**

```windres --include-dir=[path/to/includes] [input.rc] -o [output.o]```

**定义预处理器符号**

```windres -D [SYMBOL=value] [input.rc] -o [output.o]```

为 64 位 Windows **交叉编译**

```x86_64-w64-mingw32-windres [input.rc] -o [output.o]```

# SYNOPSIS

**windres** [**-i** _infile_] [**-o** _outfile_] [**-I** _format_] [**-O** _format_] [**-F** _target_] [**--include-dir** _dir_] [**-D** _sym_] [_options_]

# PARAMETERS

**-i** _file_, **--input** _file_
> 输入文件名。若未指定，则使用第一个非选项参数。

**-o** _file_, **--output** _file_
> 输出文件名。

**-I** _format_, **--input-format** _format_
> 输入格式：rc（资源脚本）、res（二进制）、coff（目标文件）。

**-O** _format_, **--output-format** _format_
> 输出格式：rc、res 或 coff。

**-F** _target_, **--target** _target_
> 为 COFF 输出指定 BFD 目标格式。

**--include-dir** _dir_
> 将目录添加到被包含文件的搜索路径。

**-D** _sym_[=_val_], **--define** _sym_[=_val_]
> 定义预处理器符号。

**-U** _sym_, **--undefine** _sym_
> 取消预处理器符号的定义。

**--preprocessor** _prog_
> 要使用的预处理器程序。默认为 `gcc -E -xc-header -DRC_INVOKED`。

**--preprocessor-arg** _arg_
> 传给预处理器的额外参数。

**--no-use-temp-file**
> 使用管道与预处理器通信（默认）。

**--use-temp-file**
> 使用临时文件而非管道与预处理器通信。

**@** _file_
> 从文件读取命令行选项。

**-v**, **--verbose**
> 启用详细输出模式。

**--help**
> 显示帮助消息。

**--version**
> 显示版本信息。

# DESCRIPTION

**windres** 是面向 Windows 应用程序的 GNU 资源编译器，属于 GNU Binutils。它将包含图标、光标、菜单、对话框和版本信息等 UI 元素的资源脚本（.rc）文件编译成 Windows 可执行文件可用的二进制格式。

该工具支持三种格式："rc"（文本资源脚本）、"res"（二进制资源文件）和 "coff"（用于链接的目标文件）。典型工作流程是将 .rc 文件编译为 COFF 目标文件，然后与应用程序链接。

对于从 Linux 到 Windows 的交叉编译，windres 通常作为 MinGW-w64 工具链的一部分使用，并带有特定于架构的前缀（例如针对 64 位 Windows 目标的 x86_64-w64-mingw32-windres）。

资源脚本在编译前会先经过 gcc 预处理，因此可以使用 #include 和 #define 指令。

# CAVEATS

资源脚本语法遵循 Microsoft 约定，但可能存在细微的兼容性差异。从 Microsoft 的 rc.exe 迁移时，某些复杂资源可能需要调整。该工具主要用于 Windows 交叉编译；Windows 原生开发通常使用 Microsoft 工具。

# HISTORY

**windres** 作为 **GNU Binutils** 的一部分开发，旨在提供 Microsoft 资源编译器（rc.exe）的自由替代品。自 **20 世纪 90 年代末**起，它就是 MinGW 和 MinGW-w64 工具链的组成部分，让类 Unix 系统上的 Windows 应用程序开发成为可能。该工具作为 Binutils 项目的一部分持续维护。

# SEE ALSO

[gcc](/man/gcc)(1), [ld](/man/ld)(1), [objcopy](/man/objcopy)(1), [objdump](/man/objdump)(1)
