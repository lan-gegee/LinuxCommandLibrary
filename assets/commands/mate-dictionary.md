# TAGLINE

MATE 桌面的图形化词典应用

# TLDR

**打开词典**

```mate-dictionary```

**查询单词**

```mate-dictionary --look-up [word]```

**使用指定数据库查询单词**

```mate-dictionary --database [wn] --look-up [word]```

**查询单词并打印到控制台而不打开 GUI**

```mate-dictionary --no-window --look-up [word]```

**使用指定来源查询单词**

```mate-dictionary --source [source_name] --look-up [word]```

# SYNOPSIS

**mate-dictionary** [_options_]

# PARAMETERS

**--look-up** _word_
> 使用预定义的词典来源查询指定的单词。

**--match** _word_
> 使用预定义的词典来源查找匹配的单词。

**--source**, **-s** _source_
> 使用指定的来源查询单词。

**--database**, **-D** _database_
> 使用指定的数据库查询单词。

**--no-window**, **-n**
> 将释义打印到控制台而不启动 GUI。

# DESCRIPTION

**mate-dictionary** 是 MATE 桌面环境的图形化词典应用。它使用 DICT 协议服务器查询单词，支持多个词典和多种搜索策略。查询结果可以保存到文件或打印输出。

# INSTALL

```apt: sudo apt install mate-utils```

```dnf: sudo dnf install mate-utils```

```pacman: sudo pacman -S mate-utils```

```apk: sudo apk add mate-dictionary```

```zypper: sudo zypper install mate-dictionary```

```nix: nix profile install nixpkgs#mate-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dict](/man/dict)(1)
