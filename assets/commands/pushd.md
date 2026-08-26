# TAGLINE

使用栈在目录之间导航

# TLDR

**将目录压入栈**

```pushd [/path/to/dir]```

**交换栈顶的两个目录**

```pushd```

**压入但不切换目录**

```pushd -n [/path/to/dir]```

**显示目录栈**

```dirs```

**从栈中弹出**

```popd```

# SYNOPSIS

**pushd** [_options_] [_dir_]

# PARAMETERS

_DIR_
> 要压入的目录。

**-n**
> 压入但不切换。

**+N**
> 将第 N 个条目（从左数）旋转到栈顶。

**-N**
> 将第 N 个条目（从右数）旋转到栈顶。

# DESCRIPTION

**pushd** 是一个 shell 内建命令，它在切换当前目录的同时将前一个目录保存到栈上。这样可以在多个工作目录之间快速导航，无需记住或重新输入完整路径。

带目录参数调用时，pushd 会切换到该目录并将旧目录压入栈。不带参数调用时，它交换栈顶的两个目录。**-n** 标志将目录压入栈但不实际切换过去。使用 **dirs** 查看当前栈的内容，使用 **popd** 返回上一个目录，使用 **+N** 或 **-N** 记法旋转到特定的栈位置。

# CAVEATS

Shell 内建命令。与 popd 和 dirs 配合使用。

# HISTORY

**pushd** 起源于 **C shell（csh）**，后被 **bash**、**zsh** 及其他 shell 采纳为管理目录栈的内建命令。

# SEE ALSO

[popd](/man/popd)(1), [dirs](/man/dirs)(1), [cd](/man/cd)(1)
