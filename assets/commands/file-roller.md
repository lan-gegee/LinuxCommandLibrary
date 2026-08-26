# TAGLINE

GNOME 图形化归档管理器

# TLDR

**打开归档管理器**

```file-roller```

**打开指定归档**

```file-roller [archive.zip]```

**解压归档**

```file-roller --extract-here [archive.tar.gz]```

**解压到目录**

```file-roller --extract-to=[directory] [archive.zip]```

**创建新归档**

```file-roller --add [file1] [file2]```

# SYNOPSIS

**file-roller** [_options_] [_archives_...]

# PARAMETERS

_ARCHIVES_
> 要打开的归档文件。

**--extract-here**
> 解压到当前目录。

**--extract-to** _DIR_
> 解压到指定目录。

**--add** _FILES_
> 用这些文件创建归档。

**--add-to** _ARCHIVE_
> 向现有归档中添加文件。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**file-roller** 是 GNOME 的归档管理器，为创建、查看和解压归档提供图形界面。它借助命令行工具支持众多格式。

该应用与 GNOME 文件管理器集成，可以在上下文菜单中直接执行归档操作。zip、tar、gz、bz2、7z、rar 等许多格式的处理都是自动完成的。

file-roller 支持拖放操作，并会在归档操作期间显示进度。

# CAVEATS

需要 GNOME 库。格式支持情况取决于已安装的工具（unrar、p7zip 等）。命令行功能比较基础。

# HISTORY

file-roller 是 **GNOME 桌面**项目的组成部分，自 GNOME 2 起便提供归档管理功能。它是 GNOME 及基于 GNOME 的发行版的默认归档管理器。

# INSTALL

```apt: sudo apt install file-roller```

```dnf: sudo dnf install file-roller```

```pacman: sudo pacman -S file-roller```

```apk: sudo apk add file-roller```

```zypper: sudo zypper install file-roller```

```brew: brew install file-roller```

```nix: nix profile install nixpkgs#file-roller```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [zip](/man/zip)(1), [7z](/man/7z)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/file-roller)```

<!-- verified: 2026-07-15 -->
