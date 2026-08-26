# TAGLINE

安排文件从仓库中移除

# TLDR

**移除文件**

```hg remove [file]```

**强制移除**

```hg remove -f [file]```

**删除后记录移除**

```hg remove -A```

**移除目录**

```hg remove [directory]```

**试运行**

```hg remove -n [file]```

# SYNOPSIS

**hg remove** [_options_] _files_

# PARAMETERS

_FILES_
> 要移除的文件。

**-f**, **--force**
> 即使文件已修改也强制移除。

**-A**, **--after**
> 记录移除已经从文件系统消失的文件。

**-I**, **--include** _PATTERN_
> 包含模式。

**-X**, **--exclude** _PATTERN_
> 排除模式。

**-n**, **--dry-run**
> 显示将要执行的操作。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hg remove** 安排文件从仓库中移除。这些文件会从工作目录中删除，并在下一次提交时被标记为移除。

-A 标志用于记录那些已经从文件系统中删除的文件的移除。force 选项可移除已修改的文件。

# CAVEATS

移除操作需要提交才生效。历史会被保留。若只是取消跟踪，请使用 forget。

# HISTORY

remove 是 **Mercurial** 自 1.0 版本以来管理被跟踪文件的核心命令。

# INSTALL

```apt: sudo apt install mercurial```

```dnf: sudo dnf install mercurial```

```pacman: sudo pacman -S mercurial```

```apk: sudo apk add mercurial```

```zypper: sudo zypper install mercurial```

```brew: brew install mercurial```

```nix: nix profile install nixpkgs#mercurial```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hg](/man/hg)(1), [hg-add](/man/hg-add)(1)
