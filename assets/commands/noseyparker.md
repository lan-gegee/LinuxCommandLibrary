# TAGLINE

用于检测文本数据中机密和敏感信息的命令行工具

# TLDR

**扫描本地目录**以查找机密

```noseyparker scan --datastore [db.np] [path/to/directory]```

按 URL **扫描 Git 仓库**

```noseyparker scan --datastore [db.np] --git-url [https://github.com/user/repo]```

从 datastore 中**报告发现结果**

```noseyparker report --datastore [db.np]```

**以 JSON 格式报告**

```noseyparker report --datastore [db.np] --format json```

**仅使用指定规则扫描**

```noseyparker scan --datastore [db.np] --rules [path/to/rules.yml] [path/to/directory]```

**列出可用的内置规则**

```noseyparker rules list```

**汇总 datastore 内容**

```noseyparker summarize --datastore [db.np]```

# SYNOPSIS

**noseyparker** _command_ [_options_]

# PARAMETERS

**scan**
> 扫描输入以查找机密，并将发现结果存入 datastore。

**report**
> 从 datastore 报告发现结果。

**summarize**
> 汇总 datastore 内容，不给出详细发现。

**rules**
> 管理和检查检测规则。

**github**
> 与 GitHub 交互以扫描仓库。

**--datastore** _PATH_
> datastore 的路径（scan/report/summarize 必需）。

**--git-url** _URL_
> 克隆并扫描指定 URL 的 Git 仓库。

**--format** _FORMAT_
> report 的输出格式（human、json、jsonl、sarif）。

**--rules** _PATH_
> 自定义规则文件的路径（YAML 格式）。

**--max-file-size** _BYTES_
> 跳过超过指定大小的文件。

**--jobs** _N_
> 并行扫描任务的数量。

**--ignore** _PATTERN_
> 用于忽略路径的 glob 模式。

**--blob-metadata**
> 在发现结果中包含 blob 元数据。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**Nosey Parker** 是一款命令行工具，用于检测文本数据和 Git 仓库中的机密与敏感信息。它扫描源代码、配置文件和提交历史，以找出意外提交的凭据、API 密钥、私钥和其他敏感数据。

该工具采用 datastore 模型，扫描结果会持久化到本地数据库，从而支持增量扫描和对发现结果的去重。多次扫描可以写入同一个 datastore，并可随时基于累积的数据生成报告。

Nosey Parker 内置 150 多条检测规则，覆盖 AWS 密钥、GitHub 令牌、SSH 私钥、数据库连接字符串等常见机密模式。还可以用 YAML 格式定义自定义规则来匹配组织特有的模式。

扫描器使用 Rust 编写以保证高性能，能够快速处理大型代码库。它执行内容感知扫描，理解 Git 历史，检查所有提交和分支而不只是当前状态。

# CAVEATS

扫描结果可能包含需要人工复核的误报。大多数操作都必须指定 datastore，其体积会随着发现的累积而增长。带完整 Git 历史扫描大型仓库可能非常消耗内存。某些检测规则可能无法识别经过混淆或编码的机密。

# HISTORY

Nosey Parker 由 **Praetorian** 创建，于 **2023 年**开源发布。它被设计为 truffleHog 和 git-secrets 等工具的现代替代品，强调性能和准确性。其 Rust 实现相比基于 Python 的替代方案带来了显著的速度提升。该项目仍在积极开发中，定期更新规则并添加功能。

# INSTALL

```brew: brew install noseyparker```

```nix: nix profile install nixpkgs#noseyparker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-secrets](/man/git-secrets)(1), [trufflehog](/man/trufflehog)(1), [gitleaks](/man/gitleaks)(1), [detect-secrets](/man/detect-secrets)(1)
