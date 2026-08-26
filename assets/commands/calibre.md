# TAGLINE

电子书管理与格式转换套件

# TLDR

**启动** Calibre 图形界面

```calibre```

向书库**添加**图书

```calibredb add [book.epub]```

**转换**电子书格式

```ebook-convert [input.epub] [output.mobi]```

**启动**内容服务器

```calibre-server```

**编辑**电子书

```ebook-edit [book.epub]```

# SYNOPSIS

**calibre**

# DESCRIPTION

**calibre** 是一款功能全面的电子书管理应用。它提供书库整理、格式转换、元数据编辑、电子书同步到设备等功能，并内置阅读器和编辑器。

该应用支持几乎所有电子书格式和大多数电子阅读器。

# COMPONENTS

**calibre**
> 主图形界面应用

**calibredb**
> 命令行书库管理

**ebook-convert**
> 格式转换

**ebook-edit**
> EPUB 编辑器

**calibre-server**
> 基于 Web 的书库访问

**ebook-viewer**
> 电子书阅读器

# FEATURES

- 书库管理
- 格式转换（25 种以上格式）
- 元数据编辑与下载
- 从网站下载新闻
- 电子书编辑
- 设备同步
- 内容服务器（Web 访问）
- 搜索与过滤
- 自定义列和标签

# SUPPORTED FORMATS

**输入：** EPUB、MOBI、AZW、PDF、HTML、TXT 等 20 多种
**输出：** EPUB、MOBI、AZW3、PDF、TXT 等

# COMMAND-LINE USAGE

```bash
# Add book
calibredb add book.epub

# List books
calibredb list

# Convert format
ebook-convert input.epub output.mobi

# Start server
calibre-server /path/to/library

# Fetch metadata
fetch-ebook-metadata --isbn 9780123456789
```

# CONFIGURATION

**~/.config/calibre/**
> 配置目录，包含首选项、插件和书库设置

# CAVEATS

大型书库可能较慢。不含 DRM 移除功能（需要插件）。基于 Qt（占用较大）。某些转换效果不完美。Kindle 的 AZW3 支持在部分功能上需要 Amazon 账户。

# HISTORY

**Calibre** 由 Kovid Goyal 于 **2006** 年创建，用于管理电子书，后来成为电子书管理与转换领域的事实标准。

# INSTALL

```dnf: sudo dnf install calibre```

```pacman: sudo pacman -S calibre```

```zypper: sudo zypper install calibre```

```nix: nix profile install nixpkgs#calibre```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ebook-convert](/man/ebook-convert)(1), [calibredb](/man/calibredb)(1), [pandoc](/man/pandoc)(1)

# RESOURCES

```[Source code](https://github.com/kovidgoyal/calibre)```

```[Homepage](https://calibre-ebook.com/)```

```[Documentation](https://manual.calibre-ebook.com/)```

<!-- verified: 2026-06-22 -->
