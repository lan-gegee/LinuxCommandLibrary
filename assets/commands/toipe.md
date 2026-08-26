# TAGLINE

基于终端的打字速度测试

# TLDR

以默认设置**开始打字测试**

```toipe```

**选择一个内置词表**

```toipe -w [top1000]```

**使用自定义词表**文件

```toipe -f [path/to/words.txt]```

**设置每次测试的单词数量**

```toipe -n [50]```

**列出内置**词表

```toipe --list```

# SYNOPSIS

**toipe** [_-w wordlist_] [_-f file_] [_-n count_] [_options_]

# PARAMETERS

**-w** _WORDLIST_
> 内置词表名称（top250、top500、top1000 等）。

**-f** _FILE_
> 从自定义的换行分隔文件中读取单词。

**-n** _COUNT_
> 测试中包含的单词数量。

**-p**, **--punctuation**
> 在生成的文本中加入标点符号。

**--list**
> 列出可用的内置词表后退出。

**--help**
> 显示帮助。

# DESCRIPTION

**toipe** 是一款用 Rust 编写的基于终端的打字速度测试工具。它从词表中抽取随机单词，在终端中以单个段落的形式呈现，并在你输入时逐字符跟踪错误。每轮结束后它会打印每分钟单词数（WPM）、每分钟字符数（CPM）和准确率。

二进制文件附带多个按难度分组的内置词表。自定义词表可通过 **-f** 加载，便于练习编程关键字、外语词汇或特定领域的文本。

# CAVEATS

仅限终端环境；需要支持 raw 模式的终端。性能报告假设时钟具有一秒分辨率。自带的词表仅含英语，但 **-f** 可接受任何 UTF-8 文件。含有典型 7 位 ASCII 范围之外字符的词表可能在传统终端上无法正确渲染。

# HISTORY

**toipe** 是一款用 Rust 编写的基于终端的打字测试应用。

# INSTALL

```zypper: sudo zypper install toipe```

```brew: brew install toipe```

```nix: nix profile install nixpkgs#toipe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tt](/man/tt)(1), [typespeed](/man/typespeed)(1), [wpm](/man/wpm)(1)
