# TAGLINE

管理 ZIP 文件注释

# TLDR

**显示文件注释**

```zipnote [archive.zip]```

**编辑注释**

```zipnote [archive.zip] > [notes.txt] && vim [notes.txt] && zipnote -w [archive.zip] < [notes.txt]```

**从文件写入注释**

```zipnote -w [archive.zip] < [notes.txt]```

# SYNOPSIS

**zipnote** [_-w_] [_options_] _zipfile_

# PARAMETERS

**-w**
> 写入模式。

**-b** _PATH_
> 临时文件路径。

**-h**
> 显示帮助。

**-v**
> 显示版本。

# DESCRIPTION

**zipnote** 读写存储在 ZIP 归档中的注释。ZIP 文件支持每个文件的注释以及整个归档的注释，zipnote 提供了从命令行查看和修改这些元数据字段的方式。

在读取模式（默认）下，zipnote 输出所有文件名及其关联注释的结构化列表。输出使用特定格式，以 **@** 标记分隔各条目，可以重定向到文件进行编辑。

在写入模式（**-w**）下，zipnote 从标准输入读取修改后的结构化格式，并相应更新归档的注释。这一工作流允许批量编辑归档中所有文件的注释。zipnote 是 Info-ZIP 工具集的一部分。

# FORMAT

```
@ filename
comment text here
@ (comment above this line)
@ filename2
```

# CAVEATS

属于 Info-ZIP。需要特定格式。请小心编辑。

# HISTORY

**zipnote** 是 **Info-ZIP** 工具的一部分。它使 ZIP 文件中的注释管理成为可能。

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

[zip](/man/zip)(1), [unzip](/man/unzip)(1), [zipinfo](/man/zipinfo)(1)
