# TAGLINE

用 Go 编写的回收站 CLI 工具

# TLDR

**将文件移入回收站**

```gomi [file1] [file2]```

**交互式地从回收站恢复文件**

```gomi -r```

**列出回收站内容**

```gomi -l```

**永久清空回收站**

```gomi --empty```

# SYNOPSIS

**gomi** [_options_] _files_

# PARAMETERS

_FILES_
> 要移入回收站的文件或目录。

**-r**, **--restore**
> 交互式地选择并从回收站恢复文件。

**-l**, **--list**
> 列出当前回收站中的所有文件。

**--empty**
> 永久删除回收站中的所有文件。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**gomi** 是一个用 Go 编写的回收站 CLI，它把文件移入回收站目录而不是直接永久删除。它为删除文件提供撤销机制，并配有 fzf 风格的交互式模糊查找恢复界面。

该工具在 Linux 上遵循 XDG Trash 规范，在 macOS 上则与系统废纸篓集成。文件可以通过交互式恢复界面还原到原来的位置。

# CAVEATS

在清空回收站之前，被删文件仍会占用磁盘空间。其行为与永久删除文件的 `rm` 不同。跨文件系统移入回收站时可能改为复制文件而非移动。应定期清空回收站以释放空间。

# INSTALL

```brew: brew install gomi```

```nix: nix profile install nixpkgs#gomi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [trash-cli](/man/trash-cli)(1)
