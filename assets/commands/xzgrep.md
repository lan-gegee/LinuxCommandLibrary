# TAGLINE

用 grep 搜索 xz 压缩文件

# TLDR

在 xz 压缩文件中**搜索模式**

```xzgrep "[pattern]" [file.xz]```

**忽略大小写搜索**

```xzgrep -i "[pattern]" [file.xz]```

**统计匹配行数**

```xzgrep -c "[pattern]" [file.xz]```

**随匹配内容显示行号**

```xzgrep -n "[pattern]" [file.xz]```

**列出包含匹配项的文件**

```xzgrep -l "[pattern]" [*.xz]```

**使用扩展正则表达式搜索**

```xzgrep -E "[regex_pattern]" [file.xz]```

# SYNOPSIS

**xzgrep** [_options_] _pattern_ [_files_...]

# PARAMETERS

**-i**
> 忽略大小写搜索。

**-n**
> 显示行号。

**-c**
> 统计匹配行数。

**-l**
> 只列出包含匹配内容的文件名。

**-v**
> 反向匹配（显示不匹配的行）。

**-E**
> 使用扩展正则表达式（类似 egrep）。

**-F**
> 使用固定字符串而不是正则表达式（类似 fgrep）。

**-h**
> 输出中不显示文件名前缀。

**-H**
> 始终打印文件名前缀。

# DESCRIPTION

**xzgrep** 在 xz、lzma 和 lzip 压缩文件中搜索与模式匹配的行。它会即时解压数据并传给 grep，不会在磁盘上创建临时文件。支持所有标准的 grep 选项。另有 **xzegrep** 和 **xzfgrep** 变体可用。

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

[xz](/man/xz)(1), [grep](/man/grep)(1), [zgrep](/man/zgrep)(1), [lzgrep](/man/lzgrep)(1)
