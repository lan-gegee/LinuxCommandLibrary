# TAGLINE

管理最近执行命令哈希表的 Shell 内建命令

# TLDR

**显示命令哈希表**

```hash```

**清空哈希表**

```hash -r```

**将命令添加到哈希表**

```hash -p [/usr/local/bin/mycommand] [mycommand]```

**从哈希表中移除命令**

```hash -d [command]```

**显示命令对应的路径**

```hash -t [command]```

# SYNOPSIS

**hash** [_options_] [_name_...]

# PARAMETERS

**-r**
> 清空哈希表。

**-p** _path_ _name_
> 为 name 添加路径。

**-d** _name_
> 从哈希表中删除 name。

**-t** _name_
> 打印 name 的路径。

**-l**
> 以可复用的格式列出。

# DESCRIPTION

**hash** 是一个管理最近执行命令哈希表的 Shell 内建命令。Shell 利用该表记住命令的完整路径，避免反复搜索 PATH。

命令执行时，Shell 会将其路径存入哈希表。之后的调用直接使用缓存的路径，从而提升性能。

```bash
# View hash table
hash

# Clear after installing new software
hash -r

# Check where a command is hashed
hash -t python

# List all hashed commands
hash -l
```

# CAVEATS

这是 Shell 内建命令；行为和可用选项因 shell 而异（bash、zsh、ksh 各自实现了自己的版本）。如果被哈希的命令文件被移动或删除，哈希表就会失效。安装软件或修改 PATH 后请运行 `hash -r`。它只影响当前 shell 会话，不影响子进程。

# HISTORY

**hash** 自 Bourne shell 起就是 Unix shell 的一部分。POSIX 只强制要求 `-r` 选项；bash 在此基础上扩展了 `-p`、`-d`、`-t` 和 `-l`，用于更精细地控制命令路径缓存。

# SEE ALSO

[type](/man/type)(1), [which](/man/which)(1), [whence](/man/whence)(1), [command](/man/command)(1)

# RESOURCES

```[Documentation](https://www.gnu.org/software/bash/manual/bash.html#Bourne-Shell-Builtins)```

<!-- verified: 2026-07-17 -->
