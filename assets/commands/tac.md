# TAGLINE

按行的逆序输出文件

# TLDR

**反转文件**的行序

```tac [file.txt]```

**反转多个文件**的行序

```tac [file1.txt] [file2.txt]```

以自定义分隔符反转

```tac -s "[separator]" [file.txt]```

以正则表达式分隔符反转

```tac -r -s "[pattern]" [file.txt]```

**反转 stdin**

```cat [file.txt] | tac```

分隔符放在前面再反转（把分隔符附着到后一条记录）

```tac -b -s "[separator]" [file.txt]```

# SYNOPSIS

**tac** [_options_] [_file_...]

# DESCRIPTION

**tac** 连接并按逆序逐行输出文件。它的名字是 "cat" 倒着拼出来的，正对应其反向的功能。

默认情况下，tac 以换行符作为记录分隔符，从而反转行序。也可以指定自定义分隔符，因此它可用于反转各种文件格式中的记录。

该工具适合查看日志文件（最新的在前）、反转已排序的输出，或处理需要逆序的数据。

# PARAMETERS

**-b**, **--before**
> 将分隔符附着在记录之前而非之后。

**-r**, **--regex**
> 将分隔符解释为正则表达式。

**-s** _string_, **--separator=** _string_
> 使用 string 作为分隔符，替代换行符。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# CAVEATS

会将整个输入读入内存（对超大文件效率不高）。二进制文件可能产生意外的结果。正则表达式分隔符可能影响性能。不会反转行内的字符顺序。

# HISTORY

**tac** 是 **GNU coreutils** 的一部分，延续了 Unix 中"反向操作"工具的传统（例如反转字符顺序的 rev）。名字俏皮地把 "cat" 反转了过来。它提供了标准 Unix 所不具备的功能，不过某些 BSD 系统有类似的替代品。

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

[cat](/man/cat)(1), [rev](/man/rev)(1), [tail](/man/tail)(1), [head](/man/head)(1)
