# TAGLINE

用于声明带属性变量的 bash 内置命令

# TLDR

**声明整数变量**

```declare -i [number]=42```

**声明只读变量**

```declare -r [CONSTANT]="value"```

**声明索引数组**

```declare -a [myarray]=([element1] [element2])```

**声明关联数组**

```declare -A [mymap]=([key1]=value1 [key2]=value2)```

**导出变量**

```declare -x [ENVVAR]="value"```

**声明小写变量**

```declare -l [lower]="HELLO"```

**声明大写变量**

```declare -u [upper]="hello"```

**显示变量的属性和值**

```declare -p [variable_name]```

**列出所有函数**

```declare -f```

# SYNOPSIS

**declare** [_options_] [_name_[=_value_]...]

# PARAMETERS

**-a**
> 声明索引数组。

**-A**
> 声明关联数组（bash 4 及以上）。

**-f**
> 显示或声明函数。

**-F**
> 仅显示函数名。

**-g**
> 创建全局变量（在函数内使用）。

**-i**
> 声明整数（自动算术求值）。

**-l**
> 赋值时转换为小写。

**-n**
> 名称引用（bash 4.3 及以上）。

**-r**
> 设为只读（常量）。

**-t**
> 赋予 trace 属性（调试用）。

**-u**
> 赋值时转换为大写。

**-x**
> 导出到环境变量。

**-I**
> 从外围作用域同名变量继承属性和值（bash 5.1 及以上）。

**-p**
> 显示属性和值。

**+**_attr_
> 移除属性。

# DESCRIPTION

**declare** 是 bash 内置命令，用于声明带有特定属性的变量。虽然 bash 允许隐式创建变量，但 declare 提供了显式的类型声明和特殊行为。

整数变量（**-i**）自动执行算术运算：`declare -i x; x=5+3` 会把 x 设为 8。数组需要显式声明才能正确初始化。只读变量无法修改或撤销。

在函数内部，declare 声明的变量默认是局部的；使用 **-g** 可创建全局变量。**-n** 选项创建指向其他变量的引用，实现间接变量访问。

# CAVEATS

关联数组要求 bash 4 及以上，名称引用要求 bash 4.3 及以上。declare 是 bash 特有的；POSIX shell 使用不同的机制。-g 标志只在函数内部有效。只读变量持续到 shell 退出为止，且无法被 unset。

# HISTORY

**declare** 内置命令源自 **ksh**（Korn Shell），后被 bash 采用。相比简单赋值，它提供了更显式的变量定义方式。bash 在各版本中不断扩展 declare：**bash 4.0**（2009 年）加入关联数组，**bash 4.3**（2014 年）加入名称引用。

# SEE ALSO

[typeset](/man/typeset)(1), [local](/man/local)(1), [readonly](/man/readonly)(1), [export](/man/export)(1)
