# TAGLINE

绕过 shell 函数执行命令

# TLDR

**忽略同名 shell 函数直接运行命令**

```command [ls]```

**检查命令是否存在**（POSIX 可移植的方式）

```command -v [git] && echo "git is installed"```

**获取命令的路径**

```command -v [python3]```

**描述命令的类型**

```command -V [cd]```

**当存在同名函数时运行外部命令**

```ls() { command ls --color=auto "$@"; }```

# SYNOPSIS

**command** [**-pVv**] _command_ [_arguments_]

# PARAMETERS

**-v**
> 打印将被使用的路径名或别名（类似 **which**）。

**-V**
> 以详细方式描述命令类型。

**-p**
> 使用默认 PATH 查找命令，忽略自定义 PATH。

# DESCRIPTION

**command** 是一个 shell 内建命令，用于执行命令并绕过同名的 shell 函数。在编写包装函数时这一点至关重要——包装函数需要调用它所包装的原始命令。

配合 **-v** 时，它会打印命令的解析结果：外部命令显示其路径、别名显示其定义、内建命令和函数则给出相应标识。这是检查命令是否存在的 POSIX 可移植方式（比 **which** 更可取）。

**-V** 选项提供详细输出，描述该命令属于何种类型（内建命令、函数、别名还是外部程序）以及定义位置。

# CAVEATS

**command** 是 shell 内建命令，不是外部程序。不同 shell（bash、zsh、dash）之间的行为可能略有差异。**-v** 选项在命令存在时返回成功（0），因此非常适合条件判断。与 **which** 不同，它能正确处理内建命令和函数。

# HISTORY

**command** 内建命令由 **POSIX.2**（1992）规定，旨在提供一种绕过函数查找和检查命令可用性的标准方式。它的设计目的是取代 **which** 等不可移植的工具来确定命令路径。所有符合 POSIX 的 shell 都提供该内建命令，包括 bash、dash、zsh 和 ksh。

# SEE ALSO

[which](/man/which)(1), [type](/man/type)(1), [whence](/man/whence)(1), [builtin](/man/builtin)(1), [hash](/man/hash)(1)
