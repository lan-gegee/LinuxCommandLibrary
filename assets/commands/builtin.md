# TAGLINE

直接执行 shell 内建命令

# TLDR

**运行**内建命令

```builtin cd [/path]```

**检查**命令是否为内建命令

```type cd```

# SYNOPSIS

**builtin** _command_ [_args_]

# DESCRIPTION

**builtin** 强制 shell 执行内建命令，即使存在同名的函数或别名。它是 bash 的一个内建命令，用于绕过 shell 函数和别名，访问原始的内建实现。

当函数或别名遮蔽了内建命令时，该命令很有用。

# USAGE

```bash
# Function shadows cd
cd() {
    echo "Going to $1"
    builtin cd "$1"
}

# Now 'cd' runs the function, but function uses builtin cd

# Direct builtin usage
builtin cd /tmp  # Bypasses any cd function
```

# COMMON BUILT-INS

- **cd** - 切换目录
- **echo** - 打印文本
- **read** - 读取输入
- **test** - 条件求值
- **export** - 设置环境变量
- **source** - 执行脚本
- **alias** - 创建别名
- **set** - 设置 shell 选项

# WORKFLOW

```bash
# Create function that wraps cd
cd() {
    echo "Changing to $1"
    builtin cd "$1" && ls
}

# Use the function
cd /tmp  # Prints message and lists directory

# Use built-in directly
builtin cd /tmp  # Just changes directory
```

# CAVEATS

只对 shell 内建命令有效，对外部命令无效。不同 shell（bash、zsh 等）之间行为有所差异。除非函数/别名遮蔽了内建命令，否则不需要使用它。

# HISTORY

自 **20 世纪 80 年代末**起，**builtin** 就是 bash 及其他 shell 的一部分，用于在内建命令被遮蔽时仍可访问它们。

# SEE ALSO

[command](/man/command)(1), [type](/man/type)(1)
