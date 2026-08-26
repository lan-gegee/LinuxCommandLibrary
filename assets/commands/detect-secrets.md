# TAGLINE

检测意外提交到仓库的机密信息

# TLDR

**扫描目录中的机密**

```detect-secrets scan [path/to/directory]```

**扫描并创建基线文件**

```detect-secrets scan > [.secrets.baseline]```

**审计基线文件**

```detect-secrets audit [.secrets.baseline]```

**扫描指定文件**

```detect-secrets scan [file1] [file2]```

**使用全部插件扫描**

```detect-secrets scan --all-files [path]```

**更新现有基线**

```detect-secrets scan --baseline [.secrets.baseline]```

**作为 pre-commit 钩子运行**

```detect-secrets-hook --baseline [.secrets.baseline]```

# SYNOPSIS

**detect-secrets** _command_ [_options_] [_path_]

# PARAMETERS

**scan**
> 扫描文件中的潜在机密。

**audit**
> 交互式审计检测到的机密。

**--baseline** _file_
> 使用现有基线进行对比。

**--all-files**
> 扫描所有文件，而不只是 git 跟踪的文件。

**--exclude-files** _regex_
> 排除文件的正则表达式。

**--exclude-lines** _regex_
> 排除行内容匹配的正则表达式。

**--exclude-secrets** _regex_
> 排除机密值匹配的正则表达式。

**--list-all-plugins**
> 列出可用的检测插件。

**--no-verify**
> 禁用对检测到的机密的验证。

**-f**, **--force-use-all-plugins**
> 启用所有检测插件。

# DESCRIPTION

**detect-secrets** 是一个用于检测意外提交到代码仓库的机密（密码、API 密钥、令牌）的工具。它按已知机密格式扫描文件中的模式，并标记潜在的泄露。

该工具使用多种检测插件：高熵字符串、关键词模式（password、api_key）以及针对特定格式的检测器（AWS 密钥、私钥等）。基线文件记录已知的机密，避免对有意保留的条目反复告警。

audit 工作流允许交互式审查检测到的机密，将其标记为真阳性、假阳性或跳过。pre-commit 钩子集成可以阻止新机密被提交。

# PLUGINS

**ArtifactoryDetector**: Artifactory 令牌
**AWSKeyDetector**: AWS 访问密钥
**Base64HighEntropyString**: 高熵 base64
**BasicAuthDetector**: Basic 认证凭据
**HexHighEntropyString**: 高熵十六进制字符串
**JwtTokenDetector**: JWT 令牌
**KeywordDetector**: 机密关键词
**PrivateKeyDetector**: 私钥头
**SlackDetector**: Slack 令牌

# CONFIGURATION

**.secrets.baseline**
> 记录已知机密和审计决策的基线文件。

# CAVEATS

高熵检测器可能对随机字符串、UUID 或哈希产生误报。随着代码变更需要维护基线。部分检测依赖固定模式，可能漏掉经过混淆的机密。默认不扫描 git 历史。

# HISTORY

detect-secrets 由 **Yelp** 开发并于 **2018 年**开源。它的诞生是为了防止其庞大代码库中发生机密泄露。插件架构让检测能力可以扩展。该工具已被广泛采纳为安全开发实践和 CI/CD 流水线的一部分。

# INSTALL

```brew: brew install detect-secrets```

```nix: nix profile install nixpkgs#detect-secrets```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-secrets](/man/git-secrets)(1), [trufflehog](/man/trufflehog)(1), [gitleaks](/man/gitleaks)(1)

# RESOURCES

```[Source code](https://github.com/Yelp/detect-secrets)```

<!-- verified: 2026-07-11 -->
