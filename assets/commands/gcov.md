# TAGLINE

测试覆盖率分析程序

# TLDR

生成名为 file.cpp.gcov 的**覆盖率报告**

```gcov [path/to/file.cpp]```

为每个**基本块**写出单独的执行计数

```gcov -a [path/to/file.cpp]```

将**分支频率**写入输出并以百分比打印摘要

```gcov -b [path/to/file.cpp]```

以**被采纳分支的数量**形式写出分支频率

```gcov -c [path/to/file.cpp]```

不创建 **gcov 输出文件**

```gcov -n [path/to/file.cpp]```

写出文件级和**函数级摘要**

```gcov -f [path/to/file.cpp]```

# SYNOPSIS

**gcov** [_options_] _source-files_

# PARAMETERS

**-a**, **--all-blocks**
> 为每个基本块写出单独的执行计数

**-b**, **--branch-probabilities**
> 将分支频率以百分比形式写入输出文件

**-c**, **--branch-counts**
> 将分支频率以次数而非百分比形式写出

**-f**, **--function-summaries**
> 除文件摘要外，还为每个函数输出摘要

**-n**, **--no-output**
> 不创建 gcov 输出文件

**-l**, **--long-file-names**
> 输出文件使用长文件名

**-p**, **--preserve-paths**
> 在输出文件名中保留完整的路径信息

**-o**, **--object-directory** _DIR_
> 在 _DIR_ 中查找目标文件

**-s**, **--source-prefix** _PREFIX_
> 移除源码路径前缀，使输出文件名更短

# DESCRIPTION

**gcov** 是一个配合 GCC 使用的测试覆盖率程序，用于分析程序在测试期间执行了哪些部分。它帮助找出未经测试的代码路径，从而提高测试套件的完整性。

要使用 gcov，需要用 **-fprofile-arcs -ftest-coverage**（或 **--coverage**）编译程序。运行程序后，gcov 会读取生成的 .gcno 和 .gcda 文件，产出带注释的源代码清单，显示每行的执行计数。

输出文件（*.gcov）包含带有执行计数注释的原始源代码。标记为 **#####** 的行从未被执行过。分支信息有助于识别未测试的条件路径。

# CAVEATS

要求程序使用特殊的 GCC 标志编译。只对 GCC 编译的代码有效。多次运行程序会累积覆盖率数据，除非在每次运行之间删除 .gcda 文件。内联函数可能显示具有误导性的计数。

# HISTORY

gcov 自 20 世纪 90 年代初起就是 GNU 编译器套件（GCC）的一部分。它随 GCC 的性能剖析能力一同演进，至今仍是开源生态中进行 C/C++ 代码覆盖率分析的基础工具。

# INSTALL

```apt: sudo apt install gcc```

```dnf: sudo dnf install gcc```

```pacman: sudo pacman -S gcc```

```apk: sudo apk add gcc```

```zypper: sudo zypper install gcc```

```brew: brew install gcc```

```nix: nix profile install nixpkgs#gcc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [lcov](/man/lcov)(1), [gprof](/man/gprof)(1)

# RESOURCES

```[Documentation](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html)```

<!-- verified: 2026-07-15 -->
