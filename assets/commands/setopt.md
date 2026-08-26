# TAGLINE

启用 zsh shell 选项

# TLDR

在 zsh 中**启用一个选项**

```setopt [autocd]```

**启用多个选项**

```setopt [autocd] [extendedglob] [noclobber]```

使用大写命名方式**启用一个选项**

```setopt AUTO_CD```

**列出当前已设置的所有选项**

```setopt```

**启用匹配某个模式的选项**

```setopt -m '[a-z]*glob*'```

通过添加 NO 前缀**禁用一个选项**

```setopt noautocd```

# SYNOPSIS

**setopt** [**-m**] [_option_ ...]

# PARAMETERS

**-m**
> 将参数视为模式，并设置所有匹配这些模式的选项。模式应加引号以防止文件名展开。

# DESCRIPTION

**setopt** 是 zsh 的 shell 内建命令，用于启用 shell 选项。这些选项控制 shell 行为的多个方面，包括命令补全、glob 展开、历史记录以及与其他 shell 的兼容性。

选项名不区分大小写并忽略下划线，因此 **AUTO_CD**、**autocd** 和 **auto_cd** 都指向同一个选项。选项可以通过添加 **no** 前缀来取反（例如 **noautocd** 禁用 autocd 选项）。

不带参数调用时，setopt 列出当前设置的所有选项。命令 **unsetopt** 执行相反操作，即禁用选项。

# COMMON OPTIONS

**autocd**
> 直接输入目录名即可切换目录，无需 cd。

**extendedglob**
> 启用扩展的模式匹配运算符。

**noclobber**
> 防止 > 重定向覆盖已有文件。

**histignorealldups**
> 从历史记录中移除较旧的重复条目。

**sharehistory**
> 在所有运行中的 zsh 会话之间共享命令历史。

**correct**
> 尝试纠正命令的拼写。

**autopushd**
> 让 cd 将旧目录压入目录栈。

**promptsubst**
> 在提示符中启用参数和命令替换。

# CAVEATS

与 **set -o** 不同，错误的选项名不会中止后续 shell 代码的执行。这是因为 **set** 是 POSIX 特殊内建命令而 **setopt** 不是。用 setopt 设置的选项只影响当前 shell 会话，除非将其加入 **.zshrc** 以持久保存。

# HISTORY

**setopt** 自 zsh 早期开发以来就是其一部分。Zsh 由 Paul Falstad 于 **1990** 年在普林斯顿大学就读期间创建。丰富的选项系统是 zsh 区别于其他 shell 的特色之一，它提供对 shell 行为的细粒度控制，并为 sh、ksh 和 csh 提供兼容模式。

# SEE ALSO

[unsetopt](/man/unsetopt)(1), [zsh](/man/zsh)(1), [set](/man/set)(1)
