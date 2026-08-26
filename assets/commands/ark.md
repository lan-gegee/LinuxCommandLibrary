# TAGLINE

以图形方式创建、查看和解压归档。

# TLDR

将指定归档**解压**到当前目录

```ark -b [path/to/archive]```

将归档解压到**指定目录**

```ark -b -o [path/to/directory] [path/to/archive]```

**创建**归档并向其中添加指定文件

```ark -t [path/to/archive] [path/to/file1] [path/to/file2]```

# SYNOPSIS

**ark** [_options_] [_archive_] [_files_]

# DESCRIPTION

**ark** 是 KDE 的图形化归档工具，支持创建、查看、解压和修改归档。它通过插件支持众多格式，包括 tar、gzip、bzip2、zip、rar、7z 等。

配合命令行选项运行时，ark 可以在不显示 GUI 的批处理模式下操作，非常适合脚本编写和自动化。

# PARAMETERS

**-b, --batch**
> 使用批处理模式（无 GUI）解压归档

**-o, --destination** _directory_
> 解压到指定目录

**-t, --add-to** _archive_
> 将文件添加到归档，必要时先创建归档

**-c, --add**
> 向现有归档添加文件

**-e, --extract**
> 打开解压对话框

**-d, --dialog**
> 显示对话框选择解压选项，而不是静默解压

**-f, --changetofirstpath**
> 使用第一个归档条目的路径作为目标路径（配合 **-b** 使用）

# CAVEATS

某些归档格式需要额外的插件或外部程序。创建 RAR 需要 **rar**（专有软件），而解压可使用免费的 **unrar**。格式支持情况取决于已安装的 KDE 归档插件。

# INSTALL

```apt: sudo apt install ark```

```dnf: sudo dnf install ark```

```pacman: sudo pacman -S ark```

```apk: sudo apk add ark```

```zypper: sudo zypper install ark```

```brew: brew install ark```

```nix: nix profile install nixpkgs#ark```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[tar](/man/tar)(1), [unzip](/man/unzip)(1), [7z](/man/7z)(1)

# RESOURCES

```[Source code](https://invent.kde.org/utilities/ark)```

```[Homepage](https://apps.kde.org/ark/)```

<!-- verified: 2026-06-15 -->
