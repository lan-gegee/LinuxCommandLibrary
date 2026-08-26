# TAGLINE

用 Rust 编写的多功能快速文件清理工具

# TLDR

**查找重复文件**

```czkawka_cli dup -d [/path/to/search]```

**查找空文件**

```czkawka_cli empty-files -d [/path/to/search]```

**查找空目录**

```czkawka_cli empty-folders -d [/path/to/search]```

**查找大文件**

```czkawka_cli big -d [/path/to/search]```

**查找相似图片**

```czkawka_cli image -d [/path/to/search]```

**查找临时文件**

```czkawka_cli temp -d [/path/to/search]```

# SYNOPSIS

**czkawka_cli** _command_ [_options_]

# SUBCOMMANDS

**dup**
> 查找重复文件。

**empty-files**
> 查找空文件。

**empty-folders**
> 查找空目录。

**big**
> 查找大文件。

**temp**
> 查找临时文件。

**image**
> 查找相似图片。

**music**
> 按标签查找相似音乐。

**symlinks**
> 查找无效的符号链接。

**broken**
> 查找损坏的文件。

# PARAMETERS

**-d**, **--directories** _paths_
> 要搜索的目录。

**-e**, **--excluded** _paths_
> 要排除的目录。

**-f**, **--file-to-save** _file_
> 将结果保存到文件。

**-D**, **--delete-files**
> 删除找到的文件。

# DESCRIPTION

**czkawka_cli**（波兰语"打嗝"之意）是一个快速的重复文件查找与清理工具。它可以查找重复文件、相似图片、空文件/空目录、大文件以及临时文件。

它用 Rust 编写以保证高性能，是 Czkawka 应用程序的 CLI 版本。

# CAVEATS

**-D** 选项会永久删除文件。删除前务必先检查结果。建议先用 **-f** 保存结果。

# INSTALL

```apt: sudo apt install czkawka-cli```

```apk: sudo apk add czkawka```

```brew: brew install czkawka```

```nix: nix profile install nixpkgs#czkawka```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdupes](/man/fdupes)(1), [rmlint](/man/rmlint)(1)

# RESOURCES

```[Source code](https://github.com/qarmin/czkawka)```

<!-- verified: 2026-06-26 -->
