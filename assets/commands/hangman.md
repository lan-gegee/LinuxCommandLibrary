# TAGLINE

经典猜词游戏

# TLDR

**开始猜词游戏**

```hangman```

**使用自定义词表**

```hangman -w [wordlist.txt]```

**设置单词长度**

```hangman -l [8]```

# SYNOPSIS

**hangman** [_options_]

# PARAMETERS

**-w** _FILE_
> 词表文件。

**-l** _LEN_
> 最短单词长度。

**-k**
> 显示键盘。

**--help**
> 显示帮助信息。

# PREVIEW

```
 +---+
 |   O
 |  /|\
 |   |
_|_
 _ a n g _ a n
```

# DESCRIPTION

**hangman** 是一款经典的猜词游戏。玩家需要在错误次数过多之前猜出字母，逐步揭示隐藏的单词。

游戏会显示绞刑架并记录错误的猜测。它使用系统词典或自定义词表作为出题来源。

# CAVEATS

属于 BSD games 游戏集的一部分。需要 /usr/share/dict/words 或自定义词表。基于终端显示。

# HISTORY

hangman 自早期 Unix 系统起就是 **BSD games** 游戏集的一部分，为终端带来消遣娱乐。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bsdgames](/man/bsdgames)(6), [fortune](/man/fortune)(6)
