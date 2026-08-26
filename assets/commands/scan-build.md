# TAGLINE

Clang 静态分析器的构建集成工具

# TLDR

**分析构建过程**

```scan-build make```

**指定输出目录进行分析**

```scan-build -o [reports/] make```

**使用特定的检查器**

```scan-build -enable-checker [alpha.security] make```

**在浏览器中打开结果**

```scan-build --view make```

**配合 CMake 使用**

```scan-build cmake --build [build/]```

**列出可用的检查器**

```scan-build --list-checkers```

**详细输出**

```scan-build -v make```

# SYNOPSIS

**scan-build** [_-o dir_] [_--view_] [_options_] _build-command_

# PARAMETERS

**-o** _DIR_
> 输出目录。

**--view**
> 在浏览器中打开结果。

**-v**
> 详细输出。

**-enable-checker** _CHECKER_
> 启用检查器。

**-disable-checker** _CHECKER_
> 禁用检查器。

**--list-checkers**
> 显示可用的检查器。

**--status-bugs**
> 发现缺陷时以非零状态退出。

**-plist**
> 生成 plist 文件。

# DESCRIPTION

**scan-build** 包装构建命令，对每个被编译的源文件运行 Clang 静态分析器。它会拦截编译过程，在不执行代码的情况下分析 C、C++ 和 Objective-C 代码中的缺陷，包括空指针解引用、内存泄漏、释放后使用错误以及 API 误用等。

分析结果以 HTML 报告呈现，带有交互式路径可视化，展示导致每个缺陷的事件的确切序列。可以通过 **-enable-checker** 启用额外的检查器类别进行更深入的分析，包括安全漏洞检查和实验性检查。**--status-bugs** 标志在发现缺陷时返回非零退出码，便于集成到 CI 中。

# CAVEATS

会显著增加构建时间。误报需要调优。仅支持 C/C++ 和 Objective-C。

# HISTORY

**scan-build** 是 **Clang** 项目的一部分。它为 Clang 的静态分析能力提供了易于使用的接口。

# INSTALL

```apt: sudo apt install clang-tools```

```apk: sudo apk add clang22-analyzer```

```zypper: sudo zypper install clang-tools```

```nix: nix profile install nixpkgs#clang-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [cppcheck](/man/cppcheck)(1), [make](/man/make)(1)
