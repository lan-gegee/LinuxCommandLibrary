# TAGLINE

显示命令名是如何被解释的

# TLDR

**显示命令的类型**

```type [command]```

**显示命令的所有位置**（别名、函数、内建命令、文件）

```type -a [command]```

**只显示类型**（alias、keyword、function、builtin 或 file）

```type -t [command]```

**显示可执行文件的路径**（类似 which）

```type -P [command]```

**检查命令是否为**内建命令、别名或函数

```type -t [cd]```

**仅当是磁盘上的文件时才显示路径**

```type -p [command]```

**不查找 shell 函数**

```type -f [command]```

# SYNOPSIS

**type** [**-afptP**] _name_...

# PARAMETERS

**-a**
> 显示所有包含可执行文件的位置；包括别名、内建命令和函数

**-f**
> 不查找 shell 函数

**-p**
> 仅当 type 本应返回 "file" 时返回磁盘文件路径，否则返回空

**-P**
> 即使存在别名、内建命令或函数，也强制搜索 PATH

**-t**
> 输出单个单词：alias、keyword、function、builtin、file 或空

# DESCRIPTION

**type** 是一个 Shell 内建命令，用于显示命令名会被如何解释。它能判断某个名字是别名、Shell 关键字、函数、内建命令还是外部可执行文件。

不带选项时，type 会打印一条描述性消息，说明命令的类型和位置。使用 **-t** 时，它只输出表示类型类别的单个单词，便于在脚本中使用。

**-a** 选项显示某个名字的所有解释，揭示是否存在多个同名命令（例如别名遮蔽了可执行文件）。**-P** 选项强制进行 PATH 搜索，即使存在别名或函数也能找到可执行文件。

type 比 **which** 信息更丰富，因为它理解 Shell 内部机制（如别名、函数和内建命令），而不仅仅是 PATH 中的文件。

# EXIT STATUS

**0**
> 所有名字都被找到

**1**
> 有一个或多个名字未找到

# EXAMPLES

**识别命令类型**
```
$ type ls
ls is aliased to `ls --color=auto'

$ type cd
cd is a shell builtin

$ type -t for
keyword
```

# CAVEATS

type 是 Shell 内建命令，其行为在不同 Shell（bash、zsh 等）之间可能略有差异。为了 POSIX 兼容性，请改用 **command -v**。**-a** 选项包含的别名只在交互式 Shell 中存在。

# HISTORY

自早期 Unix 的 Bourne shell 起，**type** 命令就一直是 Shell 内建命令。它的设计目的是帮助用户理解命令解析过程——当 Shell 引入可能遮蔽可执行文件的别名和函数等特性后，这一点尤为重要。该命令已由 POSIX 规定。

# SEE ALSO

[which](/man/which)(1), [whence](/man/whence)(1), [command](/man/command)(1), [whereis](/man/whereis)(1), [bash](/man/bash)(1)
