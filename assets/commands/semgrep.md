# TAGLINE

面向代码安全与质量的轻量级静态分析工具

# TLDR

**使用自动检测的推荐规则进行扫描**

```semgrep scan --config auto```

**扫描指定目录**

```semgrep scan --config auto [path/to/src/]```

**使用注册表中的特定规则包扫描**

```semgrep scan --config p/[security-audit]```

**使用本地规则文件扫描**

```semgrep scan --config [path/to/rules.yaml] [path/to/src/]```

**使用内联模式扫描**

```semgrep scan -e '[pattern]' --lang [python]```

**以 JSON 格式输出结果**

```semgrep scan --json --config auto```

**扫描并自动应用修复**

```semgrep scan --config auto --autofix```

# SYNOPSIS

**semgrep** [_options_] [_targets_...]

# DESCRIPTION

**semgrep** 是一款快速、轻量的静态分析工具，用于查找缺陷、检测安全漏洞，并在 30 多种编程语言中强制执行代码规范。与传统 grep 不同，它能理解代码结构，并采用与目标语言语法相似的模式匹配，使规则易于编写和阅读。

规则可来自 Semgrep 注册表（使用 **--config auto** 获取推荐检查项），也可来自精选规则包（如 **p/security-audit**）以覆盖特定类别，还可来自本地 YAML 文件以实现自定义项目规则。配合 **-e** 使用内联模式可以进行快速的一次性搜索，无需编写规则文件。

输出格式包括 text、JSON、SARIF、GitLab SAST、JUnit XML、Emacs 和 Vim。该工具可自然地集成到 CI/CD 流水线中，持续保障代码质量。

# PARAMETERS

**--config** _config_
> 规则配置：auto、p/规则集名称，或 YAML 文件路径。

**-e**, **--pattern** _pattern_
> 用于临时规则的内联模式（需要 --lang）。

**--lang** _language_
> 内联模式匹配的目标语言。

**--json**
> 以 JSON 格式输出结果。

**--sarif**
> 以 SARIF 格式输出结果（适用于 GitHub Advanced Security 等）。

**--autofix**
> 对有建议修复方案的结果自动应用修复。

**--exclude** _pattern_
> 排除匹配该模式的文件或目录。可多次指定。

**--include** _pattern_
> 仅扫描匹配该模式的文件。可多次指定。

**--exclude-rule** _id_
> 跳过具有给定 ID 的规则。可多次指定。

**-o**, **--output** _file_
> 将结果保存到文件或发送到 URL。

**--severity** _level_
> 按最低严重级别过滤（INFO、WARNING、ERROR）。

**--error**
> 若有任何发现则以退出码 1 退出（默认：退出码为 0）。

**-j**, **--jobs** _N_
> 并行扫描任务数（默认：3）。

**--timeout** _seconds_
> 每个文件的最长时间（默认：5 秒）。

**-v**, **--verbose**
> 显示有关规则和解析的更多细节。

**--debug**
> 包含全部详细输出以及调试信息。

# CAVEATS

不同注册表中的规则质量参差不齐；误报需要通过 `--exclude-rule` 或 nosemgrep 注释进行调整。自定义规则有一定学习成本。没有 `--include` 过滤器时，超大型代码库可能扫描缓慢。`--autofix` 选项会直接修改文件，提交前请先审查改动。

# HISTORY

**semgrep** 由 **r2c**（现为 Semgrep Inc.）开发，于 **2019** 年前后发布。它基于学术研究构建，打造了一个实用的、理解语言结构的代码分析版 grep。

# INSTALL

```brew: brew install semgrep```

```nix: nix profile install nixpkgs#semgrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [ast-grep](/man/ast-grep)(1), [eslint](/man/eslint)(1), [pylint](/man/pylint)(1)
