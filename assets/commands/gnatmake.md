# TAGLINE

Ada 程序构建工具

# TLDR

**编译 Ada 程序**

```gnatmake [main.adb]```

**带优化编译**

```gnatmake -O2 [main.adb]```

**带调试信息编译**

```gnatmake -g [main.adb]```

**并行任务编译**

```gnatmake -j4 [main.adb]```

**指定输出的可执行文件名**

```gnatmake [main.adb] -o [program]```

**强制重新编译所有源文件**

```gnatmake -f [main.adb]```

# SYNOPSIS

**gnatmake** [_options_] _file_name_ [_options_]

# PARAMETERS

**-jN**
> 使用 N 个并行任务进行编译。

**-g**
> 生成调试信息。

**-O**_level_
> 优化级别（0、1、2、3，或 s 表示按体积优化）。

**-o** _name_
> 输出的可执行文件名。

**-c**
> 只编译，不绑定或链接。

**-f**
> 强制重新编译所有源文件。

**-q**
> 安静模式，减少输出。

**-v**
> 详细模式。

**-I**_dir_
> 将目录加入源文件搜索路径。

**--RTS=**_runtime_
> 指定 Ada 运行时库。

# DESCRIPTION

**gnatmake** 是 GNAT（GNU Ada 工具集）环境中 Ada 程序的主要构建工具。它通过分析 Ada 的 with 子句自动确定依赖关系，编译修改过的源文件，并执行绑定和链接以生成可执行文件。与传统 make 工具不同，**gnatmake** 总是从源文件重新计算依赖关系，确保准确追踪变更。

# CAVEATS

可以指定多个主文件来构建多个可执行文件。依赖关系从 Ada 源文件计算得出，而非依据目标文件的时间戳。

# INSTALL

```apt: sudo apt install gnat-12```

```dnf: sudo dnf install gcc-gnat```

```apk: sudo apk add gcc-gnat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1)
