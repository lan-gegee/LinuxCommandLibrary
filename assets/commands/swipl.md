# TAGLINE

SWI-Prolog 逻辑编程解释器

# TLDR

**启动交互式**环境

```swipl```

**加载文件**

```swipl [program.pl]```

**运行目标后退出**

```swipl -g "[goal]" -t halt [program.pl]```

**从命令行查询**

```swipl -g "[member(X,[1,2,3]),writeln(X)]" -t halt```

**编译为独立程序**

```swipl -o [output] -c [program.pl]```

# SYNOPSIS

**swipl** [_-g goal_] [_-t goal_] [_-o output_] [_options_] [_files_]

# PARAMETERS

**-g** _GOAL_
> 在进入交互式顶层之前执行的目标。可多次出现。

**-t** _GOAL_
> 使用指定目标作为交互式顶层，取代默认的 prolog/0（脚本中常用 **halt**）。

**-o** _FILE_
> 与 **-c** 配合使用时指定输出文件。

**-c** _FILES_
> 将文件编译为中间代码（保存状态）文件。

**-s** _FILE_
> 初始化后将文件作为脚本加载。

**-f** _FILE_
> 用指定文件作为初始化文件，取代默认的 **init.pl**。用 **-f none** 可跳过初始化。

**-l** _FILE_
> 加载文件（与其他 Prolog 系统兼容）。

**-x** _BOOTFILE_
> 从另一个保存状态启动。

**-O**
> 启用优化编译。

**-D** _NAME_[=_VALUE_]
> 设置一个 Prolog 标志。

**--stack-limit=**_SIZE_
> 限制 Prolog 栈的总大小（后缀 b、k、m、g）。

**-q**, **--quiet**
> 抑制提示性消息和启动横幅。

**--version**
> 打印版本与架构信息。

**--help**
> 打印简要帮助摘要。

# DESCRIPTION

**swipl** 是 SWI-Prolog 的解释器和编译器。SWI-Prolog 是最全面、使用最广泛的 Prolog 实现之一。它提供交互式 REPL，用于查询事实和规则、加载 Prolog 源文件以及编译独立的可执行程序。

SWI-Prolog 内置丰富的标准库，支持约束逻辑编程（CLP）、定子句文法、多线程、HTTP 服务器框架，以及数据库和其他语言的接口。它既支持交互式开发，也支持以编译应用的形式部署。

该系统可以从命令行执行目标、加载源文件，并通过 -c 标志创建独立的可执行程序。它被广泛用于学术研究、自然语言处理和知识表示系统。

# CAVEATS

Prolog 语法独特。属于逻辑编程范式。有学习曲线。

# HISTORY

**SWI-Prolog** 由 **Jan Wielemaker** 于 1987 年发起，是最广泛使用的 Prolog 实现之一。

# INSTALL

```apt: sudo apt install swi-prolog-core```

```dnf: sudo dnf install swi-prolog-core```

```zypper: sudo zypper install swipl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gprolog](/man/gprolog)(1), [sicstus](/man/sicstus)(1), [yap](/man/yap)(1)
