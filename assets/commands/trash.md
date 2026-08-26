# TAGLINE

将文件移入可恢复的 FreeDesktop.org 回收站

# TLDR

将文件移入**回收站**

```trash [path/to/file]```

列出**回收站中的所有文件**

```trash-list```

以交互方式**从回收站恢复**文件

```trash-restore```

清空回收站

```trash-empty```

永久删除超过 **10 天**的文件

```trash-empty 10```

从回收站中**删除**匹配模式的文件

```trash-rm "*.o"```

删除具有**特定原始位置**的文件

```trash-rm /[path/to/file_or_directory]```

# SYNOPSIS

**trash** [_options_] _file_...

**trash-list**

**trash-restore**

**trash-empty** [_days_]

**trash-rm** _pattern_

# PARAMETERS

**trash** _files_
> 将文件移入回收站（别名：trash-put）

**trash-list**
> 列出回收站中的文件，包括原始路径和删除日期

**trash-restore**
> 以交互方式从回收站恢复文件

**trash-empty** [_days_]
> 清空回收站，可选择只清理超过指定天数的文件

**trash-rm** _pattern_
> 从回收站中删除匹配模式或原始路径的文件

**-d**, **--directory**
> 移除空目录

**-f**, **--force**
> 忽略不存在的文件

**-v**, **--verbose**
> 说明正在进行的操作

**--trash-dir** _dir_
> 使用指定的回收站目录而非默认位置。

**--version**
> 显示程序的版本号并退出。

# DESCRIPTION

**trash-cli** 是 FreeDesktop.org 回收站规范的命令行实现，通过将文件移动到可恢复的回收站位置而不是永久删除，提供了比 rm 更安全的替代方案。该回收站遵循 XDG 标准，并与桌面文件管理器集成。

可以使用 trash-restore 将文件恢复到原始位置，它会呈现一个可交互选择的回收站项目菜单。trash-empty 命令永久删除回收站中的项目，并支持按时间过滤。

# CAVEATS

移除外部驱动器上的文件会在该驱动器上创建 .Trash 目录。在清空回收站之前不会释放磁盘空间。视文件管理器的实现而定，通过命令行移除的文件可能不会出现在桌面回收站中。

# HISTORY

由 **Andrea Francia** 开发，是 FreeDesktop.org 回收站规范的命令行实现。它以符合 Unix 哲学的方式访问桌面回收站功能，让终端工作流中也能安全地执行删除操作。

# INSTALL

```dnf: sudo dnf install trash-cli```

```pacman: sudo pacman -S trash-cli```

```apk: sudo apk add trash-cli```

```zypper: sudo zypper install trash-cli```

```brew: brew install trash-cli```

```nix: nix profile install nixpkgs#trash-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [trash-put](/man/trash-put)(1), [trash-list](/man/trash-list)(1), [trash-restore](/man/trash-restore)(1), [trash-empty](/man/trash-empty)(1), [trash-rm](/man/trash-rm)(1), [gio-trash](/man/gio-trash)(1), [trashy](/man/trashy)(1)
