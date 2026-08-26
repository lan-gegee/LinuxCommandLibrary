# TAGLINE

在 lzip 压缩文件中搜索模式

# TLDR

**在 lzip 压缩文件中搜索**

```lzgrep [pattern] [file.lz]```

**忽略大小写搜索**

```lzgrep -i [pattern] [file.lz]```

**显示行号**

```lzgrep -n [pattern] [file.lz]```

**搜索多个文件**

```lzgrep [pattern] [*.lz]```

**扩展正则表达式**

```lzegrep [pattern] [file.lz]```

# SYNOPSIS

**lzgrep** [_options_] _pattern_ [_file_...]

# PARAMETERS

**-i**
> 忽略大小写搜索。

**-n**
> 显示行号。

**-l**
> 只显示文件名。

**-c**
> 显示匹配计数。

**-v**
> 反转匹配。

支持所有 grep 选项。

# DESCRIPTION

**lzgrep** 在 lzip 压缩文件中搜索模式。它会在搜索前自动解压，并将选项透传给 grep。扩展正则表达式请用 lzegrep，固定字符串请用 lzfgrep。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lzip](/man/lzip)(1), [grep](/man/grep)(1), [zgrep](/man/zgrep)(1)
