# TAGLINE

用于禁用文件名通配展开的 Zsh 前置命令修饰符

# TLDR

**安装软件包时不对通配符做 Shell 展开**

```noglob apt install linux-*```

**传递含特殊字符的 URL**而无需加引号

```noglob curl https://example.com/api?key=value&page=2```

**运行 find 时不让 Shell 展开通配模式**

```noglob find . -name *.txt```

对名称中含有类 glob 语法的**包管理器使用**

```noglob pip install package[extra]```

# SYNOPSIS

**noglob** _simple command_

# DESCRIPTION

**noglob** 是一个 zsh 前置命令修饰符，它会为紧随其后的命令中的所有单词禁用文件名生成（globbing）。使用后，像 **\***、**?** 和 **[...]** 这样的模式匹配字符将被按字面处理，而不是被展开去匹配文件名。

当你想向命令传递含有 glob 字符的参数、又不想逐个加引号时，它非常有用。常见用例包括带查询字符串的 URL、带方括号的包名，以及需要原样传递通配符的命令。

**noglob** 必须出现在任何其他前置命令修饰符之前，因为它在任何解析开始之前就会被解释。

# CAVEATS

仅在 **zsh** 中可用；不是 POSIX shell 的特性。在非交互式 Shell 中无效。在 bash 中，等价物是 **set -o noglob**（或 **set -f**），但那是全局生效而非按命令生效。不能放在其他前置命令修饰符之后组合使用——它必须位于最前面。

# HISTORY

**noglob** 自早期版本起就是 **zsh** 的一部分，源自 csh 系列的 shell。C shell（**csh**）引入了选择性禁用 globbing 的概念，zsh 将其采纳并改进为前置命令修饰符，与 **nocorrect**、**builtin**、**command** 和 **exec** 并列。

# SEE ALSO

[zsh](/man/zsh)(1), [bash](/man/bash)(1)
