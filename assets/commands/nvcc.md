# TAGLINE

NVIDIA 的 CUDA 编译器驱动

# TLDR

**编译 CUDA 程序**

```nvcc [program.cu] -o [program]```

**编译为目标文件**

```nvcc -c [kernel.cu] -o [kernel.o]```

**针对特定 GPU 架构编译**

```nvcc -arch=sm_[75] [program.cu] -o [program]```

**生成 PTX 代码**

```nvcc -ptx [kernel.cu]```

**带优化编译**

```nvcc -O3 [program.cu] -o [program]```

**带调试符号编译**

```nvcc -g -G [program.cu] -o [program]```

**与外部库链接**

```nvcc [program.cu] -o [program] -l[cublas]```

**显示编译阶段**

```nvcc --dryrun [program.cu]```

# SYNOPSIS

**nvcc** [_-arch=arch_] [_-o output_] [_-c_] [_-g_] [_options_] _files_

# PARAMETERS

**-o** _FILE_
> 输出文件。

**-c**
> 仅编译，不链接。

**-arch** _ARCH_
> GPU 架构（sm_50、sm_75、sm_86 等）。

**-code** _CODE_
> GPU 代码生成。

**-gencode** _SPEC_
> 架构/代码对（例如 arch=compute_75,code=sm_75）。

**-ptx**
> 生成 PTX 汇编。

**-g**
> 主机端调试符号。

**-G**
> 设备端调试符号。

**-O** _LEVEL_
> 优化级别（0-3）。

**-I** _DIR_
> 头文件目录。

**-L** _DIR_
> 库目录。

**-l** _LIB_
> 链接库。

**--dryrun**
> 显示命令但不执行。

**-Xcompiler** _options_
> 将选项直接传递给主机编译器。

**-std** _standard_
> C++ 标准（例如 c++14、c++17、c++20）。也接受 `--std` 写法。

**-dc**
> 编译为可重定位设备代码（启用分离编译）。

**-rdc** _true|false_
> 启用或禁用可重定位设备代码。

**-dlink**
> 链接可重定位设备代码目标文件。

**-ccbin** _PATH_
> 指定主机编译器的二进制文件（例如 `/usr/bin/g++`）。

**-Xlinker** _options_
> 将选项直接传递给主机链接器。

**-lineinfo**
> 为设备代码生成行号信息（对分析器有用）。

**-use_fast_math**
> 启用快速数学优化（隐含 `-ftz=true -prec-div=false -prec-sqrt=false`）。

**-keep**
> 保留中间编译文件。

**-t** _N_
> 使用 N 个线程并行编译。

**-v**, **--verbose**
> 详细输出。

**--version**
> 显示版本。

# DESCRIPTION

**nvcc** 是 NVIDIA 的 CUDA 编译器驱动。它编译运行在 NVIDIA GPU 上的 CUDA C/C++ 代码，同时编译运行在 CPU 上的主机代码。

编译过程将设备代码（运行在 GPU 上的内核）与主机代码（CPU）分离。设备代码会编译为 PTX 中间表示，或直接编译为 SASS（GPU 机器码）。

架构选项（-arch）用于指定目标 GPU 代际。使用 `-arch=native` 可自动检测可见的 GPU，使用 `-arch=all` 可针对所有受支持的架构进行编译。前向兼容依赖 PTX 在运行时进行 JIT 编译。

该编译器与主机编译器（gcc、clang、MSVC）集成以处理 CPU 代码。分离编译允许在大型项目中将 CUDA 与常规 C++ 混合使用。

调试构建（-g -G）支持 cuda-gdb 调试。优化级别会影响主机和设备代码的性能。

CUDA 库（cuBLAS、cuDNN、cuFFT）像普通库一样链接。对于非标准安装位置，可能需要指定头文件路径和库路径。

# CAVEATS

需要 NVIDIA GPU 和驱动程序。架构不匹配会导致运行时错误。调试构建速度慢得多。寄存器占用过大会限制占用率。

# HISTORY

**nvcc** 随 **NVIDIA** 的 **CUDA** 于约 **2007 年**推出。它通过提供一种类 C 语言来编程 NVIDIA GPU，使 GPU 从仅用于图形转变为通用计算设备，开启了通用 GPU 计算的时代。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [cuda-gdb](/man/cuda-gdb)(1), [gcc](/man/gcc)(1), [clang](/man/clang)(1)
