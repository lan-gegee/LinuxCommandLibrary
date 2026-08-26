# TAGLINE

在压缩文件中搜索固定字符串

# TLDR

在 xz 文件中**搜索固定字符串**

```xzfgrep "[string]" [file.xz]```

**搜索多个字符串**

```xzfgrep -e "[str1]" -e "[str2]" [file.xz]```

**忽略大小写搜索**

```xzfgrep -i "[string]" [file.xz]```

**统计匹配行数**

```xzfgrep -c "[string]" [file.xz]```

**显示行号**

```xzfgrep -n "[string]" [file.xz]```

# SYNOPSIS

**xzfgrep** [_option..._] [_pattern_] [_file..._]

# DESCRIPTION

**xzfgrep** 在压缩文件中搜索固定字符串。它等同于 **xzgrep -F**，即模式不会被解释为正则表达式。这使得它在字面字符串搜索时比 xzgrep 更快。

压缩格式根据文件名后缀自动检测。用 xz、lzma、gzip、bzip2、lzop、zstd 或 lz4 压缩的文件会在搜索前自动解压。无法识别的后缀被视为未压缩文件。

所有选项都直接传给 grep(1)。不支持选项 **-r**、**-R**、**-d**、**-Z** 和 **-z**。

未指定文件时读取标准输入。从标准输入只支持 xz 压缩的数据。

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

[xzgrep](/man/xzgrep)(1), [xzegrep](/man/xzegrep)(1), [xz](/man/xz)(1), [fgrep](/man/fgrep)(1), [grep](/man/grep)(1), [zgrep](/man/zgrep)(1), [zfgrep](/man/zfgrep)(1)
