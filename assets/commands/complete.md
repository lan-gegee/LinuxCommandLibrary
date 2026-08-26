# TAGLINE

指定 bash 命令参数的补全方式

# TLDR

**以文件补全**

```complete -f [command]```

**以目录补全**

```complete -d [command]```

**以单词列表补全**

```complete -W '[start stop restart]' [myservice]```

**使用函数补全**

```complete -F [_my_completion] [mycommand]```

**移除补全规则**

```complete -r [command]```

**列出所有补全规则**

```complete -p```

**补全后不追加空格**

```complete -o nospace -W '[opt1 opt2]' [command]```

# SYNOPSIS

**complete** [_options_] [_name_...]

# DESCRIPTION

**complete** 用于指定命令参数应如何补全。它是 Bash 内建命令，服务于可编程补全机制，可为命令定义补全规范（compspec）。

# PARAMETERS

**-a**
> 以别名补全

**-b**
> 以内建命令补全

**-c**
> 以命令补全

**-d**
> 以目录补全

**-f**
> 以文件补全

**-g**
> 以组补全

**-j**
> 以作业补全

**-k**
> 以关键字补全

**-s**
> 以服务补全

**-u**
> 以用户补全

**-v**
> 以变量补全

**-A** _action_
> 使用指定动作进行补全

**-W** _wordlist_
> 从单词列表补全

**-F** _function_
> 调用 shell 函数生成补全

**-C** _command_
> 运行命令获取补全

**-G** _pattern_
> 用于文件的 glob 模式

**-X** _pattern_
> 过滤掉匹配的模式

**-P** _prefix_
> 为结果添加前缀

**-S** _suffix_
> 为结果添加后缀

**-p**
> 打印当前补全规则

**-r**
> 移除补全规范

# COMP-OPTIONS (-o)

**filenames**: 视为文件名处理（添加斜杠、加引号）

**nospace**: 补全后不追加空格

**nosort**: 不按字母顺序排序

**bashdefault**: 回退到 bash 默认补全

**default**: 回退到 readline 默认补全

# CAVEATS

仅为 Bash 内建命令。补全规则按会话存储。需要持久化的补全请放入 /etc/bash_completion.d/。

# SEE ALSO

[compgen](/man/compgen)(1), [bash](/man/bash)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/bash.git)```

```[Documentation](https://www.gnu.org/software/bash/manual/)```

<!-- verified: 2026-06-22 -->
