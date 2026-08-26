# TAGLINE

为 C/C++ 项目生成编译数据库

# TLDR

**从 make 生成编译数据库**

```compiledb make```

**从 make 干跑（dry-run）生成**

```compiledb -n make```

**解析已有的构建日志**

```compiledb --parse [build.log]```

**输出到指定文件**

```compiledb -o [compile_commands.json] make```

**排除特定路径**

```compiledb --exclude [/path/to/exclude] make```

# SYNOPSIS

**compiledb** [_options_] _command_ [_args_]

# DESCRIPTION

**compiledb** 从构建命令生成编译数据库（compile_commands.json）。该数据库供 clangd、clang-tidy 以及各类 IDE 用于代码智能和静态分析。

该工具拦截或解析 make 命令的输出，提取编译器调用及其标志和源文件。它既支持实际执行构建，也支持解析现有的构建日志。

# PARAMETERS

**-n**, **--no-build**
> 只解析 make 输出而不实际构建。

**-p**, **--parse** _file_
> 解析已有的构建日志文件。

**-o**, **--output** _file_
> 输出文件（默认：compile_commands.json）。

**--exclude** _path_
> 将路径排除出数据库。

**-f**, **--full-path**
> 源文件使用完整路径。

**--command-style**
> 使用命令字符串而非参数数组的形式。

**-S**, **--strict**
> 解析失败时以错误退出。

# CAVEATS

只能捕获 make 输出中的命令。未经过 make 的编译器调用可能被遗漏。复杂的构建系统可能需要额外配置。并非对所有构建系统都有效。

# HISTORY

**compiledb** 的诞生是为了弥合基于 make 的构建与需要编译数据库的现代 C/C++ 工具链之间的鸿沟。随着 clangd 和 clang-tidy 生态在 **2010 年代后期**日益流行，它作为 cmake 或 bear 之外更简单的 compile_commands.json 生成方案应运而生。

# INSTALL

```brew: brew install compiledb```

```nix: nix profile install nixpkgs#compiledb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [bear](/man/bear)(1), [cmake](/man/cmake)(1), [clangd](/man/clangd)(1)

# RESOURCES

```[Source code](https://github.com/nickdiego/compiledb)```

<!-- verified: 2026-06-22 -->
