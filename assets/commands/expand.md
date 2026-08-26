# TAGLINE

将文本文件中的制表符转换为空格

# TLDR

**将制表符转换为**空格

```expand [file.txt]```

**设置制表符宽度**

```expand -t [4] [file.txt]```

**自定义制表位**

```expand -t [4,8,12] [file.txt]```

**处理多个文件**

```expand [file1.txt] [file2.txt]```

**仅转换行首制表符**

```expand -i [file.txt]```

**从 stdin 读取**

```cat [file.txt] | expand```

# SYNOPSIS

**expand** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要处理的文件（未指定则读取 stdin）。

**-t** _N_
> 制表符宽度（默认：8）。

**-t** _LIST_
> 以逗号分隔的制表位位置。最后一个值可以加 `/` 前缀表示重复间隔，或加 `+` 前缀表示相对对齐。

**-i**, **--initial**
> 仅转换每行非空白字符之前的制表符。

**--help**
> 显示帮助信息。

**--version**
> 输出版本信息并退出。

# DESCRIPTION

**expand** 将制表符转换为空格。常用于规范化文本文件以获得一致的显示效果，或在使用对制表符处理不佳的工具之前进行预处理。

默认情况下，制表符按 8 个空格的间隔展开。可以设置自定义制表宽度或特定的制表位位置。--initial 选项只转换行首的制表符。

expand 是 unexpand 的逆操作，后者将空格转换为制表符。

# CAVEATS

如果重定向输出，会永久改变文件内容。制表符的解释与上下文相关。二进制文件可能被损坏。原始制表符无法恢复。

# HISTORY

expand 是早期 BSD 发行版中的经典 Unix 工具，为文本处理管道提供制表符到空格的转换。

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

[unexpand](/man/unexpand)(1), [col](/man/col)(1), [pr](/man/pr)(1)
