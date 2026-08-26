# TAGLINE

将终端描述从 terminfo 格式转换为 termcap 格式

# TLDR

**将 terminfo 转换为 termcap**

```infotocap [terminfo_file]```

**转换指定条目**

```infotocap -1 [term_name]```

**输出到文件**

```infotocap [input] > [output.cap]```

**详细输出模式**

```infotocap -v [terminfo]```

# SYNOPSIS

**infotocap** [_options_] _file_...

# PARAMETERS

_FILE_
> 要转换的 terminfo 源文件。

**-1**
> 每行一个条目。

**-v**
> 详细输出。

**-V**
> 显示版本。

**-w** _N_
> 设置输出宽度。

# DESCRIPTION

**infotocap** 将终端描述从 terminfo 格式转换为 termcap 格式。它实际上是 **tic**(1) 的一个链接，隐含了 **-C** 选项。它是 **captoinfo** 的逆操作。

该工具用于兼容需要 termcap 格式的旧应用程序。由于它内部调用 tic，因此也可以使用其他 tic 选项，如 **-1**、**-f**、**-v**、**-w** 和 **-x**。

# CAVEATS

某些 terminfo 能力没有对应的 termcap 等价物，无法转换。属于 ncurses 的一部分。对于复杂的终端描述，输出可能需要手动调整。

# HISTORY

infotocap 是 **ncurses** 的一部分，提供终端描述格式之间的转换。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[captoinfo](/man/captoinfo)(1), [tic](/man/tic)(1), [infocmp](/man/infocmp)(1)
