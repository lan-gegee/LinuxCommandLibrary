# TAGLINE

Mach 系统级语言的编译器与构建工具

# TLDR

**初始化新项目**脚手架

```mach init [project_name]```

**构建**项目

```mach build```

**构建并运行**生成的二进制

```mach run```

**构建并运行**项目的测试

```mach test```

**构建优化过的**发布版二进制

```mach build --release```

**管理基于 git 的**依赖

```mach dep [subcommand]```

# SYNOPSIS

**mach** _command_ [_options_]

# DESCRIPTION

**mach** 是 Mach 编程语言的命令行驱动程序。Mach 是一种静态类型、编译型的系统语言，采用手动内存管理且没有隐藏的控制流。单个自包含的二进制即可处理完整工作流：编译并链接项目、运行测试、vendor 依赖、生成文档以及交叉编译到其他目标平台。

该编译器是自举的（用 Mach 编写），不依赖 LLVM。与构建相关的子命令共享同一个配置解析器，因此 **--target**、**--profile** 和 **--release** 等全局标志在构建、运行、测试和生成文档时保持一致的行为。

# COMMANDS

**build**
> 将项目编译为目标文件；对于二进制目标还会生成链接后的可执行文件。

**run**
> 构建项目，然后执行生成的二进制。

**test**
> 构建测试二进制并运行收集到的测试。

**dep**
> 管理基于 git 的依赖（克隆、锁定、vendor）。

**init**
> 初始化新项目的脚手架。

**doc**
> 从源码 doc 注释生成 Markdown 参考文档。

**info**
> 打印编译器版本、构建主机以及已注册的目标平台能力。

**help**
> 显示某个命令的用法信息。

# PARAMETERS

**--release**, **-O0**, **-O1**, **-O2**
> 选择构建的优化级别。

**--target** _TRIPLE_
> 为给定目标平台进行交叉编译。

**--profile** _NAME_
> 选择具名的构建 profile。

**--bin** _NAME_, **--lib**
> 选择要操作的可执行文件或库产物。

**-o** _PATH_
> 将输出写入 _PATH_。

**--emit-asm**, **--emit-ir**
> 输出汇编或中间表示，代替（或伴随）常规输出。

**-L** _PATH_, **-l** _NAME_
> 添加库搜索路径，或链接到指定名称的库。

**--verbose**, **--quiet**
> 增加或减少输出量。

# CAVEATS

Mach 是一门仍在积极开发中的年轻语言；标准库刻意保持精简（"batteries not included"，不含电池），语法和工具链可能在版本之间变化。内存通过显式传递分配器手动管理。

# HISTORY

**mach** 作为 Mach 语言项目的一部分发布，该项目提供一个不依赖 LLVM 的自举编译器。它以单个二进制的形式安装，通常通过 machlang.org 上的安装脚本获取。

# SEE ALSO

[zig](/man/zig)(1), [rustc](/man/rustc)(1), [cargo](/man/cargo)(1), [clang](/man/clang)(1), [tcc](/man/tcc)(1)

# RESOURCES

```[Source code](https://github.com/octalide/mach)```

```[Homepage](https://machlang.org)```

<!-- verified: 2026-06-14 -->
