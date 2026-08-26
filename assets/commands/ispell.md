# TAGLINE

交互式拼写检查器

# TLDR

**交互式检查文件**

```ispell [file.txt]```

**从 stdin 检查**

```echo "wrods" | ispell -a```

**列出拼写错误的单词**

```ispell -l < [file.txt]```

**使用指定词典**

```ispell -d [american] [file.txt]```

**检查 TeX/LaTeX 文件**

```ispell -t [document.tex]```

从 stdin **展开词缀标志**

```echo "[BOTH/R]" | ispell -e```

# SYNOPSIS

**ispell** [_options_] _file_...

# PARAMETERS

**-a**
> 供程序使用的管道模式。

**-l**
> 仅列出拼写错误的单词。

**-d** _DICT_
> 使用指定词典。

**-t**
> TeX/LaTeX 模式。

**-n**
> nroff/troff 模式。

**-H**
> HTML 模式。

**-b**
> 为输入文件创建备份文件（.bak）。

**-x**
> 不创建备份文件。

**-B**
> 将连写的单词报告为拼写错误。

**-C**
> 将连写的单词视为合法复合词。

**-M**
> 在屏幕底部显示一行的选项小菜单。

**-N**
> 不显示选项小菜单。

**-c**
> 为从 stdin 读入的单词给出更正建议。

**-e**[_1-5_]
> 从 stdin 展开词缀标志。可选级别控制输出详细程度。

**-S**
> 按可能的正确程度对猜测列表排序。

**-W** _N_
> 指定始终视为合法的单词长度（默认 3）。

**-p** _FILE_
> 个人词典文件。

**-L** _LINES_
> 显示上下文的行数。

# DESCRIPTION

**ispell** 是一款交互式拼写检查器。它高亮文本文件中的拼写错误并提供更正建议。在交互模式下，每个拼错的单词都会连同上下文一起显示，用户可以选择建议的更正、输入替换内容，或将单词加入个人词典。

该工具支持多种语言和输入格式，包括纯文本、TeX/LaTeX、nroff/troff 和 HTML。它可以交互运行，也可以通过管道模式（-a）用于脚本编写和与其他程序集成。

# CAVEATS

已在很大程度上被 aspell/hunspell 取代。词典的可用性因系统而异。需要针对不同格式使用相应模式。

# HISTORY

ispell 由 **Ralph E. Gorin** 于 1971 年在斯坦福创建，后来由 **Geoff Kuenning** 重写为 International Ispell。

# INSTALL

```apt: sudo apt install ispell```

```pacman: sudo pacman -S ispell```

```apk: sudo apk add aspell-compat```

```zypper: sudo zypper install ispell```

```brew: brew install ispell```

```nix: nix profile install nixpkgs#ispell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aspell](/man/aspell)(1), [hunspell](/man/hunspell)(1), [spell](/man/spell)(1)
