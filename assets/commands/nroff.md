# TAGLINE

为终端显示排版文本

# TLDR

**排版文档**

```nroff [file.roff]```

**为终端排版**

```nroff -Tascii [file]```

**排版 man page**

```nroff -man [page.1]```

**使用宏排版**

```nroff -ms [file.ms]```

**预览输出**

```nroff [file] | less```

# SYNOPSIS

**nroff** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入文件。

**-T** _DEV_
> 输出设备。

**-man**
> 使用 man 宏。

**-ms**
> 使用 ms 宏。

**-me**
> 使用 me 宏。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nroff** 为终端显示排版文本，是 troff/groff 系统的一部分。

该工具处理 roff 文档，输出纯文本格式的排版结果。

# CAVEATS

groff 的一部分。输出到终端。如需印刷级排版输出请使用 groff。

# HISTORY

nroff 起源于 **Unix V7**，最初用于在行式打印机和终端上格式化文本。

# INSTALL

```apt: sudo apt install groff-base```

```dnf: sudo dnf install groff-base```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [troff](/man/troff)(1), [man](/man/man)(1)
