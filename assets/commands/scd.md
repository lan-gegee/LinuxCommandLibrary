# TAGLINE

具备学习能力的智能目录切换工具

# TLDR

**切换到匹配模式**的目录

```scd [pattern]```

**将目录添加**到索引

```scd -a [path/to/directory]```

**递归地将目录添加**到索引

```scd -ar [path/to/directory]```

**创建目录别名**

```scd --alias=[name]```

**删除目录别名**

```scd --unalias=[name]```

**显示详细的目录排名**

```scd -v [pattern]```

# SYNOPSIS

**scd** [_options_] [_pattern_...]

# PARAMETERS

**-a, --add**
> 将指定目录添加到目录索引。

**-r, --recursive**
> 递归应用 --add 或 --unindex。

**--alias**=_NAME_
> 为当前或指定目录创建别名，保存在 ~/.scdalias.zsh 中。

**--unalias**=_NAME_
> 删除别名定义。

**--unindex**
> 从索引中移除指定目录。

**-v, --verbose**
> 在选择菜单中显示目录排名。

**-h, --help**
> 显示帮助消息。

# DESCRIPTION

**scd** 是一个 Z shell 脚本，只需几个按键即可切换到任意目录。它会记录访问过的目录历史，作为已知路径的索引。该索引在每次 cd 命令后自动更新，也可以用 **scd -a** 手动填充。

要切换到某个目录，scd 只需要目标路径的少量片段即可与索引进行匹配。当有多个匹配项时会显示选择菜单，并优先考虑最近访问过的路径。还可以创建永久的目录别名以便即时访问。

scd 可作为 oh-my-zsh 插件使用，也可通过 shell 集成在 bash 中工作。

# CAVEATS

主要是 zsh 脚本；bash 支持需要单独配置。基于历史的学习需要时间才能积累出实用的索引。

# INSTALL

```aur: yay -S scd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cd](/man/cd)(1), [z](/man/z)(1), [autojump](/man/autojump)(1), [fasd](/man/fasd)(1)
