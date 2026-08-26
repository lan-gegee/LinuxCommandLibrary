# TAGLINE

MATE 桌面的归档管理器

# TLDR

**打开**指定的归档

```engrampa [path/to/archive1.tar] [path/to/archive2.tar]```

向归档中**添加**文件并退出

```engrampa --add-to=[path/to/archive.tar] [path/to/file_or_directory]```

将归档**解压**到某个目录并退出

```engrampa --extract-to=[path/to/directory] [path/to/archive.tar]```

将归档**解压**到以各归档命名的文件夹中并退出

```engrampa --extract-here [path/to/archive.tar]```

# SYNOPSIS

**engrampa** [_options_] [_files_]

# DESCRIPTION

**engrampa** 是 MATE 桌面的归档管理器。它可以创建和解压多种格式的归档，包括 tar、zip、7z、rar 等。

它是 file-roller 针对桌面环境 MATE 的分支版本。

# PARAMETERS

**-a**, **--add-to** _archive_
> 将文件添加到指定归档并退出。

**-d**, **--add** _file_
> 添加文件，提示输入归档名，然后退出。

**-e**, **--extract-to** _folder_
> 将归档解压到指定文件夹并退出。

**-f**, **--extract**
> 解压归档，提示选择目标文件夹，然后退出。

**-h**, **--extract-here**
> 以归档名作为目标文件夹解压归档并退出。

**--default-dir** _folder_
> `--add` 和 `--extract` 命令使用的默认文件夹。

**--force**
> 创建目标文件夹时不请求确认。

# CAVEATS

MATE 桌面应用。需要针对不同归档格式的相应库。与 tar 或 zip 等专用工具相比，命令行选项有限。

# INSTALL

```apt: sudo apt install engrampa```

```dnf: sudo dnf install engrampa```

```pacman: sudo pacman -S engrampa```

```apk: sudo apk add engrampa```

```zypper: sudo zypper install engrampa```

```nix: nix profile install nixpkgs#engrampa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[file-roller](/man/file-roller)(1), [tar](/man/tar)(1), [zip](/man/zip)(1), [unzip](/man/unzip)(1), [7z](/man/7z)(1)
