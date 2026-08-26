# TAGLINE

V 编程语言编译器

# TLDR

**编译文件**

```v [file.v]```

**运行文件**

```v run [file.v]```

**优化构建**

```v -prod [file.v]```

**格式化代码**

```v fmt [file.v]```

**启动 REPL**

```v repl```

**测试模块**

```v test [module]```

# SYNOPSIS

**v** [_run_] [_-prod_] [_options_] _file_

# PARAMETERS

**run**
> 编译源文件并立即执行生成的二进制文件。

**fmt**
> 使用规范的 V 风格格式化源文件。

**test**
> 编译并运行给定目录或模块中的 **_test.v** 文件。

**repl**
> 启动交互式 Read-Eval-Print Loop（读取-求值-输出循环）。

**build-module**, **build**, **init**, **new**, **install**, **remove**, **search**
> 用于模块脚手架和依赖管理的子命令。

**-o** _FILE_
> 输出二进制文件的名称。

**-prod**
> 启用生产环境优化（编译较慢，二进制更快）。

**-cc** _COMPILER_
> 要使用的后端 C 编译器（如 **clang**、**gcc**、**tcc**）。

**-g**
> 在输出中包含调试信息。

**-cflags** _FLAGS_, **-ldflags** _FLAGS_
> 为 C 编译器或链接器追加额外的标志。

**-shared**
> 构建共享库而不是可执行文件。

**-autofree**
> 启用实验性的自动内存释放管理模式。

**-gc** _MODE_
> 选择垃圾回收模式（如 **boehm**、**none**）。

**-stats**
> 输出详细统计信息（对 **v test** 尤其有用）。

**-show-timings**
> 报告各阶段的编译耗时。

**-skip-unused**
> 跳过未使用函数的代码生成（加快构建速度）。

# DESCRIPTION

**v** 是 V 编程语言的编译器。V 是一种为简洁和快速编译而设计的静态类型系统语言。它将 V 源代码经由 C 编译为本地机器码，即使大型项目也能实现近乎即时的构建。

该编译器内置了代码格式化工具、测试运行器、REPL 和软件包管理器。V 通过无空指针、变量默认不可变以及可选的垃圾回收等特性强调内存安全。它提供与 C 的无缝互操作，可以直接调用 C 库而无需绑定。

带 **-prod** 标志的生产构建会启用额外的优化。编译器还可以生成 C 源代码，以便移植到没有 V 编译器的平台。

# CAVEATS

年轻的语言。生态系统仍在成长中。V 特有。

# HISTORY

**V** 由 **Alexander Medvednikov** 创建，是一门简单、快速、安全的系统编程语言。

# INSTALL

```brew: brew install v```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [go](/man/go)(1), [zig](/man/zig)(1)
