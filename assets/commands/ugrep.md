# TAGLINE

超快速的 grep，支持交互式查询模式

# TLDR

**搜索模式**

```ugrep "[pattern]" [file]```

**递归搜索**

```ugrep -r "[pattern]"```

**交互模式**

```ugrep -Q "[pattern]"```

**搜索归档文件**

```ugrep -z "[pattern]" [archive.zip]```

**布尔查询**

```ugrep "[word1] AND [word2]"```

**模糊匹配**

```ugrep -Z "[pattern]" [file]```

# SYNOPSIS

**ugrep** [_-r_] [_-Q_] [_-z_] [_-Z_] [_options_] _pattern_ [_files_]

# PARAMETERS

**-r**
> 递归搜索。

**-Q**
> 交互式 TUI。

**-z**
> 搜索归档文件。

**-Z**
> 模糊匹配。

**-i**
> 不区分大小写。

**--bool**
> 布尔查询。

# DESCRIPTION

**ugrep** 是一款高性能文本搜索工具，设计为 grep 的现代替代品，具备扩展能力。它提供带实时结果的交互式查询模式、布尔搜索运算符（AND、OR、NOT）、近似模式的模糊匹配，以及搜索压缩归档和二进制文件内部内容的能力。

该工具与 grep 兼容，支持 POSIX、Perl 和固定字符串模式语法。它可以按文件类型过滤递归搜索目录、以包括 JSON 和 CSV 在内的多种格式输出结果，并显示匹配项周围的上下文。

归档搜索可透明地处理 ZIP、tar、gzip、bzip2 及其他压缩格式。交互式查询界面（通过 **ug** 别名调用）允许实时调整搜索条件。

# CAVEATS

与 grep 不同。功能更多。C++ 实现。

# HISTORY

**ugrep** 被开发为一个快速、功能丰富的 grep 替代品，具备交互式和模糊搜索能力。

# INSTALL

```apt: sudo apt install ugrep```

```dnf: sudo dnf install ugrep```

```pacman: sudo pacman -S ugrep```

```apk: sudo apk add ugrep```

```zypper: sudo zypper install ugrep```

```brew: brew install ugrep```

```nix: nix profile install nixpkgs#ugrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [rg](/man/rg)(1), [ag](/man/ag)(1)
