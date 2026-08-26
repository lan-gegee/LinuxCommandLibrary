# TAGLINE

命令行翻译器

# TLDR

将文本**翻译**成你的默认语言

```trans "[text]"```

**翻译成指定语言**

```trans :[target_lang] "[text]"```

在两种语言之间**互译**

```trans [source]:[target] "[text]"```

**同时翻译成多种语言**

```trans :fr+de+es "[text]"```

**简洁模式**（只显示译文）

```trans -b "[text]"```

**收听译文**（文字转语音）

```trans -p :[target] "[text]"```

**识别文本的语言**

```trans -id "[text]"```

**启动交互模式**

```trans -shell```

# SYNOPSIS

**trans** [_options_] [_source_]:[_target_] [_text ..._]

# PARAMETERS

**-b**, **-brief**
> 简洁模式；只显示译文。

**-d**, **-dictionary**
> 显示单词的词典释义。

**-id**, **-identify**
> 识别文本的语言。

**-p**, **-play**
> 通过文字转语音收听译文。

**-speak**
> 收听原文。

**-s**, **-source** _lang_
> 指定源语言。

**-t**, **-target** _lang_
> 指定目标语言。

**-i**, **-input** _file_
> 从文件读取文本。

**-o**, **-output** _file_
> 将译文写入文件。

**-shell**, **-interactive**
> 启动交互式翻译 Shell。

**-e**, **-engine** _engine_
> 使用指定的翻译引擎（google、bing、yandex、apertium）。

**-T**, **-reference**
> 打印所有支持语言的对照表。

**-V**, **-version**
> 打印版本并退出。

**-H**, **-help**
> 打印帮助信息并退出。

# DESCRIPTION

**Translate Shell**（trans）是一个命令行翻译器，由 Google Translate（默认）、Bing Translator、Yandex.Translate 和 Apertium 提供支持。它让你可以在终端中快速使用各种翻译服务。

语言代码遵循 ISO 639 标准（如 en、fr、de、zh-CN、ja）。未指定源语言时会自动检测。可以用 **+** 连接多个代码来同时指定多个目标语言。

交互模式（**-shell**）支持逐行翻译。音频播放需要 mplayer、mpv 或 mpg123。配合 **-d** 选项，该工具还可以当作词典使用。

# CAVEATS

需要联网，且依赖外部翻译服务。大量使用可能触发速率限制。音频播放需要安装兼容的音频播放器（mplayer、mpv 或 mpg123）。

# HISTORY

Translate Shell 最初名为 "Google Translate CLI"，由 **Mort Yao**（soimort）创建。它于 **2012 年**左右首次发布，用于在命令行中使用 Google Translate。该项目后来更名，并扩展为支持包括 Bing、Yandex 和 Apertium 在内的多种翻译引擎。

# INSTALL

```dnf: sudo dnf install translate-shell```

```pacman: sudo pacman -S translate-shell```

```apk: sudo apk add translate-shell```

```zypper: sudo zypper install translate-shell```

```brew: brew install translate-shell```

```nix: nix profile install nixpkgs#translate-shell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dict](/man/dict)(1), [espeak](/man/espeak)(1), [aspell](/man/aspell)(1)
