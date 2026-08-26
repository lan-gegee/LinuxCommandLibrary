# TAGLINE

REDUCE 使用的 ALGOL 风格 Standard Lisp 方言

# TLDR

**启动交互式 RLISP 会话**

```rlisp```

**加载并执行 RLISP 源文件**

```rlisp < [program.red]```

**使用自定义堆大小（以 MB 为单位）**

```rlisp -K [256]```

**隐藏横幅和垃圾回收器输出**

```rlisp -q```

**从命令行设置 Lisp 变量**

```rlisp -D [name]=[value]```

# SYNOPSIS

**rlisp** [_options_] [_file_]

# PARAMETERS

**--help**
> 显示帮助文本并退出。

**--version**
> 显示版本信息。

**-v**
> 打印扩展的启动横幅；详细模式。

**-q**
> 安静模式：抑制回显和垃圾回收器消息。

**-w**
> 强制控制台（非窗口）方式运行。

**--nogui**
> 强制使用控制台风格的应用程序。

**-K** _nnn_
> 设置堆大小（MB）；堆不会增长超过 _nnn_。

**-K** _nnn_**/**_ss_
> 设置堆大小和 Lisp 栈页数。

**-i** _file_
> 向搜索路径添加一个只读镜像文件。

**-o** _file_
> 设置 **faslout** 使用的输出镜像文件。

**-D** _name_**=**_value_
> 从命令行预先绑定一个 Lisp 变量。

**-l** _file_
> 将标准输出重定向到 _file_。

**-r** _n_**,**_m_
> 为随机数生成器设定种子，以便运行结果可复现。

**-z**
> 引导模式：不加载镜像文件直接启动。

# DESCRIPTION

**RLISP** 是 **Standard Lisp** 的类 ALGOL 表层语法，由 **REDUCE** 计算机代数系统在内部使用。它提供 Lisp 语义——符号表达式、列表、原子、递归——但使用更易读的中缀和关键字语法（**begin**/**end**、**if**/**then**/**else**、**for**、**while**），而不是 S 表达式。

启动后，**rlisp** 会进入交互式的读取-求值-打印循环。语句以分号（**;**）结尾时输出正常结果，以美元符号（**$**）结尾时则不打印结果。在 REDUCE 内部，你可以用 **symbolic;** 切换到 RLISP/符号模式，再用 **algebraic;** 切换回来。

该二进制文件是 REDUCE 的一部分，通常构建于 **CSL**（Codemist Standard Lisp）或 **PSL**（Portable Standard Lisp）之上；可用的命令行选项反映了底层 Lisp 引擎的能力。

# CAVEATS

语句必须以 **;** 或 **$** 结尾——仅按 **Return** 键不会执行。变量名和函数名不区分大小写（统一折叠为大写）。在现代系统中，RLISP 主要作为 REDUCE 的一部分出现：除 REDUCE 源码树之外很少单独使用。

# HISTORY

RLISP 于 **20 世纪 70 年代**初在**犹他大学**（Anthony Hearn、Martin Griss 等人）开发，作为符号计算系统 **REDUCE** 的实现语言，REDUCE 首次发布于 **1968 年**。RLISP '88 增加了结构化编程特性。**2008 年**，REDUCE 以 BSD 许可证成为自由开源软件，并继续随附 RLISP，它既是实现语言也是符号编程语言。

# SEE ALSO

[maxima](/man/maxima)(1)
