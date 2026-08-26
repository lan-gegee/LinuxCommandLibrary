# TAGLINE

使用 more 分页器查看 bzip2 压缩文件

# TLDR

**查看**压缩文件

```bzmore [file.txt.bz2]```

# SYNOPSIS

**bzmore** [_file_...]

# DESCRIPTION

**bzmore** 是一个用于逐页查看 bzip2 压缩文件的过滤器，基于 more 分页器。它会解压文件并以基本的分页功能显示内容。

该工具与 bzless 类似，但使用更简单的 more 分页器。

# FEATURES

- 逐页查看
- 基本搜索
- 保留原始文件
- 支持多个文件

# KEYBINDINGS

- **Space** - 下一页
- **/pattern** - 搜索
- **q** - 退出
- **h** - 帮助

# WORKFLOW

```bash
# View compressed file
bzmore logfile.bz2

# View multiple files
bzmore *.bz2
```

# CAVEATS

功能不如 bzless 丰富。无法向后翻页。搜索能力有限。建议改用功能更好的 bzless。

# HISTORY

**bzmore** 自 **1996** 年起就是 bzip2 工具集的一部分，仿照 zmore 设计。

# INSTALL

```apt: sudo apt install bzip2```

```dnf: sudo dnf install bzip2```

```pacman: sudo pacman -S bzip2```

```apk: sudo apk add bzip2```

```zypper: sudo zypper install bzip2```

```brew: brew install bzip2```

```nix: nix profile install nixpkgs#bzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[more](/man/more)(1), [bzless](/man/bzless)(1), [bzcat](/man/bzcat)(1)

# RESOURCES

```[Source code](https://gitlab.com/bzip2/bzip2)```

```[Homepage](https://sourceware.org/bzip2/)```

<!-- verified: 2026-06-22 -->
