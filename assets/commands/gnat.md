# TAGLINE

GNU Ada 编译器工具链

# TLDR

**将 Ada 程序编译**为目标文件

```gcc -c [program.adb]```

用 gnatmake **构建 Ada 可执行文件**

```gnatmake [program.adb]```

**绑定（bind）Ada 程序**

```gnatbind [program]```

**链接 Ada 程序**

```gnatlink [program]```

启用所有警告**进行编译**

```gnatmake -gnatwa [program.adb]```

清理项目的**已构建文件**

```gnatclean [program]```

只**检查语法**而不编译

```gcc -c -gnats [program.adb]```

**生成交叉引用**信息

```gnatxref [program.adb]```

# SYNOPSIS

**gcc** **-c** [_OPTIONS_] _FILE.adb_

**gnatmake** [_OPTIONS_] _FILE.adb_

**gnatbind** [_OPTIONS_] _FILE_

**gnatlink** [_OPTIONS_] _FILE_

# COMMANDS

**gnatmake**
> 构建 Ada 程序，自动处理编译、绑定和链接。

**gnatbind**
> 绑定 Ada 程序单元，生成主程序包装代码。

**gnatlink**
> 链接目标文件以创建可执行文件。

**gnatclean**
> 删除 gnatmake 生成的文件。

**gnatfind**
> 搜索 Ada 标识符的定义和引用。

**gnatxref**
> 生成交叉引用信息。

**gnatls**
> 列出已编译 Ada 单元的信息。

# PARAMETERS

**-c**
> 只编译，不链接（gcc 编译 Ada 时必需）。对 gnatmake 而言，只编译和绑定，跳过链接步骤，除非同时给出 **-b**。

**-f**
> 强制重新编译所有源文件，即使目标文件看似是最新的（gnatmake）。

**-j** _N_
> 使用 N 个进程并行编译（gnatmake）。设为 0 表示使用所有可用核心。

**-q**
> 安静模式：抑制 gnatmake 通常回显的编译命令。

**-gnatwa**
> 启用所有警告。

**-gnato**
> 启用数值溢出检查。

**-gnats**
> 仅做语法检查。

**-gnatc**
> 仅做语义检查。

**-gnatf**
> 输出完整错误（详细的错误信息）。

**-O**[_N_]
> 优化级别（0-3）。

**-g**
> 包含调试信息。

# DESCRIPTION

**GNAT**（GNU Ada Translator）是 GCC 集合中的 Ada 编译器。它可编译 Ada 83、Ada 95、Ada 2005 和 Ada 2012 程序。Ada 源文件使用 .ads（规格说明）和 .adb（程序体）扩展名。

GNAT 的构建过程分为三个阶段：编译（gcc -c）、绑定（gnatbind）和链接（gnatlink）。**gnatmake** 工具将这三个阶段自动化，分析依赖关系并只重新编译必要的部分。

# CAVEATS

与 C/C++ 不同，Ada 程序无法在单次 gcc 调用中完成编译和链接；必须使用 -c 标志，且绑定必须单独执行。gnatmake 会自动处理这一切，是大多数项目推荐的构建方式。

# HISTORY

GNAT 由纽约大学根据美国空军合同开发，首个公开版本发布于 **1995** 年。随后由 Ada Core Technologies（现为 AdaCore）维护和增强。GNAT 后来成为 GCC 的一部分，是目前使用最广泛的 Ada 编译器，在众多平台上支持完整的 Ada 语言标准。

# INSTALL

```apt: sudo apt install gnat-12```

```dnf: sudo dnf install gcc-gnat```

```apk: sudo apk add gcc-gnat```

```nix: nix profile install nixpkgs#gnat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [gprbuild](/man/gprbuild)(1), [make](/man/make)(1)

# RESOURCES

```[GNAT User's Guide](https://gcc.gnu.org/onlinedocs/gnat_ugn/)```

```[AdaCore GNAT Community](https://www.adacore.com/download)```

<!-- verified: 2026-07-17 -->
