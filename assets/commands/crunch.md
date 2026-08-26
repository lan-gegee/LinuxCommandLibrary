# TAGLINE

用于密码测试的字典生成器

# TLDR

使用默认字符集**生成指定长度的所有组合**

```crunch [4] [6]```

使用自定义字符集**生成字典**

```crunch [4] [4] [abc123]```

将字典输出到文件

```crunch [6] [8] -o [wordlist.txt]```

按模式生成（@ = 小写字母，, = 大写字母，% = 数字，^ = 符号）

```crunch [8] [8] -t [@@@@%%%%]```

限制输出文件大小（如每个文件 10MB）

```crunch [6] [6] -b [10mb] -o [START]```

基于文件中的单词生成

```crunch [4] [4] -p [word1] [word2] [word3]```

# SYNOPSIS

**crunch** _min-len_ _max-len_ [_charset_] [_options_]

# PARAMETERS

_MIN-LEN_
> 生成字符串的最小长度。

_MAX-LEN_
> 生成字符串的最大长度。

_CHARSET_
> 用于生成的字符集（默认：小写字母表）。

**-o** _FILE_
> 输出到文件而不是 stdout。

**-t** _PATTERN_
> 使用占位符指定模式（@ , % ^）。

**-b** _SIZE_
> 将输出拆分为指定大小的多个文件。

**-c** _COUNT_
> 每个输出文件的行数。

**-p** _WORDS_
> 生成指定单词的排列组合。

**-d** _NUM_
> 限制连续重复字符的数量。

**-e** _STRING_
> 在指定字符串处停止生成。

**-f** _FILE_ _CHARSET_
> 从文件读取字符集（如 charset.lst）。

**-i**
> 反转输出顺序，使第一个字符变化最频繁。

**-l** _CHARS_
> 在 -t 模式中将字符视为字面量（覆盖 @,%^）。

**-s** _STRING_
> 从指定字符串开始（用于断点续跑）。

**-u**
> 禁用打印百分比信息的线程。

**-z** _COMP_
> 压缩输出（gzip、bzip2、lzma、7z）。

# DESCRIPTION

**crunch** 是一个字典生成器，根据指定的条件创建所有可能组合的列表。它常被用于经授权的渗透测试，以生成密码列表、暴力破解字典以及测试安全防护措施。

该工具能高效地生成组合，支持自定义字符集、模式和大小限制。模式允许在特定位置混合不同类型的字符（字母、数字、符号）。排列模式则生成给定单词的所有排列方式。

输出可以通过管道传给其他工具，也可以拆分成便于管理的大小以应对超大字典。压缩选项有助于管理大规模生成时的磁盘空间。

# CAVEATS

大型字典会占用大量磁盘空间和生成时间。请负责任地使用，仅用于经授权的安全测试。生成大列表前确保存储空间充足。注意组合数量会随长度呈指数级增长。

# HISTORY

crunch 是为安全社区开发的灵活字典生成器。它已成为 Kali Linux 等渗透测试发行版中的标准工具。借助该工具，安全专业人员可以测试密码策略和身份验证系统。

# INSTALL

```apt: sudo apt install crunch```

```brew: brew install crunch```

```nix: nix profile install nixpkgs#crunch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[john](/man/john)(1), [hashcat](/man/hashcat)(1), [hydra](/man/hydra)(1)
