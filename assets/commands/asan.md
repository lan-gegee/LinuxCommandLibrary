# TAGLINE

通过编译器插桩在运行时检测内存错误。

# TLDR

**用 AddressSanitizer 编译 C 程序**

```gcc -fsanitize=address -g [program.c] -o [program]```

**用 ASan 编译 C++ 程序**

```g++ -fsanitize=address -g [program.cpp] -o [program]```

**使用 Clang 配合 ASan 编译**

```clang -fsanitize=address -g [program.c] -o [program]```

**以自定义 ASan 选项运行**

```ASAN_OPTIONS=detect_leaks=1:verbosity=1 ./[program]```

**同时启用 ASan 与 UBSan 编译**

```gcc -fsanitize=address,undefined -g [program.c] -o [program]```

**保留帧指针以便调试编译**

```gcc -fsanitize=address -g -fno-omit-frame-pointer [program.c] -o [program]```

# SYNOPSIS

**gcc** **-fsanitize=address** [_options_] _source_files_

# PARAMETERS

**-fsanitize=address**
> 启用 AddressSanitizer 插桩。

**-g**
> 包含调试信息，以获得有意义的堆栈跟踪。

**-fno-omit-frame-pointer**
> 保留帧指针，获得更好的堆栈跟踪。

**-O1**
> 至少以 -O1 编译，兼顾合理的性能和可读的堆栈跟踪。

**-fno-optimize-sibling-calls**
> 禁用尾调用消除，获得完整、准确的堆栈跟踪。

**-fsanitize-recover=address**
> 检测到错误后继续执行（ASAN_OPTIONS=halt_on_error=0 所必需）。

**-static-libasan**
> 静态链接 ASan 运行时（GCC；Clang 使用 **-static-libsan**）。GCC 默认使用共享运行时，Clang 默认静态。

# ENVIRONMENT VARIABLES

**ASAN_OPTIONS**
> AddressSanitizer 的运行时选项（冒号分隔的 key=value 键值对）。

**detect_leaks=1**
> 启用内存泄漏检测（x86_64 Linux 上默认开启）。

**detect_stack_use_after_return=1**
> 检测函数返回后对栈内存的使用（Linux 上默认开启）。

**halt_on_error=0**
> 发生可恢复错误后继续运行（仅在以 -fsanitize-recover=address 编译时有效；默认行为是中止）。

**abort_on_error=1**
> 出错时调用 abort() 而非 _exit()，从而生成核心转储。

**log_path=**_path_
> 将报告写入 _path_.pid 而不是 stderr。

**verbosity=1**
> 提高输出的详细程度。

**symbolize=1**
> 启用堆栈跟踪的符号化。

**print_stats=1**
> 在退出时打印内存使用统计。

**ASAN_SYMBOLIZER_PATH**
> 用于将地址解析为源码位置的 llvm-symbolizer 路径。

# DESCRIPTION

**AddressSanitizer（ASan）** 是内置于 GCC 和 Clang 的快速内存错误检测器。它能以相对较低的开销在运行时检测缓冲区溢出、释放后使用、返回后使用、内存泄漏以及其他内存破坏类缺陷。

通过 **-fsanitize=address** 启用后，编译器会对内存访问和分配进行插桩。插桩后的程序维护一块影子内存来追踪每个字节的状态。内存错误一发生就会被立即检测出来，并生成详细报告，包括错误位置以及分配/释放点的堆栈跟踪。

ASan 通常带来约 2 倍的性能下降和 3 倍的内存开销，因此适合测试和开发环境，不适合生产环境。配合 **-g** 编译可在报告中显示源码位置。

# CAVEATS

ASan 除 UBSan 外不能与其他 sanitizer 组合使用。程序必须重新编译；ASan 无法分析现有的二进制文件。误报罕见但在自定义分配器场景下可能出现。内存开销可能在内存受限的系统上引发内存耗尽。并非所有平台都支持全部 ASan 特性。

# HISTORY

AddressSanitizer 由 **Google** 开发，于 **2012** 年随 **LLVM 3.1** 首次发布，**2013** 年被加入 GCC 4.8。它由 Konstantin Serebryany 等人设计，旨在成为比 Valgrind 更快的内存错误检测方案。此后 ASan 已在 Chrome、Firefox 和 Linux 内核等大型软件项目中发现了数千个缺陷。

# SEE ALSO

[valgrind](/man/valgrind)(1), [gcc](/man/gcc)(1), [clang](/man/clang)(1)

# RESOURCES

```[Source code](https://github.com/google/sanitizers)```

```[Documentation](https://clang.llvm.org/docs/AddressSanitizer.html)```

<!-- verified: 2026-06-16 -->
