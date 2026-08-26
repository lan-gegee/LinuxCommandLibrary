# TAGLINE

使用 StarDict 格式的控制台词典

# TLDR

**查询单词**

```sdcv [word]```

**使用指定词典查询**

```sdcv -u "[dictionary_name]" [word]```

**列出可用词典**

```sdcv -l```

**非交互模式**

```sdcv -n [word]```

**仅显示完全匹配**

```sdcv -e [word]```

**指定数据目录**

```sdcv --data-dir [/path/to/dicts] [word]```

**JSON 输出**

```sdcv --json [word]```

# SYNOPSIS

**sdcv** [_-u dict_] [_-n_] [_-e_] [_-j_] [_--data-dir dir_] [_options_] [_word_]

# PARAMETERS

**-l**, **--list-dicts**
> 列出可用词典。

**-u** _DICT_
> 使用指定的词典。

**-n**, **--non-interactive**
> 非交互模式。

**-e**, **--exact-search**
> 仅显示完全匹配。

**-x**, **--only-data-dir**
> 只使用 data-dir 中的词典，不搜索用户和系统目录。

**--data-dir** _DIR_
> 词典数据目录。

**-j**, **--json**
> JSON 输出。

**--color**
> 彩色输出。

**--utf8-input**
> UTF-8 输入。

**--utf8-output**
> UTF-8 输出。

**-v**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**sdcv**（StarDict console version）提供命令行词典查询。它使用广泛可得、采用 StarDict 格式的词典。

词典存放在 ~/.stardict/dic 或系统目录中。有多种语言和专业词典可供下载。

交互模式提供提示符以便连续查询多个词。非交互模式适合脚本编写和集成。

当精确匹配失败时，模糊搜索会查找相似的单词。这有助于处理拼写变体或错别字。

可以同时搜索多个词典。除非选择了特定词典，否则会显示所有词典的结果。

输出格式支持终端显示和程序化处理。JSON 输出便于与其他工具集成。

# CONFIGURATION

**~/.stardict/dic/**
> 默认的用户词典目录，StarDict 格式的词典存放于此。

**/usr/share/stardict/dic/**
> 系统级词典目录。

**STARDICT_DATA_DIR**
> 覆盖默认词典数据目录的环境变量。

**SDCV_PAGER**
> 指定用于输出显示的分页器的环境变量。

**SDCV_HISTFILE**
> 设置历史文件位置的环境变量。

**~/.sdcv_ordering**
> 指定搜索结果中词典排序的文件。

# CAVEATS

需要先安装词典文件。质量因词典而异。某些词典体积较大。可能出现字符编码问题。

# HISTORY

**sdcv** 是 **StarDict** 的控制台版本。StarDict 是 **Hu Zheng** 于 **2003 年**发起的开源词典项目，其跨平台 GUI 颇受欢迎，sdcv 则将它扩展到了命令行用户。当前维护版本由 GitHub 上的 **Evgeniy Dushistov** 负责。

# INSTALL

```apt: sudo apt install sdcv```

```dnf: sudo dnf install sdcv```

```pacman: sudo pacman -S sdcv```

```apk: sudo apk add sdcv```

```zypper: sudo zypper install sdcv```

```brew: brew install sdcv```

```nix: nix profile install nixpkgs#sdcv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dict](/man/dict)(1), [dictd](/man/dictd)(8), [espeak](/man/espeak)(1)
