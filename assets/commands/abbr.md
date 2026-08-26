# TAGLINE

fish shell 缩写管理器

# TLDR

**添加**一个新缩写

```abbr --add [abbreviation_name] [command] [arguments]```

**重命名**一个已有缩写

```abbr --rename [old_name] [new_name]```

**删除**一个已有缩写

```abbr --erase [abbreviation_name]```

**列出**所有缩写名

```abbr --list```

以可导出的格式**显示**所有缩写

```abbr --show```

通过 **SSH** 从其他主机导入缩写

```ssh [hostname] abbr --show | source```

# SYNOPSIS

**abbr** [_--add_] [_--erase_] [_--rename_] [_--show_] [_--list_] [_--query_] [_NAME_] [_EXPANSION_]

# DESCRIPTION

**abbr** 管理 fish shell 的缩写。缩写是用户自定义的词，在命令行输入并以空格或回车确认后展开为更长的内容。与别名这种简单的命令替换不同，缩写允许用户在执行前查看并编辑展开后的文本。

缩写只作用于交互式输入的命令，在脚本或函数中不会展开。它们可以限定为只在命令位置触发，或在行内任意位置触发，还支持正则表达式模式以及通过 shell 函数实现的动态展开。

# PARAMETERS

**--add NAME EXPANSION**
> 创建一个新缩写，将 NAME 展开为 EXPANSION

**--erase NAME**
> 移除一个或多个缩写

**--rename OLD_WORD NEW_WORD**
> 重命名一个已有缩写

**--show**
> 以适合导出的格式显示所有缩写

**--list**
> 只打印缩写名

**--query NAME**
> 检查 NAME 是否为已定义的缩写

**--position command|anywhere**
> 缩写在何处展开；默认只在命令位置展开

**--regex PATTERN**
> 使用 PCRE2 正则表达式模式而非字面文本进行匹配

**--set-cursor[=MARKER]**
> 展开后把光标定位到标记处；默认标记为 %

**--function FUNCTION**
> 使用函数输出进行动态展开，而不是静态文本

**--command COMMAND**
> 仅当作为指定命令的参数使用时才展开

# CAVEATS

缩写只对交互式输入的命令展开，在脚本或函数中无效。这是 fish shell 特有的功能，其他 shell 中不可用。

# HISTORY

属于 **fish shell**（friendly interactive shell），一个专注于易用性的现代命令行 Shell。

# SEE ALSO

[fish](/man/fish)(1), [alias](/man/alias)(1)

# RESOURCES

```[Source code](https://github.com/fish-shell/fish-shell)```

```[Homepage](https://fishshell.com)```

```[Documentation](https://fishshell.com/docs/current/cmds/abbr.html)```

<!-- verified: 2026-06-10 -->
