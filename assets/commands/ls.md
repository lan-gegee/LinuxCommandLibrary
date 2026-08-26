# TAGLINE

列出目录内容

# TLDR

**列出文件**

```ls```

**以详细信息列出**

```ls -l```

**列出全部，包括隐藏文件**

```ls -la```

**以人类可读格式显示大小**

```ls -lh```

**按时间排序**

```ls -lt```

**按大小排序**

```ls -lS```

**递归列出**

```ls -R```

# SYNOPSIS

**ls** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要列出的文件或目录。

**-l**
> 长列表格式。

**-a**
> 包含隐藏文件。

**-h**
> 以人类可读的格式显示大小。

**-t**
> 按修改时间排序。

**-S**
> 按大小排序。

**-R**
> 递归列出。

**-r**
> 反转排序顺序。

**-1**
> 每行一个文件。

**-d**
> 列出目录本身而非其内容。

**--color** _WHEN_
> 为输出着色（auto、always、never）。

**-i**
> 打印 inode 编号。

**-F**, **--classify**
> 追加类型指示符（/ 表示目录，* 表示可执行文件）。

# DESCRIPTION

**ls** 列出目录内容。不带参数时，列出当前目录。使用 **-l** 时，会显示每个条目的权限、所有者、大小和修改时间。

条目默认按字母顺序排序。可用 **-t**（时间）、**-S**（大小）或 **-r**（逆序）改变排序方式。**--color** 选项按文件类型着色高亮（目录、可执行文件、符号链接）。

# CAVEATS

输出因实现而异。颜色需要终端支持。隐藏文件以点号开头。

# HISTORY

ls 可追溯到 1971 年 AT&T 贝尔实验室最初的 **Unix** 系统，至今仍是基础命令之一。

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

[dir](/man/dir)(1), [exa](/man/exa)(1), [lsd](/man/lsd)(1), [tree](/man/tree)(1)
