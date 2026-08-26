# TAGLINE

将文件移入回收站而不是永久删除

# TLDR

将指定文件移入**回收站**

```gio trash [path/to/file_or_directory1] [path/to/file_or_directory2] ...```

**列出**回收站中的项目

```gio trash --list```

将指定项目从回收站**恢复**到原位置

```gio trash --restore trash:///[original/path/to/file]```

永久**清空**回收站

```gio trash --empty```

# SYNOPSIS

**gio trash** [_options_] [_file_...]

# PARAMETERS

**--list**
> 列出回收站中的项目

**--empty**
> 永久清空回收站。

**--restore**
> 将文件从回收站恢复到原位置。需要提供以 trash:// 开头的 URI。如果原目录不存在，将会重新创建。

**-f**, **--force**
> 忽略不存在的和不可删除的文件。

# DESCRIPTION

**gio trash** 遵循 FreeDesktop.org 回收站规范，将文件移入回收站而不是永久删除。文件被放置在 **~/.local/share/Trash/** 中，并附带用于恢复的元数据。

它相当于命令行版的"把文件拖入 GNOME 文件（Nautilus）的回收站"。被删除的文件可以在文件管理器的回收站位置查看，或用 **gio trash --list** 列出。来自外部驱动器的文件会被放入该驱动器上的 .Trash-UID 目录。

# CAVEATS

回收站存储是按文件系统划分的；当某个文件系统已满时，从其中删除文件到回收站可能失败。非常大的文件在被清空之前会一直占用磁盘空间。某些文件系统（如 USB 驱动器上的 FAT）可能不支持完整的回收站元数据。

# HISTORY

当 GLib 于 **2016 年**将 GVfs 工具整合进 gio 工具时，gio trash 取代了较旧的 gvfs-trash 命令。其底层的 FreeDesktop.org 回收站规范可追溯到 **2004 年**。

# INSTALL

```apt: sudo apt install libglib2.0-bin```

```dnf: sudo dnf install glib```

```apk: sudo apk add glib```

```brew: brew install glib```

```nix: nix profile install nixpkgs#glib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gio](/man/gio)(1), [rm](/man/rm)(1), [trash-cli](/man/trash-cli)(1), [trash-put](/man/trash-put)(1), [trash-restore](/man/trash-restore)(1), [trash-empty](/man/trash-empty)(1)
