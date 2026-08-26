# TAGLINE

用扩展正则表达式搜索 xz 文件

# TLDR

使用扩展正则表达式**搜索** xz/lzma 文件

```xzegrep "[pattern]" [file.xz]```

**忽略大小写**搜索

```xzegrep -i "[pattern]" [file.xz]```

递归**搜索**压缩文件

```xzegrep -r "[pattern]" [directory]```

只**显示匹配的文件**而非行

```xzegrep -l "[pattern]" [*.xz]```

**显示匹配行的行号**

```xzegrep -n "[pattern]" [file.xz]```

在每个匹配周围**打印 N 行上下文**

```xzegrep -C [3] "[pattern]" [file.xz]```

# SYNOPSIS

**xzegrep** [_grep-options_] _pattern_ [_file_...]

# PARAMETERS

**-i**, **--ignore-case**
> 忽略大小写差异。

**-l**, **--files-with-matches**
> 只打印包含匹配内容的文件名。

**-n**, **--line-number**
> 在每行前加上行号。

**-c**, **--count**
> 只打印每个文件中匹配行的数量。

**-v**, **--invert-match**
> 选择不匹配的行。

**-h**, **--no-filename**
> 输出中不显示文件名前缀。

**-H**, **--with-filename**
> 始终打印文件名前缀。

**-r**, **--recursive**
> 递归搜索目录。

**-A** _N_ / **-B** _N_ / **-C** _N_
> 打印每个匹配之后 / 之前 / 前后的 N 行。

**-q**, **--quiet**
> 抑制所有正常输出；若有任意一行匹配则以退出码 0 结束。

# DESCRIPTION

**xzegrep** 对用 **xz**、**lzma**、**gzip** 或 **bzip2** 压缩（按扩展名检测）的文件的解压内容调用 **grep -E**。它是 **xz**-utils 的封装，相当于 gzip 文件对应的 **zegrep**：即 **xzgrep -E** 的便捷快捷方式，接受扩展正则表达式并将其他所有参数转发给 **grep**。

如果未给出文件，xzegrep 从标准输入读取。**grep** 接受的大多数选项都可以传递过去。

# CAVEATS

整个文件必须在内存中解压或通过管道传输，因此搜索非常大的归档并不比手动运行 **xz -dc | grep -E** 更快。在许多发行版上，**xzegrep** 正被弃用，建议改用 **xzgrep -E**。

# INSTALL

```apt: sudo apt install xz-utils```

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xzgrep](/man/xzgrep)(1), [xz](/man/xz)(1), [egrep](/man/egrep)(1), [grep](/man/grep)(1)
