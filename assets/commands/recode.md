# TAGLINE

在不同字符编码之间转换文本

# TLDR

**将文件从 Latin-1 转换为 UTF-8**

```recode latin1..utf8 [file]```

**从 UTF-8 转换为 Latin-1**

```recode utf8..latin1 [file]```

**将 HTML 实体转换为 UTF-8**

```recode html..utf8 [file]```

**将 UTF-8 转换为 HTML 实体**

```recode utf8..html [file]```

**转换并保存为新文件**（保留原文件）

```recode latin1..utf8 < [input] > [output]```

**列出所有可用字符集**

```recode -l```

**以详细输出模式转换**

```recode -v latin1..utf8 [file]```

# SYNOPSIS

**recode** [_options_] _request_ [_file_...]

# PARAMETERS

_request_
> 转换说明，格式为：source..destination

**-l**, **--list**
> 列出所有已知的字符集和表面形式

**-f**, **--force**
> 即使可能丢失信息也强制转换

**-s**, **--strict**
> 严格模式；遇到无法转换的字符即中止

**-d**, **--diacritics-only**
> 只转换变音符，保留其他字符

**-c**, **--colstrings**
> 启用面向列的字符串模式

**-g**, **--graphics**
> 显示图形化的转换摘要

**-v**, **--verbose**
> 详细输出，显示转换细节

**-q**, **--quiet**
> 抑制警告和进度消息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**recode** 在不同字符编码之间转换文本文件，还可以转换转义序列。它支持超过 300 种字符集，包括 ASCII、Latin 系列、UTF-8、UTF-16 以及各种国家级编码。

转换请求使用 **source..destination** 格式，两部分分别指定源和目标字符集。无法在目标字符集中表示的字符将按模式处理（严格、强制或默认的有损转换）。

除字符集转换外，recode 还能处理表面形式的变换，例如 CRLF 行尾、Base64、quoted-printable、HTML/XML 实体以及各种转义序列。

可以处理多个文件，每个文件都会被原地转换。使用 shell 重定向可保留原文件。

# CAVEATS

原地转换会直接修改文件。如果对转换结果不确定，请务必备份文件或使用重定向保留原文件。

不兼容字符集之间的转换可能丢失信息。使用 **-s**（严格）检测到问题字符即中止，或使用 **-f**（强制）继续转换。

HTML 实体转换（**html** 字符集）处理数字实体。像 **&amp;** 这样的命名实体需要额外处理。

# HISTORY

Recode 由 **François Pinard** 于 **1990 年**开始编写，是最早面向 Unix 的综合性字符集转换工具之一。它后来成为 GNU 项目，至今在批量处理文本编码转换方面仍然实用。

# INSTALL

```apt: sudo apt install recode```

```dnf: sudo dnf install recode```

```pacman: sudo pacman -S recode```

```apk: sudo apk add recode```

```zypper: sudo zypper install recode```

```brew: brew install recode```

```nix: nix profile install nixpkgs#recode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iconv](/man/iconv)(1), [uconv](/man/uconv)(1), [convmv](/man/convmv)(1), [file](/man/file)(1)
