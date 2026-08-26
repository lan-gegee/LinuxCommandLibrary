# TAGLINE

从 shell 目录栈中弹出目录

# TLDR

**从栈中弹出目录**

```popd```

**弹出并切换到第 N 个目录**

```popd +[N]```

**弹出但不切换目录**

```popd -n```

**显示目录栈**

```dirs```

# SYNOPSIS

**popd** [_options_] [_+N_|-N_]

# PARAMETERS

**+N**
> 从左侧移除第 N 个条目。

**-N**
> 从右侧移除第 N 个条目。

**-n**
> 不切换目录。

# DESCRIPTION

**popd** 从 shell 的目录栈中移除栈顶目录，并切换到新的栈顶目录。它与 **pushd**（向栈中添加目录）互为补充。

使用 **+N** 或 **-N** 可以按位置从栈中移除特定条目。**-n** 标志只移除条目而不实际改变当前目录。使用 **dirs** 可查看当前栈的内容。这是 bash、zsh 及其他 shell 中可用的内建命令。

# CAVEATS

Shell 内建命令。与 pushd 和 dirs 配合使用。

# HISTORY

popd 是用于目录栈管理的 **shell 内建命令**。

# SEE ALSO

[pushd](/man/pushd)(1), [dirs](/man/dirs)(1), [cd](/man/cd)(1)
