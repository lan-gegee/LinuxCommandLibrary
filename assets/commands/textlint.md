# TAGLINE

可插拔的自然语言 linter

# TLDR

**检查 markdown 文件**

```textlint "[docs/**/*.md]"```

**检查目录**

```textlint [docs/]```

**自动修复问题**

```textlint --fix [README.md]```

**试运行以预览修复效果**

```textlint --fix --dry-run --format diff [README.md]```

**使用指定的配置文件**

```textlint -c [.textlintrc.json] [file.md]```

**检查 stdin**

```cat [README.md] | textlint --stdin --stdin-filename "README.md"```

**以 JSON 格式输出**

```textlint --format json [docs/]```

**初始化配置**

```textlint --init```

# SYNOPSIS

**textlint** [_options_] [_file_|_dir_|_glob_...]

# PARAMETERS

**-c**, **--config** _file_
> 配置文件路径。

**--ignore-path** _file_
> 包含忽略模式的文件（默认：.textlintignore）。

**--init**
> 若配置文件不存在则创建。

**--fix**
> 自动修复问题。

**--dry-run**
> 预览修复而不写入。

**--debug**
> 输出调试信息。

**--print-config**
> 打印解析后的配置。

**--stdin**
> 检查来自 stdin 的文本。

**--stdin-filename** _name_
> stdin 输入使用的文件名。

**-f**, **--format** _format_
> 输出格式：stylish、json、checkstyle、compact、junit、tap、unix。

**-o**, **--output-file** _file_
> 将报告写入文件。

**--no-color**
> 禁用彩色输出。

**--quiet**
> 仅报告错误。

**--no-textlintrc**
> 禁用 .textlintrc 加载。

**--rule** _rule_
> 要使用的规则包。

**--preset** _preset_
> 要加载的预设包。

**--plugin** _plugin_
> 要使用的插件包。

**--cache**
> 只检查有改动的文件。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**textlint** 是一款针对自然语言文本的可插拔 linter。它使用可配置的规则检查散文中的风格问题、语法问题和写作不一致。

规则以 npm 软件包的形式安装，并在 .textlintrc 中配置。现有规则涵盖拼写、术语、句子长度、冗余短语和写作风格指南。预设（preset）打包了常用的规则集。

该工具通过插件支持 Markdown、纯文本及其他格式。它可以集成到编辑器和 CI/CD 流水线中，实现自动化文本质量检查。

自动修复模式可以自动纠正许多问题。应用更改前，可先用 dry-run 配合 diff 格式预览。

通过 npm 安装：`npm install textlint`

# CAVEATS

需要 Node.js 和 npm。规则必须单独安装。多条规则并存时配置复杂度会上升。某些规则之间可能相互冲突。

# HISTORY

**textlint** 由 azu 创建，是一款受 ESLint 启发的散文 linter。它将可插拔架构模式应用于自然语言检查，让社区能够为不同的写作风格和语言开发专门的规则。

# INSTALL

```nix: nix profile install nixpkgs#textlint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [vale](/man/vale)(1), [markdownlint](/man/markdownlint)(1), [proselint](/man/proselint)(1)
