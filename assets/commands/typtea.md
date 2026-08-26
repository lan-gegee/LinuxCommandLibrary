# TAGLINE

带编程语言词表的极简终端打字速度测试

# TLDR

**开始 30 秒英语打字测试**（默认）

```typtea start```

**运行 60 秒测试**

```typtea start --duration [60]```

**练习 Rust 关键字**

```typtea start --lang [rust]```

**同时指定时长与语言**

```typtea start --duration [45] --lang [javascript]```

**列出所有支持的语言**

```typtea start --list-langs```

**显示帮助**

```typtea --help```

# SYNOPSIS

**typtea** _command_ [_options_]

**typtea start** [**--duration** _SECONDS_] [**--lang** _LANG_] [**--list-langs**]

# PARAMETERS

**start**
> 开始一次打字测试。

**--duration** _SECONDS_
> 测试时长（秒）（默认 `30`）。

**--lang** _LANG_
> 要使用的词表。`english`（默认）以及 30 多种编程语言（如 `go`、`rust`、`python`、`javascript`、`typescript`、`c`、`cpp`、`java`、`kotlin`、`swift`、`ruby`、`php`、`lua`、`haskell`、`scala`、`zig`、`elixir`、`shell`）。

**--list-langs**
> 打印所有可用的词表。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**typtea** 是一款面向程序员的极简终端打字测试器。它从英语或特定语言的关键字列表生成源源不断的单词，显示一个滚动的三行视口，并实时报告 WPM（每分钟单词数）和准确率。界面基于 **Bubble Tea** / **Lipgloss** 构建，能优雅地处理窗口缩放、颜色以及鼠标/键盘输入。

# CAVEATS

二进制文件名为小写（`typtea`）。所有模式都在 `start` 子命令之下——在较新版本中，不带参数运行 `typtea` 只会打印帮助信息。

# HISTORY

**typtea** 由 **Ashish Kumar**（GitHub 用户 `ashish0kumar`）开发，使用 **Go** 和 **Bubble Tea** 编写。通过 GitHub Releases 分发，并被多个发行版打包（如 FreeBSD ports、AUR）。

# INSTALL

```brew: brew install typtea```

```nix: nix profile install nixpkgs#typtea```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[typioca](/man/typioca)(1), [tt](/man/tt)(1), [ttyper](/man/ttyper)(1), [smassh](/man/smassh)(1)
