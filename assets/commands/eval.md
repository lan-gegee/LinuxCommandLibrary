# TAGLINE

用于动态执行命令的 Shell 内建命令

# TLDR

**执行动态构建的**命令

```cmd="ls -la"; eval "$cmd"```

**两次展开变量**（变量间接引用）

```var="PATH"; eval "echo \$$var"```

**用动态名称设置变量**

```key="myvar"; eval "$key=hello"; echo "$myvar"```

**执行存储在变量中、带管道的**命令

```cmd="ps aux | grep bash"; eval "$cmd"```

**将 eval 与命令替换结合使用**

```eval "$(ssh-agent -s)"```

# SYNOPSIS

**eval** [_argument_...]

# PARAMETERS

_ARGUMENT_
> 要拼接并执行的参数。

# DESCRIPTION

**eval** 是一个 POSIX 特殊 shell 内建命令，它把各个参数以空格拼接起来，然后将得到的字符串作为 shell 命令读取并执行。这使得动态构建命令和对变量进行双重展开成为可能。

当命令字符串需要以编程方式构建或存储在变量中时，该命令非常有用。它还支持变量间接引用（访问名字存放在另一个变量中的变量）。一个常见的实际用法是用 `eval "$(ssh-agent -s)"` 初始化 ssh-agent。

如果没有参数或只有空参数，eval 返回退出状态 0。否则返回所执行命令的退出状态。

# CAVEATS

对不可信输入存在安全风险。由于参数会被 shell 重新解析，把用户提供的字符串交给 **eval** 在功能上等同于 C 语言中的 **system(未消毒输入)** — 它可以运行任意命令，包括通过元字符和命令替换注入的命令。引号必须按两层规划（eval 看到的一层和最终执行命令看到的一层），这让调试变得困难。如果只需要变量间接引用，优先使用数组（bash/zsh 中的 **"$cmd[@]"**）或 **printf -v**；把 **eval** 留给 **eval "$(ssh-agent -s)"** 这类输入可信的场景。

# HISTORY

**eval** 是 **IEEE Std 1003.1**（POSIX.1）定义的标准 POSIX 特殊 shell 内建命令，最早出现在原始 Bourne shell 及其所有衍生版本中，包括 bash、zsh、ksh 和 dash。它为 shell 脚本提供了重要的元编程能力。

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [exec](/man/exec)(1), [set](/man/set)(1)
