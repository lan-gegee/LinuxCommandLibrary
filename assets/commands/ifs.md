# TAGLINE

控制分词的 Shell 变量

# TLDR

**设置字段分隔符**

```IFS=':' read -ra arr <<< "a:b:c"```

**按换行符分割**

```IFS=$'\n'```

**保存并恢复 IFS**

```OLD_IFS="$IFS"; IFS=','; ...; IFS="$OLD_IFS"```

**默认 IFS**

```IFS=$' \t\n'```

# SYNOPSIS

**IFS** is a shell variable

# PARAMETERS

**IFS**
> 内部字段分隔符（Internal Field Separator）变量。

# DESCRIPTION

**IFS**（Internal Field Separator，内部字段分隔符）是一个控制分词的 Shell 变量。它定义了用于将字符串拆分为字段的字符。

默认 IFS 为空格、制表符和换行符。修改 IFS 会影响 read、for 循环以及分词行为。

# CAVEATS

是 Shell 变量而非命令。全局影响分词行为。用完后要恢复。

# HISTORY

IFS 是标准的 **POSIX shell** 变量，存在于所有与 Bourne 兼容的 Shell 中。

# SEE ALSO

[read](/man/read)(1), [bash](/man/bash)(1), [sh](/man/sh)(1)
