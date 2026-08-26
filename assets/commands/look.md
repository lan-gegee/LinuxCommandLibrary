# TAGLINE

使用二分查找在已排序文件中查找以给定前缀开头的行

# TLDR

查找**以指定前缀开头**的行

```look [prefix] [path/to/file]```

仅按字母数字进行**不区分大小写**的搜索

```look -f -d [prefix] [path/to/file]```

指定**终止字符**

```look -t [char] [prefix] [path/to/file]```

在**系统字典**中搜索

```look [prefix]```

# SYNOPSIS

**look** [_options_] _string_ [_file_ ...]

# DESCRIPTION

**look** 使用二分查找在已排序文件中查找以给定前缀开头的行。若未提供文件参数，则搜索系统字典（/usr/share/dict/words），并自动采用不区分大小写、仅比较字母数字的方式。

# PARAMETERS

**-f, --ignore-case**
> 忽略字母字符的大小写

**-d, --alphanum**
> 仅比较字母数字字符（字典顺序）

**-t, --terminate CHAR**
> 指定字符串终止字符；仅比较前缀中直到第一次出现 CHAR（含）为止的字符

# CAVEATS

要求输入文件已排序。为获得正确结果，文件必须以 LC_COLLATE 设为 'C' 的方式排序，因为 look 不按当前 locale 的排序规则进行比较。未指定文件时，会隐式应用 -f 和 -d。找到匹配行时退出码为 0，未找到时为 1，出错时大于 1。

# INSTALL

```apt: sudo apt install bsdextrautils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [sort](/man/sort)(1), [spell](/man/spell)(1)
