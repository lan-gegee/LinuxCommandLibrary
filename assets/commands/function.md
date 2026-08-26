# TAGLINE

shell 函数定义关键字

# TLDR

**定义函数**

```function greet() { echo "Hello $1"; }```

**调用函数**

```greet [World]```

**列出已定义的函数**

```declare -F```

**显示函数定义**

```declare -f [function_name]```

**取消函数定义**

```unset -f [function_name]```

# SYNOPSIS

**function** _name_() { _commands_; }

# PARAMETERS

_NAME_
> 函数名称。

_COMMANDS_
> 函数体的命令。

**$1**, **$2** 等
> 位置参数。

**$@**
> 所有参数。

**return** _N_
> 以指定状态码退出函数。

**local** _VAR_
> 声明局部变量。

# DESCRIPTION

**function** 是用于定义可复用命令组的 shell 关键字。函数可以封装命令、接受参数，并能返回退出状态值。

函数支持代码复用、模块化，让脚本更整洁。使用 `local` 关键字可以为变量提供局部作用域。参数通过位置变量（$1、$2 等）访问。

在 bash 中，`function name() { ...; }` 和 `name() { ...; }` 两种语法都可以定义函数。POSIX 可移植的形式省略 `function` 关键字。在 ksh 和 zsh 中，同样支持 `function` 关键字。

# CAVEATS

函数必须先定义后使用。`return` 只能设置退出状态（0-255），不能返回输出值——要捕获输出请使用命令替换。变量作用域需要显式声明 `local`；否则变量是全局的。

# SEE ALSO

[bash](/man/bash)(1), [declare](/man/declare)(1), [local](/man/local)(1), [unset](/man/unset)(1)
