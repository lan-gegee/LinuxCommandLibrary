# TAGLINE

创建和修改 ZIP 归档

# TLDR

**创建 ZIP 归档**

```zip [archive.zip] [file1] [file2]```

**从目录创建归档**

```zip -r [archive.zip] [directory/]```

**向已有归档添加文件**

```zip [archive.zip] [newfile.txt]```

**以指定压缩级别创建归档**

```zip -9 [archive.zip] [files]```

**创建加密归档**

```zip -e [archive.zip] [files]```

**排除文件不入归档**

```zip -r [archive.zip] [directory/] -x "*.log"```

**只更新有变化的文件**

```zip -u [archive.zip] [files]```

**创建归档时排除目录**

```zip -r [archive.zip] [dir/] -x [dir/subdir/*]```

**从归档中删除文件**

```zip -d [archive.zip] [file_to_remove]```

**将文件移入归档（删除原文件）**

```zip -m [archive.zip] [file1] [file2]```

**创建分为 100 MB 卷的分卷归档**

```zip -s [100m] [archive.zip] [files]```

**测试归档完整性**

```zip -T [archive.zip]```

# SYNOPSIS

**zip** [_options_] _archive_ _files_...

# DESCRIPTION

**zip** 创建和修改 ZIP 归档，这是一种广泛支持的压缩归档格式。它使用 DEFLATE 算法压缩文件（或不压缩直接存储），并将名称、时间戳和权限等元数据一并打包。

ZIP 归档跨平台兼容，在 Windows、macOS 和大多数 Unix 系统上原生受支持。该格式支持目录结构、加密以及跨多个文件的分卷归档。

zip 可以创建新归档、向现有归档添加文件、更新变化的文件或删除条目。它常用于文件分发、备份和数据交换。

# PARAMETERS

**-r**
> 递归处理目录。

**-9**
> 最大压缩。

**-0**
> 仅存储（不压缩）。

**-e**
> 加密归档（提示输入密码）。

**-P** _password_
> 使用指定密码。

**-u**
> 只更新有变化的文件。

**-f**
> 刷新（仅更新已有条目）。

**-d**
> 从归档中删除条目。

**-x** _pattern_
> 排除匹配模式的文件。

**-i** _pattern_
> 只包含匹配的文件。

**-j**
> 去除目录路径。

**-q**
> 安静模式。

**-v**
> 详细输出。

**-m**
> 将文件移入归档（成功归档后删除原文件）。

**-g**
> 扩展（追加到）已有归档。

**-T**
> 创建后测试归档完整性。检查失败则中止。

**-@**
> 从标准输入读取文件列表。

**-s** _size_
> 将归档分割为指定大小的分卷（如 `100m`、`1g`）。

**-sf**
> 显示将被操作的文件，然后退出而不创建归档。

**-FS**
> 将归档内容与文件系统同步：添加新文件、更新有变化的文件，并删除磁盘上已不存在的条目。

**-y**
> 将符号链接按链接本身存储，而不是跟随链接。

# CAVEATS

默认加密很弱（ZipCrypto）；强加密请使用 7z。不启用 ZIP64 时单个文件最大为 4GB。在命令行上输入密码不安全。时间戳可能损失精度。

# HISTORY

ZIP 格式由 **Phil Katz** 于 **1989 年**为其 **PKZIP** 创建。同年启动了 **Info-ZIP** 项目以提供自由实现。Info-ZIP 的 zip 成为标准的 Unix ZIP 工具，几乎所有类 Unix 系统都有收录。该格式不断演进，以支持更大的文件（ZIP64）和更好的压缩。

# INSTALL

```apt: sudo apt install zip```

```dnf: sudo dnf install zip```

```pacman: sudo pacman -S zip```

```apk: sudo apk add zip```

```zypper: sudo zypper install zip```

```brew: brew install zip```

```nix: nix profile install nixpkgs#zip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unzip](/man/unzip)(1), [tar](/man/tar)(1), [gzip](/man/gzip)(1), [7z](/man/7z)(1)
