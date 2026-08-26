# TAGLINE

在 lzip 压缩文件中搜索扩展正则表达式模式

# TLDR

**使用扩展正则表达式搜索**

```lzegrep [pattern] [file.lz]```

**忽略大小写搜索**

```lzegrep -i [pattern] [file.lz]```

**显示行号**

```lzegrep -n [pattern] [file.lz]```

# SYNOPSIS

**lzegrep** [_options_] _pattern_ [_file_...]

# PARAMETERS

**-i**
> 忽略大小写匹配。

**-n**
> 在每个匹配行前加上行号。

**-v**
> 反转匹配；显示不匹配的行。

**-c**
> 只打印每个文件中匹配行的数量。

**-l**
> 只打印包含匹配项的文件名。

**-h**
> 输出中不显示文件名前缀。

**-H**
> 强制在输出中显示文件名前缀。

**-e** _PATTERN_
> 使用 _PATTERN_ 作为搜索模式；适合指定多个模式。

# DESCRIPTION

**lzegrep** 在 lzip 压缩文件中搜索扩展正则表达式模式。它等价于 **lzgrep -E**，内部将解压后的数据通过管道传给 **grep -E**（或 **egrep**）。未压缩的文件会被直接搜索。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lzgrep](/man/lzgrep)(1), [egrep](/man/egrep)(1)
