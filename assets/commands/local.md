# TAGLINE

bash 内置命令，用于在函数内声明局部作用域的变量

# TLDR

**声明一个局部变量**

```local [varname]```

**声明一个带初始值的局部变量**

```local [varname]="[value]"```

**声明一个局部整数变量**

```local -i [count]=0```

**声明一个局部索引数组**

```local -a [array]=([a] [b] [c])```

**声明一个局部只读变量**

```local -r [constant]="[value]"```

**从外围作用域的同名变量继承属性和值**

```local -I [varname]```

# SYNOPSIS

**local** [_option_] _name_[=_value_] ...

# PARAMETERS

**-a**
> 声明为索引数组。

**-A**
> 声明为关联数组。

**-i**
> 声明为整数。

**-l**
> 转换为小写。

**-u**
> 转换为大写。

**-r**
> 设为只读。

**-n**
> 作为对另一个变量的名称引用。

**-x**
> 标记为导出到子进程。

**-I**
> 从外围作用域中同名变量继承属性和值。

# DESCRIPTION

**local** 是 bash 内置命令，用于在函数内声明局部作用域的变量。局部变量在其声明的函数之外不可见。

使用 local 可以防止函数内的变量污染全局命名空间或与之冲突。返回状态为零，除非在函数外使用 local、提供了无效名称或变量是只读的。

# EXAMPLE

```bash
my_function() {
    local result="success"
    local -i count=5
    echo "$result: $count"
}
# $result and $count not accessible here
```

# CAVEATS

仅在函数内有效。不符合 POSIX 标准（为保证可移植性请用 typeset）。局部变量会遮蔽同名全局变量。子 shell 能继承但不能修改。

# SEE ALSO

[declare](/man/declare)(1), [typeset](/man/typeset)(1), [export](/man/export)(1), [readonly](/man/readonly)(1), [unset](/man/unset)(1), [bash](/man/bash)(1)
