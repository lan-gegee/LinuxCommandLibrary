# TAGLINE

反转每行中的字符顺序

# TLDR

**反转**输入到终端的文本（交互模式）

```rev```

**反转**文本字符串 "hello"

```echo "hello" | rev```

**反转**整个文件并输出到 stdout

```rev [path/to/file]```

**使用** '\0' 作为行分隔符（零终止）

```rev -0 [path/to/file]```

# SYNOPSIS

**rev** [_options_] [_file_...]

# PARAMETERS

**-0, --zero**
> 使用 NUL 字符而不是换行符作为行终止符

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**rev** 反转输入中每一行的字符顺序。它从命令行指定的文件读取，未给出文件时从标准输入读取。每行独立反转。

该命令适用于文本处理、创建回文效果，或处理需要颠倒字符顺序的数据。

# CAVEATS

只反转各行内部的字符；不改变行本身的顺序。多字节字符在某些语言环境下可能无法正确处理。属于 util-linux 软件包。

# HISTORY

**rev** 命令首次出现于 Version 7 Unix，此后一直是标准工具。它最初是作为一个简单的文本变换工具而创建的。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tac](/man/tac)(1), [cat](/man/cat)(1), [cut](/man/cut)(1), [tr](/man/tr)(1)
