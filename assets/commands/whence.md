# TAGLINE

显示命令名会被如何解释

# TLDR

**显示名称如何解析**（路径、别名或类型）

```whence [command]```

**详细的描述信息**（类似 type 或 command -V）

```whence -v [command]```

带函数体的 **csh 风格输出**（zsh；与 which 相同）

```whence -c [command]```

**只输出单词类型**：alias、builtin、command、function、hashed、reserved 或 none（zsh）

```whence -w [command]```

沿 PATH 的**所有匹配项**（及其他解释方式）

```whence -a [command]```

即使 name 是别名、函数或内建命令也**强制搜索 PATH**

```whence -p [command]```

**以 csh 格式显示所有出现位置**（zsh；与 where 相同）

```whence -ca [command]```

# SYNOPSIS

**whence** [**-afpv**] _name_...

**whence** [**-vcwfpamsS**] [**-x** _num_] _name_... (zsh)

# PARAMETERS

**-v**
> 输出更详细的报告

**-a**
> 报告所有解释 / 搜索整个命令路径（而不只是第一个匹配）

**-p**
> 即使 name 是别名、保留字、函数或内建命令，也执行 PATH 搜索

**-f**
> 跳过 shell 函数的搜索（ksh）。在 zsh 中配合 **-c** 使用时，显示 shell 函数的内容

**-c**（zsh）
> 以类似 csh 的格式打印结果（优先于 **-v**）。单独使用时等同于 zsh 的 **which** 内建命令

**-w**（zsh）
> 打印 `name: word`，其中 word 为：alias、builtin、command、function、hashed、reserved 或 none

**-m**（zsh）
> 将参数视为模式并显示匹配的命令（模式字符需加引号）

**-s**（zsh）
> 如果路径名包含符号链接，同时打印去除符号链接后的路径名

**-S**（zsh）
> 类似 **-s**，但会打印符号链接解析的中间步骤

**-x** _num_（zsh）
> 用 **-c** 输出 shell 函数时展开制表符（思路同 **functions -x**）

# DESCRIPTION

**whence** 是 **ksh** 和 **zsh** 中的 shell 内建命令，报告每个 _name_ 作为命令使用时会被如何解释。与外部的 **which** 工具不同，它理解 shell 别名、函数、内建命令、保留字和哈希过的命令，而不仅仅是 PATH 上的可执行文件。

不带选项时，**whence** 通常为外部命令打印解析出的路径，或指示别名等其他 shell 对象。**-v** 会附加描述性消息，类似 **type** 或 **command -V**。**-p** 在名称被 shell 结构遮蔽时强制进行文件系统 PATH 搜索。

在 **zsh** 中，**whence** 是多个相关内建命令的底层实现：

- **which** 等价于 **whence -c**
- **where** 等价于 **whence -ca**
- **type** 等价于 **whence -v**

**ksh** 提供的选项集较小（**-a**、**-f**、**-p**、**-v**）。**bash** 和 POSIX shell 不提供 **whence**；在这些 shell 中请改用 **type**、**command -v** 或 **command -V**。

# EXIT STATUS

**0**
> 名称已找到（被识别为 shell 能理解的命令形式）

**非零**
> 名称未被识别。在 zsh 中，针对 **-v**、**-c** 或 **-w** 的未找到消息会写入标准输出（而非标准错误），这与其他某些 shell 不同

# EXAMPLES

**在 zsh 中解析命令**

```
$ whence ls
/bin/ls

$ whence -v ls
ls is /bin/ls

$ whence -w cd
cd: builtin

$ whence -w for
for: reserved
```

**查找 PATH 上的所有匹配（zsh）**

```
$ whence -a python3
```

# CAVEATS

**whence** 不是独立程序，在 bash 或普通 sh 中不可用。需要可移植性的脚本应优先使用 **command -v**（POSIX）或 **type**。

**-m**（zsh）的模式匹配只作用于命令名的最后一段路径；请传入基名，而不是带 `/` 的完整路径。

选项字母和输出格式在 ksh 与 zsh 之间有所差异。**-c**、**-w**、**-m**、**-s** 和 **-S** 等特性是 zsh 的扩展。

# HISTORY

**whence** 起源于 KornShell（**ksh**），是该 shell 的命令查询报告器。**zsh** 采用它并在其上构建了更丰富的接口，将 **which**、**where** 和 **type** 实现为 **whence** 的变体。POSIX 未对其作规定。

# SEE ALSO

[type](/man/type)(1), [which](/man/which)(1), [command](/man/command)(1), [hash](/man/hash)(1), [whereis](/man/whereis)(1)

# RESOURCES

```[Documentation](https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html#index-whence)```

```[Source code](https://github.com/zsh-users/zsh)```

<!-- verified: 2026-08-06 -->
