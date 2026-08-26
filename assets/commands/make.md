# TAGLINE

从源码构建程序

# TLDR

**构建默认目标**

```make```

**构建指定目标**

```make [target]```

**并行执行任务**

```make -j [4]```

**使用指定的 makefile**

```make -f [Makefile.custom]```

**试运行（只打印命令而不执行）**

```make -n```

**覆盖变量**

```make [VAR=value] [target]```

**构建前切换到指定目录**

```make -C [path/to/dir]```

**强制重建所有目标**

```make -B```

# SYNOPSIS

**make** [_options_] [_target_] [_VAR=value_ ...]

# PARAMETERS

_TARGET_
> 要构建的目标。默认为 Makefile 中的第一个目标。

**-f** _FILE_
> 将 _FILE_ 作为 makefile 读取。

**-j** [_N_]
> 最多并行运行 _N_ 个任务。省略 _N_ 则不限制数量。

**-n**, **--dry-run**
> 打印将要执行的命令但不实际运行。

**-B**, **--always-make**
> 无条件重建所有目标。

**-C** _DIR_
> 在读取 makefile 或进行其他操作前先切换到 _DIR_。

**-k**, **--keep-going**
> 出错后继续构建其他目标。

**-s**, **--silent**
> 执行命令时不打印命令本身。

**-p**
> 打印内部的规则和变量数据库，然后正常继续。

**-q**, **--question**
> 若所有目标均为最新则返回退出状态 0，否则返回非零；不执行任何操作。

**-r**, **--no-builtin-rules**
> 禁用内建的隐式规则。

**-d**
> 打印所考察文件和规则的详细调试信息。

**-I** _DIR_
> 在 _DIR_ 中搜索被 include 的 makefile。

**--help**
> 显示帮助信息。

# DESCRIPTION

**make** 是一个构建自动化工具，它从 Makefile 中读取指令，将源代码编译并链接为程序。每个 Makefile 定义若干目标（要构建的文件）、它们的依赖（所依赖的源文件），以及生成它们所需的 shell 命令。调用时，make 会构建依赖图，只执行那些目标已过期的命令。

该工具通过比较文件的修改时间戳来判断哪些内容需要重建——如果某个源文件比对应的目标更新，该目标及其所有依赖它的内容都会被重建。这种增量方式避免了冗余的重复编译，能大幅加速大型构建。`-j` 选项可在多个 CPU 核心上并行执行相互独立的目标，进一步缩短构建时间。

Make 基于规则的系统还支持模式规则、隐式规则和变量，使 Makefile 既简洁又能从简单的单文件项目扩展到复杂的多目录软件系统。变量可以在命令行上覆盖（如 `make CC=clang`），特殊目标 `clean` 是清理构建产物的约定俗成的名称。

# CAVEATS

Makefile 中的配方行必须使用真正的制表符缩进，不能用空格。GNU make、BSD make 及其他实现之间的行为可能存在差异。并行构建（`-j`）可能暴露未声明的依赖关系。

# HISTORY

make 由 **Stuart Feldman** 于 **1976 年**在贝尔实验室创建，是软件开发中历史最悠久、使用最广泛的构建工具之一。

# INSTALL

```apt: sudo apt install make```

```dnf: sudo dnf install make```

```pacman: sudo pacman -S make```

```apk: sudo apk add make```

```zypper: sudo zypper install make```

```brew: brew install make```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmake](/man/cmake)(1), [ninja](/man/ninja)(1), [autoconf](/man/autoconf)(1)
