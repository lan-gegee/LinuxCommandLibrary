# TAGLINE

面向 IDE 功能的 C/C++ 语言服务器

# TLDR

**启动语言服务器（通常由编辑器启动）**

```clangd```

**使用指定的 compile_commands.json 目录**

```clangd --compile-commands-dir=[/path/to/build]```

**启用持久化后台索引与 clang-tidy 检查**

```clangd --background-index --clang-tidy```

**降低大型项目的内存压力**

```clangd --pch-storage=memory -j=[4]```

**在服务器循环之外解析单个文件以调试配置**

```clangd --check=[src/main.cpp]```

**启用详细日志以便排查问题**

```clangd --log=verbose --pretty```

**检查版本**

```clangd --version```

# SYNOPSIS

**clangd** [_options_]

# DESCRIPTION

**clangd** 是一个 C/C++/Objective-C 语言服务器，为支持 Language Server Protocol（LSP）的编辑器提供代码补全、诊断、跳转到定义和重构等 IDE 功能。

它使用 clang 编译器前端来解析和理解代码，提供基于真实编译的准确结果。clangd 读取 compile_commands.json 或 compile_flags.txt 来了解项目的构建设置。

该服务器通过 stdin/stdout 使用 JSON-RPC 通信，因此兼容 VS Code、Vim、Emacs、Sublime Text 及其他支持 LSP 的编辑器。

# PARAMETERS

**--compile-commands-dir=** _DIR_
> 在 _DIR_ 而非源码树中查找 compile_commands.json。

**--background-index**
> 在后台索引项目源码并将索引持久化到磁盘，加快启动速度。

**--clang-tidy**
> 将 clang-tidy 检查作为诊断的一部分运行。

**--completion-style=** _STYLE_
> 补全项的粒度：`detailed`（每个重载一项）或 `bundled`（分组）。

**--header-insertion=** _MODE_
> 补全时自动包含头文件：`iwyu`（include-what-you-use）或 `never`。

**--all-scopes-completion**
> 建议当前作用域之外命名空间中的符号，并按需插入限定符。

**--fallback-style=** _STYLE_
> 找不到 .clang-format 文件时应用的 clang-format 风格（如 `LLVM`、`Google`）。

**--log=** _LEVEL_
> stderr 的日志详细程度：`error`、`info` 或 `verbose`。

**--pretty**
> 美化打印 JSON-RPC 输出（配合 --log 便于调试）。

**--pch-storage=** _TYPE_
> 将预编译头存储在 `disk`（默认，内存占用低）或 `memory`（更快）。

**--query-driver=** _GLOBS_
> 以逗号分隔的编译器二进制文件通配模式，clangd 可执行它们来探测系统头文件路径。

**-j** _N_
> 异步工作线程数（也用于后台索引）。

**--limit-results=** _N_
> 限制每个请求返回的结果数（默认 100；0 = 不限制）。

**--limit-references=** _N_
> 限制返回的引用数（默认 1000；0 = 不限制）。

**--offset-encoding=** _ENC_
> 强制位置编码：`utf-8`、`utf-16` 或 `utf-32`。

**--enable-config**
> 从 `.clangd` 和 `clangd/config.yaml` YAML 文件读取用户级和项目级配置。

**--check** [= _FILE_ ]
> 隔离解析单个文件而非作为服务器运行；用于复现崩溃或诊断环境配置。

**--version**
> 显示版本信息。

**--help**
> 显示可用选项（用 `--help-hidden` 可查看实验性标志）。

# CONFIGURATION

**.clangd**
> 项目级配置，涵盖编译器标志、诊断和补全行为。

**compile_commands.json**
> 由构建系统生成的编译数据库，用于精确的项目分析。

**compile_flags.txt**
> 每行一个简单编译器标志的文件，可作为 compile_commands.json 的替代。

# CAVEATS

需要 compile_commands.json 或 compile_flags.txt 才能进行准确分析。大型项目的初始索引可能较慢。内存占用随项目规模增长。某些功能需要较新版本的 clangd。若配置不当可能找不到系统头文件。

# HISTORY

**clangd** 作为 **LLVM/Clang 项目**的一部分自约 **2017** 年开始开发，旨在为 C 语言家族提供现代语言服务器。它取代了早期基于 libclang 的补全工具。该项目发展迅速，陆续加入了语义高亮、内嵌提示（inlay hints）和改进的索引等功能。如今它被认为是最强大的 C++ 语言服务器之一。

# INSTALL

```apt: sudo apt install clangd```

```apk: sudo apk add clang22-extra-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [clang-format](/man/clang-format)(1), [clang-tidy](/man/clang-tidy)(1)
