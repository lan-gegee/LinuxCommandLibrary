# TAGLINE

安排文件移除

# TLDR

**移除文件**

```fossil rm [file]```

**强制移除**

```fossil rm -f [file]```

**以 dry run 方式移除**

```fossil rm --dry-run [file]```

# SYNOPSIS

**fossil** **rm** [_options_] _file_...

# PARAMETERS

**--dry-run**
> 显示将被移除的内容。

**-f**, **--force**
> 强制移除。

**--hard**
> 同时从磁盘删除。

# DESCRIPTION

**fossil rm** 安排文件在下次提交时从仓库中移除。默认情况下文件保留在磁盘上，只是从版本控制中移除。

**--hard** 选项会同时从仓库和文件系统中删除文件。这适合在清理不需要的文件的同时将其从版本控制中移除。

与只对尚未提交文件生效的 **fossil forget** 不同，**fossil rm** 处理的是已在仓库中被跟踪的文件。

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

[fossil-add](/man/fossil-add)(1), [fossil-forget](/man/fossil-forget)(1)

# RESOURCES

```[Homepage](https://fossil-scm.org/)```

```[Documentation](https://fossil-scm.org/home/help?cmd=rm)```

<!-- verified: 2026-07-15 -->
