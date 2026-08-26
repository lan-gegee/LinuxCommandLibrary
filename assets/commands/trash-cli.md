# TAGLINE

FreeDesktop.org 回收站命令行工具

# TLDR

**将文件移入回收站**

```trash-put [file]```

**列出回收站中的文件**

```trash-list```

**恢复文件**

```trash-restore```

**清空回收站**

```trash-empty```

**删除超过指定天数的文件**

```trash-empty [30]```

**删除特定的回收站文件**

```trash-rm [pattern]```

# SYNOPSIS

**trash-put** _files_
**trash-list**
**trash-restore**
**trash-empty** [_days_]
**trash-rm** _pattern_

# COMMANDS

**trash-put** _FILES_
> 将文件移入回收站。

**trash-list**
> 列出回收站中的文件。

**trash-restore**
> 以交互方式恢复文件。

**trash-empty** [_N_]
> 清空回收站（或删除超过 N 天的文件）。

**trash-rm** _PATTERN_
> 删除匹配的回收站文件。

# PARAMETERS

**-d**, **--directory**
> 允许移除目录（trash-put）。

**-f**, **--force**
> 忽略不存在的文件，不打印错误消息。

**-i**
> 静默忽略不存在的文件（trash-put）。

**-v**, **--verbose**
> 说明正在进行的操作。

**--trash-dir** _DIR_
> 使用指定目录作为回收站文件夹，而非默认位置。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**trash-cli** 为 FreeDesktop.org 回收站提供命令行界面。它将文件移入回收站，而不是永久删除。

按照 freedesktop.org 规范，文件被移动到 ~/.local/share/Trash。桌面环境可以看到并恢复这些文件。

恢复是交互式的。trash-restore 会为回收站中的文件编号，你可以选择要恢复哪些文件。

清空回收站会永久删除其中的文件。按时间清空只删除旧文件，使最近的删除操作仍可撤销。

这些工具支持外部驱动器上基于文件系统的回收站。每个已挂载的文件系统都有各自的回收站目录。

将 rm 别名为 trash-put 可以获得更安全的默认行为，同时保持熟悉的语法。

# CAVEATS

回收站中的文件在被清空之前会占用磁盘空间。移入大文件会占满磁盘。在不支持回收站的文件系统上无法使用。root 的回收站是独立的。

# HISTORY

**trash-cli** 由 **Andrea Francia** 创建，旨在通过命令行访问标准的 Linux 回收站。它遵循 FreeDesktop.org Trash 规范以保证互操作性。

# INSTALL

```dnf: sudo dnf install trash-cli```

```pacman: sudo pacman -S trash-cli```

```zypper: sudo zypper install trash-cli```

```brew: brew install trash-cli```

```nix: nix profile install nixpkgs#trash-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [gio](/man/gio)(1), [gvfs-trash](/man/gvfs-trash)(1)
