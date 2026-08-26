# TAGLINE

以源代码为挑战的 CLI 打字游戏

# TLDR

**开始**打字挑战

```gittype```

用特定语言**练习**

```gittype --lang rust```

设置难度级别

```gittype --difficulty hard```

查看统计数据

```gittype --stats```

# SYNOPSIS

**gittype** [_options_]

# PARAMETERS

**--lang** _LANGUAGE_
> 编程语言：rust、python、go、javascript 等。

**--difficulty** _LEVEL_
> 难度：easy、medium、hard

**--duration** _SECONDS_
> 设置挑战时长

**--stats**
> 显示打字统计

**--list-langs**
> 列出可用语言

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gittype** 是一个打字练习游戏，使用来自开源仓库的真实源代码作为打字挑战。它帮助程序员练习输入带有正确语法和特殊字符的代码。

该工具从 GitHub 获取代码片段并作为打字练习呈现，同时跟踪速度（WPM）和准确率。

# CAVEATS

获取代码片段需要联网。代码片段的复杂程度不一。不适合用来学习实际的编程概念。

# HISTORY

**gittype** 的创建目的是让开发者通过真实世界的示例而非普通文本，有趣地练习代码输入。

# INSTALL

```brew: brew install gittype```

```nix: nix profile install nixpkgs#gittype```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[typespeed](/man/typespeed)(1), [ttyper](/man/ttyper)(1)
