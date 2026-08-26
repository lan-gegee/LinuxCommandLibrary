# TAGLINE

设备树编译器

# TLDR

**将 DTS 编译为 DTB**

```dtc -I dts -O dtb -o [output.dtb] [input.dts]```

**将 DTB 反编译为 DTS**

```dtc -I dtb -O dts -o [output.dts] [input.dtb]```

**检查 DTS 语法**

```dtc -I dts -O dts [input.dts]```

**指定包含文件搜索路径**

```dtc -I dts -O dtb -i [include_path] -o [output.dtb] [input.dts]```

**生成汇编输出**

```dtc -I dts -O asm -o [output.S] [input.dts]```

# SYNOPSIS

**dtc** [_options_] _input_file_

# PARAMETERS

**-I** _format_
> 输入格式（dts、dtb、fs）。

**-O** _format_
> 输出格式（dts、dtb、asm）。

**-o** _file_
> 输出文件。

**-i** _path_
> 包含文件搜索路径。

**-W** _warning_
> 启用警告。

**-E** _error_
> 启用错误。

**-@**
> 为 overlay 生成符号。

# DESCRIPTION

**dtc**（设备树编译器）将设备树源码（DTS）文件编译为设备树二进制（DTB）格式，也可以执行相反的操作，把 DTB 反编译回 DTS。设备树是一种描述硬件组件及其相互关系的数据结构，让 Linux 内核无需硬编码板级专用代码即可支持各种硬件平台。

该编译器是嵌入式 Linux 开发的重要工具，尤其适用于 ARM、RISC-V 和 PowerPC 平台。DTS 文件以人类可读的方式描述硬件（CPU、内存、外设、中断、总线），而 DTB 是由引导加载程序加载并在运行时传递给内核的二进制格式。

dtc 支持设备树 overlay，允许在运行时修改基础设备树。这对于树莓派 HAT 或 BeagleBone 扩展板等附加硬件特别有用——overlay 可以在不修改基础系统设备树的情况下描述额外的硬件。

该工具内置验证和警告系统，可以捕获设备树语法和结构中的常见错误。它还能生成汇编输出，用于集成到固件构建中。

# INSTALL

```apt: sudo apt install device-tree-compiler```

```dnf: sudo dnf install dtc```

```pacman: sudo pacman -S dtc```

```apk: sudo apk add dtc```

```zypper: sudo zypper install dtc```

```brew: brew install dtc```

```nix: nix profile install nixpkgs#dtc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

