# TAGLINE

检查文件是否包含有效的 UTF-8 编码文本

# TLDR

**检查文件是否为有效 UTF-8**

```isutf8 [file]```

**检查多个文件**

```isutf8 [file1] [file2] [file3]```

**安静模式（仅返回退出码）**

```isutf8 -q [file]```

**只列出无效的文件**

```isutf8 -l [files...]```

# SYNOPSIS

**isutf8** [_options_] _file_...

# PARAMETERS

**-q**, **--quiet**
> 无输出，只有退出码。

**-l**, **--list**
> 列出不是有效 UTF-8 的文件。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**isutf8** 检查文件是否包含有效的 UTF-8 编码文本。它是 moreutils 软件包的一部分。如果为有效 UTF-8 则返回退出码 0，否则返回 1。适用于脚本中在处理文件前验证其编码。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[file](/man/file)(1), [iconv](/man/iconv)(1)
