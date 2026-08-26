# TAGLINE

转换或删除字符

# TLDR

**转换字符**（小写转大写）

```echo "hello" | tr 'a-z' 'A-Z'```

**删除指定字符**

```echo "hello 123" | tr -d '0-9'```

**压缩重复字符**

```echo "helllo" | tr -s 'l'```

**将换行符替换为空格**

```tr '\n' ' ' < [file]```

**删除不可打印字符**

```tr -cd '[:print:]' < [file]```

**将空格转换为制表符**

```tr ' ' '\t' < [file]```

**删除指定字符以外的所有字符**

```echo "hello123" | tr -cd '0-9'```

# SYNOPSIS

**tr** [_options_] _set1_ [_set2_]

# PARAMETERS

**-d**, **--delete**
> 删除 set1 中的字符

**-s**, **--squeeze-repeats**
> 将重复出现的字符合并为单个

**-c**, **-C**, **--complement**
> 使用 set1 的补集

**-t**, **--truncate-set1**
> 将 set1 截断为与 set2 相同的长度

# CHARACTER CLASSES

**[:alnum:]**: 字母和数字
**[:alpha:]**: 字母
**[:digit:]**: 数字
**[:lower:]**: 小写字母
**[:upper:]**: 大写字母
**[:space:]**: 空白字符
**[:blank:]**: 空格和制表符
**[:print:]**: 可打印字符
**[:punct:]**: 标点符号
**[:cntrl:]**: 控制字符

# DESCRIPTION

**tr** 对标准输入中的字符进行转换、删除或压缩，并将结果写入标准输出。它逐字符操作，因此执行简单转换非常高效。

转换会把 set1 中的每个字符替换为 set2 中对应位置的字符。如果 set2 更短，则重复其最后一个字符；如果更长，多出的字符会被忽略。

使用 **-d** 时，set1 中的字符会被删除。使用 **-s** 时，set1 中重复出现的字符会被压缩为单个。两者可以组合使用。

**-c** 取 set1 的补集，即"所有不在 set1 中的字符"，适合只保留特定字符的场景。

# CAVEATS

Tr 操作的是字符，而不是字符串或模式。需要基于模式的替换时，请使用 **sed** 或 **awk**。

方括号中的字符类必须使用 [:class:] 语法。不要与正则表达式 [a-z] 混淆——后者也可用，但在不同 locale 下与 [:lower:] 的含义有所不同。

Tr 只从 stdin 读取；无法直接处理文件。请使用重定向或管道。

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

[sed](/man/sed)(1), [awk](/man/awk)(1), [cut](/man/cut)(1), [iconv](/man/iconv)(1)
