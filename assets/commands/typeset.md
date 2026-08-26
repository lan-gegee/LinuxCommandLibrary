# TAGLINE

声明带有属性的 Shell 变量

# TLDR

**声明整数变量**

```typeset -i [count]=0```

**声明只读变量**

```typeset -r [CONSTANT]="[value]"```

**声明大写转换变量**

```typeset -u [name]="[value]"```

**声明小写转换变量**

```typeset -l [name]="[VALUE]"```

**将变量导出**给子进程

```typeset -x [PATH]="[/usr/bin]"```

**声明数组**

```typeset -a [myarray]=([one] [two] [three])```

**声明关联数组**（bash 4+）

```typeset -A [mymap]=([key1]="[val1]" [key2]="[val2]")```

**列出具有指定属性的所有变量**

```typeset -i```

# SYNOPSIS

**typeset** [**-aAfFgilnrtux**] [**-p**] [_name_[=_value_]...]

# PARAMETERS

**-a**
> 声明索引数组变量

**-A**
> 声明关联数组变量（bash 4+）

**-f**
> 显示函数名及定义

**-F**
> 仅显示函数名

**-g**
> 在函数中使用时创建全局变量（仅 bash）

**-i**
> 将变量视为整数；赋值时进行算术求值

**-l**
> 赋值时将值转换为小写

**-n**
> 创建 nameref（对另一个变量的引用）

**-r**
> 将变量设为只读

**-t**
> 为变量赋予 trace 属性

**-u**
> 赋值时将值转换为大写

**-x**
> 将变量导出到子进程的环境

**-p**
> 显示变量的属性和值

# DESCRIPTION

**typeset** 是一个 Shell 内建命令，用于声明变量并为其赋予属性。在 bash 中它是 **declare** 的同义词，为了兼容 ksh (KornShell) 而保留。

变量可以被赋予类型属性，例如整数（**-i**）用于自动算术求值；也可以被赋予变换属性，例如大写（**-u**）和小写（**-l**）。只读属性（**-r**）可防止赋值后被修改。

在函数内不带 **-g** 使用时，typeset 会创建局部变量并遮蔽任何同名全局变量。函数退出后该变量会被恢复。

不带参数时，typeset 显示所有变量及其属性。仅带属性标志时（例如 **typeset -i**），列出具有该属性的变量。

# CAVEATS

在 bash 中，**typeset** 被标记为已过时，建议改用 **declare**，但两者的行为完全相同。不同 Shell（bash、ksh、zsh）之间行为有差异。**-n** nameref 选项需要 bash 4.3+ 或 ksh93。关联数组（**-A**）需要 bash 4+。

# HISTORY

**typeset** 起源于 **David Korn** 于 **20 世纪 80 年代初**在贝尔实验室开发的 **KornShell**（ksh）。bash 创建时实现了类似的功能即 **declare**，同时保留了 **typeset** 作为别名以兼容 ksh。对于面向多种 Korn 系 Shell 的可移植脚本而言，该命令仍然十分重要。

# SEE ALSO

[declare](/man/declare)(1), [local](/man/local)(1), [export](/man/export)(1), [readonly](/man/readonly)(1), [bash](/man/bash)(1)
