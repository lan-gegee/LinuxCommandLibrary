# TAGLINE

提取字体文件信息

# TLDR

**查询字体文件**

```fc-query [font.ttf]```

**显示特定属性**

```fc-query --format '%{family}\n' [font.ttf]```

**列出所有属性**

```fc-query --format '%{=unparse}\n' [font.ttf]```

**查询字体索引**

```fc-query --index [0] [font.ttc]```

# SYNOPSIS

**fc-query** [_options_] _font-file_

# PARAMETERS

_FONT-FILE_
> 要查询的字体文件（.ttf、.otf、.ttc）。

**-f**, **--format** _FORMAT_
> 输出格式字符串。

**-i**, **--index** _N_
> 只查询每个文件中给定索引处的字体面。

**-b**, **--ignore-blanks**
> 计算支持的语言时忽略空白字形。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fc-query** 无需安装即可从字体文件中提取并显示信息。它是 fontconfig 的一部分，可显示字族、样式、字重和支持的语言等字体属性。

该工具直接查询单个字体文件而非系统字体缓存。格式字符串可用于提取特定属性。对于字体集合（.ttc），可通过索引选择特定字体。

fc-query 适合在安装前检查字体，或编写脚本管理字体。

# CAVEATS

只读取单个文件，不支持目录。格式字符串语法需要学习。某些字体的元数据可能不完整。

# HISTORY

fc-query 是 **fontconfig** 的一部分，fontconfig 是 Keith Packard 为 X.org 创建的字体配置库。它提供对 fontconfig 系统所用字体元数据的编程式访问。

# INSTALL

```apt: sudo apt install fontconfig```

```dnf: sudo dnf install fontconfig```

```pacman: sudo pacman -S fontconfig```

```apk: sudo apk add fontconfig```

```zypper: sudo zypper install fontconfig```

```brew: brew install fontconfig```

```nix: nix profile install nixpkgs#fontconfig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fc-scan](/man/fc-scan)(1), [fc-list](/man/fc-list)(1), [fc-cache](/man/fc-cache)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/fontconfig/fontconfig)```

```[Homepage](https://www.freedesktop.org/wiki/Software/fontconfig/)```

<!-- verified: 2026-07-15 -->
