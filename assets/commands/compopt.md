# TAGLINE

在 Bash 中动态修改补全选项

# TLDR

**为补全函数启用文件名补全**

```compopt -o filenames```

**仅启用目录补全**

```compopt -o dirnames```

**禁用默认补全行为**

```compopt +o default```

**补全后不追加空格**

```compopt -o nospace```

**移除 nospace 选项**

```compopt +o nospace```

**为指定命令设置选项**

```compopt -o filenames [command_name]```

# SYNOPSIS

**compopt** [-o _option_] [-DE] [+o _option_] [_name_...]

# PARAMETERS

**-o** _OPTION_
> 启用指定的补全选项。

**+o** _OPTION_
> 禁用指定的补全选项。

**-D**
> 应用于默认补全（未定义专用补全时生效）。

**-E**
> 应用于空命令补全（在空行上触发的补全）。

**-I**
> 应用于首个单词的补全。

**filenames**
> 执行文件名补全及相应处理（转义、尾部斜杠）。

**dirnames**
> 执行目录名补全。

**nospace**
> 补全后不追加空格。

**default**
> 无匹配时使用默认的 readline 补全。

**bashdefault**
> 无匹配时使用 bash 默认补全。

**plusdirs**
> 在补全候选中加入目录名。

# DESCRIPTION

**compopt** 是一个 Bash 内建命令，用于在可编程补全函数中动态修改补全行为。它让补全函数能够根据上下文或参数调整自身选项。

在补全函数内不带参数调用时，compopt 修改的是当前补全的选项。提供命令名时，它修改的是这些命令的补全规范，作用类似 **complete -o**。

要创建能根据补全对象自适应行为的复杂补全函数，这个命令必不可少。例如，函数可以只在用户正在补全文件路径参数时才启用文件名补全。

# CAVEATS

compopt 只能在可编程补全的上下文中工作。它必须在补全函数内部调用，或在指定命名命令时调用。在没有指定命令名的情况下于补全上下文之外使用 compopt 会报错。

# HISTORY

compopt 于 **2009 年**发布的 **Bash 4.0** 中引入。它的加入提供了对补全选项的动态控制，与设置静态补全规范的 **complete** 内建命令形成互补，使更具上下文感知能力的补全函数成为可能。

# SEE ALSO

[complete](/man/complete)(1), [compgen](/man/compgen)(1), [bash](/man/bash)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/bash.git)```

```[Documentation](https://www.gnu.org/software/bash/manual/)```

<!-- verified: 2026-06-22 -->
