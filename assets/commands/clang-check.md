# TAGLINE

基于 Clang 的静态分析与 AST 检查工具

# TLDR

对源文件**运行语法检查**

```clang-check [source.cpp]```

**带指定编译器标志检查**

```clang-check [source.cpp] -- -std=c++17 -I[/include/path]```

**导出源文件的 AST**

```clang-check -ast-dump [source.cpp]```

只导出匹配**过滤器**的 AST 节点

```clang-check -ast-dump -ast-dump-filter [functionName] [source.cpp]```

**使用编译数据库进行分析**

```clang-check -p [build/] [source.cpp]```

将 **fix-it** 修复建议应用到源文件

```clang-check -fixit [source.cpp]```

# SYNOPSIS

**clang-check** [_options_] _source-files_ [**--**] [_compiler-options_]

# PARAMETERS

**-p** _path_
> 编译数据库（compile_commands.json）的路径。

**-ast-dump**
> 将 AST 导出到 stdout。

**-ast-list**
> 列出 AST 节点。

**-ast-print**
> 美化打印 AST。

**-analyze**
> 运行静态分析。

**-ast-dump-filter** _name_
> 过滤 AST 导出/打印，仅显示限定名匹配的节点。

**-fixit**
> 将 fix-it 修复建议应用到输入源文件。

**--extra-arg** _arg_
> 追加到编译器命令行末尾的附加参数。

**--extra-arg-before** _arg_
> 前置到编译器命令行的附加参数。

# DESCRIPTION

**clang-check** 是一个结合了 LibTooling 框架（用于运行 Clang 工具）与基本 Clang 诊断的工具。它执行语法检查、类型检查，并可以导出或美化打印抽象语法树（AST）以供检查。它还可以自动应用 fix-it 修复建议。

作为 LLVM/Clang 工具链的一部分，它适合在不完整编译的情况下进行快速验证和 AST 探索。

# CAVEATS

需要安装 Clang。若要在整个项目范围内以正确的头文件路径进行分析，请使用编译数据库（compile_commands.json）。

# INSTALL

```apt: sudo apt install clang-tools```

```apk: sudo apk add clang22-extra-tools```

```zypper: sudo zypper install clang-tools```

```nix: nix profile install nixpkgs#clang-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [clang-tidy](/man/clang-tidy)(1), [clang-format](/man/clang-format)(1)
