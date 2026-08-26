# TAGLINE

面向技术计算的高级高性能编程语言

# TLDR

**启动 Julia REPL**

```julia```

**运行 Julia 脚本**

```julia [script.jl]```

**以多线程运行**

```julia --threads [4] [script.jl]```

**求值表达式**

```julia -e '[println("Hello")]'```

**以安静模式运行**（不显示横幅）

```julia -q```

**以指定项目启动**

```julia --project=[path/to/project]```

**安装软件包**（在 REPL 中）

```julia -e 'using Pkg; Pkg.add("[PackageName]")'```

**预编译软件包**

```julia -e 'using Pkg; Pkg.precompile()'```

# SYNOPSIS

**julia** [_options_] [_script.jl_] [_args ..._]

# PARAMETERS

**-e** _expr_
> 求值表达式。

**-E** _expr_
> 求值并显示结果。

**-p**, **--procs** _n_
> 启动 n 个工作进程。

**-t**, **--threads** _n_
> 启用 n 个线程（或 "auto"）。

**--project** _path_
> 设置项目/环境目录。

**-q**, **--quiet**
> 不显示启动横幅。

**-i**
> 脚本执行后进入交互模式。

**-L**, **--load** _file_
> 启动时加载文件。

**-J**, **--sysimage** _file_
> 使用自定义系统映像。

**--startup-file** _yes|no_
> 是否加载 ~/.julia/config/startup.jl。

**--history-file** _yes|no_
> 是否加载/保存命令历史。

**-O**, **--optimize** _level_
> 优化级别（0-3）。

**--compile** _yes|no|all|min_
> 编译模式。

**--code-coverage** _none|user|all_
> 启用代码覆盖率统计。

**--track-allocation** _none|user|all_
> 跟踪内存分配。

**--depwarn** _yes|no|error_
> 弃用警告的处理方式。

**--help**
> 显示帮助信息。

**--version**
> 显示版本号。

# DESCRIPTION

**Julia** 是一门面向技术计算的高级高性能编程语言。它兼具 Python 等动态语言的易用性和 C 等编译型语言的速度，这得益于基于 LLVM 的即时（JIT）编译。

REPL（读取-求值-打印循环）提供了交互式环境，支持制表符补全、帮助系统（输入 ?）、shell 模式（输入 ;）和包管理模式（输入 ]）。包管理器 Pkg 通过 Project.toml 和 Manifest.toml 文件处理依赖关系。

Julia 擅长数值与科学计算，原生支持多维数组、复数和数学运算。并行计算内置于语言之中，包括线程、分布式计算和 GPU 支持。

其类型系统既能带来高性能（通过类型推断），又保留了灵活性（多重派发让函数根据参数类型表现出不同行为）。这使得 Julia 既适合快速原型开发，也适合生产环境部署。

包环境为每个项目隔离依赖。使用 --project 标志激活指定环境。软件包从 General 注册表或 Git 仓库安装。

# CAVEATS

由于 JIT 编译，首次运行较慢（即"首图耗时"问题）。软件包更新后的预编译需要时间。简单任务的内存占用可能高于 Python。部分 Python 库没有 Julia 对应物。并行化时需要注意线程安全。

# HISTORY

**Julia** 由 Jeff Bezanson、Stefan Karpinski、Viral B. Shah 和 Alan Edelman 在 MIT 开发，项目始于 **2009 年**，**2012 年**公开发布。**2018 年 8 月**发布的 1.0 版本标志着语言进入稳定期。此后 Julia 在科学计算、数据科学和机器学习领域获得了广泛采用。

# INSTALL

```dnf: sudo dnf install julia```

```pacman: sudo pacman -S julia```

```brew: brew install julia```

```nix: nix profile install nixpkgs#julia```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [matlab](/man/matlab)(1), [octave](/man/octave)(1)
