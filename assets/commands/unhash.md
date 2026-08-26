# TAGLINE

移除 zsh 内部哈希表中的条目

# TLDR

从命令哈希表中**移除一个命令**

```unhash [ls]```

**移除别名**（等价于 unalias）

```unhash -a [ll]```

移除 **shell 函数**

```unhash -f [my_function]```

移除**命名目录**（hash -d 条目）

```unhash -d [projects]```

移除**后缀别名**

```unhash -s [md]```

按**模式**移除条目

```unhash -m "[tmp_*]"```

# SYNOPSIS

**unhash** [**-adfms**] _name_ ...

# DESCRIPTION

**unhash** 是一个 Zsh 内建命令，用于从 shell 的某个内部哈希表中移除指定名称的条目。默认它作用于命令哈希表，该表缓存最近执行过的命令的完整路径。选项可选择其他哈希表（别名、函数、命名目录或后缀别名），而 **-m** 标志将剩余参数视为模式，一次匹配并移除多个条目。

相关的内建命令 **unalias**、**unfunction** 和 **unsetopt** 都是薄封装，它们以预设的相应标志调用 **unhash**。直接使用 **unhash** 主要适用于脚本和函数内部需要动态确定要修改的哈希表的场景。

# PARAMETERS

**-a**
> 移除普通别名或全局别名。等价于 **unalias**。

**-s**
> 移除后缀别名。

**-f**
> 移除 shell 函数。等价于 **unfunction**。

**-d**
> 移除用 **hash -d** 创建的命名目录条目。

**-m**
> 将每个 _name_ 视为模式；所选哈希表中所有匹配的条目都会被移除。模式应加引号以防止文件名展开。

# CAVEATS

仅在 **Zsh** 中可用；Bash 使用 **hash -d** 移除单个条目，没有直接的等价物。从命令哈希表中移除某个名称会强制 Zsh 在下次调用该命令时重新搜索 **$PATH**，这也是安装新二进制文件后清除过期条目的常见原因。移除全局别名时必须加引号，否则它们会在到达 **unhash** 之前被展开。

# HISTORY

**unhash** 自 **Paul Falstad** 于 **1990 年**发布的早期版本起就是 **Zsh** 的一部分。它与 **hash** 内建命令的设计相对应，但作用相反，并随着 Zsh 引入别名、命名目录和后缀别名而扩展为覆盖多个内部表。

# SEE ALSO

[hash](/man/hash)(1), [unalias](/man/unalias)(1), [unset](/man/unset)(1), [zsh](/man/zsh)(1)
