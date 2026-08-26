# TAGLINE

在 bash 中生成补全候选

# TLDR

**列出所有命令**

```compgen -c```

**列出以指定前缀开头的命令**

```compgen -c [ls]```

**列出所有别名**

```compgen -a```

**列出所有 shell 函数**

```compgen -A function```

**列出所有内建命令**

```compgen -b```

**列出所有变量**

```compgen -v```

**从单词列表生成补全**

```compgen -W '[start stop restart]' -- [sta]```

**列出所有用户**

```compgen -u```

# SYNOPSIS

**compgen** [_options_] [_word_]

# DESCRIPTION

**compgen** 是一个 Bash 内建命令，为某个单词生成可能的补全候选。它主要用于可编程补全函数中，但也可在交互时用来发现可用的命令、函数、变量及其他 shell 对象。给定单词参数时，只显示以该单词开头的匹配项。

# PARAMETERS

**-a**
> 生成别名名称。

**-b**
> 生成 shell 内建命令名称。

**-c**
> 生成命令名称（内建命令、函数以及 PATH 上的可执行文件）。

**-d**
> 生成目录名称。

**-e**
> 生成已导出的 shell 变量名称。

**-f**
> 生成文件名。

**-g**
> 生成组名称。

**-j**
> 生成作业名称。

**-k**
> 生成 shell 保留字（关键字）。

**-s**
> 生成服务名称。

**-u**
> 生成用户名。

**-v**
> 生成 shell 变量名称。

**-A** _action_
> 按给定的动作生成补全。有效动作包括：alias、arrayvar、binding、builtin、command、directory、disabled、enabled、export、file、function、group、hostname、job、keyword、running、service、setopt、signal、stopped、user、variable。

**-F** _function_
> 调用 shell 函数来生成补全。

**-C** _command_
> 在子 shell 中运行命令并将其输出作为补全。

**-W** _wordlist_
> 按 IFS 分割单词列表并从中生成匹配项。

**-G** _pattern_
> 展开 glob 模式并将结果作为补全。

**-P** _prefix_
> 为每个生成的补全添加前缀。

**-S** _suffix_
> 为每个生成的补全追加后缀。

**-X** _pattern_
> 使用模式过滤补全；前导 **!** 表示取反过滤。

# CAVEATS

仅为 Bash 内建命令，其他 shell 中不可用。除非选项无效或没有匹配项，否则返回真。通常在补全脚本中与 complete 内建命令配合使用。

# SEE ALSO

[complete](/man/complete)(1), [bash](/man/bash)(1)
