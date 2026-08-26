# TAGLINE

提供 King James 版圣经文本的命令行阅读器

# TLDR

**列出**所有书卷

```kjv -l```

打开指定的**书卷**

```kjv [Genesis]```

打开指定的**章节**

```kjv [Genesis] [2]```

打开指定的**经节**

```kjv [John] [3]:[16]```

打开一个**经节范围**

```kjv [Proverbs] [3]:[1-6]```

显示跨**多个章节**的经节

```kjv [Matthew] [1]:[7]-[2]:[6]```

**搜索**某个模式

```kjv /[Plagues]```

在**指定书卷**内搜索

```kjv [1Jn]/[antichrist]```

# SYNOPSIS

**kjv** [_options_] [_reference_]

# PARAMETERS

**-l**
> 列出所有书卷

_BOOK_
> 显示整卷书

_BOOK CHAPTER_
> 显示指定章节

_BOOK CHAPTER:VERSE_
> 显示指定经节

_BOOK CHAPTER:START-END_
> 显示经节范围

**/**_PATTERN_
> 在全部文本中搜索模式

_BOOK_**/**_PATTERN_
> 在指定书卷内搜索

# DESCRIPTION

**kjv** 是一款提供 King James 版圣经文本的命令行阅读器。它支持灵活的引用格式，可用于查找书卷、章节、经节和范围。

该工具还包含搜索功能，可以在全部文本或指定书卷内查找包含特定词语或模式的经节。

# CAVEATS

仅包含 King James 版文本。书名可使用多种缩写。搜索默认不区分大小写。

# HISTORY

kjv 是遵循 Unix 哲学打造的简洁终端圣经阅读器。它无需图形界面或浏览器即可快速访问圣经文本。

# INSTALL

```nix: nix profile install nixpkgs#kjv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [grep](/man/grep)(1)
