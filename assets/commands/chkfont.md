# TAGLINE

FIGlet 字体文件校验器

# TLDR

**检查 FIGlet 字体文件的错误**

```chkfont [path/to/font.flf]```

**检查多个字体文件**

```chkfont [font1.flf] [font2.flf]```

**检查标准 FIGlet 目录中的字体**

```chkfont /usr/share/figlet/[big.flf]```

# SYNOPSIS

**chkfont** _fontfile..._

# DESCRIPTION

**chkfont** 校验 FIGlet 2.0 及以后版本的字体文件（**.flf**）中的格式错误。它检查字体文件结构并报告常见问题，且不修改文件。

该工具主要供字体设计者和编辑者在发布前验证字体文件，或诊断自定义 FIGlet 字体的问题。

# PARAMETERS

**fontfile**
> 一个或多个要检查的 FIGlet 字体文件。文件应带有 **.flf** 扩展名

# CAVEATS

不能处理压缩的字体文件（**.flf.gz**）。检查前请先用 **gunzip** 解压字体。

只校验 FIGlet 字体格式，不支持 FIGlet 控制文件或其他字体格式。

# HISTORY

**chkfont** 是 FIGlet 项目的一部分。FIGlet 由 Glenn Chappell 和 Ian Chai 于 1991 年编写，它使用特殊字体将普通文本变成大字横幅。当前版本由 Claudio Matsuoka 维护。

# INSTALL

```apt: sudo apt install figlet```

```dnf: sudo dnf install figlet```

```pacman: sudo pacman -S figlet```

```apk: sudo apk add figlet```

```zypper: sudo zypper install figlet```

```brew: brew install figlet```

```nix: nix profile install nixpkgs#figlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(6), [figlist](/man/figlist)(6), [showfigfonts](/man/showfigfonts)(6), [toilet](/man/toilet)(1)

# RESOURCES

```[Source code](https://github.com/cmatsuoka/figlet)```

```[Homepage](http://www.figlet.org)```

<!-- verified: 2026-06-22 -->
