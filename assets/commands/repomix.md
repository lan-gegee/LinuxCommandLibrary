# TAGLINE

将代码仓库打包为 AI 友好的格式

# TLDR

**打包仓库**

```repomix```

**打包指定目录**

```repomix [path/to/repo]```

**自定义输出文件**

```repomix -o [output.txt]```

**包含特定文件**

```repomix --include "[*.ts,*.js]"```

**排除模式**

```repomix --ignore "[node_modules,dist]"```

**XML 输出格式**

```repomix --style xml```

# SYNOPSIS

**repomix** [_-o file_] [_--include pattern_] [_--ignore pattern_] [_path_]

# PARAMETERS

**-o**, **--output** _FILE_
> 输出文件名。

**--include** _PATTERN_
> 包含模式。

**--ignore** _PATTERN_
> 忽略模式。

**--style** _FORMAT_
> 输出风格（plain、xml、markdown）。

**--top-files-len** _N_
> 摘要中的文件数量。

**-c**, **--config** _FILE_
> 配置文件路径。

# DESCRIPTION

**repomix** 将整个代码仓库打包成单个文本文件，针对在 AI 语言模型对话中作为上下文使用而优化。它以清晰的文件边界标记和目录树摘要拼接源文件，使 LLM 易于理解代码库的完整结构和内容。

该工具自动遵循 .gitignore 规则，跳过依赖和构建产物等无关文件。包含与排除模式可对要打包的文件进行细粒度控制。内置的 token 计数功能可估算输出将占用 LLM 上下文窗口的空间，帮助用户保持在模型限制之内。

输出格式包括纯文本、XML 和 Markdown，每种格式都有清晰的文件分隔符和可选的元数据头。可以通过 **repomix.config.json** 文件进行配置，以便在整个项目中保持一致的用法。

# CONFIGURATION

**repomix.config.json**
> 项目级配置文件，指定默认输出格式、包含/排除模式和输出文件名。会从仓库根目录自动加载。

# CAVEATS

大型仓库可能超出限制。二进制文件会被跳过。需要 Node.js。

# HISTORY

**repomix** 的创建目的是将代码库打包为单个文件，以适配 AI 语言模型的上下文窗口。

# INSTALL

```brew: brew install repomix```

```nix: nix profile install nixpkgs#repomix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [tree](/man/tree)(1), [cat](/man/cat)(1)
