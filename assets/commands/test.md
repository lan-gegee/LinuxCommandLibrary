# TAGLINE

求值条件表达式

# TLDR

**检查文件是否存在**

```test -e [path/to/file] && echo "exists"```

**检查文件是否为目录**

```test -d [path/to/dir] && echo "is directory"```

**检查文件是否可读**

```test -r [path/to/file] && echo "readable"```

**比较字符串是否相等**

```test "[string1]" = "[string2]"```

**检查字符串是否非空**

```test -n "[string]"```

**比较整数**

```test [5] -gt [3] && echo "greater"```

**用 AND 组合条件**

```test -f [file] -a -r [file]```

**用 OR 组合条件**

```test -f [file1] -o -f [file2]```

# SYNOPSIS

**test** _EXPRESSION_

**[** _EXPRESSION_ **]**

# FILE TESTS

**-e** _FILE_
> 文件存在时为真。

**-f** _FILE_
> 文件存在且为普通文件时为真。

**-d** _FILE_
> 文件存在且为目录时为真。

**-r** _FILE_
> 文件可读时为真。

**-w** _FILE_
> 文件可写时为真。

**-x** _FILE_
> 文件可执行时为真。

**-s** _FILE_
> 文件存在且大小大于零时为真。

**-L** _FILE_
> 文件是符号链接时为真。

**-b** _FILE_
> 文件是块设备文件时为真。

**-c** _FILE_
> 文件是字符设备文件时为真。

**-p** _FILE_
> 文件是命名管道（FIFO）时为真。

**-S** _FILE_
> 文件是套接字时为真。

**-g** _FILE_
> 文件设置了 set-group-ID 位时为真。

**-u** _FILE_
> 文件设置了 set-user-ID 位时为真。

**-O** _FILE_
> 文件由有效用户 ID 所有时为真。

_FILE1_ **-nt** _FILE2_
> FILE1 比 FILE2 新（按修改日期）时为真。

_FILE1_ **-ot** _FILE2_
> FILE1 比 FILE2 旧时为真。

_FILE1_ **-ef** _FILE2_
> FILE1 与 FILE2 指向相同的设备号和 inode 号时为真。

# STRING TESTS

**-n** _STRING_
> 字符串长度非零时为真。

**-z** _STRING_
> 字符串长度为零时为真。

_STRING1_ **=** _STRING2_
> 两字符串相等时为真。

_STRING1_ **!=** _STRING2_
> 两字符串不相等时为真。

# INTEGER COMPARISONS

_INT1_ **-eq** _INT2_
> 等于。

_INT1_ **-ne** _INT2_
> 不等于。

_INT1_ **-lt** _INT2_
> 小于。

_INT1_ **-le** _INT2_
> 小于或等于。

_INT1_ **-gt** _INT2_
> 大于。

_INT1_ **-ge** _INT2_
> 大于或等于。

# OPERATORS

**!** _EXPR_
> 表达式为假时为真。

_EXPR1_ **-a** _EXPR2_
> 两个表达式都为真时为真（AND）。

_EXPR1_ **-o** _EXPR2_
> 任一表达式为真时为真（OR）。

# DESCRIPTION

**test** 对条件表达式求值，返回退出状态 0（真）或 1（假）。它常用于 shell 脚本中，在 if 语句和循环里做判断。

该命令也可以写作 **[**，此时必须以 **]** 作为最后一个参数。这种方括号写法在条件语句中更易读：**if [ -f file ]; then**。

现代 shell 还提供 **[[**，它支持模式匹配等额外特性以及更安全的字符串处理，但不符合 POSIX 标准。

# CAVEATS

test 表达式中的变量应加引号，以正确处理空值和空格。**[** 形式要求方括号两侧有空格。为了符合 POSIX 规范，字符串比较应使用 **=** 而非 **==**。整数比较运算符（-eq、-lt）与字符串运算符不同。

# HISTORY

test 是最古老的 Unix 工具之一，可追溯到 **1979** 年的 Version 7 Unix。方括号记法 **[** 是作为别名加入的，用于提高 shell 脚本的可读性。两种形式均由 POSIX 规定，既可作为 shell 内建命令也可作为独立命令使用。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [expr](/man/expr)(1)
