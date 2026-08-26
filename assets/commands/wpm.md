# TAGLINE

终端打字速度测试

# TLDR

**开始打字测试**

```wpm```

**使用文本文件练习**

```wpm [text.txt]```

**设置时长**

```wpm -d [60]```

**设置单词数量**

```wpm -w [50]```

# SYNOPSIS

**wpm** [_-d seconds_] [_-w count_] [_options_] [_file_]

# PARAMETERS

**-d** _SEC_
> 时长。

**-w** _COUNT_
> 单词数量。

**--help**
> 显示帮助。

# DESCRIPTION

**wpm** 是基于终端的打字速度测试工具，测量每分钟单词数和准确率。它呈现一段文本让用户输入，在无干扰的终端环境中跟踪速度和错误率。

可以提供自定义文本文件来练习特定内容，还可以配置测试时长或单词数量。该工具适合练习盲打，也适合长期对比打字表现。

# CAVEATS

仅支持终端。存在多种实现。属于练习工具。

# HISTORY

**wpm**（words per minute）类工具在终端中测量打字速度，用于练习和基准测试。

# INSTALL

```nix: nix profile install nixpkgs#wpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toipe](/man/toipe)(1), [tt](/man/tt)(1), [typespeed](/man/typespeed)(1)
