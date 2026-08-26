# TAGLINE

为命令创建简短别名

# TLDR

**列出**所有别名

```alias```

**创建**一个简单别名

```alias [ll]='ls -la'```

创建带**参数**的别名

```alias [grep]='grep --color=auto'```

**移除**一个别名

```unalias [ll]```

创建**持久化**别名（添加到 ~/.bashrc 或 ~/.zshrc）

```echo "alias ll='ls -la'" >> ~/.bashrc```

# SYNOPSIS

**alias** [_name_[=_value_]...]

# DESCRIPTION

**alias** 是一个 shell 内建命令，用于为命令或命令序列创建简称。当你输入别名时，shell 会在执行前将其替换为关联的值。

别名适合为带特定选项的常用命令创建快捷方式，减少敲击键盘并避免重复出错。

# PARAMETERS

不带参数时，**alias** 显示所有已定义的别名。带 **name** 时显示该别名的定义。带 **name=value** 时创建或更新别名。

# CAVEATS

在 shell 脚本中默认不展开别名。别名不接受出现在展开文本中间的参数（这种需求请用函数）。别名是特定于 shell 的，要持久化必须定义在该 shell 的配置文件里。

# PERSISTENT ALIASES

要让别名永久生效，需将其添加到 shell 配置中。

**Bash**
> ~/.bashrc 或 ~/.bash_aliases

**Zsh**
> ~/.zshrc 或 ~/.zsh_aliases

**Fish**
> 使用 **alias --save** 或编辑 ~/.config/fish/config.fish

# HISTORY

**alias** 命令自 **1970 年代**末期的 C shell（csh）起就是 Unix shell 的特性。后来 Bash、Zsh 及大多数现代 shell 都采用了语法类似的版本。

# SEE ALSO

[unalias](/man/unalias)(1), [type](/man/type)(1), [function](/man/function)(1)
