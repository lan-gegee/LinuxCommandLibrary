# TAGLINE

取消跟踪文件但不删除它们

# TLDR

**忘记文件**

```fossil forget [file]```

**忘记多个文件**

```fossil forget [file1] [file2]```

**以 dry run 方式忘记**

```fossil forget --dry-run [file]```

# SYNOPSIS

**fossil** **forget** [_options_] _file_...

# PARAMETERS

**--dry-run**
> 显示将被忘记的内容。

# DESCRIPTION

**fossil forget** 将文件从源代码控制中移除，但把它们留在工作目录中。当你误添加了文件、想取消跟踪而不删除它们时，这很有用。

与 **fossil rm** 或 **fossil delete** 不同，被忘记的文件在磁盘上原样保留。该命令只影响暂存区，移除尚未提交文件的计划添加。

# INSTALL

```apt: sudo apt install fossil```

```dnf: sudo dnf install fossil```

```pacman: sudo pacman -S fossil```

```apk: sudo apk add fossil```

```zypper: sudo zypper install fossil```

```brew: brew install fossil```

```nix: nix profile install nixpkgs#fossil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fossil-rm](/man/fossil-rm)(1), [fossil-add](/man/fossil-add)(1)

# RESOURCES

```[Homepage](https://fossil-scm.org/)```

```[Documentation](https://fossil-scm.org/home/help?cmd=forget)```

<!-- verified: 2026-07-15 -->
