# TAGLINE

内存调试与分析框架

# TLDR

**检查内存泄漏**

```valgrind --leak-check=full [./program]```

**运行并显示详细的泄漏信息**

```valgrind --leak-check=full --show-leak-kinds=all [./program]```

**跟踪内存来源**

```valgrind --track-origins=yes [./program]```

使用 **cachegrind** 进行缓存分析

```valgrind --tool=cachegrind [./program]```

使用 **callgrind** 进行调用分析

```valgrind --tool=callgrind [./program]```

使用 **helgrind** 检测线程错误

```valgrind --tool=helgrind [./program]```

为已知问题**生成屏蔽条目**

```valgrind --gen-suppressions=all [./program]```

# SYNOPSIS

**valgrind** [**--tool=**_toolname_] [_options_] _program_ [_args_]

# PARAMETERS

**--tool=**_name_
> 选择工具（memcheck、cachegrind、callgrind、helgrind、drd、massif）

**--leak-check=**_level_
> 检查内存泄漏（no、summary、full）

**--show-leak-kinds=**_kinds_
> 显示哪些类型的泄漏（definite、indirect、possible、reachable、all）

**--track-origins=**_yes|no_
> 跟踪未初始化值的来源

**--log-file=**_file_
> 将输出写入文件

**--xml=**_yes_
> 以 XML 格式输出

**--gen-suppressions=**_level_
> 生成屏蔽条目（no、yes、all）

**--suppressions=**_file_
> 使用来自文件的屏蔽规则

**-v**, **--verbose**
> 更详细的输出

**-q**, **--quiet**
> 更简洁的输出

**--num-callers=**_N_
> 错误报告的最大栈深度（默认：12）

**--vgdb=**_yes|no|full_
> 启用 gdb 服务器以便在 Valgrind 下调试

# TOOLS

**memcheck**：内存错误检测器（默认）
**cachegrind**：缓存和分支分析器
**callgrind**：调用图分析器
**helgrind**：线程错误检测器
**drd**：线程错误检测器（算法不同）
**massif**：堆分析器

# DESCRIPTION

**valgrind** 是一个面向动态分析工具的插桩框架。默认工具 memcheck 可检测内存管理问题：泄漏、使用未初始化内存、缓冲区溢出以及无效的释放。

在 Valgrind 下运行时程序会显著变慢（10-50 倍），因为每一次内存访问都会被插桩。这是正常且预期的现象。

输出会指出错误类型、位置（若以 **-g** 编译则包含行号）以及调用栈。"Definitely lost" 内存是真正的泄漏；"still reachable" 可能是延迟到退出时才清理的可接受情况。

其他工具用于分析性能（cachegrind、callgrind）、检测线程问题（helgrind、drd）或分析堆使用情况（massif）。

# CAVEATS

编译程序时请加 **-g** 以获得行号，并使用 **-O0** 或 **-O1** 以保证调试准确（高优化级别会干扰源码映射）。

会出现误报，尤其是在系统库上。可使用屏蔽文件忽略已知问题。

未经额外配置，Valgrind 与 JIT 编译器或自定义内存分配器的配合不佳。

# HISTORY

**Valgrind** 由 **Julian Seward** 创建，于 **2002 年**首次发布。名称源自北欧神话中瓦尔哈拉的入口。它已成为 Linux 上 C/C++ 的标准内存调试工具。

# INSTALL

```apt: sudo apt install valgrind```

```dnf: sudo dnf install valgrind```

```pacman: sudo pacman -S valgrind```

```apk: sudo apk add valgrind```

```zypper: sudo zypper install valgrind```

```brew: brew install valgrind```

```nix: nix profile install nixpkgs#valgrind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [strace](/man/strace)(1), [ltrace](/man/ltrace)(1), [asan](/man/asan)(7)
