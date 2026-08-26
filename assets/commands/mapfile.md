# TAGLINE

从标准输入读取行到 bash 数组

# TLDR

**将文件读入数组**

```mapfile [array] < [file.txt]```

**按行数限制读取**

```mapfile -n [10] [array] < [file.txt]```

**跳过前 N 行**

```mapfile -s [2] [array] < [file.txt]```

**移除末尾换行符**

```mapfile -t [array] < [file.txt]```

**使用指定分隔符**

```mapfile -d ':' [array] < [file.txt]```

**从命令读取**

```mapfile [array] < <(ls)```

# SYNOPSIS

**mapfile** [_options_] [_array_]

# PARAMETERS

_ARRAY_
> 数组变量名。

**-n** _COUNT_
> 最大读取行数。

**-s** _COUNT_
> 要跳过的行数。

**-t**
> 移除末尾的分隔符。

**-d** _DELIM_
> 使用指定分隔符代替换行符（bash 4.4+）。

**-O** _ORIGIN_
> 从数组索引 ORIGIN 处开始赋值（默认：0）。

**-u** _FD_
> 从文件描述符 FD 读取而不是标准输入。

**-C** _CALLBACK_
> 每读取一批（quantum）行后求值 CALLBACK。

**-c** _QUANTUM_
> 每次 CALLBACK 调用之间的行数（默认：5000）。

# DESCRIPTION

**mapfile**（又名 **readarray**）是 bash 的内建命令，它从标准输入读取行并写入一个索引数组变量。不指定变量名时，使用默认数组 `MAPFILE`。

与 `while read` 循环相比，把文件读入数组时它的速度显著更快，因为它是内建实现，而不是在子 shell 中运行。

# CAVEATS

Bash 特有的内建命令（bash 4.0+）。在 sh 或其他 POSIX shell 中不可用。`-d` 选项需要 bash 4.4 或更高版本。无法在子 shell 上下文中从管道读取——请使用进程替换（`< <(command)`）而不是管道（`command | mapfile`）。

# HISTORY

**mapfile** 在 **Bash 4.0**（2009 年发布）中作为高效读取文件到数组的内建命令加入。`-d` 分隔符选项于 **Bash 4.4** 中加入。

# SEE ALSO

[read](/man/read)(1), [bash](/man/bash)(1)
