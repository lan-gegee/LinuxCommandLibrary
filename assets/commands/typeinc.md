# TAGLINE

终端打字速度训练器

# TLDR

**开始打字练习**

```typeinc```

**使用文件练习**

```typeinc [text.txt]```

**设置时长**

```typeinc -t [60]```

**自定义单词数**

```typeinc -w [100]```

# SYNOPSIS

**typeinc** [_-t seconds_] [_-w count_] [_options_] [_file_]

# PARAMETERS

**-t** _SEC_
> 时长（秒）。

**-w** _COUNT_
> 单词数。

**-l** _LANG_
> 语言。

**--help**
> 显示帮助。

# DESCRIPTION

**typeinc** 是一款基于终端的打字练习应用，以每分钟单词数衡量打字速度，并通过错误计数追踪准确率。它提供了一个无干扰的环境，让你直接在终端中提升键盘技能。

测试可以使用内置词表，也可以使用自定义文本文件来练习特定内容。时长和单词数上限都可以配置，从而创建短时间训练或长时间练习。完成后会显示带详细统计的结果。

# CAVEATS

仅在终端中运行。定制能力有限。属于练习工具。

# HISTORY

**typeinc** 是一款用于提升打字速度和准确率的终端打字练习应用。

# INSTALL

```nix: nix profile install nixpkgs#typeinc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toipe](/man/toipe)(1), [tt](/man/tt)(1), [typespeed](/man/typespeed)(1)
