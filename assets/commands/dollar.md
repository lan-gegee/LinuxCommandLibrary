# TAGLINE

Shell 中用于变量和命令的展开运算符

# TLDR

**引用变量**

```echo $[VARIABLE]```

**命令替换**

```result=$(command)```

**算术展开**

```echo $((1 + 2))```

**带默认值的参数展开**

```echo ${VAR:-[default]}```

**字符串长度**

```echo ${#VAR}```

# SYNOPSIS

**$**_name_
**${**_name_**}**
**$(**_command_**)**
**$((**_expression_**))**

# PARAMETERS

**${var}**
> 变量的值。

**${var:-default}**
> 若 var 未设置或为空，则使用 default。

**${var:=default}**
> 若 var 未设置或为空，则为其赋值 default。

**${var:+alternate}**
> 若 var 已设置，则使用 alternate。

**${var:?error}**
> 若 var 未设置，则以错误消息退出。

**${#var}**
> var 的字符串长度。

**${var%pattern}**
> 删除最短的后缀匹配。

**${var%%pattern}**
> 删除最长的后缀匹配。

**${var#pattern}**
> 删除最短的前缀匹配。

**${var##pattern}**
> 删除最长的前缀匹配。

**${var/old/new}**
> 将第一个 old 替换为 new。

**${var//old/new}**
> 将所有 old 替换为 new。

**${var:offset:length}**
> 提取子串。

**$?**
> 上一条命令的退出状态。

**$$**
> 当前 Shell 的 PID。

**$!**
> 最后一个后台任务的 PID。

**$0**
> 脚本或 Shell 的名称。

**$1**-**$9**
> 位置参数。

**$@**
> 作为独立单词的全部位置参数。

**$***
> 作为单个单词的全部位置参数。

**$#**
> 位置参数的数量。

# DESCRIPTION

**$** 是 Shell 中用于变量、命令和算术的展开运算符。它会在命令执行前触发值的替换。

变量展开 **$VAR** 或 **${VAR}** 用于取得变量的值。花括号形式支持各种修饰符，访问数组和复杂展开时必须使用。

命令替换 **$(command)** 会执行命令并将其输出替换进来。它取代了较旧的反引号语法。

算术展开 **$((expr))** 用于计算数学表达式。

# CAVEATS

未经引号包裹的展开会经历单词拆分和 glob 展开。除非你明确想要拆分，否则请始终写成 **"$var"**。

**$*** 与 **$@** 在引号内行为不同：**"$@"** 保留参数边界，**"$*"** 则将它们连接在一起。

命令替换会去掉输出末尾的换行符。

# INSTALL

```aur: yay -S dollar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [env](/man/env)(1), [export](/man/export)(1)
