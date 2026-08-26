# TAGLINE

生成易记的 XKCD 风格口令短语

# TLDR

**生成口令短语**

```xkcdpass```

**以指定单词数量生成**

```xkcdpass -n [6]```

**使用分隔符生成**

```xkcdpass -d "-"```

**生成多个口令短语**

```xkcdpass -c [5]```

**使用自定义词表**

```xkcdpass -w [/path/to/wordlist]```

**按单词长度过滤**

```xkcdpass --min [4] --max [8]```

**生成含数字的口令短语**

```xkcdpass --valid-chars "[a-z0-9]"```

# SYNOPSIS

**xkcdpass** [_-n count_] [_-d delimiter_] [_-w wordlist_] [_options_]

# PARAMETERS

**-n** _COUNT_
> 单词数量。

**-d** _DELIM_
> 单词之间的分隔符。

**-w** _FILE_
> 词表文件。

**-c** _N_
> 口令短语的数量。

**--min** _N_
> 最短单词长度。

**--max** _N_
> 最长单词长度。

**--valid-chars** _CHARS_
> 有效字符的正则表达式。

**-v**, **--verbose**
> 显示熵信息。

**-a** _ACROSTIC_
> 藏头模式。

**-i**, **--interactive**
> 交互模式。

**--help**
> 显示帮助。

# DESCRIPTION

**xkcdpass** 使用随机单词生成易记的口令短语。它的灵感来自讨论密码强度的 XKCD 第 936 期漫画。

词典中的随机单词构成口令短语。四个或更多随机单词即可提供很强的安全性，同时保持易于记忆。

默认词表包含常见英文单词。可以使用自定义词表来支持其他语言或专用词汇。

熵信息反映口令短语的强度。更长的口令短语和更大的词表会提高熵值。

藏头模式生成的口令短语首字母可拼出一个单词，这有助于记忆，同时保持随机性。

单词长度过滤可以排除过短或过长的单词，从而改善可读性和输入速度。

# CAVEATS

安全性取决于词表大小。过小的词表会降低熵。随机选取必须是真随机。未经检验不应用于高安全需求场景。

# HISTORY

**xkcdpass** 的创作灵感来自 **Randall Munroe** 的 **XKCD 第 936 期漫画**。该漫画展示了随机单词口令短语比复杂但短的密码更安全且更易记。

# INSTALL

```pacman: sudo pacman -S xkcdpass```

```apk: sudo apk add xkcdpass```

```nix: nix profile install nixpkgs#xkcdpass```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwgen](/man/pwgen)(1), [makepasswd](/man/makepasswd)(1), [apg](/man/apg)(1), [openssl](/man/openssl)(1)
