# TAGLINE

具备语法感知能力的散文 linter

# TLDR

在当前目录中**检查文件**

```vale [path/to/files]```

**递归检查 markdown 文件**

```vale [docs/**/*.md]```

**使用指定的配置文件**

```vale --config [.vale.ini] [file.md]```

**只显示错误**（忽略警告和建议）

```vale --minAlertLevel error [file.md]```

**以 JSON 格式输出**

```vale --output JSON [file.md]```

**从标准输入检查内容**

```echo "[text]" | vale --ext .md```

**列出已配置的目录**

```vale ls-dirs```

从配置文件**同步样式包**

```vale sync```

# SYNOPSIS

**vale** [_options_] [_files ..._]

# PARAMETERS

**--config** _file_
> 使用指定的配置文件（.vale.ini）。

**--ext** _extension_
> 为标准输入指定文件扩展名（如 `.md`、`.rst`）。

**--glob** _pattern_
> 只检查匹配 glob 模式的文件。

**--filter** _expr_
> 使用 CEL 风格的表达式过滤规则（如 `".Level == 'error'"`）。

**--minAlertLevel** _level_
> 最低警报级别：`suggestion`、`warning` 或 `error`。

**--output** _format_
> 输出格式：`CLI`（默认）、`JSON`、`line` 或模板文件路径。

**--no-exit**
> 无论有无错误都以状态码 0 退出。

**--no-wrap**
> 不对输出的行进行折行。

**--no-global**
> 跳过加载全局配置。

**--relative**
> 以相对于当前目录的路径进行报告。

**--sort**
> 按文件路径和行号排序输出。

**--ignore-syntax**
> 将所有输入视为纯文本（跳过语法感知解析）。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助消息。

# SUBCOMMANDS

**sync**
> 下载并安装配置中声明的软件包。

**ls-config**
> 以 JSON 格式打印生效的配置。

**ls-dirs**
> 打印 Vale 配置目录的位置。

**ls-metrics** _file_
> 打印给定文件的可读性等指标。

**ls-vars**
> 打印支持的环境变量。

# DESCRIPTION

**Vale** 是一个语法感知的散文 linter，为文档和散文带来类似代码的 lint 检查。它依据可自定义的风格规则检查文本的一致性、语法以及企业风格指南的符合度。

Vale 支持 Markdown、AsciiDoc、reStructuredText、HTML 等标记格式。它可以选用社区风格包（Microsoft、Google、write-good），也可以使用 YAML 中定义的自定义规则。

配置通过 **.vale.ini** 文件管理，其中指定要使用的风格、要检查的文件模式以及词汇例外。

# CAVEATS

Vale 的风格包必须先通过 **vale sync** 安装才能使用。自定义词汇（可接受的术语、拼写例外）必须在 vale 配置中设置。复杂的基于正则表达式的规则可能影响大型文档的处理性能。

# HISTORY

Vale 由 Errata AI 的 **Joseph Kato** 创建，于 **2017 年**首次发布。它的设计目标是提供像代码 linter 那样可维护、可扩展的散文检查。Vale 使用 Go 编写以保证性能和跨平台支持，已被 GitLab、Grafana 和 Linode 等许多技术文档团队采用。

# INSTALL

```pacman: sudo pacman -S vale```

```apk: sudo apk add vale```

```zypper: sudo zypper install vale```

```brew: brew install vale```

```nix: nix profile install nixpkgs#vale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[proselint](/man/proselint)(1), [write-good](/man/write-good)(1), [textlint](/man/textlint)(1), [aspell](/man/aspell)(1)
