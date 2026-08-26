# TAGLINE

Shell 内建的文本输出命令

# TLDR

**打印文本（zsh/ksh）**

```print "Hello, World!"```

**打印但不换行**

```print -n "text"```

**打印到文件描述符**

```print -u [2] "Error message"```

**处理转义序列打印**

```print "Line1\nLine2"```

# SYNOPSIS

**print** [_options_] [_args_]

# PARAMETERS

_ARGS_
> 要打印的文本。

**-n**
> 不输出末尾换行符。

**-r**
> 忽略 echo 的转义约定（原始输出）。

**-R**
> BSD 风格的 echo；仅配合 **-e** 时才处理转义序列。

**-u** _N_
> 打印到文件描述符 N（例如 -u2 表示 stderr）。

**-l**
> 每个参数单独占一行打印。

**-N**
> 用 null 字节分隔并终止各参数。

**-f** _format_
> 使用 printf 风格的格式字符串格式化参数。

**-P**（zsh）
> 对参数执行提示符展开。

**-s**（zsh）
> 将参数保存到历史列表而不打印。

**-v** _name_（zsh）
> 将输出存储到参数 _name_ 中而不打印。

**-c**（zsh）
> 按列打印参数。

# DESCRIPTION

**print** 是 ksh 和 zsh 中可用的 shell 内建命令，将文本输出到 stdout。它比 **echo** 提供更多控制，支持转义序列处理、输出到特定文件描述符以及禁止末尾换行。

**-u** 选项将输出定向到带编号的文件描述符（适用于写入 stderr 或其他已打开的描述符），而 **-l** 将每个参数单独打印在一行上。与 echo 不同，print 的行为是一致的，不会受到看起来像选项的参数值的影响。

# CAVEATS

Shell 内建命令。bash 中不可用（请使用 printf）。

# HISTORY

print 是用于文本输出的 **ksh/zsh 内建命令**。

# SEE ALSO

[echo](/man/echo)(1), [printf](/man/printf)(1)
