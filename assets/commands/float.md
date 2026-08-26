# TAGLINE

声明浮点型 Shell 变量

# TLDR

**声明浮点变量**并赋值

```float [myvar]=3.14```

**声明多个浮点变量**

```float [x]=1.5 [y]=2.7```

**用算术表达式声明浮点数**

```float [result]='10.0 / 3.0'```

**列出**当前已设置的所有浮点变量

```float```

**声明浮点变量并导出**到环境

```float -x [myvar]=9.81```

将浮点变量设为**只读**

```float -r [PI]=3.14159265```

# SYNOPSIS

**float** [**-ghlrtux**] [_name_[=_value_]...]

# PARAMETERS

**-g**
> 在函数内部使用时创建全局变量

**-h**
> 隐藏变量；即使在外层作用域中已导出，也不导出给子进程

**-l**
> 左对齐并去除前导空白

**-r**
> 将变量设为只读

**-t**
> 为变量打标记（用户自定义属性）

**-u**
> 赋值时强制转为大写（针对字符串上下文）

**-x**
> 将变量导出到子进程的环境

**+**_attr_
> 移除指定的属性

# DESCRIPTION

**float** 是一个 zsh 内建命令，用于声明带浮点属性的变量。它等同于 **typeset -E**，使变量以浮点（科学计数法）形式存储和显示。

当向浮点变量赋值时，zsh 会执行算术求值，因此可以写 `float x=1.0/3.0` 这样的表达式。结果以双精度浮点数存储。用 float 声明的变量默认以科学计数法显示（例如 `3.1400000000000000e+00`）。

不带参数运行时，**float** 会列出当前声明的所有浮点变量及其值。

# CAVEATS

仅在 **zsh** 中可用；不是 bash 或其他 POSIX shell 的内建命令。浮点运算受 IEEE 754 常见的精度限制和舍入误差影响。只读的浮点变量无法被 unset 或修改。

# HISTORY

**float** 内建命令在 **zsh** 中引入，作为 **typeset -E** 的便捷简写。zsh 自 **4.0 版本**（2001 年）起支持浮点运算，这是其超出 POSIX sh 要求的扩展数学能力的一部分。zsh 中的 float、integer 和 readonly 内建命令都是围绕 typeset 的专用封装。

# SEE ALSO

[typeset](/man/typeset)(1), [declare](/man/declare)(1), [readonly](/man/readonly)(1), [zsh](/man/zsh)(1)
