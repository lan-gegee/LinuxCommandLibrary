# TAGLINE

在 Shell 脚本中求值条件表达式

# TLDR

**测试条件（test 的同义词）**

```[ -f [file] ] && echo "exists"```

**字符串比较**

```[ "[string1]" = "[string2]" ]```

**数值比较**

```[ [5] -gt [3] ]```

**文件测试**

```[ -d [directory] ] && echo "is directory"```

**组合多个条件**

```[ -f [file] ] && [ -r [file] ]```

# SYNOPSIS

**[** _expression_ **]**

# FILE TESTS

**-e** _file_：文件存在
**-f** _file_：普通文件
**-d** _file_：目录
**-r** _file_：可读
**-w** _file_：可写
**-x** _file_：可执行
**-s** _file_：大小 > 0
**-L** _file_：符号链接

# STRING TESTS

**-z** _string_：长度为零
**-n** _string_：长度非零
_s1_ **=** _s2_：字符串相等
_s1_ **!=** _s2_：字符串不相等

# NUMERIC TESTS

_n1_ **-eq** _n2_：等于
_n1_ **-ne** _n2_：不等于
_n1_ **-lt** _n2_：小于
_n1_ **-le** _n2_：小于或等于
_n1_ **-gt** _n2_：大于
_n1_ **-ge** _n2_：大于或等于

# DESCRIPTION

**[** 是用于求值条件表达式的 POSIX test 命令。它等价于 **test**，但要求以 **]** 结尾。**[** 和 **]** 周围的空格是必需的。

该命令返回退出状态 0（真）或 1（假），用于 if 语句和条件执行。

```bash
if [ -f "$file" ]; then
    echo "File exists"
fi

[ -d "$dir" ] && cd "$dir"
```

在 bash/zsh 中，**[[** 提供了支持模式匹配且语法更安全的增强版本。

# CAVEATS

**[** 是一个命令，不是语法。必须使用空格：应写成 **[ "$a" = "$b" ]** 而不是 **["$a"="$b"]**。

务必给变量加引号，如 **[ "$var" = "test" ]**，以正确处理空值和空格。

用 **-a** 和 **-o** 表示与/或，或者在方括号外结合 **&&** 和 **||** 使用。

**=** 比较字符串，**-eq** 比较数字：**[ "01" = "1" ]** 为假，而 **[ 01 -eq 1 ]** 为真。

# HISTORY

**[**（即 test）是最早的一批 Unix 命令之一，由 POSIX.1 规定。**[[** 增强版本由 **ksh88** 引入，随后被 bash 和 zsh 采用。

# INSTALL

```aur: yay -S bracket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[test](/man/test)(1), [bash](/man/bash)(1), [sh](/man/sh)(1)
