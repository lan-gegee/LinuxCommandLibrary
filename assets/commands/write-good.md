# TAGLINE

面向文档的英文散文 linter

# TLDR

**检查单个文件**中的散文问题

```write-good [path/to/file.md]```

使用 glob 模式**检查多个文件**

```write-good [**/*.md]```

**检查内联文本**

```write-good --text="[It should have been defined there.]"```

**禁用被动语态检查**

```write-good --no-passive [path/to/file.md]```

**禁用副词警告**

```write-good --no-adverb [path/to/file.md]```

**只检查特定问题**

```write-good --passive --adverb [path/to/file.md]```

**解析来自标准输入的文本**

```echo "[The file was written by him.]" | write-good```

# SYNOPSIS

**write-good** [**--text**=_string_] [**--no-**_check_] [_file_|_glob_...]

# PARAMETERS

**--text**=_string_
> 分析给定的文本字符串而不是文件。

**--no-passive**
> 禁用被动语态检测。

**--no-adverb**
> 禁用副词警告（really、extremely 等）。

**--no-illusion**
> 禁用词汇幻影检测（重复出现的单词）。

**--no-so**
> 禁用以 "so" 开头的句子的警告。

**--no-thereIs**
> 禁用句首 "there is/are" 的警告。

**--no-weasel**
> 禁用模糊用词（weasel word）检测。

**--no-tooWordy**
> 禁用冗长短语检测。

**--no-cliches**
> 禁用陈词滥调检测。

**--yes-eprime**
> 启用 E-Prime 检查，标记 "to be" 的各种形式（默认禁用）。

**--parse**
> 启用便于解析的输出和 Unix 风格退出码。

**--whitelist** _WORDS_
> 以逗号分隔的白名单单词列表，这些词不会出现在建议中。

# DESCRIPTION

**write-good** 是一个英文散文 linter，帮助识别常见的写作问题。它会标记被动语态、不必要的副词、模糊用词、陈词滥调、词汇幻影（重复的单词）和冗长短语。

该工具专为编写文档、README 和技术内容的开发者设计。它可以分析单个文件、通过 glob 模式分析多个文件，或分析内联文本字符串。

每条建议都包含有问题的文本、其在文件中的位置，以及解释问题的原因。可以使用 **--no-** 标志选择性地禁用某些检查，也可以只指定需要的检查项来单独启用。

write-good 通过编辑器插件集成到 Vim（经由 ALE）、Sublime Text、VS Code 等编辑器中。它也可以在 Docker 容器中运行，用于 CI/CD 流水线。

# CAVEATS

该 linter 刻意保持"朴素"，可能会产生误报。被动语态和副词并不总是错的，审阅建议时需要自行判断。该工具专注于常见问题，并非全面的语法检查器。某些技术写作确实需要被动结构。

# HISTORY

**write-good** 由 **Brian Ford**（btford）创建，大约于 **2014 年**首次发布。它已成为 JavaScript 社区中提升文档质量的流行工具，并被用于开源项目的 CI 流水线。

# INSTALL

```brew: brew install write-good```

```nix: nix profile install nixpkgs#write-good```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vale](/man/vale)(1), [proselint](/man/proselint)(1), [grammarly](/man/grammarly)(1), [aspell](/man/aspell)(1)
