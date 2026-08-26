# TAGLINE

在 ZIP 归档内搜索

# TLDR

**在 ZIP 中搜索**

```zipgrep [pattern] [archive.zip]```

**搜索指定文件**

```zipgrep [pattern] [archive.zip] [file.txt]```

**不区分大小写**

```zipgrep -i [pattern] [archive.zip]```

**显示行号**

```zipgrep -n [pattern] [archive.zip]```

**统计匹配数**

```zipgrep -c [pattern] [archive.zip]```

**只列出匹配的文件**

```zipgrep -l [pattern] [archive.zip]```

**搜索但排除子目录中的文件**

```zipgrep [pattern] [archive.zip] *.[ch] -x */*```

# SYNOPSIS

**zipgrep** [_egrep_options_] _pattern_ _file_[_.zip_] [_file(s)_] [**-x** _xfile(s)_]

# PARAMETERS

**-i**
> 不区分大小写。

**-n**
> 显示行号。

**-c**
> 统计匹配数。

**-l**
> 只列出文件。

**-h**
> 不带文件名前缀。

**-v**
> 反向匹配。

_pattern_
> 搜索模式。

_members_
> 归档内要搜索的特定文件。

**-x** _xfile(s)_
> 从处理中排除指定的归档成员。通配符会匹配目录分隔符。

# DESCRIPTION

**zipgrep** 在 ZIP 归档内搜索文本模式，无需手动解压。它作为 **unzip** 和 **egrep** 的 Shell 封装工作，将解压后的文件内容通过管道传给模式匹配，以类似 grep 的格式显示结果。

模式匹配通过 egrep 支持扩展正则表达式。输出会显示每个命中项的文件名和匹配行，类似于对解压内容运行 grep。可选的成员参数可将搜索限制在归档内的特定文件。

ZIP 归档文件名之前的所有选项都会传给 egrep，因此标准的 grep 选项均受支持：**-i** 不区分大小写、**-n** 显示行号、**-c** 统计匹配数、**-l** 列出匹配的文件名。如果找不到字面文件名，则会追加 .zip 后缀。zipgrep 是 Info-ZIP 工具集的一部分。

# CAVEATS

它是 unzip/egrep 的 Shell 封装。大型归档可能较慢。属于 Info-ZIP。

# HISTORY

**zipgrep** 是 **Info-ZIP** 工具的一部分。它为 ZIP 内容提供 grep 功能。

# INSTALL

```apt: sudo apt install unzip```

```dnf: sudo dnf install unzip```

```pacman: sudo pacman -S unzip```

```apk: sudo apk add unzip```

```zypper: sudo zypper install unzip```

```brew: brew install unzip```

```nix: nix profile install nixpkgs#unzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unzip](/man/unzip)(1), [grep](/man/grep)(1), [zgrep](/man/zgrep)(1)
