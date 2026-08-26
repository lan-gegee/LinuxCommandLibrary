# TAGLINE

带语言模式的终端打字测试

# TLDR

**使用默认单词开始打字测试**

```ttyper```

**限制测试的单词数量**

```ttyper -w [25]```

**用编程语言单词练习**

```ttyper -l [rust]```

**使用自定义单词文件**

```ttyper -c [/path/to/wordlist.txt]```

**用指定语言文件练习**

```ttyper -l [python] -w [50]```

**显示可用的语言**

```ttyper --list-languages```

# SYNOPSIS

**ttyper** [_options_]

# PARAMETERS

**-w**, **--words** _count_
> 测试包含的单词数量。

**-l**, **--language** _lang_
> 使用指定编程语言的单词。

**-c**, **--contents** _file_
> 使用自定义文件作为单词来源。

**--list-languages**
> 显示可用的内置语言。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**ttyper** 是一个用 Rust 和 Ratatui 构建的终端打字测试工具。它以每分钟单词数（WPM）和准确率衡量打字水平，并在你输入时提供即时的视觉反馈。

测试中正确的字符显示为绿色，错误的显示为红色。统计指标包括原始 WPM、调整后 WPM（考虑错误）以及准确率百分比，完成后展示结果。

编程语言模式包含各语言的关键字和常见标识符，便于开发者练习特定语言的输入习惯。自定义词表则支持个性化的练习内容。

# CAVEATS

需要支持 Unicode 的终端。配置存储在 ~/.config/ttyper/ 中。默认情况下结果不会跨会话保存。终端大小会影响显示布局。

# HISTORY

**ttyper** 的诞生是为了提供终端原生的替代方案，取代 Monkeytype 等基于网页的打字测试。开发者希望在不离开终端环境的情况下进行打字练习。它使用 Rust 构建，借助 Ratatui 框架展现了现代终端 UI 的能力。

# INSTALL

```pacman: sudo pacman -S ttyper```

```zypper: sudo zypper install ttyper```

```nix: nix profile install nixpkgs#ttyper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[typespeed](/man/typespeed)(6), [wpm](/man/wpm)(1), [gtypist](/man/gtypist)(1)
