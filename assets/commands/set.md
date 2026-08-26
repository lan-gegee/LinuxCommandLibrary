# TAGLINE

设置 shell 选项和位置参数

# TLDR

**启用严格模式**（出错退出、未定义变量报错、管道失败报错）

```set -euo pipefail```

任一命令返回非零状态时**立即退出**

```set -e```

**将未定义变量视为错误**

```set -u```

**在执行前打印命令**（调试用）

```set -x```

**禁用某个选项**（用 + 代替 -）

```set +x```

**禁用文件名展开**（glob）

```set -f```

**列出所有 shell 变量**和函数

```set```

**设置位置参数**

```set -- [arg1] [arg2] [arg3]```

# SYNOPSIS

**set** [**-abefhkmnptuvxBCEHPT**] [**-o** _option-name_] [**--**] [_arg_...]

# PARAMETERS

**-a** (**allexport**)
> 导出所有创建或修改的变量和函数

**-b** (**notify**)
> 立即报告已终止后台任务的状态

**-e** (**errexit**)
> 任一命令返回非零状态时立即退出

**-f** (**noglob**)
> 禁用文件名展开（glob）

**-h** (**hashall**)
> 在查找命令时记住其位置

**-k** (**keyword**)
> 将所有赋值参数放入环境中

**-m** (**monitor**)
> 启用作业控制

**-n** (**noexec**)
> 读取命令但不执行（语法检查）

**-p** (**privileged**)
> 启用特权模式

**-t** (**onecmd**)
> 读取并执行一条命令后退出

**-u** (**nounset**)
> 展开时将未定义变量视为错误

**-v** (**verbose**)
> 在读取时打印 shell 输入行

**-x** (**xtrace**)
> 在执行前打印命令及其参数

**-B** (**braceexpand**)
> 启用花括号展开（默认开启）

**-C** (**noclobber**)
> 防止输出重定向覆盖文件

**-E** (**errtrace**)
> ERR trap 由 shell 函数和子 shell 继承

**-H** (**histexpand**)
> 启用 ! 风格的历史替换

**-P** (**physical**)
> 对 cd 等命令不解析符号链接

**-T** (**functrace**)
> DEBUG 和 RETURN trap 由函数继承

**-o pipefail**
> 管道返回最后一个非零命令的状态

**--**
> 选项结束；其余参数成为位置参数

# DESCRIPTION

**set** 是一个 shell 内建命令，用于控制 shell 选项和位置参数。选项可改变脚本编写、调试和交互使用时的 shell 行为。使用 **-** 启用选项，使用 **+** 禁用选项。

不带参数调用时，**set** 显示所有 shell 变量和函数。配合 **--** 和参数时，它将位置参数（**$1**、**$2** 等）设置为提供的值。

组合 **set -euo pipefail** 是 shell 脚本常用的"严格模式"，遇到错误、未定义变量引用或管道失败时立即退出——及早发现缺陷并防止静默失败。

# CAVEATS

**-e** 选项有许多例外情况：它不会因 **if** 测试中的命令、**while**/**until** 条件、以 **!** 取反的命令，或 **&&** 与 **||** 左侧的命令而触发退出。理解这些例外对脚本中可靠的错误处理非常重要。

# HISTORY

**set** 命令自 **Stephen Bourne** 于 **1979** 年在贝尔实验室创建 Bourne shell 以来就是其中的一部分。它被纳入 POSIX，并在 bash 中通过 **pipefail** 等额外选项得到扩展。shell 选项的概念甚至早于 Bourne shell，可追溯到早期 Unix shell。

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [shopt](/man/shopt)(1), [unset](/man/unset)(1), [export](/man/export)(1)
